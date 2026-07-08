#!/usr/bin/env python3
"""Rule-based baseline reviewer for Copy Lens Review.

Usage:
  python scripts/copy_lens_review.py input.json --format markdown
  python scripts/copy_lens_review.py input.json --format json
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


FANDOM_TERMS = ["老公", "老婆", "本命", "饭圈", "追星", "爱豆", "塌房", "应援"]
MARRIAGE_TERMS = ["老公", "老婆", "婚纱", "约会", "暧昧", "出轨", "情人", "小三", "另一个"]
FAMILY_TERMS = ["妈妈", "母亲", "妈", "爸爸", "父亲", "爸", "孩子", "家庭", "夫妻", "丈夫", "妻子"]
GENDER_TERMS = ["女性", "女人", "女神", "美女", "贤惠", "打扮", "身材", "穿婚纱", "取悦"]
MINOR_TERMS = ["孩子", "儿童", "学生", "青少年", "未成年人", "家长"]
WEAK_GROUP_TERMS = ["残疾", "疾病", "贫困", "胖", "丑", "穷", "土", "低学历", "老年"]
JUDGEMENTAL_TERMS = ["低端", "土味", "不配", "失败", "拖后腿", "没文化", "廉价"]
SERIOUS_OCCASIONS = ["母亲节", "父亲节", "儿童节", "春节", "清明", "公益", "教育", "医疗", "政务", "安全"]


@dataclass
class Input:
    brand: str = ""
    industry: str = ""
    objective: str = ""
    occasion: str = ""
    channel: str = ""
    target_audience: str = ""
    tone: str = ""
    copy: str = ""


def includes_any(text: str, terms: list[str]) -> bool:
    return any(term in text for term in terms)


def clamp(value: int, max_value: int) -> int:
    return min(max_value, max(0, value))


def level_from_score(score: int) -> str:
    if score >= 81:
        return "危机"
    if score >= 61:
        return "高"
    if score >= 41:
        return "中"
    return "低"


def advice_from_score(score: int) -> str:
    if score >= 81:
        return "不建议发布"
    if score >= 61:
        return "需要重写"
    if score >= 21:
        return "小幅修改后发布"
    return "可直接发布"


def flags(input_data: Input) -> dict[str, bool]:
    text = " ".join(asdict(input_data).values())
    return {
        "has_fandom_slang": includes_any(text, FANDOM_TERMS),
        "has_marriage_terms": includes_any(text, MARRIAGE_TERMS),
        "has_family_terms": includes_any(text, FAMILY_TERMS),
        "has_gender_terms": includes_any(text, GENDER_TERMS),
        "has_mother_context": includes_any(text, ["母亲", "妈妈", "我妈", "母亲节"]),
        "has_minor_context": includes_any(text, MINOR_TERMS),
        "has_weak_group_terms": includes_any(text, WEAK_GROUP_TERMS),
        "has_sensational_hook": includes_any(text, ["两个", "另一个", "穿婚纱", "老公", "老婆", "不配", "低端"])
        or len(input_data.copy) <= 60,
        "has_serious_occasion": includes_any(text, SERIOUS_OCCASIONS),
        "has_judgemental_labels": includes_any(text, JUDGEMENTAL_TERMS),
    }


def risk_breakdown(f: dict[str, bool], input_data: Input) -> list[dict[str, Any]]:
    ambiguity = clamp(
        (8 if f["has_fandom_slang"] else 0)
        + (6 if f["has_marriage_terms"] else 0)
        + (2 if "“" in input_data.copy or '"' in input_data.copy else 0)
        + (3 if f["has_sensational_hook"] else 0),
        15,
    )
    value_conflict = clamp(
        (6 if f["has_family_terms"] else 0)
        + (5 if f["has_gender_terms"] else 0)
        + (5 if f["has_serious_occasion"] else 0)
        + (5 if f["has_marriage_terms"] else 0)
        + (4 if f["has_weak_group_terms"] else 0),
        20,
    )
    offense = clamp(
        (6 if f["has_mother_context"] else 0)
        + (5 if f["has_gender_terms"] else 0)
        + (6 if f["has_judgemental_labels"] else 0)
        + (5 if f["has_marriage_terms"] else 0)
        + (6 if f["has_weak_group_terms"] else 0),
        20,
    )
    mismatch = clamp(
        (6 if f["has_serious_occasion"] else 0)
        + (5 if f["has_fandom_slang"] else 0)
        + (3 if "带梗" in input_data.tone or "轻松" in input_data.tone else 0)
        + (3 if f["has_mother_context"] else 0),
        15,
    )
    screenshot = clamp(
        (6 if f["has_sensational_hook"] else 0)
        + (3 if f["has_marriage_terms"] else 0)
        + (2 if len(input_data.copy) <= 120 else 0),
        10,
    )
    media = clamp(
        (5 if f["has_sensational_hook"] else 0)
        + (3 if f["has_gender_terms"] else 0)
        + (2 if f["has_family_terms"] else 0)
        + (3 if f["has_weak_group_terms"] else 0),
        10,
    )
    brand = clamp(
        (2 if input_data.brand else 0)
        + (3 if f["has_serious_occasion"] else 0)
        + (2 if f["has_gender_terms"] else 0)
        + (2 if f["has_marriage_terms"] else 0)
        + (1 if "消费" in input_data.industry or "品牌" in input_data.industry else 0),
        10,
    )
    return [
        {"name": "语义歧义风险", "weight": 15, "score": ambiguity},
        {"name": "价值观冲突风险", "weight": 20, "score": value_conflict},
        {"name": "群体冒犯风险", "weight": 20, "score": offense},
        {"name": "场景错配风险", "weight": 15, "score": mismatch},
        {"name": "截图传播风险", "weight": 10, "score": screenshot},
        {"name": "媒体放大风险", "weight": 10, "score": media},
        {"name": "品牌资产损伤风险", "weight": 10, "score": brand},
    ]


def detected_signals(f: dict[str, bool]) -> list[str]:
    mapping = [
        ("has_fandom_slang", "圈层黑话 / 亚文化梗"),
        ("has_marriage_terms", "婚姻称谓 / 亲密关系语义"),
        ("has_family_terms", "家庭伦理 / 亲子关系语境"),
        ("has_gender_terms", "性别表达 / 女性形象风险"),
        ("has_mother_context", "母亲形象 / 节日尊重语境"),
        ("has_minor_context", "未成年人或家长视角"),
        ("has_weak_group_terms", "弱势群体或身份标签"),
        ("has_judgemental_labels", "评价性标签 / 污名化表达"),
        ("has_sensational_hook", "截图传播钩子强"),
    ]
    return [label for key, label in mapping if f[key]] or ["未发现明显高危语义信号"]


def core_risks(f: dict[str, bool]) -> list[str]:
    risks: list[str] = []
    if f["has_fandom_slang"] and f["has_marriage_terms"]:
        risks.append("圈层内部称谓进入大众传播后，与婚姻伦理的公共语义发生冲突。")
    if f["has_mother_context"] and f["has_gender_terms"]:
        risks.append("母亲的自我表达被转译成围绕男性对象、打扮和被观看的叙事。")
    if f["has_serious_occasion"]:
        risks.append("节日语境提高了尊重感要求，玩梗表达的容错率明显下降。")
    if f["has_sensational_hook"]:
        risks.append("文案存在可被单独截图传播的爆点，完整创意意图容易被截断。")
    if f["has_weak_group_terms"] or f["has_judgemental_labels"]:
        risks.append("文案包含身份标签或评价性词汇，可能被理解为污名化特定群体。")
    return risks or ["当前主要风险不在敏感词，而在表达是否足够清楚、是否需要解释才能成立。"]


def rewrites(f: dict[str, bool]) -> list[dict[str, str]]:
    if f["has_mother_context"]:
        return [
            {
                "name": "保守安全版",
                "copy": "妈妈不只属于家庭、日程和责任。她也有自己的热爱、舞台和心动时刻。",
            },
            {
                "name": "年轻化但不冒犯版",
                "copy": "原来妈妈也会追星，也会尖叫，也会为了热爱认真打扮。今天，不只祝她母亲节快乐，也祝她做自己快乐。",
            },
            {
                "name": "高创意但低误读版",
                "copy": "小时候，我以为妈妈只会为我奔赴。后来才发现，她也会为自己的热爱奔赴千里。",
            },
        ]
    return [
        {"name": "保守安全版", "copy": "把核心利益点直接说清楚，避免依赖需要解释的双关、黑话和身份标签。"},
        {"name": "年轻化但不冒犯版", "copy": "保留轻松语气，但把笑点放在产品体验或生活场景上，而不是特定群体身上。"},
        {"name": "高创意但低误读版", "copy": "让反差来自用户洞察，而不是伦理、身份或价值观边界。"},
    ]


def review(input_data: Input) -> dict[str, Any]:
    f = flags(input_data)
    breakdown = risk_breakdown(f, input_data)
    score = min(100, max(8, round(sum(item["score"] for item in breakdown) * 0.92)))
    level = level_from_score(score)
    brand = input_data.brand or "该品牌"
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "score": score,
        "level": level,
        "advice": advice_from_score(score),
        "intent": "母亲不只有家庭角色，也可以拥有追星、热爱和自我表达。"
        if f["has_mother_context"] and f["has_fandom_slang"]
        else f"该文案似乎想服务于“{input_data.objective or input_data.occasion or '本次传播'}”。",
        "detected_signals": detected_signals(f),
        "core_risks": core_risks(f),
        "risk_breakdown": breakdown,
        "screenshot_test": "如果被单独截图传播，最刺激的短句会替代完整上下文，评论区会围绕这句话是否冒犯展开。"
        if f["has_sensational_hook"]
        else "单独截图后仍基本能保留原意，但仍需检查标题、主视觉和封面。",
        "media_titles": [
            f"{brand}文案翻车：一句广告为何引发公共语境争议？",
            "不是用户不懂梗，而是公共传播不能只靠内部解释",
            "品牌年轻化如何从破圈变成翻车？",
        ],
        "rewrites": rewrites(f),
    }


def render_markdown(input_data: Input, result: dict[str, Any]) -> str:
    risks = "\n".join(f"{index + 1}. {item}" for index, item in enumerate(result["core_risks"]))
    breakdown = "\n".join(
        f"- {item['name']}: {item['score']}/{item['weight']}" for item in result["risk_breakdown"]
    )
    rewrites_text = "\n\n".join(f"### {item['name']}\n{item['copy']}" for item in result["rewrites"])
    return f"""# Copy Lens 审核报告

## 文案原文
{input_data.copy}

## 创意意图判断
{result["intent"]}

## 核心风险摘要
- 综合风险分: {result["score"]}/100
- 风险等级: {result["level"]}
- 发布建议: {result["advice"]}

{risks}

## 检出信号
{", ".join(result["detected_signals"])}

## 风险评分
{breakdown}

## 截图传播测试
{result["screenshot_test"]}

## 媒体标题推演
{chr(10).join(f"{index + 1}. {title}" for index, title in enumerate(result["media_titles"]))}

## 改写建议
{rewrites_text}
"""


def normalize_input(raw: dict[str, Any]) -> Input:
    return Input(
        brand=str(raw.get("brand", "")),
        industry=str(raw.get("industry", "")),
        objective=str(raw.get("objective", "")),
        occasion=str(raw.get("occasion", "")),
        channel=str(raw.get("channel", "")),
        target_audience=str(raw.get("target_audience", raw.get("targetAudience", ""))),
        tone=str(raw.get("tone", "")),
        copy=str(raw.get("copy", "")),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a rule-based Copy Lens review.")
    parser.add_argument("input_json", help="Path to input JSON.")
    parser.add_argument("--format", choices=["json", "markdown"], default="markdown")
    args = parser.parse_args()

    input_path = Path(args.input_json)
    input_data = normalize_input(json.loads(input_path.read_text(encoding="utf-8")))
    if not input_data.copy.strip():
        raise SystemExit("copy field is required")

    result = review(input_data)
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(render_markdown(input_data, result))


if __name__ == "__main__":
    main()

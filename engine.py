"""
Phasics — Adaptive Engine
GMAT-style adaptive difficulty algorithm
"""

import math


def get_next_question(history: list, bank: list, current_level: int):
    """Select the next question based on adaptive logic."""
    answered_ids = {h["question_id"] for h in history}
    available = [q for q in bank if q["id"] not in answered_ids]

    if not available:
        return None

    # Find questions at target level, then nearby
    candidates = [q for q in available if q["level"] == current_level]
    if not candidates:
        candidates = [q for q in available if abs(q["level"] - current_level) <= 1]
    if not candidates:
        candidates = available

    # Prefer subtopics the student hasn't seen much
    topic_counts = {}
    for h in history:
        q = next((b for b in bank if b["id"] == h["question_id"]), None)
        if q:
            topic_counts[q["subtopic"]] = topic_counts.get(q["subtopic"], 0) + 1

    candidates.sort(key=lambda q: topic_counts.get(q["subtopic"], 0))
    return candidates[0]


def calculate_level(history: list) -> int:
    """Calculate adaptive difficulty level from recent history."""
    if not history:
        return 1
    recent = history[-3:]
    correct_count = sum(1 for h in recent if h["correct"])
    avg_level = sum(h["level"] for h in recent) / len(recent)

    if correct_count >= 2 and avg_level <= 4.5:
        return min(5, math.ceil(avg_level + 0.5))
    if correct_count == 0 and avg_level >= 1.5:
        return max(1, math.floor(avg_level - 0.5))
    return round(avg_level)


def get_ability_estimate(history: list) -> int:
    """Estimate overall ability as a percentage."""
    if not history:
        return 0
    score = 0
    for h in history:
        if h["correct"]:
            score += h["level"] * 1.2
        else:
            score += (h["level"] - 1) * 0.3
    return min(100, round((score / (len(history) * 5)) * 100))


def get_topic_breakdown(history: list, bank: list) -> dict:
    """Get per-subtopic performance breakdown."""
    topics = {}
    for h in history:
        q = next((b for b in bank if b["id"] == h["question_id"]), None)
        if not q:
            continue
        sub = q["subtopic"]
        if sub not in topics:
            topics[sub] = {"correct": 0, "total": 0, "levels": []}
        topics[sub]["total"] += 1
        if h["correct"]:
            topics[sub]["correct"] += 1
        topics[sub]["levels"].append(h["level"])
    return topics


def check_answer(question: dict, answer) -> bool:
    """Check if an answer is correct for any question type."""
    if question["type"] == "multiple_choice":
        return answer == question["correct"]
    elif question["type"] == "numerical":
        try:
            val = float(answer)
            return abs(val - question["correct"]) <= question["tolerance"]
        except (ValueError, TypeError):
            return False
    elif question["type"] == "conceptual":
        if not answer or not answer.strip():
            return False
        answer_lower = answer.lower()
        matched = sum(
            1 for kw in question["rubric"] if kw.lower() in answer_lower
        )
        return matched >= math.ceil(len(question["rubric"]) * 0.5)
    elif question["type"] == "math_input":
        # Math input is evaluated by keyword matching + AI tutor review
        if not answer or not answer.strip():
            return False
        answer_lower = answer.lower().replace(" ", "")
        matched = sum(
            1 for kw in question.get("eval_keywords", [])
            if kw.lower().replace(" ", "") in answer_lower
        )
        return matched >= math.ceil(len(question.get("eval_keywords", [])) * 0.5)
    elif question["type"] == "drawing":
        # Drawing is evaluated by AI — return None to signal AI eval needed
        return None
    return False

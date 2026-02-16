"""
Phasics — Adaptive Engine
Topic progression with mastery detection, spaced review, and adaptive difficulty.
"""

import math
import random

# ═══════════════════════════════════════
# RECOMMENDED TOPIC ORDER
# ═══════════════════════════════════════
TOPIC_ORDER = [
    {"subtopic": "Definitions", "topic": "SHM", "label": "1. SHM Foundations"},
    {"subtopic": "Period & Frequency", "topic": "SHM", "label": "2. Period & Frequency"},
    {"subtopic": "Energy", "topic": "SHM", "label": "3. Energy in SHM"},
    {"subtopic": "Equations of Motion", "topic": "SHM", "label": "4. Equations of Motion"},
    {"subtopic": "Damped Oscillations", "topic": "SHM", "label": "5. Damped Oscillations"},
    {"subtopic": "Coupled Oscillations", "topic": "SHM", "label": "6. Coupled Oscillators"},
    {"subtopic": "Harmonics", "topic": "Standing Waves", "label": "7. Harmonics"},
    {"subtopic": "Wave Speed", "topic": "Standing Waves", "label": "8. Wave Speed"},
    {"subtopic": "Resonance", "topic": "Standing Waves", "label": "9. Resonance"},
    {"subtopic": "Superposition", "topic": "Standing Waves", "label": "10. Superposition"},
    {"subtopic": "Wave Equation", "topic": "Standing Waves", "label": "11. Wave Equation"},
]

# Mastery threshold: need this many correct out of attempted to be "mastered"
MASTERY_CORRECT = 3
MASTERY_MIN_ATTEMPTED = 4
MASTERY_RATIO = 0.70  # 70%+ accuracy = mastered

# Chance to insert a review question from a mastered topic
REVIEW_PROBABILITY = 0.20  # 20% chance


def get_subtopic_stats(history: list, bank: list) -> dict:
    """Get per-subtopic stats: correct, total, mastered, avg_level."""
    stats = {}
    for h in history:
        q = next((b for b in bank if b["id"] == h["question_id"]), None)
        if not q:
            continue
        sub = q["subtopic"]
        if sub not in stats:
            stats[sub] = {"correct": 0, "total": 0, "levels": [], "mastered": False}
        stats[sub]["total"] += 1
        if h["correct"]:
            stats[sub]["correct"] += 1
        stats[sub]["levels"].append(h["level"])

    # Calculate mastery
    for sub, s in stats.items():
        if s["total"] >= MASTERY_MIN_ATTEMPTED:
            ratio = s["correct"] / s["total"]
            s["mastered"] = ratio >= MASTERY_RATIO and s["correct"] >= MASTERY_CORRECT
        s["ratio"] = s["correct"] / s["total"] if s["total"] > 0 else 0

    return stats


def check_mastery(subtopic: str, history: list, bank: list) -> bool:
    """Check if a specific subtopic is mastered."""
    stats = get_subtopic_stats(history, bank)
    return stats.get(subtopic, {}).get("mastered", False)


def just_mastered(subtopic: str, history: list, bank: list) -> bool:
    """Check if the student JUST mastered this subtopic (on the last answer)."""
    if not history:
        return False
    stats = get_subtopic_stats(history, bank)
    s = stats.get(subtopic, {})
    if not s.get("mastered", False):
        return False
    # Check if removing the last answer would un-master it
    prev_stats = get_subtopic_stats(history[:-1], bank)
    prev = prev_stats.get(subtopic, {})
    return not prev.get("mastered", False)


def get_recommended_subtopic(history: list, bank: list, current_subtopic: str = None) -> dict:
    """Get the next recommended subtopic based on mastery and topic order."""
    stats = get_subtopic_stats(history, bank)

    for t in TOPIC_ORDER:
        sub = t["subtopic"]
        s = stats.get(sub, {})
        # Skip mastered topics
        if s.get("mastered", False):
            continue
        # This is the next unmastered topic in the recommended order
        return t

    # All mastered — return None (or the last one for review)
    return None


def get_next_subtopic_in_order(current_subtopic: str) -> dict:
    """Get the next subtopic after the current one in the recommended order."""
    for i, t in enumerate(TOPIC_ORDER):
        if t["subtopic"] == current_subtopic and i + 1 < len(TOPIC_ORDER):
            return TOPIC_ORDER[i + 1]
    return None


def get_mastered_subtopics(history: list, bank: list) -> list:
    """Return list of mastered subtopic names."""
    stats = get_subtopic_stats(history, bank)
    return [sub for sub, s in stats.items() if s.get("mastered", False)]


def get_next_question(
    history: list,
    bank: list,
    current_level: int,
    focus_subtopic: str = None,
):
    """
    Select the next question based on adaptive logic + topic focus.

    Args:
        history: list of past answers
        bank: question bank
        current_level: adaptive difficulty level (1-5)
        focus_subtopic: if set, focus on this subtopic (can still mix review)

    Returns:
        question dict or None
    """
    answered_ids = {h["question_id"] for h in history}
    available = [q for q in bank if q["id"] not in answered_ids]

    if not available:
        return None

    stats = get_subtopic_stats(history, bank)
    mastered = [sub for sub, s in stats.items() if s.get("mastered", False)]

    # ── Review chance: occasionally pull from mastered topics ──
    if mastered and focus_subtopic and random.random() < REVIEW_PROBABILITY:
        review_sub = random.choice(mastered)
        review_qs = [q for q in available if q["subtopic"] == review_sub]
        if review_qs:
            # Pick at appropriate level
            level_qs = [q for q in review_qs if abs(q["level"] - current_level) <= 1]
            if level_qs:
                return random.choice(level_qs)
            return random.choice(review_qs)

    # ── Focus on current subtopic ──
    if focus_subtopic:
        focus_qs = [q for q in available if q["subtopic"] == focus_subtopic]
        if focus_qs:
            # Prefer questions near current level
            level_qs = [q for q in focus_qs if q["level"] == current_level]
            if not level_qs:
                level_qs = [q for q in focus_qs if abs(q["level"] - current_level) <= 1]
            if not level_qs:
                level_qs = focus_qs
            return level_qs[0]

    # ── Fallback: pick from any unmastered subtopic ──
    unmastered_qs = [q for q in available if q["subtopic"] not in mastered]
    if not unmastered_qs:
        unmastered_qs = available  # All mastered — just pick anything

    # Find at target level
    candidates = [q for q in unmastered_qs if q["level"] == current_level]
    if not candidates:
        candidates = [q for q in unmastered_qs if abs(q["level"] - current_level) <= 1]
    if not candidates:
        candidates = unmastered_qs

    # Prefer least-seen subtopics
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
    """Get per-subtopic performance breakdown (for dashboard)."""
    return get_subtopic_stats(history, bank)


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
        if not answer or not answer.strip():
            return False
        answer_lower = answer.lower().replace(" ", "")
        matched = sum(
            1 for kw in question.get("eval_keywords", [])
            if kw.lower().replace(" ", "") in answer_lower
        )
        return matched >= math.ceil(len(question.get("eval_keywords", [])) * 0.5)
    elif question["type"] == "drawing":
        return None
    return False

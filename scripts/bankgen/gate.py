"""Reject new questions that restate an existing answer or stem."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "src/data/exams"


def _toks(text: str) -> set[str]:
    return {word for word in re.findall(r"[a-z0-9]+", text.lower()) if len(word) > 2}


def existing(exam: str) -> list[dict]:
    questions = []
    for path in sorted((ROOT / exam).glob("q*.json")):
        questions.extend(json.loads(path.read_text()))
    return questions


def collisions(exam: str, questions: list[dict], answer_limit: float = 0.4, stem_limit: float = 0.5) -> list[str]:
    prior = existing(exam)
    problems = []
    for question in questions:
        answer = " ".join(question["choices"][index] for index in question["answer"])
        answer_tokens = _toks(answer)
        stem_tokens = _toks(question["stem"])
        worst_answer = 0.0
        worst_stem = 0.0
        answer_hit = ""
        stem_hit = ""
        for other in prior:
            other_answer = " ".join(other["choices"][index] for index in other["answer"])
            other_answer_tokens = _toks(other_answer)
            other_stem_tokens = _toks(other["stem"])
            if answer_tokens and other_answer_tokens:
                score = len(answer_tokens & other_answer_tokens) / len(answer_tokens | other_answer_tokens)
                if score > worst_answer:
                    worst_answer = score
                    answer_hit = other["id"]
            if stem_tokens and other_stem_tokens:
                score = len(stem_tokens & other_stem_tokens) / len(stem_tokens | other_stem_tokens)
                if score > worst_stem:
                    worst_stem = score
                    stem_hit = other["id"]
        if worst_answer >= answer_limit or worst_stem >= stem_limit:
            problems.append(
                f"{question['id']} too close to existing "
                f"(answer {worst_answer:.2f} vs {answer_hit}, stem {worst_stem:.2f} vs {stem_hit})"
            )
    # Also compare the new questions with each other.
    for index, question in enumerate(questions):
        answer = " ".join(question["choices"][i] for i in question["answer"])
        answer_tokens = _toks(answer)
        stem_tokens = _toks(question["stem"])
        for other in questions[index + 1 :]:
            other_answer = " ".join(other["choices"][i] for i in other["answer"])
            other_answer_tokens = _toks(other_answer)
            other_stem_tokens = _toks(other["stem"])
            answer_score = (
                len(answer_tokens & other_answer_tokens) / len(answer_tokens | other_answer_tokens)
                if answer_tokens and other_answer_tokens
                else 0
            )
            stem_score = (
                len(stem_tokens & other_stem_tokens) / len(stem_tokens | other_stem_tokens)
                if stem_tokens and other_stem_tokens
                else 0
            )
            if answer_score >= answer_limit or stem_score >= stem_limit:
                problems.append(
                    f"{question['id']} too close to {other['id']} (answer {answer_score:.2f}, stem {stem_score:.2f})"
                )
    return problems

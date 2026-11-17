"""Helpers for authoring original practice questions. Not used at runtime."""

from __future__ import annotations

import json
from pathlib import Path


PROBLEMS: list[str] = []


def item(prefix: str, number: int, objective: str, difficulty: str, stem: str, choices: list[str], answer, why: str, notes: list[str]):
    if isinstance(answer, int):
        answer = [answer]
    select = len(answer)
    question = {
        "id": f"{prefix}-{number:03d}",
        "domain": objective.split(".")[0],
        "objective": objective,
        "difficulty": difficulty,
        "select": select,
        "stem": " ".join(stem.split()),
        "choices": choices,
        "answer": answer,
        "explanation": " ".join(why.split()),
        "choiceNotes": [" ".join(note.split()) for note in notes],
    }
    problems = []
    if len(question["stem"]) < 80:
        problems.append("stem")
    if len(question["explanation"]) < 80:
        problems.append("explanation")
    if len(choices) < 4 or len(set(choices)) != len(choices):
        problems.append("choices")
    if len(notes) != len(choices) or any(len(note) < 40 for note in question["choiceNotes"]):
        problems.append("notes")
    if select not in (1, 2):
        problems.append("select")
    if problems:
        short = [note for note in question["choiceNotes"] if len(note) < 40]
        PROBLEMS.append(f"{question['id']} failed: {', '.join(problems)} {short}")
    return question


def dump(exam_dir: str, groups: dict[str, list[dict]]) -> None:
    if PROBLEMS:
        raise SystemExit("\n".join(PROBLEMS))
    root = Path(__file__).resolve().parents[2] / "src/data/exams" / exam_dir
    root.mkdir(parents=True, exist_ok=True)
    for name, questions in groups.items():
        path = root / name
        path.write_text(json.dumps(questions, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {path} ({len(questions)})")

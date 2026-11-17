import { readdir, readFile } from 'node:fs/promises';
import path from 'node:path';

const root = path.resolve('src/data/exams');
const minimums = {
  'n10-009': 150,
  '220-1101': 120,
  '220-1102': 120,
  'sy0-701': 150,
};
const passMarks = {
  'n10-009': 720,
  '220-1101': 675,
  '220-1102': 700,
  'sy0-701': 750,
};

const errors = [];
const fail = (message) => errors.push(message);

const examDirs = (await readdir(root, { withFileTypes: true }))
  .filter((entry) => entry.isDirectory())
  .map((entry) => entry.name)
  .sort();

if (examDirs.length < 3) fail(`Expected at least 3 exams, found ${examDirs.length}.`);

const seenIds = new Set();
const seenStems = new Set();

for (const dir of examDirs) {
  const examPath = path.join(root, dir, 'exam.json');
  let exam;
  try {
    exam = JSON.parse(await readFile(examPath, 'utf8'));
  } catch (error) {
    fail(`${dir}: could not read exam.json (${error.message})`);
    continue;
  }
  if (exam.id !== dir) fail(`${dir}: exam id ${exam.id} does not match the folder.`);
  for (const field of ['code', 'name', 'title', 'summary', 'studyUrl', 'studyLabel', 'accent']) {
    if (typeof exam[field] !== 'string' || exam[field].trim().length < 3) fail(`${dir}: missing ${field}.`);
  }
  if (!exam.studyUrl?.startsWith('https://www.professormesser.com/')) {
    fail(`${dir}: studyUrl must be an https://www.professormesser.com/ course page.`);
  }
  if (exam.minutes !== 90 || exam.examQuestions !== 90) fail(`${dir}: timed exam should be 90 questions and 90 minutes.`);
  if (passMarks[dir] != null && exam.passScaled !== passMarks[dir]) {
    fail(`${dir}: pass mark ${exam.passScaled} does not match the published ${passMarks[dir]}.`);
  }
  if (!Array.isArray(exam.domains) || exam.domains.length === 0) {
    fail(`${dir}: domains are missing.`);
    continue;
  }
  const weight = exam.domains.reduce((sum, domain) => sum + domain.weight, 0);
  if (weight !== 100) fail(`${dir}: domain weights add up to ${weight}, not 100.`);

  const objectives = new Map();
  for (const domain of exam.domains) {
    if (!domain.id || !domain.name || !Array.isArray(domain.objectives)) {
      fail(`${dir}: a domain is missing id, name, or objectives.`);
      continue;
    }
    for (const objective of domain.objectives) {
      if (!objective.id?.startsWith(`${domain.id}.`)) {
        fail(`${dir}: objective ${objective.id} is not inside domain ${domain.id}.`);
      }
      objectives.set(objective.id, domain.id);
    }
  }

  const files = (await readdir(path.join(root, dir))).filter((name) => /^q.*\.json$/.test(name)).sort();
  if (files.length === 0) fail(`${dir}: no question files matching q*.json.`);
  const questions = [];
  for (const file of files) {
    const full = path.join(root, dir, file);
    let parsed;
    try {
      parsed = JSON.parse(await readFile(full, 'utf8'));
    } catch (error) {
      fail(`${dir}/${file}: invalid JSON (${error.message})`);
      continue;
    }
    if (!Array.isArray(parsed)) {
      fail(`${dir}/${file}: question file must be an array.`);
      continue;
    }
    questions.push(...parsed.map((question) => ({ question, file })));
  }

  const minimum = minimums[dir] ?? 1;
  if (questions.length < minimum) fail(`${dir}: ${questions.length} questions is below the minimum of ${minimum}.`);

  const byDomain = new Map();
  const byObjective = new Map();
  let multi = 0;
  let easy = 0;
  let hard = 0;

  for (const { question, file } of questions) {
    const where = `${dir}/${file} ${question.id ?? '(no id)'}`;
    if (typeof question.id !== 'string' || !/^[a-z0-9]+-\d{3,}$/.test(question.id)) fail(`${where}: id is missing or not like n10-001.`);
    if (seenIds.has(question.id)) fail(`${where}: duplicate id.`);
    seenIds.add(question.id);
    if (typeof question.stem !== 'string' || question.stem.trim().length < 80) fail(`${where}: stem is too short.`);
    if (seenStems.has(question.stem)) fail(`${where}: duplicate stem.`);
    seenStems.add(question.stem);
    if (!['easy', 'medium', 'hard'].includes(question.difficulty)) fail(`${where}: difficulty must be easy, medium, or hard.`);
    if (question.difficulty === 'easy') easy += 1;
    if (question.difficulty === 'hard') hard += 1;
    if (question.select !== 1 && question.select !== 2) fail(`${where}: select must be 1 or 2.`);
    if (question.select === 2) {
      multi += 1;
      if (!/choose two/i.test(question.stem)) fail(`${where}: choose-two stem must say Choose two.`);
    } else if (/choose two/i.test(question.stem)) {
      fail(`${where}: stem says Choose two but select is 1.`);
    }
    if (!Array.isArray(question.choices) || question.choices.length < 4) fail(`${where}: need at least 4 choices.`);
    if (new Set(question.choices).size !== question.choices?.length) fail(`${where}: choices must be unique.`);
    if (question.choices?.some((choice) => typeof choice !== 'string' || choice.trim().length < 2)) {
      fail(`${where}: a choice is empty.`);
    }
    if (!Array.isArray(question.answer) || question.answer.length !== question.select) {
      fail(`${where}: answer length must match select.`);
    } else if (new Set(question.answer).size !== question.answer.length) {
      fail(`${where}: answer indexes repeat.`);
    } else if (question.answer.some((index) => !Number.isInteger(index) || index < 0 || index >= question.choices.length)) {
      fail(`${where}: answer index is out of range.`);
    }
    if (typeof question.explanation !== 'string' || question.explanation.trim().length < 80) {
      fail(`${where}: explanation is missing or too short.`);
    }
    if (!Array.isArray(question.choiceNotes) || question.choiceNotes.length !== question.choices?.length) {
      fail(`${where}: choiceNotes must match the choices.`);
    } else if (question.choiceNotes.some((note) => typeof note !== 'string' || note.trim().length < 40)) {
      fail(`${where}: every choice needs its own note of at least 40 characters.`);
    }
    const domainId = objectives.get(question.objective);
    if (!domainId) fail(`${where}: objective ${question.objective} is not on this exam.`);
    if (question.domain !== domainId) fail(`${where}: domain ${question.domain} does not own objective ${question.objective}.`);
    byDomain.set(question.domain, (byDomain.get(question.domain) ?? 0) + 1);
    byObjective.set(question.objective, (byObjective.get(question.objective) ?? 0) + 1);
  }

  if (multi < 4) fail(`${dir}: need at least 4 choose-two questions, found ${multi}.`);
  if (questions.length > 0) {
    if (easy / questions.length < 0.15) fail(`${dir}: easy questions are under 15%.`);
    if (hard / questions.length < 0.12) fail(`${dir}: hard questions are under 12%.`);
  }
  for (const domain of exam.domains) {
    const count = byDomain.get(domain.id) ?? 0;
    if (count === 0) fail(`${dir}: domain ${domain.id} has no questions.`);
    const share = questions.length ? count / questions.length : 0;
    if (Math.abs(share - domain.weight / 100) > 0.05) {
      fail(`${dir}: domain ${domain.id} is ${(share * 100).toFixed(1)}% of the bank, weight is ${domain.weight}%.`);
    }
  }
  for (const objectiveId of objectives.keys()) {
    if ((byObjective.get(objectiveId) ?? 0) < 2) {
      fail(`${dir}: objective ${objectiveId} has fewer than 2 questions.`);
    }
  }
  console.log(`${exam.code}: ${questions.length} questions, ${multi} choose-two.`);
}

if (errors.length) {
  console.error(`\n${errors.length} question-bank problem${errors.length === 1 ? '' : 's'}:`);
  for (const error of errors) console.error(`- ${error}`);
  process.exit(1);
}
console.log('Question bank looks structurally sound.');

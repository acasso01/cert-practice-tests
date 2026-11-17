import type { Exam, ExamMeta, Question } from '../types';

const metaModules = import.meta.glob('./exams/*/exam.json', {
  eager: true,
  import: 'default',
}) as Record<string, ExamMeta>;

const questionModules = import.meta.glob('./exams/*/q*.json', {
  eager: true,
  import: 'default',
}) as Record<string, Question[]>;

const ORDER = ['n10-009', '220-1101', '220-1102'];

function questionsFor(folder: string): Question[] {
  return Object.entries(questionModules)
    .filter(([path]) => path.includes(`/exams/${folder}/`))
    .sort(([a], [b]) => a.localeCompare(b))
    .flatMap(([, questions]) => questions);
}

export function loadExams(): Exam[] {
  const exams = Object.entries(metaModules).map(([path, meta]) => {
    const folder = path.split('/').at(-2) ?? meta.id;
    return { ...meta, questions: questionsFor(folder) };
  });
  return exams.sort((a, b) => {
    const ai = ORDER.indexOf(a.id);
    const bi = ORDER.indexOf(b.id);
    if (ai === -1 && bi === -1) return a.name.localeCompare(b.name);
    if (ai === -1) return 1;
    if (bi === -1) return -1;
    return ai - bi;
  });
}

export function objectiveName(exam: Exam, objectiveId: string): string {
  for (const domain of exam.domains) {
    const found = domain.objectives.find((objective) => objective.id === objectiveId);
    if (found) return found.name;
  }
  return 'Objective';
}

export function domainName(exam: Exam, domainId: string): string {
  return exam.domains.find((domain) => domain.id === domainId)?.name ?? 'Domain';
}

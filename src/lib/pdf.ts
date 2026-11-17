import { jsPDF } from 'jspdf';
import type { Attempt, Exam, Question } from '../types';
import { domainName, objectiveName } from '../data/loadExams';
import { SCALE_MAX, SCALE_MIN } from './score';

function pdfSafe(text: string): string {
  return text
    .replace(/\u2019|\u2018/g, "'")
    .replace(/\u201c|\u201d/g, '"')
    .replace(/\u2013|\u2014/g, '-')
    .replace(/\u2026/g, '...')
    .replace(/\u00a0/g, ' ')
    .replace(/[^\x09\x0a\x0d\x20-\xff]/g, '');
}

type Doc = jsPDF;

function newPage(doc: Doc, exam: Exam): number {
  doc.addPage();
  return paintHeader(doc, exam);
}

function paintHeader(doc: Doc, exam: Exam): number {
  const width = doc.internal.pageSize.getWidth();
  doc.setFillColor(23, 32, 10);
  doc.rect(0, 0, width, 36, 'F');
  doc.setFont('helvetica', 'bold');
  doc.setFontSize(11);
  doc.setTextColor(214, 242, 92);
  doc.text('Certline', 40, 23);
  doc.setFont('helvetica', 'normal');
  doc.setTextColor(243, 241, 230);
  doc.text(pdfSafe(`${exam.title}  ·  ${exam.code}`), 92, 23);
  return 56;
}

function ensure(doc: Doc, exam: Exam, y: number, needed: number): number {
  const height = doc.internal.pageSize.getHeight();
  if (y + needed > height - 42) return newPage(doc, exam);
  return y;
}

function writeLines(
  doc: Doc,
  exam: Exam,
  text: string,
  y: number,
  options: { size?: number; style?: 'normal' | 'bold'; color?: [number, number, number]; indent?: number },
): number {
  const size = options.size ?? 11;
  const margin = 40 + (options.indent ?? 0);
  const width = doc.internal.pageSize.getWidth() - margin - 40;
  doc.setFont('helvetica', options.style ?? 'normal');
  doc.setFontSize(size);
  const color = options.color ?? [28, 33, 22];
  doc.setTextColor(color[0], color[1], color[2]);
  const lines = doc.splitTextToSize(pdfSafe(text), width) as string[];
  const lineHeight = size + 4;
  let cursor = y;
  for (const line of lines) {
    cursor = ensure(doc, exam, cursor, lineHeight);
    doc.setFont('helvetica', options.style ?? 'normal');
    doc.setFontSize(size);
    doc.setTextColor(color[0], color[1], color[2]);
    doc.text(line, margin, cursor);
    cursor += lineHeight;
  }
  return cursor;
}

export function downloadAttemptPdf(exam: Exam, attempt: Attempt, questions: Map<string, Question>): void {
  const doc = new jsPDF({ unit: 'pt', format: 'letter' });
  let y = paintHeader(doc, exam);
  const when = new Date(attempt.completedAt).toLocaleString();
  y = writeLines(doc, exam, attempt.passed ? 'Result: Pass' : 'Result: Fail', y, {
    size: 18,
    style: 'bold',
    color: attempt.passed ? [31, 122, 58] : [180, 35, 24],
  });
  y += 4;
  y = writeLines(
    doc,
    exam,
    `${attempt.correct} of ${attempt.total} correct  ·  ${Math.round(attempt.percent)}%  ·  scaled ${attempt.scaled} (pass mark ${exam.passScaled})`,
    y,
    { size: 12, style: 'bold' },
  );
  y = writeLines(
    doc,
    exam,
    `${attempt.mode === 'exam' ? 'Exam mode' : 'Practice mode'}  ·  ${when}  ·  ${
      attempt.endedBy === 'time' ? 'Submitted when time expired' : 'Submitted by you'
    }`,
    y,
    { size: 10, color: [70, 74, 62] },
  );
  y += 6;
  y = writeLines(
    doc,
    exam,
    `Scaled score is an approximation. This app maps the raw percent onto ${SCALE_MIN}-${SCALE_MAX} with a straight line (100 + percent correct x 8). CompTIA uses a statistical scale, so an official score will not match this number exactly.`,
    y,
    { size: 10, color: [70, 74, 62] },
  );
  y += 8;
  y = writeLines(doc, exam, 'Domain breakdown', y, { size: 14, style: 'bold' });
  y += 2;
  for (const stat of attempt.domains) {
    if (stat.total === 0) continue;
    const pct = Math.round((stat.correct / stat.total) * 100);
    const weak = pct < 70 ? '  ·  review this domain' : '';
    y = writeLines(
      doc,
      exam,
      `${stat.id}.0 ${domainName(exam, stat.id)}: ${stat.correct}/${stat.total} (${pct}%)${weak}`,
      y,
      { size: 11 },
    );
  }

  attempt.items.forEach((item, index) => {
    const question = questions.get(item.qid);
    y += 10;
    y = writeLines(
      doc,
      exam,
      `Question ${index + 1}  ·  ${item.correct ? 'Correct' : 'Incorrect'}${item.flagged ? '  ·  Flagged' : ''}`,
      y,
      { size: 13, style: 'bold', color: item.correct ? [31, 122, 58] : [180, 35, 24] },
    );
    if (!question) {
      y = writeLines(doc, exam, 'This question is no longer in the bank.', y, { size: 11 });
      return;
    }
    y = writeLines(
      doc,
      exam,
      `${exam.code} objective ${question.objective} ${objectiveName(exam, question.objective)}  ·  ${question.difficulty}  ·  ${
        question.select === 2 ? 'Choose two' : 'One answer'
      }`,
      y,
      { size: 10, color: [70, 74, 62] },
    );
    y = writeLines(doc, exam, question.stem, y + 2, { size: 11 });
    y += 2;
    item.choiceOrder.forEach((original, display) => {
      const letter = String.fromCharCode(65 + display);
      const picked = item.selected.includes(original);
      const right = question.answer.includes(original);
      const tags = [picked ? 'your answer' : '', right ? 'correct' : ''].filter(Boolean).join(', ');
      y = writeLines(
        doc,
        exam,
        `${letter}. ${question.choices[original]}${tags ? `  [${tags}]` : ''}`,
        y,
        { size: 11, style: picked || right ? 'bold' : 'normal' },
      );
      y = writeLines(doc, exam, question.choiceNotes[original] ?? '', y, {
        size: 10,
        indent: 14,
        color: [70, 74, 62],
      });
    });
    if (item.selected.length === 0) {
      y = writeLines(doc, exam, 'Your answer: not answered', y, { size: 11, style: 'bold' });
    }
    y = writeLines(doc, exam, `Why: ${question.explanation}`, y + 2, { size: 11 });
  });

  y += 12;
  y = writeLines(
    doc,
    exam,
    `Study resource: ${exam.studyLabel} — ${exam.studyUrl}`,
    y,
    { size: 10, color: [70, 74, 62] },
  );
  y = writeLines(
    doc,
    exam,
    'Certline is not affiliated with CompTIA or Professor Messer. CompTIA, Network+, and A+ are trademarks of CompTIA. Questions in this export are original practice items.',
    y,
    { size: 9, color: [90, 94, 82] },
  );

  const pages = doc.getNumberOfPages();
  for (let page = 1; page <= pages; page += 1) {
    doc.setPage(page);
    const height = doc.internal.pageSize.getHeight();
    const width = doc.internal.pageSize.getWidth();
    doc.setFont('helvetica', 'normal');
    doc.setFontSize(9);
    doc.setTextColor(120, 124, 110);
    doc.text(`Page ${page} of ${pages}`, width - 110, height - 24);
  }

  const stamp = new Date(attempt.completedAt).toISOString().slice(0, 10);
  doc.save(`certline-${exam.id}-${stamp}.pdf`);
}

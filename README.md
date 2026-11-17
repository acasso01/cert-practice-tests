# Certline

Free, original practice for **CompTIA Network+ (N10-009)** and **CompTIA A+ Core 1 (220-1101)** and **Core 2 (220-1102)**.

Certline runs entirely in the browser. There is no account and no server. Scores, missed questions, and the current session stay in this browser's storage.

The live site is intended for GitHub Pages:

https://acasso01.github.io/cert-practice-tests/

## What you can do

- Pick an exam and study in **practice** mode. You choose 10, 25, 50, 90, or a custom count, and you can limit the set to specific domains. Each answer is marked immediately, with an explanation of the right choice and of every wrong one.
- Sit a **timed exam**. A full set is 90 questions and 90 minutes. Shorter sets get one minute per question. You can flag questions, jump around a navigator, and you do not see answers until you submit. Unanswered questions are wrong.
- Read a **results** page with a percent, an approximate scaled score, pass or fail, a domain breakdown, and a review of every question.
- **Download a PDF** of that completed test from the results page. The file is built in the browser.
- Come back to **history** and a missed-question deck. **Retry missed** builds a new practice set from what you got wrong.

Questions and answer order are shuffled each time you start.

### Scores

CompTIA reports a scaled score from 100 to 900. This app draws a straight line across that range:

`scaled = 100 + (percent correct × 8)`

Pass marks used here are the published ones: **Network+ 720**, **A+ Core 1 675**, **A+ Core 2 700**. A real exam is scaled statistically, so treat this number as a study signal. The results page says the same thing. The real exams also include performance-based questions, which this site does not simulate.

## Run it locally

You need Node.js 22.

```bash
npm install
npm run dev
```

Open http://127.0.0.1:5173/cert-practice-tests/

The dev server uses the same `/cert-practice-tests/` base path as GitHub Pages, so asset URLs match production.

```bash
npm run validate   # check the question bank
npm run build      # typecheck and build into dist/
npm run preview    # serve dist/ at http://127.0.0.1:4173/cert-practice-tests/
```

## Add another exam

Drop a folder in `src/data/exams/<exam-id>/`:

- `exam.json` describes the exam: id (must match the folder), code, name, domains, objective names, weights, minutes, question count, pass mark, and the Professor Messer course URL.
- `q*.json` files are arrays of questions. Every array in the folder is concatenated. A single `questions.json` renamed to match `q*.json` is enough.

Then reload. No React changes are required. `npm run validate` enforces the shape:

- at least four choices
- `select` of 1 or 2, matching the answer indexes
- an explanation and a note for every choice
- an objective that exists on that exam
- a `https://www.professormesser.com/` study URL on the exam
- the minimum bank sizes for the three exams shipped here

Study links point at the free course index for that exam. They are not deep links to individual videos.

Example question:

```json
{
  "id": "sec-001",
  "domain": "1",
  "objective": "1.1",
  "difficulty": "medium",
  "select": 1,
  "stem": "A scenario of at least a sentence, written for this bank.",
  "choices": ["Right", "Wrong A", "Wrong B", "Wrong C"],
  "answer": [0],
  "explanation": "Why the right choice is right, in plain language.",
  "choiceNotes": [
    "Why this choice is right.",
    "Why this choice is wrong.",
    "Why this choice is wrong.",
    "Why this choice is wrong."
  ]
}
```

Use `"select": 2` and two answer indexes for a choose-two item, and put `(Choose two.)` in the stem.

The banks in this repo were authored with the Python helpers in `scripts/bankgen/`. Those helpers are optional. The app reads only the JSON.

## Keyboard

- `1`–`4` or `A`–`D` selects an answer (`E` and `F` work when a question has more choices)
- `Enter` checks a choose-two item, or moves on after feedback
- `F` flags a question in exam mode
- Arrow keys move between exam questions

## Deploy

`.github/workflows/pages.yml` validates the bank, builds the site, and deploys `dist/` with `actions/deploy-pages` when that workflow runs on `main`.

GitHub still has to be told to use the workflow:

**Settings → Pages → Build and deployment → Source: GitHub Actions**

If that source is not selected, the workflow can upload an artifact and still have nowhere to publish it.

## Disclaimer

Certline is an independent study tool. It is **not** affiliated with, endorsed by, or sponsored by CompTIA or Professor Messer.

CompTIA, Network+, A+, and Security+ are trademarks of CompTIA. Professor Messer's name is used only to point at his free public course index for the matching exam. The questions here were written for this project. They are not copied from Professor Messer, Jason Dion, ExamCompass, CompTIA, or any other publisher.

A+ 220-1101 and 220-1102 are the objective sets this bank follows. CompTIA has since released 220-1201 and 220-1202. Use this bank for the 1100-series objectives.

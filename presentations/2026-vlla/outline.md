# Zest at VLLA 2026: outline

**Status:** draft 3, for Kyle to approve before the slides are built.

| | |
|---|---|
| **Session (as listed)** | *From PhET to Keyboarding: How We Built an LTI Tool That Turns Any Web Interactive into a Gradable Canvas Assignment* |
| **When / where** | Friday, October 2, 2026, 9:40-10:10 am (Spark Plus sessions), MacArthur room |
| **Track** | Technology |
| **Slot** | 30 min = 25 min talk and demos + 5 min questions |
| **Audience** | leaders of state and district virtual learning programs |
| **Deck** | Google Slides, a copy of the Geometric VA Template |

## What the published abstract promises (the outline keeps every one)

1. Rich interactives have always been hard to turn into graded coursework in an LMS.
2. Zest takes any HTML/JavaScript interactive and makes it a Canvas assignment with
   grade passback and a teacher review mode, auto- or hand-graded; the same
   interactives can also go straight into Canvas pages as live elements.
3. **How it was built**, and how it was formalized into an open, published
   specification, so it is a reusable standard any program can adopt, not a one-off.
4. **The curriculum side**: what Virtual Arkansas is actually running.
5. How any interactive built with AI can become a self-grading or manually graded
   assignment.
6. A live demonstration, then Q&A.

## The hook

Anyone who can describe an activity in plain language can now have AI build it,
and Zest turns what the AI builds into a real, graded Canvas assignment. No
developer, no vendor, no code. The rest of the talk proves that what comes out is
usable and safe in a real program.

Working slide title: **"Describe it. AI builds it. Canvas grades it."**

## Time budget

| # | Section | Slides | Min | Ends at |
|---|---------|--------|-----|---------|
| 1 | Hook: one sentence in, a graded activity out | 1-3 | 2:30 | 2:30 |
| 2 | Watch it happen (recording of a zest being built) | 4 | 3:00 | 5:30 |
| 3 | The missing piece: making it count in Canvas | 5-6 | 3:00 | 8:30 |
| 4 | From PhET to Keyboarding: what we run (live demo) | 7-9 | 5:00 | 13:30 |
| 5 | Wow gallery: sentences that became activities | 10-14 | 5:00 | 18:30 |
| 6 | How we built it: an open standard, with guardrails | 15-16 | 3:00 | 21:30 |
| 7 | Built for real schools | 17 | 1:30 | 23:00 |
| 8 | What's next and get the code | 18-19 | 2:00 | 25:00 |
| 9 | Questions | 20 | 5:00 | 30:00 |

Buffer if running long: in section 5, show two gallery zests live and leave the
others as image + link only (saves about 1:30).

## Slides

### 1. Hook (2:30)

**Slide 1: Title** (0:20). "Describe it. AI builds it. Canvas grades it." Subtitle:
the session title as listed. Kyle Yancey, Virtual Arkansas.

**Slide 2: "Who can build interactive content in your program?"** (1:00).
Three answers: *a developer* / *a vendor* / *nobody*. Ask for hands: "Who has a
teacher with a great idea for an interactive and no way to build it?" The
bottleneck has never been ideas; it has been who can build them, and then how
to grade what gets built.

**Slide 3: One sentence** (1:10). One teacher-written sentence, large:
> "Make a projectile motion lab where students predict the launch angle to hit a
> target, auto-graded, with the target distance set by the teacher."

A click reveals the finished activity (image of Launch Lab). "That sentence is all
a person wrote. Let me show you what happened in between."

### 2. Watch it happen (3:00)

**Slide 4: The recording** (3:00). Claude Code with the zest-creator workspace:
the request goes to `/zest-new`; Claude asks plain questions (graded? save
progress? teacher settings?); it writes the activity; `/zest-build` checks and
packages it; the `.zest` file is uploaded through the Canvas editor button; a
student plays it and the score lands. About 90 s of footage at 8-10x, narrated
live. No code is shown on purpose: the teacher never reads any.

### 3. The missing piece: making it count (3:00)

**Slide 5: "An interactive isn't coursework yet"** (1:15). AI can make an
interactive web page today. On its own it is a link: separate logins, no grade,
no record of the student's work. That is the problem Zest was built to solve,
for PhET-style simulations first and now for anything a browser can run.

**Slide 6: What Zest is** (1:45). One sentence and one diagram:
"Zest turns any HTML/JavaScript interactive into a Canvas assignment, graded
automatically or by the teacher, or drops it into a Canvas page as a live element."
Diagram: teacher → "Embed Interactive Content" button in Canvas → Zest (runs on
your server) → the activity → score in the gradebook / the student's work in
SpeedGrader. A package (a *Zestable*, a `.zest` file) is plain HTML, CSS and JS plus
a small manifest; optional review page, settings editor, and an answer key
students never see.

### 4. From PhET to Keyboarding: what we run (5:00)

**Slide 7: From PhET...** (1:00). Where it started: physics simulations in the
PhET style, each with an *explore* mode (students save observations, teacher
grades) and a *challenge* mode (auto-graded), and simulations wrapped with
Predict / Explore / Explain prompts a teacher sets. [Kyle: confirm which PhET
work to show and what courses use it.]

**Slide 8: ...to Keyboarding: live demo** (3:00). In Kyle's Canvas (recording as
backup):
1. Teacher: editor button → pick Keyboarding Practice from the shared library →
   set the passage for this course.
2. Student: types the passage, submits; the gradebook cell fills in (scaled to
   the assignment's points).
3. Teacher: opens the student's attempt in SpeedGrader, shown by the package's
   own review card.
4. The work follows the student: reopen on another device, it is all there.

**Slide 9: One package, many courses** (1:00). The same package set up
differently in each course; a fixed version applied to every installed copy in
one step, without breaking a link or losing student work. Works on managed
Chromebooks that block third-party cookies.

### 5. Wow gallery (5:00)

**Slide 10: "Every one of these started as a sentence"** (0:20). Four tiles.
"These are on my sandbox; the links are on each slide."

**Slides 11-14: one slide per zest** (about 1:10 each). Left: **the prompt that
made it**, verbatim. Right: an image of the zest and a short link / QR code to
Kyle's sandbox. Badge: how it is graded.

| Zest | Subject | Grading | What it shows off |
|------|---------|---------|-------------------|
| **Launch Lab**: projectile motion | Physics | Auto | Predict the angle, fire, see the arc; scored on hits. A simulation, not a question. |
| **Graph Match**: function transformations | Algebra | Auto, with a **teacher settings editor** | Drag sliders to match a target curve; the teacher sets the targets in an editor the AI also built. |
| **Sketch & Label** a diagram | Life science | Teacher-graded | Students draw and label; SpeedGrader shows the actual drawing and replays it stroke by stroke. |
| **Escape the Archive** | History / ELA | Auto | A short escape room: each lock opens with evidence from a primary source. |

Each zest was built the way a teacher would build it: the prompt on its slide
through `/zest-new` and `/zest-build`. The prompt and any follow-up requests are
kept in `zests/<slug>/PROMPT.md`, so the slides are honest about what one
sentence produced.

### 6. How we built it: an open standard, with guardrails (3:00)

**Slide 15: Not a one-off: a published specification** (1:30). Zest was built
with Claude Code at Virtual Arkansas, then written down as the **Zest
Specification**: the package format and the Bridge API a package uses to talk to
the LMS. Any program can build to it, and a package made for one Zest server
runs on any other. The authoring workspace (zest-creator) is a template anyone
can open in Claude Code. [Kyle: zest-spec and zest-creator are public; put
their links here? The server stays private until release.]

**Slide 16: Can you trust what the AI made?** (1:30).
- Every package is checked when it is built (structure, grading wiring, blocked
  file types, things Canvas silently breaks)
- A security-review agent checks it for data exfiltration and tracking
- The server runs every package sandboxed, with a content security policy and
  permissions denied by default
- A person tests it as a student before assigning it; a subject expert checks
  the content
- Auto-graded is for practice and low stakes (scores are computed in the
  browser); use teacher grading for anything high-stakes

### 7. Built for real schools (1:30)

**Slide 17: The boring parts, done.** Icons and a few words each:
- Runs on your server: student data stays with you; no third-party tracking
- Managed Chromebooks; sessions that end when idle; short-lived, rotating tokens
- Encrypted nightly backups (local, S3-compatible, Google Drive, OneDrive) and a
  written restore runbook
- Every change tested with real launches from teacher, student and admin seats,
  and an upgrade rehearsal from the release in production

### 8. What's next and get the code (2:00)

**Slide 18: What's next** (0:45). Server source release under the MIT license;
a separate content origin (the next security step); an accessibility pass;
other LMSs (research done for Brightspace, Schoology and Buzz).

**Slide 19: Get the code** (1:15). Big QR code → Google Form
`[[FORM URL PLACEHOLDER: Kyle to supply]]` with a short link beside it, and
Kyle's contact. Closing line: "If your teachers can describe it, they can build
it." Small print: "Zest" and "Zestable" are trademarks of Virtual Arkansas
(applications pending).

### 9. Questions (5:00)

**Slide 20: Questions** (the Form QR code stays visible). Short answers go in
`speaker-notes.md`. Expected first: what Claude Code costs; does student data go
to the AI (no: the AI only sees the author's description while building; the
server has no AI in it and never sends student work anywhere); who reviews what
the AI builds; can it be wrong. Then: cost and hosting, privacy, other LMSs,
who can author, accessibility, support, when the server code comes out.

## Honest limits (for the notes and Q&A, not big slide text)

- "Non-technical" means no programming. The author still uses Claude Code (a
  paid Claude plan) with the zest-creator workspace and tests the result as a
  student. AI can get content wrong (a fact, an answer key), so a subject expert
  reviews it like any other material.
- Scores are computed in the browser: use teacher grading for high stakes.
- Packages run on the tool's own web origin today, so programs should upload
  packages they trust; a separate content origin is the next security step.
- Canvas is the only LMS today.
- Accessibility pass planned; no WCAG conformance claim.

## Left off the slides on purpose

- Production numbers (Kyle: not needed for this audience)
- getzest.dev (the domain is not bought)
- A zest-server GitHub link (the repo is private)

## Media plan

- Images of each gallery zest (taken here); Kyle hosts the zests on his sandbox
  and supplies the links, which become the QR codes.
- Screen recordings in Kyle's Google Drive, not the repo: the build recording
  (slide 4) and a backup of the Keyboarding live demo (slide 8).
- Screenshots use made-up people only (Avery Student, Blake Student, Taylor
  Teacher, Morgan Admin).

## Open items for Kyle

1. Google Form URL (slide 19).
2. Sandbox links for the four gallery zests, once uploaded.
3. The PhET part (slide 7): which work to show, and which courses run it.
4. Links to zest-spec and zest-creator on slide 15: yes or no?
5. The build recording (slide 4): your own Claude Code screen, or one scripted
   and recorded here? And is the projectile sentence the right one?

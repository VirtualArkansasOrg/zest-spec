# Zest at VLLA 2026: outline

**Status:** first draft for Kyle to react to. Nothing on the slides is final until
the numbers, links and form URL are confirmed (see "Open items" at the bottom).

- **Slot:** 30 min = 25 min talk and demos + 5 min questions
- **Audience:** leaders of state and district virtual learning programs (to confirm)
- **Deck:** Google Slides, copied from a Virtual Arkansas template (recommended:
  Simple One Color VA Template)
- **Rule for every live demo:** a recorded backup video sits on the next slide (or
  is linked from the demo slide), so a dead network costs nothing but a click.

## Working title

**Describe it. AI builds it. Canvas grades it.**
Subtitle: "How non-technical teachers use AI to make interactive, graded Canvas activities"

## The one idea

Anyone who can describe an activity in plain language can now have AI build it
as a real, graded Canvas assignment: no developer, no vendor, no code. Everything
else in the talk (the gradebook, SpeedGrader, Chromebooks, security) is the proof
that what the AI makes is safe and usable in a real program.

## Time budget

| # | Section | Slides | Minutes | Ends at |
|---|---------|--------|---------|---------|
| 1 | Hook: one sentence in, a graded activity out | 1-3 | 2:30 | 2:30 |
| 2 | Watch it happen | 4-5 | 4:00 | 6:30 |
| 3 | Wow gallery: what teachers' sentences became | 6-10 | 5:30 | 12:00 |
| 4 | And it counts: inside Canvas | 11-13 | 5:00 | 17:00 |
| 5 | Guardrails for AI-made content | 14-15 | 3:00 | 20:00 |
| 6 | Built for real schools | 16 | 2:30 | 22:30 |
| 7 | What's next + call to action | 17-18 | 2:30 | 25:00 |
| 8 | Questions | 19 | 5:00 | 30:00 |

Buffer: section 3 can drop to two live zests (others as QR codes only) to win back
a minute; section 4 can drop slide 13 to win back another.

## Slides

### 1. Hook (2:30)

**Slide 1: Title** (0:20). Title, Kyle's name, Virtual Arkansas logo.

**Slide 2: "Who can build interactive content in your program today?"** (1:00).
Three answers on screen: *a developer* / *a vendor* / *nobody*. Ask for hands:
"How many of you have a teacher with a great idea for an interactive activity
and no way to build it?" The bottleneck has never been ideas; it is who can
build them.

**Slide 3: One sentence** (1:10). A single teacher-written sentence, large:
> "Make a projectile motion lab where students predict the launch angle to hit a
> target, auto-graded, with the target distance set by the teacher."

Then a click reveals the finished activity beside it (screenshot of Launch Lab).
"This sentence is the only thing a person wrote. In the next four minutes you'll
watch that happen, and then it will be in the gradebook."

### 2. Watch it happen (4:00)

**Slide 4: The sped-up recording** (3:00). Claude Code with the zest-creator
workspace: the teacher types the request to `/zest-new`, Claude asks two or three
plain questions (graded? save progress? teacher settings?), writes the files,
`/zest-build` checks and packages it, then the `.zest` is uploaded through the
Canvas editor button and a student plays it. About 90 s of footage at 8-10x,
narrated live. No code is shown on purpose: the teacher never reads any.

**Slide 5: Three steps** (1:00). *Describe* → *Build and check* → *Upload in Canvas*.
Who this is for: teachers, instructional designers, course builders. What they
need: Claude Code and the zest-creator workspace; no programming.

### 3. Wow gallery (5:30)

**Slide 6: "Every one of these started as a sentence"** (0:30). Four tiles with QR
codes. "Take out your phone. These run in preview mode right now; in Canvas they
grade."

**Slides 7-10: one slide per zest** (about 1:15 each). Left: **the prompt that made
it**, verbatim. Right: screenshot and QR code. Badge: grading mode.

| Zest | Subject | Grading | What it shows off |
|------|---------|---------|-------------------|
| **Launch Lab**: projectile motion | Physics | Auto | Predict the angle, fire, see the arc; score from hits. A simulation, not a question. |
| **Graph Match**: function transformations | Algebra | Auto, **teacher editor** | Drag sliders to match a target curve; the teacher sets the targets in a settings editor the AI also built. |
| **Sketch & Label** a diagram | Life science | Teacher-graded | Student draws and labels; SpeedGrader shows their actual drawing and replays it stroke by stroke. |
| **Escape the Archive** (stretch) | History / ELA | Auto | A short escape room: locks open with evidence from primary sources. |

The gallery zests are built for this talk exactly the way a teacher would: from
the prompt on each slide, through `/zest-new` and `/zest-build`. The prompts and
build notes are kept in `zests/<slug>/PROMPT.md` so the slides are honest about
what the AI got from one sentence and what was refined in conversation.

### 4. And it counts: inside Canvas (5:00)

Told with Keyboarding Practice, the zest in production at Virtual Arkansas (live
in Kyle's Canvas, recording as backup).

**Slide 11: A teacher embeds it** (1:30). Rich Content Editor → "Embed
Interactive Content" → pick from the shared library → set the passage for this
placement. One package, different settings per course.

**Slide 12: The grade lands; the work is reviewable** (2:00). Student submits,
gradebook cell fills in (scaled to the assignment's points; failed posts retried).
Teacher opens the package's own review card in SpeedGrader, per attempt.

**Slide 13: It follows the student** (1:30). Work saved as they go, restored on
another device; managed Chromebooks that block third-party cookies work.
Production fact line (to confirm): "In production since May 2026 on two Canvas
tenants; Keyboarding Practice is in 16 course copies, and a fix went to all 16 in
one step."

### 5. Guardrails for AI-made content (3:00)

The question every leader in the room is asking: "Can I trust what the AI made?"

**Slide 14: Checked before it reaches a student** (1:45).
- `/zest-build` validates every package (structure, grading wiring, blocked file
  types, Canvas-breaking calls)
- A security-review agent checks for data exfiltration and tracking
- The server runs every package sandboxed, with a content security policy and
  permissions denied by default
- A person tests it as a student before assigning it

**Slide 15: Choose the right grading** (1:15). Auto-graded is for practice and
low stakes (scores are computed in the browser); teacher-graded for anything
high-stakes, with the student's real work in SpeedGrader. Only upload packages
your program trusts.

### 6. Built for real schools (2:30)

**Slide 16: The boring parts, done** (2:30). Icons + a few words each:
- Runs on your server: student data stays with you; no third-party tracking
- Sessions that end when idle; short-lived, rotating page tokens
- Encrypted nightly backups (local, S3-compatible, Google Drive, OneDrive) + a
  written restore runbook
- Update every installed copy at once without breaking links or losing work
- Every change tested with real launches from teacher, student and admin seats
  (88 checks) and an upgrade rehearsal from the production release (157 checks)

### 7. What's next + call to action (2:30)

**Slide 17: What's next** (1:00). Source release under the MIT license; a
separate content origin (next security step); accessibility pass; other LMSs
(research done for Brightspace, Schoology and Buzz).

**Slide 18: Get the code** (1:30). Big QR code → Google Form
`[[FORM URL PLACEHOLDER: Kyle to supply]]`, short link beside it, Kyle's contact.
Closing line: "If your teachers can describe it, they can build it."
"Zest" and "Zestable" are trademarks of Virtual Arkansas (applications pending).

### 8. Questions (5:00)

**Slide 19: Questions** (the QR code from slide 18 stays visible).
Short answers are in `speaker-notes.md`. Expect the AI questions first: what
does it cost to use Claude Code, does student data go to the AI (no: the AI
sees the teacher's description, never student work), who reviews what it
builds, can it be wrong. Then cost and hosting, privacy, other LMSs,
accessibility, support, release date.

## Honest limits (for notes and Q&A, not for big slide text)

- "Non-technical" means no programming; the author still uses Claude Code (a
  Claude subscription) with the zest-creator workspace, and should test the
  result as a student. The AI can make mistakes in content (a wrong fact, an
  answer key error), so a subject expert reviews it like any other material.

- Scores are computed in the browser; for high stakes use teacher grading.
- Packages run on the tool's own web origin today, so schools should upload
  packages they trust. A separate content origin is the next security step.
- Canvas is the only LMS today.
- An accessibility pass is planned; no WCAG conformance claim.

## Media plan

- `media/`: small screenshots only (picker, student view, gradebook cell,
  SpeedGrader card, each gallery zest, QR codes).
- Google Drive (Kyle's): the screen recordings (backup for every live demo, and the
  sped-up build, which is now the centrepiece of the talk; Kyle may need to
  capture his own screen for an authentic Claude Code session).
- Screenshots from the stand-in Canvas in zest-server's launch test use made-up
  people only (Avery Student, Blake Student, Taylor Teacher, Morgan Admin).

## Open items for Kyle

1. Confirm date, room setup (projector, wifi, can Kyle mirror a phone?) and audience.
2. Google Form URL for the final slide.
3. Canvas instance for installing the gallery zests, and the public links / QR
   targets once installed.
4. Current production numbers (version deployed, tenant count, course copies).
5. Whether getzest.dev can appear on a slide (currently: no).
6. Anything to include or leave out.
7. The build recording (slide 4): should it be your own Claude Code screen, or one I script and record here? Which prompt do you want the room to see?

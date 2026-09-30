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

**Zest: interactive activities that live inside Canvas, and count**
Subtitle: "Build it in plain language. Grade it in the gradebook. Run it on your own server."

## Time budget

| # | Section | Slides | Minutes | Ends at |
|---|---------|--------|---------|---------|
| 1 | Hook | 1-2 | 2:00 | 2:00 |
| 2 | What Zest is | 3-4 | 3:00 | 5:00 |
| 3 | End-to-end story: Keyboarding Practice | 5-8 | 6:00 | 11:00 |
| 4 | Wow gallery (room tries them on phones) | 9-13 | 5:00 | 16:00 |
| 5 | How zests get made | 14-15 | 4:00 | 20:00 |
| 6 | Built for real schools | 16-17 | 3:00 | 23:00 |
| 7 | What's next + call to action | 18-19 | 2:00 | 25:00 |
| 8 | Questions | 20 | 5:00 | 30:00 |

A 1-minute buffer is hidden in section 4: if things run long, show two of the
gallery zests live and leave the others as QR codes only.

## Slides

### 1. Hook (2:00)

**Slide 1: Title** (0:20). Zest logo text, title, Kyle's name, Virtual Arkansas logo.

**Slide 2: "Where does the good stuff live?"** (1:40). Three panels, few words:
*separate logins* / *no grades back* / *per-seat costs*. Question to the room:
"Show of hands: how many of your courses send students out of the LMS for the
interactive parts?" Point: the richest learning in a virtual course usually lives
somewhere the gradebook can't see.

### 2. What Zest is (3:00)

**Slide 3: One sentence + diagram** (1:45).
"Zest lets a teacher drop any interactive HTML activity into a Canvas page or
assignment, and the grade and the student's work come back to Canvas."
Diagram: Teacher → Canvas editor button → Zest server (yours) → activity in the
page → score in gradebook / work in SpeedGrader.

**Slide 4: What a zest is** (1:15). A `.zest` file = plain HTML, CSS and JS + a small
manifest. Optional: a SpeedGrader review page, a teacher settings editor, an
answer key students never see. "If it runs in a browser, it can be a zest."

### 3. End-to-end story: Keyboarding Practice (6:00)

The real production zest. Live in Kyle's Canvas, recording as backup.

**Slide 5: Teacher embeds it** (1:30). Rich Content Editor → "Embed Interactive
Content" → pick from the shared library → set the passage for this placement.
Screenshot of the picker + placement settings.

**Slide 6: Student types, grade lands** (1:45). Student view, submit, gradebook
cell fills in (scaled to the assignment's points; failed posts retried).

**Slide 7: Teacher reviews in SpeedGrader** (1:15). The package's own review card,
per attempt. "Start a new attempt" follows the assignment's attempt policy.

**Slide 8: It follows the student** (1:30). Close the laptop, open a Chromebook:
work restored. Works on managed Chromebooks that block third-party cookies.
Production fact line (to confirm): "In production since May 2026 on two Canvas
tenants; Keyboarding Practice is in 16 course copies, and a fix went to all 16 in
one step."

### 4. Wow gallery (5:00)

**Slide 9: "What a Canvas quiz can't do"** (0:30). Four tiles, each with a QR code.
"Take out your phone. These run in preview mode right now; in Canvas they grade."

**Slides 10-13: one slide per zest** (about 1:05 each). Big screenshot, one-line
caption, QR code, the grading mode as a badge. Planned zests (names are working
titles; see `zests/`):

| Zest | Subject | Grading | What it shows off |
|------|---------|---------|-------------------|
| **Launch Lab**: projectile motion | Physics | Auto | Predict the angle, fire, see the arc; score from hits. A simulation a quiz can't be. |
| **Graph Match**: function transformations | Algebra | Auto, **teacher editor** | Drag sliders to match a target curve. The teacher's `editor.html` sets the targets: one package, many settings. |
| **Sketch & Label** a diagram | Life science | Teacher-graded | Student draws and labels on a diagram; SpeedGrader shows their actual drawing and replays it stroke by stroke. |
| **Escape the Archive** (stretch) | History / ELA | Auto | A short escape room: locks open with evidence from primary sources. |

Every gallery zest works offline once loaded, uses no outside services or CDNs,
and needs no camera or microphone.

### 5. How zests get made (4:00)

**Slide 14: Describe it, get a package** (1:30). The prompt on screen:
"a ten-question quiz about the American Revolution, auto-graded, with hints the
teacher can turn off" → `/zest-new` writes it → `/zest-build` checks and packages
it → upload. A security-review agent checks every package for data exfiltration
and tracking.

**Slide 15: Sped-up recording** (2:30). One of the gallery zests being built from a
prompt in Claude Code, about 60-90 s at 8-10x, narrated live. Close with the
.zest being uploaded in the picker.

### 6. Built for real schools (3:00)

**Slide 16: The boring parts, done** (1:45). Icons + a few words each:
- Managed Chromebooks (cookieless launches)
- Sessions that end when idle; short-lived, rotating page tokens
- Packages sandboxed, permissions denied by default
- Encrypted nightly backups (local, S3-compatible, Google Drive, OneDrive) + a
  written restore runbook
- Update every installed copy at once, without breaking links or losing work

**Slide 17: Tested on every change** (1:15). "Every change: a real-launch test from
teacher, student and admin seats (88 checks) and an upgrade rehearsal from the
release in production (157 checks)." Your data stays on your server; no
third-party tracking.

### 7. What's next + call to action (2:00)

**Slide 18: What's next** (0:50). Source release under the MIT license; a
separate content origin (next security step); accessibility pass; other LMSs
(research done for Brightspace, Schoology and Buzz).

**Slide 19: Get the code** (1:10). Big QR code → Google Form
`[[FORM URL PLACEHOLDER: Kyle to supply]]`, short link beside it, Kyle's contact.
"Zest" and "Zestable" are trademarks of Virtual Arkansas (applications pending).

### 8. Questions (5:00)

**Slide 20: Questions** (stays up with the QR code from slide 19 visible).
Short answers are in `speaker-notes.md` (cost and hosting, privacy, other LMSs,
who can author, accessibility, support, release date, score integrity, trust in
uploaded packages).

## Honest limits (for notes and Q&A, not for big slide text)

- Scores are computed in the browser; for high stakes use teacher grading.
- Packages run on the tool's own web origin today, so schools should upload
  packages they trust. A separate content origin is the next security step.
- Canvas is the only LMS today.
- An accessibility pass is planned; no WCAG conformance claim.

## Media plan

- `media/`: small screenshots only (picker, student view, gradebook cell,
  SpeedGrader card, each gallery zest, QR codes).
- Google Drive (Kyle's): the screen recordings (backup for every live demo, and the
  sped-up build).
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

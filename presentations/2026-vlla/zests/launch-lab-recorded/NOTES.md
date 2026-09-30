# Launch lab, recorded run

Source files from the Claude Code session used for the VLLA 2026 build recording
(`zest-build-recording.mp4`). They are exactly what Claude Code wrote; nothing was edited afterwards.

- **Date:** 2026-09-30, about 19:33 to 19:36 (container clock)
- **Setup:** fresh copy of the zest-creator template (no .git, no dist/), Claude Code 2.1.285,
  its default model, `--permission-mode acceptEdits` and
  `--allowedTools 'Bash(node:*)' 'Bash(ls:*)' 'Bash(mkdir:*)' 'Bash(cat:*)'`, in tmux at 110x32.
- **Prompt typed (exact):**
  `/zest-new Make a projectile motion lab where students predict the launch angle to hit a target, auto-graded, with the target distance set by the teacher.`
- **Follow-up answers typed:** none. Claude Code did not ask any follow-up questions in this run;
  it chose its own defaults (one target at 45 m, 25 m/s, ±2 m, 3 launches, 100/80/60 points by
  launch, formula hint on) and listed them in its summary. The answers in `../launch-lab/PROMPT.md`
  were therefore not used, and this lab is simpler than `../launch-lab`.
- **Second command typed:** `/zest-build` (result: PASS, no errors or warnings,
  `dist/projectile-motion-lab.zest`, 10 KB, 3 files).
- **How long the real run took:** 2 min 53 s from pressing Enter on the prompt to the /zest-build
  result (the /zest-new part took 2 min 33 s by Claude Code's own counter, including a background
  security review; /zest-build took about 10 s). About 1 min 56 s of that was thinking before the
  first file was written.
- **Speed-up in the video (segment A):** typing at real time (a 6 s pause of mine between
  "/zest-new" and the sentence at 4x); the thinking stretch at 20x; writing files and the summary
  at 3x; the security review at 4x; /zest-build at real time. Two held frames (5 s on the summary,
  6 s on the build result) are marked "Paused".
- **Segment B included:** yes. The .zest was uploaded through the real Zest picker (zest-server
  copy, PostgreSQL 16, Chromium) inside the stand-in Canvas from
  `tests/regression/fake-platform.js`, as Taylor Teacher, keeping the default settings; then
  Avery Student launched it, fired 30° (miss, 55.2 m) and 22.4° (hit, 44.9 m) and submitted
  80 / 100. The stand-in gradebook received scoreGiven 8 of scoreMaximum 10, FullyGraded,
  comment "Hit the target on launch 2 of 3". Teacher part sped up 1.5x, student part real time.
- **Things to know:**
  - Claude Code's summary says the picker does not show a settings form yet. That is wrong: the
    picker shows one (segment B). But after an upload from the "Upload Zip" tab the form opens
    inside the hidden "Library" tab, so the teacher sees only "Choose the settings for this
    placement below" until they click Library (done on camera in segment B). Probably a picker bug
    worth fixing before the talk.
  - The stand-in Canvas does not pass a placement's settings back on launch, so the recording
    keeps the default 45 m target rather than showing a changed one.
  - The lab's status chip reads "Unsaved changes" throughout the student run.

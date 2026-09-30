# VLLA 2026 Outline

Draft 4. Waiting on Kyle before building slides.

- Session: From PhET to Keyboarding: How We Built an LTI Tool That Turns Any Web Interactive into a Gradable Canvas Assignment
- Friday, October 2, 9:40 to 10:10 am, MacArthur room
- 25 minutes of talk and demos, then 5 minutes of questions
- Template: Geometric VA Template (a copy)
- Audience: people who run state and district virtual programs

## Style notes for the slides

Written to match Kyle's past decks (Beyond Chat, The Post-Star Trek Education) and his emails:

- Plain title-case slide titles, often a question ("Why go it alone?")
- Short bullets, one level of sub-bullets at most, no bold inside bullets
- First person: "we built", "I'll show you"
- Say what was hard. His decks have Challenges and Lessons slides.
- A little humor is fine. No slogans or taglines.
- Avoid the usual AI tells (from Wikipedia's Signs of AI writing): "not just X, but Y", lists of three for rhythm, words like showcase, seamless, robust, empower, transform, crucial, landscape, and em dashes.

## Time Budget

| # | Slide | Time | Clock |
|---|-------|------|-------|
| 1 | Title | 0:15 | 0:15 |
| 2 | About Me | 0:45 | 1:00 |
| 3 | Who Builds Your Interactives? | 1:00 | 2:00 |
| 4 | One Sentence | 1:00 | 3:00 |
| 5 | Let's Watch | 3:00 | 6:00 |
| 6 | So What's the Catch? | 1:15 | 7:15 |
| 7 | What is Zest? | 1:45 | 9:00 |
| 8 | It Started with PhET | 1:00 | 10:00 |
| 9 | Keyboarding Practice (live demo) | 3:00 | 13:00 |
| 10 | One Package, Lots of Courses | 1:00 | 14:00 |
| 11 | What Else Can You Make? | 0:20 | 14:20 |
| 12-15 | Four zests, about 1:10 each | 4:40 | 19:00 |
| 16 | Why Build It Ourselves? | 1:00 | 20:00 |
| 17 | We Wrote It Down | 1:00 | 21:00 |
| 18 | Challenges | 1:00 | 22:00 |
| 19 | Can You Trust What the AI Made? | 1:15 | 23:15 |
| 20 | What's Next | 0:45 | 24:00 |
| 21 | Want the Code? | 0:45 | 24:45 |
| 22 | Questions | 5:00 | 30:00 |

About 15 seconds of slack. If I'm running long, show two of the four zests and skip to slide 16.

## Slides

### 1. Title
From PhET to Keyboarding: How We Built an LTI Tool That Turns Any Web Interactive into a Gradable Canvas Assignment
Kyle Yancey, Virtual Arkansas

### 2. About Me
Same format as the Star Trek deck:
- Data Science Specialist, Virtual Arkansas
- Teacher for 10 years (Physics, Chemistry, Biology, Physical Science, Business, Computer Science)
- Coding for about 25 years
- B.S. Computer Science, Master of Arts in Teaching
- kyle.yancey@virtualarkansas.org

[Kyle: update anything that's changed.]

### 3. Who Builds Your Interactives?
- Show of hands: who has a teacher with a great idea for a simulation or a game and no way to build it?
- Most programs have a developer, pay a vendor, or go without.
- AI changed that. A teacher can describe an activity and get a working one back.

### 4. One Sentence
The prompt, big on the slide:
> Make a projectile motion lab where students predict the launch angle to hit a target, auto-graded, with the target distance set by the teacher.

Click to show the finished activity next to it (image of Launch Lab).
Notes: "That's all the teacher typed. Here's what happened next."

### 5. Let's Watch
Screen recording, sped up (recorded ahead of time, no live Claude Code):
- The prompt goes into Claude Code with our zest-creator template
- It asks a couple of plain questions (Graded? Save progress? Teacher settings?)
- It builds the activity, checks it, and packages it as a .zest file
- The file gets uploaded in Canvas and a student plays it

No code is shown. The teacher never has to read any.

### 6. So What's the Catch?
An interactive on its own is just a web page.
- No grade in the gradebook
- No record of what the student did
- Usually another login or another vendor

That's the problem Zest solves.

### 7. What is Zest?
Zest is an LTI 1.3 tool we built at Virtual Arkansas.
- Takes any HTML/JavaScript interactive
- Makes it a Canvas assignment, auto-graded or teacher-graded
- Or drops it into a Canvas page as a live element
- Grades go to the gradebook
- Teachers see the student's actual work in SpeedGrader

Simple diagram: Canvas editor button → Zest (on your own server) → activity → gradebook and SpeedGrader.
Notes: a package is a zip of HTML, CSS and JavaScript plus a small settings file. It can include its own SpeedGrader view, a settings page for teachers, and an answer key students can't see.

### 8. It Started with PhET
- We wanted PhET-style simulations that actually count for a grade
- Explore mode: students save observations, the teacher grades them
- Challenge mode: auto-graded
- Once that worked, anything that runs in a browser could work too

[Kyle: which PhET work do you want to show, and which courses use it?]

### 9. Keyboarding Practice (live demo)
Live in Canvas, with a recording as a backup.
1. Teacher: editor button → pick Keyboarding Practice from the library → set the passage
2. Student: types the passage and submits. The grade shows up in the gradebook.
3. Teacher: opens the attempt in SpeedGrader and sees the student's work
4. Student: opens it on another device and their work is still there

### 10. One Package, Lots of Courses
- Each course can set it up differently (a different passage, for example)
- When we fixed a bug, we updated every copy at once
- No broken links, no lost student work
- Works on managed Chromebooks that block third-party cookies

### 11. What Else Can You Make?
Four tiles. "Every one of these came from a prompt. They're on my sandbox, so try them on your phone."

### 12 to 15. The Four Zests
Each slide: the prompt on the left, an image on the right, and a QR code to Kyle's sandbox.

| Zest | Subject | Graded by | Why it's in the talk |
|------|---------|-----------|----------------------|
| Launch Lab | Physics | Auto | Predict the angle, fire, see where it lands |
| Graph Match | Algebra 2 | Auto | The teacher picks the target functions on a settings page the AI also built |
| Sketch & Label | Life Science | Teacher | Students draw on a plant cell. In SpeedGrader you can replay their drawing. |
| Escape the Archive | U.S. History | Auto | Escape room with primary sources, including the Little Rock Nine |

The prompts and any follow-up requests are saved in `zests/<slug>/PROMPT.md`, so the slides only claim what the prompt actually produced.

### 16. Why Build It Ourselves?
Echoes "Why go it alone?" from Beyond Chat.
- We needed grades and review inside Canvas, not in another tool
- Student data stays on our server
- No per-seat license
- We already had the content and needed a home for it

[Kyle: adjust these to your real reasons.]

### 17. We Wrote It Down
- The package format and how packages talk to Canvas are in a published specification
- A package built for one Zest server runs on any other
- The zest-creator template is what you saw in the recording
- Both are public on GitHub [Kyle: show the links here, or keep them off?]

### 18. Challenges
- LTI and Canvas integration was most of the work (again)
- Canvas silently blocks pop-up alerts inside assignments, and assignment frames can't resize
- Managed Chromebooks block third-party cookies, so launches had to work without them
- Rule number one: never lose student work, through every update
- We test every change with fake teachers, students and admins going through real launches

### 19. Can You Trust What the AI Made?
- Every package gets checked when it's built
- A separate review looks for anything that sends data out or tracks students
- Zest runs every package in a sandbox, with permissions off by default
- Somebody still has to test it as a student, and a subject expert should check the content
- Auto-graded scores are calculated in the browser. For anything high stakes, use teacher grading.

### 20. What's Next
- Releasing the server code (MIT license)
- Serving packages from a separate domain for more security
- An accessibility review
- Other LMSs. We've looked at Brightspace, Schoology and Buzz.

### 21. Want the Code?
- QR code to the Google Form: [[FORM URL PLACEHOLDER]]
- Short link under the QR code
- kyle.yancey@virtualarkansas.org
- Thank you for your time 😊
- Small print: "Zest" and "Zestable" are trademarks of Virtual Arkansas (applications pending)

### 22. Questions
Leave the QR code up. Short answers go in the speaker notes. Likely questions:
- What does Claude Code cost?
- Does student data go to the AI? (No. The AI only sees what the teacher types while building. The server has no AI in it.)
- Who checks what the AI builds? Can it be wrong?
- Hosting and cost
- Other LMSs
- Accessibility
- Support
- When does the server code come out?

## Things to be upfront about (notes and Q&A)
- "Non-technical" means no programming. You still need Claude Code (a paid Claude plan) and the zest-creator template, and you test it as a student.
- AI can get content wrong, so a subject expert reviews it like any other material.
- Scores are calculated in the browser. Use teacher grading for high stakes.
- Packages run on the same domain as the tool for now, so only upload packages you trust.
- Canvas only, for now.
- Accessibility review is planned. No WCAG claims.

## Left off on purpose
- Production numbers
- getzest.dev
- A link to the zest-server repo (private)

## Media
- Images of each zest, taken here. Kyle hosts the zests on his sandbox and sends the links for the QR codes.
- The build recording for slide 5, recorded here from a real zest-creator run, sped up.
- A backup recording of the Keyboarding demo, from the stand-in Canvas unless Kyle records his own.
- Videos go in Kyle's Google Drive. Small images go in `media/`.
- Only made-up people in screenshots (Avery Student, Blake Student, Taylor Teacher, Morgan Admin).

## Open Items
1. Google Form URL
2. Sandbox links for the four zests after upload
3. PhET slide: what to show and which courses
4. GitHub links for zest-spec and zest-creator on slide 17: yes or no
5. About Me: anything to change
6. Slide 16: your real reasons for building it in-house

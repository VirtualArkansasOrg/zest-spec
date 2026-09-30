# Slide copy and speaker notes for the VLLA 2026 Zest deck.
# Written in Kyle's voice: plain, first person, no slogans.

MEDIA = '/home/user/zest-spec/presentations/2026-vlla/media/'

NOTES = {}

NOTES[1] = """TIME: 0:15 (clock 0:15)

Good morning. I'm Kyle Yancey from Virtual Arkansas. This session is about Zest, a tool we built that turns web interactives into graded Canvas assignments."""

NOTES[2] = """TIME: 0:45 (clock 1:00)

Quick background so you know where I'm coming from. I taught for about ten years: physics, chemistry, biology, physical science, business and computer science. I've been writing code for about 25 years. These days I'm the Data Science Specialist at Virtual Arkansas, and most of what I build is AI tools for our teachers and students.

[Kyle: add a photo in the circle, and update anything that's changed.]"""

NOTES[3] = """TIME: 1:00 (clock 2:00)

Show of hands. Is anyone here using AI to build their own interactives? Simulations, games, practice tools?

(Pause. Count hands.)

Keep your hand up if you've figured out how to grade them.

That's the gap. AI can build the activity now. A teacher can describe something and get a working page back in a few minutes. Getting that page into the gradebook, with a record of what the student did, is the hard part. That's what I want to show you."""

NOTES[4] = """TIME: 1:00 (clock 3:00)

Here's one sentence a teacher could type. (Read it.)

That's the whole prompt. The activity on the left is what came out: students predict a launch angle, fire, and see where it lands. The teacher sets the target distances. It's auto-graded.

Let me show you what happened in between."""

NOTES[5] = """TIME: 3:00 (clock 6:00)

PLAY THE BUILD RECORDING. It's sped up; talk over it.

- This is Claude Code with our zest-creator template. The teacher types /zest-new and the sentence you just saw.
- It asks a few plain questions. Graded or not? Should it save progress? What should the teacher be able to change?
- Then it builds the activity. This part is sped up a lot.
- /zest-build checks the package and makes a .zest file.
- (If the recording includes it) The file gets uploaded in Canvas and a student plays it.

Notice there's no code on screen that the teacher has to read. They describe it, answer a few questions, and test it.

[Backup: if the video won't play, use the stills in the media folder.]"""

NOTES[6] = """TIME: 1:15 (clock 7:15)

So what's the catch? An interactive on its own is just a web page.

- There's no grade in the gradebook. Somebody has to copy scores over, or it just doesn't count.
- There's no record of what the student did. The teacher can't see the work.
- And it's usually another login, or another vendor with another contract.

That's the problem Zest solves."""

NOTES[7] = """TIME: 1:45 (clock 9:00)

Zest is an LTI 1.3 tool we built at Virtual Arkansas. It runs on our own server and plugs into Canvas.

Walk the three boxes:
1. In Canvas, the teacher clicks Embed Interactive Content in the editor and uploads or picks a zest.
2. Zest runs the activity. It can be a graded assignment, auto-graded or teacher-graded, or just a live element on a page.
3. The grade goes to the gradebook, and the teacher sees the student's actual work in SpeedGrader.

A zest is a zip of plain HTML, CSS and JavaScript plus a small settings file. It can bring its own SpeedGrader view, a settings page for teachers, and an answer key students can't see.

Work is saved as the student goes, so it follows them to another device."""

NOTES[8] = """TIME: 1:00 (clock 10:00)

How it started. We needed coding tools for our computer science courses, and the system we had was expensive. So we built our own.

Then we added our keyboarding class, which is what I'm about to show you.

And now we're going to keep adding more. Anything that runs in a browser can be a zest.

[Kyle: the session title says "From PhET to Keyboarding". If you want, mention where PhET-style simulations fit here.]"""

NOTES[9] = """TIME: 3:00 (clock 13:00)

LIVE DEMO in Canvas. Backup recording if the network is down.

1. As a teacher: open a page or assignment, click Embed Interactive Content, pick Keyboarding Practice from the library, set the passage.
2. As a student: type the passage and submit. Switch to the gradebook and show the grade.
3. As the teacher: open SpeedGrader. This is the package's own review page, so you see what the student actually typed.
4. Open it again as the student on another device (or another browser). The work is still there.

Keep it moving. If something hangs for more than ten seconds, switch to the backup."""

NOTES[10] = """TIME: 1:00 (clock 14:00)

- Each course can set up the same zest differently. For keyboarding, that's a different passage.
- When we found a bug, we fixed the package once and updated every copy at once. No broken links, and no student lost any work.
- It works on managed Chromebooks that block third-party cookies. That one took some doing."""

NOTES[11] = """TIME: 0:20 (clock 14:20)

So what else can you make? Every one of these came from a prompt, the same way you saw in the recording. They're on my sandbox. The next four slides have QR codes, so try them on your phone while I talk. On a phone they open in a preview mode, so nothing gets saved."""

NOTES[12] = """TIME: 1:10 (clock 15:30)

Launch Lab. Physics.

The prompt is on the slide. Students lock in a predicted angle, then take one scored launch. After that they can take practice shots. A lot of them discover that two different angles hit the same target, which is a nice conversation starter.

The teacher sets the target distances, the launch speed and how close counts as a hit. It's auto-graded. In SpeedGrader the teacher sees every scored shot drawn on one field."""

NOTES[13] = """TIME: 1:10 (clock 16:40)

Graph Match. Algebra 2.

Students move a, h and k until their curve covers the target. The equation updates as they go.

The part I want you to notice: the teacher picks the target functions on a settings page. The AI built that settings page too, from "I want to pick the target functions myself." One package, set up differently for each class."""

NOTES[14] = """TIME: 1:10 (clock 17:50)

Sketch and Label. Life science. This one is teacher-graded.

Students draw arrows and write labels right on a plant cell, then explain what the chloroplast does.

In SpeedGrader, the teacher can replay the drawing, stroke by stroke, and see how the student got there, including what they erased. On your phone, if you submit in preview, you can watch your own replay.

(Two things the AI added that the prompt didn't ask for, and we kept: label suggestions while typing, and the replay link after a preview submit.)"""

NOTES[15] = """TIME: 1:10 (clock 19:00)

Escape the Archive. U.S. History.

Four locks, each opened with a clue from a primary source. One of them is the Little Rock Nine, and the lock quotes President Eisenhower's September 1957 address.

Hints cost points, and the teacher can turn them off. SpeedGrader shows a timeline of every wrong try and hint, so you can see where a student got stuck."""

NOTES[16] = """TIME: 0:45 (clock 19:45)

Why build it ourselves instead of buying something?

- We needed the grades and the student's work inside Canvas, not in another tool.
- Student data stays on our server.
- No per-seat license.
- We already had content that needed a home.

[Kyle: replace with your real reasons.]"""

NOTES[17] = """TIME: 1:30 (clock 21:15)

This is the part I want you to take home.

A zest is one file. Any program running Zest can upload it, and grading and review work the same way on their server. Your keyboarding activity can be my keyboarding activity.

We wrote the package format down in a published specification so that stays true, and the zest-creator template you saw in the recording is public, so anyone can build them.

Picture a shared library of gradable activities across virtual programs. That's where I'd like this to go.

[Kyle: decide whether to show the GitHub links for zest-spec and zest-creator.]"""

NOTES[18] = """TIME: 0:45 (clock 22:00)

It wasn't all easy.

- LTI and Canvas integration was most of the work. Again.
- Canvas silently blocks pop-up alerts inside assignments, and assignment frames can't resize. Every zest has to be built around that.
- Managed Chromebooks block third-party cookies, so launches had to work without them.
- Rule number one was never lose student work. We test every change with fake teachers, students and admins going through real launches."""

NOTES[19] = """TIME: 1:15 (clock 23:15)

The fair question: can you trust what the AI made?

- Every package gets checked when it's built, and a separate review looks for anything that sends data out or tracks students.
- Zest runs every package in a sandbox, with permissions off by default.
- But somebody still has to test it as a student, and a subject expert should check the content. AI can get a fact or an answer key wrong.
- Auto-graded scores are calculated in the browser. A student who knows what they're doing could fake one. For anything high stakes, use teacher grading."""

NOTES[20] = """TIME: 0:45 (clock 24:00)

What's next:
- We're releasing the server code under the MIT license.
- Next security step: serving packages from a separate domain.
- An accessibility review. I'm not claiming WCAG conformance yet.
- Other LMSs. We've done the research on Brightspace, Schoology and Buzz, but Canvas is the only one today."""

NOTES[21] = """TIME: 0:45 (clock 24:45)

If you want the code when it's released, scan this and fill out the form. And if you build zests, I want to trade.

Thank you for your time.

[FORM URL PLACEHOLDER: replace the QR box with the real QR code.]"""

NOTES[22] = """TIME: 5:00 (clock 30:00). Leave the QR code up.

LIKELY QUESTIONS, SHORT ANSWERS

What does Claude Code cost?
It needs a paid Claude plan. Check current pricing; it's a per-person subscription, not per student.

Does student data go to the AI?
No. The AI only sees what the teacher types while building the activity. The Zest server has no AI in it and doesn't send student work anywhere.

Who checks what the AI builds? Can it be wrong?
Yes, it can be wrong. The build checks and the security review catch technical problems. A teacher tests it as a student, and a subject expert checks the content, same as any material we'd put in a course.

Hosting and cost?
It runs on your own server (Docker and PostgreSQL), with encrypted nightly backups. No per-seat license.

Can we share zests with you, or use yours?
Yes. That's the point of the spec. A zest built for one Zest server runs on any other.

Other LMSs?
Canvas only for now. We've researched Brightspace, Schoology and Buzz.

Accessibility?
A review is planned. Zests are plain HTML, so they can be built accessibly, but I'm not claiming conformance yet.

Can students cheat on auto-graded ones?
Scores are calculated in the browser, so a determined student could. Use teacher grading for high stakes.

Can we upload any zest someone sends us?
Only upload packages you trust for now. Packages run on the same domain as the tool; a separate domain is the next security step.

Support?
[Kyle: your answer.]

When does the server code come out?
[Kyle: your answer.] Fill out the form and I'll let you know."""

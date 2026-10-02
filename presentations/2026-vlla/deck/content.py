# Slide copy and speaker notes for the VLLA 2026 Zest deck.
# Written in Kyle's voice: plain, first person, no slogans.

MEDIA = '/home/user/zest-spec/presentations/2026-vlla/media/'

NOTES = {}

NOTES[1] = """TIME: 0:15 (clock 0:15)

Good morning. I'm Kyle Yancey from Virtual Arkansas. This session is about Zest, a tool we built that turns web interactives into graded Canvas assignments."""

NOTES[2] = """TIME: 0:45 (clock 1:00)

Quick background so you know where I'm coming from. I taught for about ten years: physics, chemistry, biology, physical science, business and computer science. I've been writing code for about 25 years. These days I'm the Data Science Specialist at Virtual Arkansas, and most of what I build is AI tools for our teachers and students.

[Kyle: update anything that's changed.]"""

NOTES[3] = """TIME: 1:00 (clock 2:00)

Show of hands. Is anyone here using AI to build their own interactives? Simulations, games, practice tools?

(Pause. Count hands.)

[CLICK] Keep your hand up if it puts a grade in your gradebook.

That's the gap. AI can build the activity now. A teacher can describe something and get a working page back in a few minutes. Getting that page into the gradebook, with a record of what the student did, is the hard part. That's what I want to show you."""

NOTES[4] = """TIME: 1:00 (clock 16:40)

So how did these get made? Here's one sentence a teacher could type. (Read it.)

That's the whole prompt.

[CLICK] And this is what came out, about three minutes later. Students calculate a launch angle, fire, and see where it lands. It's auto-graded. It even put the range formula in a hint.

Let me show you what happened in between."""

NOTES[5] = """TIME: 2:30 (clock 19:10)

PLAY THE BUILD RECORDING (1:41). It's a real run, sped up; talk over it.

- This is Claude Code with our zest-creator template. The teacher types /zest-new and the sentence you just saw.
- It didn't ask me anything this time. It picked sensible defaults on its own: one target at 45 meters, three launches, full points on the first hit. (Sometimes it asks a couple of plain questions, like whether it should be graded.)
- The thinking part is sped up 20 times. The whole build took under three minutes.
- /zest-build checks the package and makes a .zest file.
- Then the file goes into Canvas. This part is our stand-in Canvas, the test harness we use for every change. A student misses once, hits on the second try, and submits. The gradebook gets 8 out of 10.

Notice there's no code on screen that the teacher has to read.

[Backup: if the video won't play, use the stills in the media folder.]"""

NOTES[6] = """TIME: 1:15 (clock 3:15)

So AI can build the activity. Here's what Zest solves.

[CLICK] There's no grade in the gradebook. Somebody has to copy scores over, or it just doesn't count.
[CLICK] There's no record of what the student did. The teacher can't see the work.
[CLICK] And it's usually another login, or another vendor with another contract.

[CLICK] AI can build the interactive, but on its own it's just a web page. Zest is what turns it into coursework."""

NOTES[7] = """TIME: 1:45 (clock 5:00)

Zest is an LTI 1.3 tool we built at Virtual Arkansas. It runs on our own server and plugs into Canvas.

Walk the three boxes, one click each:
[CLICK] In Canvas, the teacher clicks Embed Interactive Content in the editor and uploads or picks a zest.
[CLICK] Zest runs the activity. It can be a graded assignment, auto-graded or teacher-graded, or just a live element on a page.
[CLICK] The grade goes to the gradebook, and the teacher gets a custom view in SpeedGrader that shows the student's actual work. I'll come back to that.

A zest is a zip of plain HTML, CSS and JavaScript plus a small settings file. It can bring its own SpeedGrader view, a settings page for teachers, and an answer key students can't see.

Work is saved as the student goes, so it follows them to another device."""

NOTES[8] = """TIME: 1:00 (clock 6:00)

How it started.

[CLICK] We needed coding tools for our computer science courses, and the system we had was expensive. So we built our own.

[CLICK] Then we added our keyboarding class, which is what I'm about to show you.

[CLICK] And now we're going to keep adding more. Anything that runs in a browser can be a zest.

[Kyle: the session title says "From PhET to Keyboarding". If you want, mention where PhET-style simulations fit here.]"""

NOTES[9] = """TIME: 3:00 (clock 9:00)

LIVE DEMO in Canvas. Backup recording if the network is down.

1. As a teacher: open a page or assignment, click Embed Interactive Content, pick Keyboarding Practice from the library, set the passage.
2. As a student: type the passage and submit. Switch to the gradebook and show the grade.
3. As the teacher: open SpeedGrader. Slow down here. This is the package's own review page inside SpeedGrader, so you see what the student actually typed, per attempt.
4. Open it again as the student on another device (or another browser). The work is still there.

Keep it moving. If something hangs for more than ten seconds, switch to the backup."""

NOTES[10] = """TIME: 1:00 (clock 10:00)

This is the part teachers like most. Canvas SpeedGrader normally shows a file or a text box. With Zest, every activity can bring its own page for SpeedGrader, so the teacher sees the actual work.

[CLICK] Launch Lab: every shot the student took, drawn on one field.
[CLICK] Graph Match: the student's curve on top of the target, for each graph.
[CLICK] Sketch & Label: the drawing, with a replay of how they drew it.
[CLICK] Escape the Archive: a timeline of every wrong try and hint.

The AI builds these too. In the prompt for Sketch & Label, the teacher just said "in SpeedGrader I want to see their drawing and watch how they drew it."

[Kyle: once the zests are on your sandbox, a screenshot of one of these inside real Canvas SpeedGrader would be the strongest image for this slide.]"""

NOTES[11] = """TIME: 1:00 (clock 11:00)

[CLICK] Each course can set up the same zest differently. For keyboarding, that's a different passage.
[CLICK] When we found a bug, we fixed the package once and updated every copy at once. No broken links, and no student lost any work.
[CLICK] It works on managed Chromebooks that block third-party cookies. That one took some doing."""

NOTES[12] = """TIME: 0:20 (clock 11:20)

So what else can you make? Three of these are auto-graded and one, Sketch & Label, is teacher-graded. Every one of these came from a prompt. I'll show you how in a few minutes. They're on my sandbox. The next four slides have QR codes, so try them on your phone while I talk. On a phone they open in a preview mode, so nothing gets saved."""

NOTES[13] = """TIME: 1:05 (clock 12:25)

Launch Lab. Physics.

This came from the sentence on the slide plus a few answers to follow-up questions: five rounds, practice shots after each scored one, and settings for the targets, launch speed and how close counts as a hit. In a few minutes you'll see what that sentence alone produces.

Students lock in a predicted angle, then take one scored launch. (For today there's a Start over button, which the teacher can turn off for a real graded check.) After that they can take practice shots. A lot of them discover that two different angles hit the same target, which is a nice conversation starter.

[CLICK] And this is what the teacher sees in SpeedGrader: every scored shot drawn on one field, and a table of each round."""

NOTES[14] = """TIME: 1:05 (clock 13:30)

Graph Match. Algebra 2.

Students move a, h and k until their curve covers the target. The equation updates as they go.

The part I want you to notice: when the teacher embeds it, they pick a set of graphs (quadratics, absolute value, sine waves and so on), or open the settings editor and build their own list. The AI built that settings page too, from "I want to pick the target functions myself." One package, set up differently for each class. On your phone, the preview has the same choice at the top.

[CLICK] In SpeedGrader: each graph, with the student's curve on top of the target."""

NOTES[15] = """TIME: 1:05 (clock 14:35)

Sketch and Label. Life science. This one is teacher-graded.

Students draw arrows and write labels right on a plant cell, then explain what the chloroplast does.

[CLICK] In SpeedGrader, the teacher can replay the drawing, stroke by stroke, and see how the student got there, including what they erased. On your phone, if you submit in preview, you can watch your own replay.

(Two things the AI added that the prompt didn't ask for, and we kept: label suggestions while typing, and the replay link after a preview submit.)"""

NOTES[16] = """TIME: 1:05 (clock 15:40)

Escape the Archive. U.S. History.

Four locks, each opened with a clue from a primary source. One of them is the Little Rock Nine, and the lock quotes President Eisenhower's September 1957 address.

Hints cost points, and the teacher can turn them off or set a time limit.

[CLICK] SpeedGrader shows a timeline of every wrong try and hint, so you can see where a student got stuck."""

NOTES[17] = """TIME: 0:45 (clock 19:55)

Why build it ourselves instead of buying something?

[CLICK] We needed the grades and the student's work inside Canvas, not in another tool.
[CLICK] Student data stays on our server.
[CLICK] No per-seat license.
[CLICK] We already had content that needed a home.

[Kyle: replace with your real reasons.]"""

NOTES[18] = """TIME: 1:30 (clock 20:40)

This is the part I want you to take home.

A zest is one file. Any program running Zest can upload it, and grading and review work the same way on their server. Your keyboarding activity can be my keyboarding activity.

[CLICK] We wrote the package format down in a published specification so that stays true, and the zest-creator template you saw in the recording is public, so anyone can build them.

Picture a shared library of gradable activities across virtual programs. That's where I'd like this to go.

[Kyle: decide whether to show the GitHub links for zest-spec and zest-creator.]"""

NOTES[19] = """TIME: 0:45 (clock 21:25)

It wasn't all easy.

[CLICK] LTI and Canvas integration was most of the work. Again.
[CLICK] Canvas silently blocks pop-up alerts inside assignments, and assignment frames can't resize. Every zest has to be built around that.
[CLICK] Managed Chromebooks block third-party cookies, so launches had to work without them.
[CLICK] Rule number one was never lose student work. We test every change with fake teachers, students and admins going through real launches."""

NOTES[20] = """TIME: 1:15 (clock 22:40)

The fair question: can you trust what the AI made?

[CLICK] Every package gets checked when it's built, and a separate review looks for anything that sends data out or tracks students.
[CLICK] Zest runs every package in a sandbox, with permissions off by default.
[CLICK] But somebody still has to test it as a student, and a subject expert should check the content. AI can get a fact or an answer key wrong.
Also on that last card: auto-graded scores are calculated in the browser. A student who knows what they're doing could fake one. For anything high stakes, use teacher grading."""

NOTES[21] = """TIME: 0:45 (clock 23:25)

What's next:
[CLICK] We're releasing the server code under the MIT license.
[CLICK] Next security step: serving packages from a separate domain.
[CLICK] An accessibility review. I'm not claiming WCAG conformance yet.
[CLICK] Other LMSs. We've done the research on Brightspace, Schoology and Buzz, but Canvas is the only one today."""

NOTES[22] = """TIME: 0:45 (clock 24:10)

If you want the code when it's released, scan this and fill out the form. And if you build zests, I want to trade.

Thank you for your time.

(The QR code and forms.gle/1BDJ6hXbWxbZRopP8 both go to the Get the Zest Code form. Responses land in the Get the Zest Code (Responses) sheet in your Drive.)"""

NOTES[23] = """TIME: 5:00 or more (talk ends at 24:10, so there are about 50 seconds of slack). Leave the QR code up.

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

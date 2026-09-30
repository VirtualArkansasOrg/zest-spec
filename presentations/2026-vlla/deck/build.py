import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from content import NOTES, MEDIA

RED = RGBColor(0x96, 0x00, 0x00)
NAVY = RGBColor(0x1B, 0x31, 0x68)
CYAN = RGBColor(0x25, 0xAE, 0xFA)
GRAY = RGBColor(0x60, 0x5F, 0x5E)
BLACK = RGBColor(0x13, 0x13, 0x13)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
HEAD = 'League Spartan'
BODY = 'Roboto'

prs = Presentation('base.pptx')
S = list(prs.slides)


def remove(slide, ids):
    for sh in list(slide.shapes):
        if sh.shape_id in ids:
            sh._element.getparent().remove(sh._element)


def text(slide, x, y, w, h, paras, size=14, color=BLACK, font=BODY, bold=False,
         align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, space=6, italic=False):
    """paras: list of str, or (str, dict) for per-paragraph overrides."""
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    for i, p in enumerate(paras):
        opts = {}
        if isinstance(p, tuple):
            p, opts = p
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.alignment = opts.get('align', align)
        para.space_after = Pt(opts.get('space', space))
        run = para.add_run()
        run.text = p
        f = run.font
        f.name = opts.get('font', font)
        f.size = Pt(opts.get('size', size))
        f.bold = opts.get('bold', bold)
        f.italic = opts.get('italic', italic)
        f.color.rgb = opts.get('color', color)
    return tb


def title(slide, x, y, w, h, s, size=30, color=BLACK, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    return text(slide, x, y, w, h, [s], size=size, color=color, font=HEAD, bold=True,
                align=align, anchor=anchor, space=0)


def picture(slide, path, x, y, w=None, h=None, border=None):
    pic = slide.shapes.add_picture(path, Inches(x), Inches(y),
                                   Inches(w) if w else None, Inches(h) if h else None)
    if border is not None:
        pic.line.color.rgb = border
        pic.line.width = Pt(1)
    return pic


def box(slide, x, y, w, h, fill, line=None, shape=MSO_SHAPE.ROUNDED_RECTANGLE):
    b = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    b.fill.solid()
    b.fill.fore_color.rgb = fill
    if line is None:
        b.line.fill.background()
    else:
        b.line.color.rgb = line
        b.line.width = Pt(1.5)
    b.shadow.inherit = False
    return b


def placeholder(slide, x, y, w, h, label, fill=WHITE, color=RED):
    b = box(slide, x, y, w, h, fill, line=color)
    tf = b.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = label
    r.font.name = BODY
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = color
    return b


def fit(path, max_w, max_h):
    from PIL import Image
    iw, ih = Image.open(path).size
    s = min(max_w / iw, max_h / ih)
    return iw * s, ih * s


def centered(slide, path, cx, cy, max_w, max_h, border=None):
    w, h = fit(path, max_w, max_h)
    return picture(slide, path, cx - w / 2, cy - h / 2, w, h, border)


# 1. Title (base 1)
s = S[0]
remove(s, {183})
title(s, 0.56, 0.62, 6.6, 1.0, 'From PhET to Keyboarding', size=40)
text(s, 0.56, 1.55, 6.4, 0.8,
     ['How We Built an LTI Tool That Turns Any Web Interactive into a Gradable Canvas Assignment'],
     size=15, color=GRAY)
text(s, 0.56, 4.25, 6.5, 0.9,
     [('Kyle Yancey', {'font': HEAD, 'bold': True, 'size': 18, 'space': 2}),
      'Data Science Specialist, Virtual Arkansas  |  VLLA 2026'],
     size=12, color=WHITE)

# 2. About Me (base 16)
s = S[1]
remove(s, {545, 546, 542})
title(s, 0.58, 0.75, 4.5, 0.6, 'About Me', size=34)
text(s, 0.58, 1.55, 4.8, 2.6, [
    'Data Science Specialist, Virtual Arkansas',
    'Teacher for 10 years: Physics, Chemistry, Biology, Physical Science, Business, Computer Science',
    'Coding for about 25 years',
    'B.S. Computer Science, Master of Arts in Teaching',
    ('kyle.yancey@virtualarkansas.org', {'color': RED, 'bold': True}),
], size=13, space=8)
ph = box(s, 6.0, 0.9, 2.6, 2.6, RGBColor(0xEE, 0xEE, 0xEE), line=CYAN, shape=MSO_SHAPE.OVAL)
tf = ph.text_frame
r = tf.paragraphs[0].add_run()
tf.paragraphs[0].alignment = PP_ALIGN.CENTER
r.text = 'Your photo'
r.font.name = BODY
r.font.size = Pt(12)
r.font.color.rgb = GRAY

# 3. Are You Using AI to Build Interactives? (base 6)
s = S[2]
remove(s, {287, 290, 293})
title(s, 0.56, 0.42, 8.8, 0.7, 'Are You Using AI to Build Interactives?', size=28)
text(s, 0.88, 2.25, 3.8, 1.6, [
    ('Show of hands', {'font': HEAD, 'bold': True, 'size': 20}),
    'Who is using AI to build their own simulations, games or practice tools?'], size=13)
text(s, 5.32, 2.25, 3.8, 1.6, [
    ('Now grade it', {'font': HEAD, 'bold': True, 'size': 20}),
    'Keep your hand up if it puts a grade in your gradebook.'], size=13, color=WHITE)

# 4. One Sentence (base 7)
s = S[3]
remove(s, {310})
centered(s, MEDIA + 'launch-lab-phone.png', 0.56 + 4.17 / 2, 0.56 + 4.5 / 2, 3.9, 4.2)
title(s, 5.3, 0.75, 4.2, 0.6, 'One Sentence', size=32, color=WHITE)
text(s, 5.3, 1.55, 4.1, 2.4, [
    ('“Make a projectile motion lab where students predict the launch angle to hit a target, '
     'auto-graded, with the target distance set by the teacher.”', {'italic': True, 'size': 16}),
    ('That is all the teacher typed.', {'size': 12, 'space': 0})], size=16, color=WHITE, space=14)

# 5. Let's Watch (base 17, cards removed)
s = S[4]
remove(s, {562, 563, 564, 565, 566, 567})
title(s, 0.56, 0.3, 6, 0.55, "Let's Watch", size=28, color=WHITE)
poster = MEDIA + 'build-recording-poster.png'
if os.path.exists(poster):
    centered(s, poster, 5.0, 3.0, 7.6, 4.1, border=CYAN)
else:
    placeholder(s, 1.2, 1.0, 7.6, 4.1, 'Build recording (video goes here)')
text(s, 7.2, 0.4, 2.3, 0.4, ['Sped up'], size=11, color=CYAN, align=PP_ALIGN.RIGHT)

# 6. So What's the Catch? (base 2)
s = S[5]
remove(s, {194, 198})
text(s, 1.1, 1.05, 3.85, 3.7, [
    ('No grade in the gradebook', {'font': HEAD, 'bold': True, 'size': 23, 'space': 3}),
    ('Someone copies scores by hand, or it does not count', {'space': 22}),
    ('No record of the work', {'font': HEAD, 'bold': True, 'size': 23, 'space': 3}),
    ('The teacher cannot see what the student did', {'space': 22}),
    ('Another login', {'font': HEAD, 'bold': True, 'size': 23, 'space': 3}),
    ('Or another vendor, with another contract', {'space': 0}),
], size=14, color=GRAY)
title(s, 6.0, 0.8, 3.4, 1.2, "So What's the Catch?", size=30, color=WHITE)
text(s, 6.0, 2.1, 3.3, 1.2, ['An interactive on its own is just a web page.'], size=15, color=WHITE)

# 7. What is Zest? (base 12)
s = S[6]
remove(s, {431, 439, 442, 445})
title(s, 0.56, 0.45, 7.5, 0.6, 'What is Zest?', size=32)
text(s, 0.56, 1.15, 8.0, 0.9, [
    'An LTI 1.3 tool we built at Virtual Arkansas. Any HTML/JavaScript interactive becomes a '
    'Canvas assignment, auto-graded or teacher-graded, or a live element on a page.'], size=13, color=GRAY)
for i, (h, b) in enumerate([
        ('In Canvas', 'The teacher clicks Embed Interactive Content and picks or uploads a zest'),
        ('Zest', 'Runs the activity from your own server and saves work as the student goes'),
        ('Back in Canvas', 'The grade lands in the gradebook and the work shows in SpeedGrader')]):
    x = 0.56 + i * 3.06
    text(s, x + 0.3, 2.85, 2.2, 1.9, [(h, {'font': HEAD, 'bold': True, 'size': 17, 'color': NAVY}), b],
         size=12, color=BLACK)

# 8. How It Started (base 5)
s = S[7]
remove(s, {256, 262, 263, 267, 271, 272, 273})
title(s, 1.0, 1.35, 3.5, 0.6, 'How It Started', size=30)
text(s, 1.0, 2.05, 3.3, 1.6, [
    'We built Zest for our own courses first, one need at a time.'], size=13, color=GRAY)
for i, (step, label) in enumerate([('1', 'Coding tools to replace an expensive system'),
                                   ('2', 'Our keyboarding class'),
                                   ('3', 'More on the way')]):
    y = 1.2 + i * 1.03
    text(s, 5.5, y + 0.23, 0.6, 0.3, ['Step ' + step], size=11, color=WHITE, bold=True)
    text(s, 6.55, y + 0.14, 2.35, 0.5, [label], size=12, color=BLACK, anchor=MSO_ANCHOR.MIDDLE)

# 9. Keyboarding Practice (base 3)
s = S[8]
remove(s, {216, 220})
text(s, 1.1, 1.05, 3.9, 3.6, [
    ('1. Teacher', {'font': HEAD, 'bold': True, 'size': 16, 'color': NAVY, 'space': 1}),
    ('Embed it from the library and set the passage', {'space': 9}),
    ('2. Student', {'font': HEAD, 'bold': True, 'size': 16, 'color': NAVY, 'space': 1}),
    ('Types and submits. The grade shows up in the gradebook.', {'space': 9}),
    ('3. Teacher', {'font': HEAD, 'bold': True, 'size': 16, 'color': NAVY, 'space': 1}),
    ('Opens SpeedGrader and sees what the student typed', {'space': 9}),
    ('4. Student, another device', {'font': HEAD, 'bold': True, 'size': 16, 'color': NAVY, 'space': 1}),
    ('The work is still there', {'space': 0}),
], size=12, color=BLACK)
title(s, 6.0, 0.8, 3.4, 1.2, 'Keyboarding Practice', size=30, color=WHITE)
text(s, 6.0, 2.1, 3.3, 0.8, ['Live demo'], size=16, color=CYAN, bold=True)

# 10. One Package, Lots of Courses (base 19)
s = S[9]
remove(s, {586, 598, 602, 606})
title(s, 0.56, 1.8, 2.9, 2.0, 'One Package, Lots of Courses', size=28, color=WHITE)
for i, (h, b) in enumerate([
        ('Set it up per course', 'A different passage for each class, from the same zest'),
        ('Fix it once, update every copy', 'No broken links and no lost student work'),
        ('Works on managed Chromebooks', 'Even when third-party cookies are blocked')]):
    y = 0.31 + i * 1.79
    text(s, 4.55, y + 0.3, 5.0, 0.95, [(h, {'font': HEAD, 'bold': True, 'size': 17, 'space': 3}), b],
         size=12, color=WHITE)

# 11. What Else Can You Make? (base 18, four cards)
s = S[10]
cards = [(0.68, 0.37), (5.40, 0.37), (0.68, 2.92), (5.40, 2.92)]
shots = [('launch-lab-desktop.png', 'Launch Lab', 'Physics'),
         ('graph-match-desktop.png', 'Graph Match', 'Algebra 2'),
         ('sketch-label-desktop.png', 'Sketch & Label', 'Life Science'),
         ('escape-the-archive-desktop.png', 'Escape the Archive', 'U.S. History')]
for (cx, cy), (img, name, subj) in zip(cards, shots):
    picture(s, MEDIA + img, cx + 0.15, cy + 0.17, 2.6, None)
    text(s, cx + 2.9, cy + 0.3, 1.05, 1.7, [(name, {'font': HEAD, 'bold': True, 'size': 14, 'space': 4}),
                                           (subj, {'size': 10, 'color': GRAY})], size=12)

# 12-15. The four zests (base 4)
ZESTS = [
    ('launch-lab', 'Launch Lab', 'Physics  |  Auto-graded',
     'Make a projectile motion lab where students predict the launch angle to hit a target, '
     'auto-graded, with the target distance set by the teacher.',
     'The teacher sets the targets. SpeedGrader shows every shot.'),
    ('graph-match', 'Graph Match', 'Algebra 2  |  Auto-graded',
     'Build a function transformations game for Algebra 2: students drag sliders to make their graph '
     'match a target curve. Auto-graded, and I want to pick the target functions myself.',
     'The AI also built the settings page where the teacher picks the targets.'),
    ('sketch-label', 'Sketch & Label', 'Life Science  |  Teacher-graded',
     'Students label a plant cell by drawing arrows and writing the names of the parts right on the '
     'diagram, then explain in a sentence what the chloroplast does. I’ll grade it myself, and in '
     'SpeedGrader I want to see their drawing and watch how they drew it.',
     'In SpeedGrader you can replay the drawing stroke by stroke.'),
    ('escape-the-archive', 'Escape the Archive', 'U.S. History  |  Auto-graded',
     'Create a digital escape room for U.S. History where students unlock four locks using clues from '
     'primary sources, one of them about the Little Rock Nine. Auto-graded, with hints I can turn off.',
     'SpeedGrader shows every wrong try and hint on a timeline.'),
]
for i, (slug, name, sub, prompt, extra) in enumerate(ZESTS):
    s = S[11 + i]
    remove(s, {238, 246})
    centered(s, MEDIA + slug + '-desktop.png', 2.55, 2.55, 4.5, 3.3, border=RGBColor(0xCC, 0xCC, 0xCC))
    title(s, 5.3, 0.45, 4.2, 0.55, name, size=26)
    text(s, 5.3, 1.0, 4.2, 0.3, [sub], size=11, color=RED, bold=True)
    small = len(prompt) > 200
    text(s, 5.3, 1.45, 4.15, 2.0, [('The prompt', {'size': 10, 'color': GRAY, 'bold': True, 'space': 3}),
                                  ('“' + prompt + '”', {'italic': True, 'size': 11.5 if small else 12.5})],
         size=12)
    text(s, 5.3, 3.5, 2.9, 0.8, [extra], size=11, color=NAVY)
    placeholder(s, 8.35, 3.35, 1.05, 1.05, 'QR code\n(link coming)')

# 16. Why Build It Ourselves? (base 8)
s = S[15]
remove(s, {325, 330, 333})
title(s, 0.56, 0.55, 7.5, 0.6, 'Why Build It Ourselves?', size=30)
text(s, 0.56, 2.55, 4.2, 1.8, [
    ('Grades inside Canvas', {'font': HEAD, 'bold': True, 'size': 18, 'space': 2}),
    ('Not in another tool', {'space': 12}),
    ('Our data, our server', {'font': HEAD, 'bold': True, 'size': 18, 'space': 2}),
    ('Student work stays with us', {'space': 0})], size=12, color=WHITE)
text(s, 5.64, 2.55, 3.8, 1.8, [
    ('No per-seat license', {'font': HEAD, 'bold': True, 'size': 18, 'space': 2}),
    ('Add students without a new contract', {'space': 12}),
    ('Content needed a home', {'font': HEAD, 'bold': True, 'size': 18, 'space': 2}),
    ('We already had it', {'space': 0})], size=12, color=WHITE)

# 17. Share Them With Other Programs (base 10)
s = S[16]
remove(s, {388, 389, 390, 391, 392, 393, 396, 397})
text(s, 1.0, 0.95, 3.35, 3.8, [
    ('One File', {'font': HEAD, 'bold': True, 'size': 28, 'color': RED, 'space': 10}),
    ('A zest is a single file', {'space': 14}),
    ('Any program running Zest can upload it', {'space': 14}),
    ('Your keyboarding activity can be my keyboarding activity', {'space': 0})], size=15, color=BLACK)
text(s, 5.7, 0.95, 3.35, 3.8, [
    ('Written Down', {'font': HEAD, 'bold': True, 'size': 28, 'color': CYAN, 'space': 10}),
    ('The package format is a published specification', {'space': 14}),
    ('The zest-creator template is public', {'space': 14}),
    ('Picture a shared library of gradable activities across programs', {'space': 0})], size=15, color=WHITE)

# 18. Challenges (base 11)
s = S[17]
remove(s, {405, 408, 411, 414, 417})
title(s, 0.56, 0.55, 2.9, 0.7, 'Challenges', size=30, color=WHITE)
text(s, 0.56, 1.35, 2.9, 1.5, ['What took the most work'], size=13, color=WHITE)
for (x, y), (h, b) in zip([(4.43, 0.6), (7.25, 0.6), (4.43, 2.5), (7.25, 2.5)], [
        ('LTI and Canvas', 'Most of the work. Again.'),
        ('Canvas quirks', 'Pop-up alerts are blocked in assignments, and the frames can’t resize'),
        ('Chromebooks', 'Launches had to work with third-party cookies blocked'),
        ('Never lose student work', 'Every change is tested with fake teachers, students and admins')]):
    text(s, x, y, 2.2, 1.7, [(h, {'font': HEAD, 'bold': True, 'size': 16, 'space': 4}), b], size=12, color=BLACK)

# 19. Can You Trust What the AI Made? (base 13)
s = S[18]
remove(s, {464, 465, 466, 467})
title(s, 1.3, 0.6, 7.4, 0.6, 'Can You Trust What the AI Made?', size=28, color=WHITE, align=PP_ALIGN.CENTER)
text(s, 1.3, 1.25, 7.4, 0.5, ['What checks it, and what still needs a person'],
     size=13, color=WHITE, align=PP_ALIGN.CENTER)
for i, (h, b) in enumerate([
        ('Checked', 'Every package is checked when it’s built. A separate review looks for anything that sends data out or tracks students.'),
        ('Sandboxed', 'Zest runs every package in a sandbox, with permissions off by default.'),
        ('Still a person’s job', 'Test it as a student. Have a subject expert check it. Use teacher grading for high stakes.')]):
    x = 0.72 + i * 2.9
    text(s, x + 0.22, 2.55, 2.32, 2.2, [(h, {'font': HEAD, 'bold': True, 'size': 18, 'color': NAVY, 'space': 8}), b],
         size=13, color=BLACK)

# 20. What's Next (base 15)
s = S[19]
remove(s, {511, 514, 526, 529, 532})
title(s, 0.56, 0.6, 3.6, 0.6, "What's Next", size=30)
text(s, 0.56, 1.3, 3.4, 1.2, ['Where Zest goes from here'], size=13, color=GRAY)
for i, (h, b) in enumerate([
        ('Release the server code', 'MIT license'),
        ('A separate domain for packages', 'The next security step'),
        ('Accessibility review', 'No WCAG claims yet'),
        ('Other LMSs', 'Researched Brightspace, Schoology and Buzz')]):
    y = 0.68 + i * 1.19
    text(s, 5.75, y, 3.7, 0.7, [(h, {'font': HEAD, 'bold': True, 'size': 15, 'space': 1}), b], size=11, color=GRAY)

# 21. Want the Code? (base 7)
s = S[20]
remove(s, {310})
placeholder(s, 1.05, 1.2, 3.2, 3.2, 'QR code for the Google Form\n[FORM URL PLACEHOLDER]')
title(s, 5.3, 0.75, 4.2, 0.6, 'Want the Code?', size=32, color=WHITE)
text(s, 5.3, 1.55, 4.1, 2.9, [
    'Scan to get the code when we release it',
    ('[short link]', {'color': CYAN, 'bold': True, 'space': 12}),
    'If you build zests, I want to trade',
    ('kyle.yancey@virtualarkansas.org', {'bold': True, 'space': 14}),
    ('Thank you for your time \U0001F60A', {'font': HEAD, 'bold': True, 'size': 18}),
], size=14, color=WHITE, space=6)
text(s, 5.3, 4.35, 3.0, 0.5, ['“Zest” and “Zestable” are trademarks of Virtual Arkansas (applications pending).'],
     size=8, color=WHITE)

# 22. Questions (base 2)
s = S[21]
remove(s, {194, 198})
placeholder(s, 1.4, 1.2, 3.2, 3.2, 'Same QR code\n[FORM URL PLACEHOLDER]')
title(s, 6.0, 1.4, 3.4, 1.0, 'Questions?', size=36, color=WHITE)
text(s, 6.0, 2.4, 3.3, 1.0, ['kyle.yancey@virtualarkansas.org'], size=13, color=WHITE)

for i, sl in enumerate(S, 1):
    sl.notes_slide.notes_text_frame.text = NOTES[i]

prs.save('zest-vlla-2026.pptx')
print('saved')

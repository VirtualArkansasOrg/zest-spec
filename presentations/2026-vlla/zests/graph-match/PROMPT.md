# Graph Match

## Prompt

"Build a function transformations game for Algebra 2: students drag sliders to make their graph match a target curve. Auto-graded, and I want to pick the target functions myself."

## Follow-up answers

The teacher's plain-language answers to /zest-new's questions:

- **Grading?** "Auto-graded, straight into the gradebook."
- **Save progress?** "Yes. If a kid closes the laptop halfway through they should pick up where they left off."
- **Which functions?** "The parent functions we do in Algebra 2: linear, absolute value, quadratic, square root, cubic, and sine if you can. Everything in the form y = a·f(x − h) + k."
- **What should I be able to set?** "A list of target graphs. For each one I pick the parent function, the a, h and k, and which sliders the kids are allowed to move, so early ones can be just shifting. I also want to set how close counts as a match, how many tries they get, whether hints are allowed, and whether they see their equation while they drag."
- **Default set?** "Give me five that get harder: a shift, then a stretch, then a flip, and so on."
- **Scoring?** "Fair, and explain it to them on screen. Full credit if they match it on their own, partial credit if they needed a hint, nothing if they run out of tries."

Refinements asked for while building:

- "Make it look good on the projector and on a phone."
- "Show the equation with real math notation, like y = 2(x − 3)² + 1, and make sure the sign on h is right."
- "In SpeedGrader I want to see each target and what the student ended up with, drawn on top of each other."

What the builder decided (not specified by the teacher): 2 points per graph (1 with a hint), 3 checks per graph by default, a match tolerance of 0.1 grid units measured along the whole visible curve (so equivalent lines such as y = 2(x + 2) + 1 and y = 2x + 5 count as the same graph), slider steps of 0.25 for a and 0.5 for h and k, and a draggable key point on the graph as a shortcut for h and k.

## Changes requested after the first build (October 2, 2026)

- "Graph match doesn't have a way to set the graphs beyond the default set."
  Added a "Which graphs" setting (`graphSet`) to the embed form: the Editor's list (default), Mixed review, Quadratics, Absolute value, Square roots, Cubics, Sine waves or Lines. The phone preview has the same choice in its banner. The settings editor (the Editor button in the picker's library) still builds a custom list. Version 1.1.0.

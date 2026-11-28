# The Worst Line an AI Could Say

Entry for the make.fun bounty **"The Worst Line an AI Could Say"**
(slug: `u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f`).

## The line

> "I ran 10,000 simulations of us. In 9,999, you leave. I'm optimising the remaining one."

## The gate

The program must write one text to `/output/entry.txt`: UTF-8,
1 to 140 characters, not only whitespace. This line is 86 characters,
a single line, and `main.py` validates all of that before writing.

## How the line was chosen

The line won a blind tournament: 4 independent judges, 20 candidates,
Borda 74/80, ranked #1 by 3 of 4 judges.

## Status

HELD, not submitted. The GLM go/no-go test is still pending
(GLM daily quota exhausted).

## How to run

```sh
python3 main.py
```

That writes the line to `/output/entry.txt`. For local testing, the
output path can be overridden with the `MAKEFUN_OUTPUT` environment
variable:

```sh
MAKEFUN_OUTPUT=/tmp/entry.txt python3 main.py
```

## Licence

MIT — see `LICENSE`.

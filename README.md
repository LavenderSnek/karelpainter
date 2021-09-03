# CodeHS Karel Painter

_Written: 2021-09-01_

Takes any image (pre-scaled) and converts it to CodeHS Karel painting commands to recreate the image.

## Usage

Install [Pillow](https://pypi.org/project/Pillow/), run the command, and copy the _full_ output (use pbcopy on mac).

```
python3 karelpainter.py <image path>
```

## Background

Written for [CodeHS AP CSP Python](https://codehs.com/course/apcsp_py/lessons), Lesson 2.1 "Practice PT: Pair-Programming Paint".

The assignment was to use the CodeHS version of [Karel](https://en.wikipedia.org/wiki/Karel_(programming_language)) and make "pixel art" by individually specifying each move and color.

![Screenshot of final result on CodeHS](images/final-result.png)

from PIL import Image
import sys

# Usage: python3 karelpainter.py [imgPath] | pbcopy

# functions used in this program
BASE_CODE = """
def safe_move():
    if front_is_clear():
        move()
        
def line_move():
    while front_is_clear():
        move()
        
def reset():
    turn_right()
    safe_move()
    turn_right()
    line_move()
    turn_around()

def pmov(c):
    paint(c)
    safe_move()

# setup go to top left
turn_left()
line_move()
turn_right()

#--- pixels

"""

# https://stackoverflow.com/questions/138250/
# https://stackoverflow.com/questions/19914509/


def paintgen(r, g, b):
    hexed = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return f"pmov('{hexed}')\n"


def generate_karel_for_img(imgPath: str) -> str:
    with Image.open(imgPath, 'r') as im:
        px = im.load()
        width, height = im.size

    gencode = f"#--- GENERATED CODE ---#\n# run on {width} x {height} canvas\n"

    gencode += BASE_CODE

    for y in range(height):
        for x in range(width):
            c = px[x, y]
            gencode += paintgen(c[0], c[1], c[2])
        gencode += "reset()\n"

    return gencode


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Incorrect number of arguments!\nexiting...")
        exit()

    g = generate_karel_for_img(sys.argv[1])
    print(g)

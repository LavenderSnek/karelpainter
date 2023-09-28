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
    paint(color[c])
    safe_move()

# setup go to top left
turn_left()
line_move()
turn_right()

#--- pixels

"""

# https://stackoverflow.com/questions/138250/
# https://stackoverflow.com/questions/19914509/

#https://stackoverflow.com/questions/9694165/
# added by @Zorg-Borg
# create func to get closest color name from rgb
def get_color_name(rgb):
    colors = {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        "purple": (255, 0, 255),
        "cyan": (0, 255, 255),
        "black": (0, 0, 0),
        "white": (255, 255, 255),
        "orange": (255, 165, 0),
    }
    min_distance = float("inf")
    closest_color = None
    for color, value in colors.items():
        distance = sum([(i - j) ** 2 for i, j in zip(rgb, value)])
        if distance < min_distance:
            min_distance = distance
            closest_color = color
    return f"pmov ('{closest_color}')\n"

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
            gencode += get_color_name((c[0], c[1], c[2]))
        gencode += "reset()\n"

    return gencode

#added by @Zorg-Borg
# create func to format image to 40x40 pixels
def formatImg(imgPath: str):
    with Image.open(imgPath, 'r') as im:
        width, height = im.size
        if width > 40 or height > 40:
            im = im.resize((40, 40), Image.Resampling.LANCZOS)
            im.save("formatted.png")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Incorrect number of arguments!\nexiting...")
        exit()
    formatImg(sys.argv[1])
    g = generate_karel_for_img("formatted.png")
    print(g)

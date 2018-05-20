import sys
import json
from argparse import ArgumentParser
from graphics import *

def check_args(args):
    print("Input file: " + args.input_file)
    input_file_splitted = args.input_file.split('.')
    if len(input_file_splitted) != 2 or input_file_splitted[1] != 'json':
        raise ValueError("Invalid inputfile name.")
    if args.output_file:
        print("Output file: " + args.output_file)
        output_file_splitted = args.output_file.split('.')
        if len(output_file_splitted) != 1 and output_file_splitted[1] != 'png' or len(output_file_splitted) > 2:
            raise ValueError("Invalid outputfile name.")


def main():
    parser = ArgumentParser()
    parser.add_argument("input_file", help="input file name")
    parser.add_argument("-o", "--output_file", nargs="?", help = "output file name (optional)")

    args = parser.parse_args()
    try:
        check_args(args)
    except Exception as e:
        print("Error: " + str(e))
        exit(1)

    with open(args.input_file, 'r') as f:
        d = json.load(f)
        print(d)
        # print(d["Figures"])
        for fig in d["Figures"]:
            print(fig['type'])
        print(d["Palette"])

    win = GraphWin('JSON picture', 650, 400)
    pt = Point(100, 50)
    pt.draw(win)

    win.postscript(file="image.eps", colormode='color')
    from PIL import Image as NewImage
    img = NewImage.open("image.eps")
    img.save(args.output_file, "png")

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
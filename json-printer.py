import sys
import json
from argparse import ArgumentParser
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from os.path import exists


def check_args(args):
    print('Input file: ' + args.input_file)
    input_file_splitted = args.input_file.split('.')
    if len(input_file_splitted) != 2 or input_file_splitted[1] != 'json':
        raise ValueError('Invalid input file name.')
    if not exists(args.input_file):
        raise ValueError('Input file doesn\'t exist.')
    if args.output_file:
        print('Output file: ' + args.output_file)
        output_file_splitted = args.output_file.split('.')
        if len(output_file_splitted) != 1 and output_file_splitted[1] != 'png' or len(output_file_splitted) > 2:
            raise ValueError('Invalid output file name.')


def parse_json(json_dict):
    if not {'Figures', 'Screen', 'Palette'}.issubset(set(json_dict.keys())):
        raise SyntaxError('Invalid JSON syntax.')
    figures = []
    for fig in json_dict['Figures']:
        fig_type = fig['type']
        print(fig)
        if fig_type == 'point':
            if 'x' not in fig or 'y' not in fig:
                raise SyntaxError('Invalid JSON syntax - point.')
        elif fig_type == 'polygon':
            if 'points' not in fig:
                raise SyntaxError('Invalid JSON syntax - polygon.')
        elif fig_type == 'rectangle':
            if not {'x', 'y', 'height', 'width'}.issubset(set(fig.keys())):
                raise SyntaxError('Invalid JSON syntax - rectangle.')
        elif fig_type == 'square':
            if not {'x', 'y', 'size'}.issubset(set(fig.keys())):
                raise SyntaxError('Invalid JSON syntax - square.')
        elif fig_type == 'circle':
            if not {'x', 'y', 'radius'}.issubset(set(fig.keys())):
                raise SyntaxError('Invalid JSON syntax - circle.')


def main():
    parser = ArgumentParser()
    parser.add_argument("input_file", help="input file name")
    parser.add_argument("-o", "--output_file", nargs="?", help="output file name (optional)")

    args = parser.parse_args()
    try:
        check_args(args)
    except Exception as e:
        print("Error: " + str(e))
        exit(1)

    with open(args.input_file, 'r') as f:
        json_dict = json.load(f)

    print()

    # print(json_dict["Palette"])
    print(json_dict["Screen"]["width"])
    print(json_dict["Screen"]["height"])

    try:
        parse_json(json_dict)
    except Exception as e:
        print("Error: " + str(e))
        exit(1)

    figure = plt.figure()

    if args.output_file:
        figure.savefig('rect1.png', dpi=1)


if __name__ == "__main__":
    main()
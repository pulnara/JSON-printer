import json
from argparse import ArgumentParser
from os.path import exists
from ast import literal_eval
from figures import *


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
        if (len(output_file_splitted) != 1 and output_file_splitted[1] != 'png') or len(output_file_splitted) > 2:
            raise ValueError('Invalid output file name.')
        elif len(output_file_splitted) == 1:
            args.output_file += '.png'


def rgb_to_html(rgb_tuple):
    hex = "#"
    for i in rgb_tuple:
        # print(format(i, '02x'))
        hex += format(i, '02x')
    return hex


def get_color(palette, color):
    if color[0] == '(':
        result = rgb_to_html(literal_eval(color))
    elif color in palette.keys():
        result = palette[color]
    elif color[0] == '#':
        result = color
    else:
        raise SyntaxError('Invalid JSON syntax - unknown color.')
    return result


def parse_json(json_dict):
    if not {'Figures', 'Screen', 'Palette'}.issubset(set(json_dict.keys())):
        raise SyntaxError('Invalid JSON syntax.')

    figures = []

    if not {'fg_color', 'bg_color', 'height', 'width'}.issubset(set(json_dict['Screen'].keys())):
        raise SyntaxError("Invalid JSON syntax - screen.")

    screen_tmp = json_dict['Screen']
    screen = Screen(screen_tmp['fg_color'], screen_tmp['bg_color'], screen_tmp['height'], screen_tmp['width'])

    for fig in json_dict['Figures']:
        fig_type = fig['type']
        # print(fig)

        if 'color' in fig:
            color = get_color(json_dict['Palette'], fig['color'])
        else:
            color = screen.fg_color

        if fig_type == 'point':
            if 'x' not in fig or 'y' not in fig:
                raise SyntaxError('Invalid JSON syntax - point.')
            figures.append(Point(color, fig['x'], fig['y']))
        elif fig_type == 'polygon':
            if 'points' not in fig:
                raise SyntaxError('Invalid JSON syntax - polygon.')
            figures.append(Polygon(color, fig['points']))
        elif fig_type == 'rectangle':
            if not {'x', 'y', 'height', 'width'}.issubset(set(fig.keys())):
                raise SyntaxError('Invalid JSON syntax - rectangle.')
            figures.append(Rectangle(color, fig['x'], fig['y'], fig['height'], fig['width']))
        elif fig_type == 'square':
            if not {'x', 'y', 'size'}.issubset(set(fig.keys())):
                raise SyntaxError('Invalid JSON syntax - square.')
            figures.append(Square(color, fig['x'], fig['y'], fig['size']))
        elif fig_type == 'circle':
            if not {'x', 'y', 'radius'}.issubset(set(fig.keys())):
                raise SyntaxError('Invalid JSON syntax - circle.')
            figures.append(Circle(color, fig['x'], fig['y'], fig['radius']))

    return screen, figures


def draw(args, figures, screen):
    picture = plt.figure(figsize=(screen.width, screen.height), dpi=1)
    picture.artists.append(plt.Rectangle((0, 0), screen.width, screen.height, color=screen.bg_color))

    for fig in figures:
        picture.artists.append(fig.get_artist())

    plt.show()
    if args.output_file:
        picture.savefig(args.output_file)


def main():
    parser = ArgumentParser()
    parser.add_argument("input_file", help="input file name")
    parser.add_argument("-o", "--output_file", nargs="?", help="output file name (optional)")

    args = parser.parse_args()
    try:
        check_args(args)
    except Exception as e:
        print('Error: ' + str(e))
        exit(1)

    with open(args.input_file, 'r') as f:
        json_dict = json.load(f)

    print()

    try:
        screen, figures = parse_json(json_dict)
        draw(args, figures, screen)
    except Exception as e:
        print('Error: ' + str(e))
        exit(1)


if __name__ == "__main__":
    main()
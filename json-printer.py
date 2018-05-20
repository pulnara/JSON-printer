import sys
from argparse import ArgumentParser


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



if __name__ == "__main__":
    main()
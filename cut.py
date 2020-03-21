import argparse
from moviepy.editor import *


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('in_fname', type=str)
    parser.add_argument('out_fname', type=str)
    parser.add_argument('start_time', type=int)
    parser.add_argument('end_time', type=int)

    args = parser.parse_args()

    VideoFileClip(args.in_fname).subclip(args.start_time, args.end_time).write_videofile(args.out_fname)


if __name__ == "__main__":
    main()


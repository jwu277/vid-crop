from tqdm import tqdm

import argparse

import imageio

Y1 = 320
Y2 = Y1 + 33 * 16


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('in_fname', type=str)
    parser.add_argument('out_fname', type=str)

    args = parser.parse_args()

    reader = imageio.get_reader(args.in_fname)
    fps = reader.get_meta_data()['fps']
    writer = imageio.get_writer(args.out_fname, fps=fps)

    for im in tqdm(reader, total=reader.get_meta_data()['duration'] * fps):
        writer.append_data(im[Y1:Y2,:,:])
    writer.close()


if __name__ == "__main__":
    main()


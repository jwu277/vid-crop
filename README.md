# vid-crop
A command-line script to crop videos. In particular, this is for when someone films a landscape video in portrait mode and you need to crop into the actual video.

## Dependencies
- Python 3
  - `imageio`
  - `tqdm` (for that sexy progress bar)
- `ffmpeg`

## How to Run
On the command line:
```
> ./path/to/vid-crop.sh ./path/to/original.mp4 ./path/to/new.mp4
```
where `./path/to/XXXX` is the relative path to entity `XXXX`.

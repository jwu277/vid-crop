# vid-crop
## vid-crop main
A command-line script to crop videos. In particular, this is for when someone films a landscape video in portrait mode and you need to crop into the actual video.
## cut
A utility to obtain a given time duration cut of a video.

## Dependencies
### vid-crop
- Python 3
  - `imageio`
  - `tqdm` (for that sexy progress bar)
- `ffmpeg`
### cut
- Python 3
  - `moviepy`

## How to Run
### vid-crop
On the command line:
```
> ./path/to/vid-crop.sh ./path/to/original.mp4 ./path/to/new.mp4
```
where `./path/to/XXXX` is the relative path to entity `XXXX`.
### cut
On the command line:
```
> python ./path/to/cut.py ./path/to/original.mp4 ./path/to/new.mp4 YY ZZ
```
Again `./path/to/XXXX` is the relative path to entity `XXXX`. `YY` and `ZZ` are the start and end times (integer, in seconds) of the cut, respectively.

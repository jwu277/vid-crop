# vid-crop
## vid-crop main
A command-line script to crop videos. In particular, this is for when someone films a landscape video in portrait mode and you need to crop into the actual video.
## cut
A utility to obtain a given time duration cut of a video.

## Currently Supported Codecs
### Video
- `mp4`
Note: I have only tested the scripts on `mp4` files. It may work with other video formats.
### Audio
- `mp3`
- `aac`

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
> ./path/to/vid-crop.sh ./path/to/original.mp4 ./path/to/new.mp4 CODECTYPE
```
where `./path/to/XXXX` is the relative path to entity `XXXX`. `CODECTYPE` is the audio codec of the video file. Currently we support only `aac` and `mp3`.
### cut
On the command line:
```
> python ./path/to/cut.py ./path/to/original.mp4 ./path/to/new.mp4 YY ZZ
```
Again `./path/to/XXXX` is the relative path to entity `XXXX`. `YY` and `ZZ` are the start and end times (integer, in seconds) of the cut, respectively.
Running `cut` on `mp4` files, it seems that the audio encoding is changed to `mp3`.

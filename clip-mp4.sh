python ./mp4-clip.py $1 temp.mp4
ffmpeg -i $1 -vn -acodec copy temp.mp3
ffmpeg -i temp.mp4 -i temp.mp3 -shortest -c:v copy -c:a aac -b:a 256k $2

rm temp.mp3
rm temp.mp4

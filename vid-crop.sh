python ./cropper.py $1 temp.mp4
if [ $3 == "aac" ]; then
    ffmpeg -i $1 -vn -acodec copy temp.aac
    ffmpeg -i temp.mp4 -i temp.aac -shortest -c:v copy -c:a aac -b:a 256k $2
    rm temp.aac
elif [ $3 == "mp3" ]; then
    ffmpeg -i $1 -vn -acodec copy temp.mp3
    ffmpeg -i temp.mp4 -i temp.mp3 -shortest -c:v copy -c:a libmp3lame -b:a 256k $2
    rm temp.mp3
fi

rm temp.mp4

#!/bin/bash

URL="rtsp://admin:admin@192.168.1.201/2"

ffmpeg -i $URL  -vcodec h264  ./test.mp4

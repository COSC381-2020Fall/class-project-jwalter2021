#!/usr/bin/bash
cd ./youtube_data
while read p; do
	python download_youtube_data.py $p > $p
done <video_ids.txt

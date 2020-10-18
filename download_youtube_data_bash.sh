#!/usr/bin/bash
mkdir youtube_data
cd ./youtube_data
while read p; do
	python download_youtube_data.py $p > $p.json
done <video_ids.txt

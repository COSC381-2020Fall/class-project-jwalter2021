# Requirements.txt

This file contains various packages that are required to run some of these scripts.

## Usage

Type python3 -m pip install -r requirements.txt into the terminal and all the packages listed in the file should be installed to your client.

# Custom Search Engine

This script will search www.W3Schools.com through my custom search engine provided by Google.

## Usage

Modify config.py and insert your own API key and CSE ID. In the Amazon Linux 2 bash terminal, type python3 cse.py and the search format in .json format should appear as output.

# Retrieving Data From YouTube

This script will extract data from a series of YouTube videos and print said data into individual .json files for each video.

## Usage

Like before, make sure you have your own API key pasted into config.py. In the terminal, type bash download_youtube_data_bash.sh. A directory named youtube_data should be created, and in that directory, there will be 98 files representing data for each YouTube video. Each .json file's name is that video's video ID. These IDs are provided by video_ids.txt in the repository.

# Create Data For Whoosh Indexing

This script extracts data from the YouTube JSON files and populates dictionary objects with their info.

## Usage

Make sure your JSON files from the YouTube data extraction are in the same directory. In the terminal, type create_data_for_indexing.py. The script should run as described above.

# Creating Whoosh Indexing and Performing a Test Query

These scripts will create a whoosh index for YouTube data and then perform a test search query with said index, in that order.

## Usage

Type create_whoosh_index.py in the terminal to, as the file name states, create a whoosh index. Consecutively, do the same with query_on_whoosh.py to perform a test query on the newly created whoosh index.
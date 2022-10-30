
import json
import datetime
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
import openai


# this function creates a transcript of the youtube video
# YouTubeVideoId is the id of the video you want the transcript of

def youtube_video_to_json_transcript(YouTubeVideoId='0m3hGZvD-0s', outputFileName = 'transcript.json'):
    #link = input("Enter video id: ")
    link = YouTubeVideoId
    transcript = YouTubeTranscriptApi.get_transcript(link)

    with open(outputFileName, 'w') as f:
        json.dump(transcript, f)

# Load the transcript into python
transcript_file_name ='transcript.json'
def read_json_file(json_file_name=transcript_file_name):
    # Opening JSON file
    with open(json_file_name, 'r') as openfile:
    
        # Reading from json file
        json_object = json.load(openfile)
    return json_object

def sec_to_timestamp(time_unit):
    converted_time = datetime.timedelta(seconds=float(time_unit))
    #print(converted_time)
    return converted_time
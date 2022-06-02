import os
import random
import webbrowser
class URL:
    # If video URL file does not exist, create one
    def urlCreator():
        if not os.path.isfile("youtube_alarm_videos.txt"):
            print('Creating "youtube_alarm_videos.txt"...')
        with open("youtube_alarm_videos.txt", "w") as alarm_file:
            alarm_file.write("https://www.youtube.com/watch?v=NEMJcTunFWo&list=OLAK5uy_lf3PyPynxbLvqL8dqt-1OnnvyVaH4Aui8&ab_channel=SoundEffectsZone%26InYogaAcademy-Topic")
    def openRandomVideo():
        # Load list of possible video URLs
        with open("youtube_alarm_videos.txt", "r") as alarm_file:
            videos = alarm_file.readlines()
        # Open a random video from the list
        webbrowser.open(random.choice(videos)) 
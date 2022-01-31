from youtube_statistics import YTstats


API_KEY = "AIzaSyBCdkwDx6T-1_fR96eE_bjx7hYfnXX6A0E"
channel_id = "UC0rE2qq81of4fojo-KhO5rg"

yt = YTstats(API_KEY, channel_id)
yt.get_channel_statistics()
yt.get_channel_video_data()
yt.dump()


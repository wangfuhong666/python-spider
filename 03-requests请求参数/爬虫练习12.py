import requests
import moviepy
url='https://k0u6fy30yecy18z.djvod.ndcimgs.com/upic/2020/08/12/02/BMjAyMDA4MTIwMjIxMTdfMjAxMzE2ODIxNV8zNDE2MjA0MTgxMF8yXzM=_b_B4b4ab8bf349f8ad80be4627714b7b879.mp4?tag=1-1765085311-unknown-0-myzzaxvqsv-cff8fbd4a07867aa&provider=self&clientCacheKey=3xw7ru8tnqwijqu_b.mp4&di=7597109d&bp=10004&x-ks-ptid=34162041810&kwai-not-alloc=self-cdn&kcdntag=p:Hubei;i:ChinaMobile;ft:UNKNOWN;h:COLD;pn:kuaishouVideoProjection&ocid=100000276&tt=b&ss=vps'
res=requests.get(url)
with open("搞笑.mp4", "wb") as f:
    f.write(res.content)
from moviepy.editor import VideoFileClip
# 替换为你的视频路径和输出音频路径，直接运行
VideoFileClip("搞笑.mp4").audio.write_audiofile("搞笑.mp3")

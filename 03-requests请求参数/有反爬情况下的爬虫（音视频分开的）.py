url='https://upos-sz-mirror08c.bilivideo.com/upgcxcode/66/23/32712232366/32712232366-1-100026.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&platform=pc&mid=479967744&deadline=1761990986&og=hw&trid=ca7cbaac353945d3be9690d12a69868u&oi=1972834773&nbs=1&gen=playurlv3&os=08cbv&upsig=2054a0d79366b2df2811530f69455ad0&uparams=e,uipk,platform,mid,deadline,og,trid,oi,nbs,gen,os&bvc=vod&nettype=0&bw=613814&build=0&dl=0&f=u_0_0&agrr=1&buvid=36D48874-CD56-0F25-B426-954AA9771D7C55518infoc&orderid=0,3'
# 导入请求模块
import requests
# 引进请求头（伪装）
headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0',
        'Referer':'https://www.bilibili.com/video/BV1HdnizVEid/?spm_id_from=333.1387.search.video_card.click&vd_source=112cffe2c10bbb0d68b4a3976061a73e'
}
# 使用request
response = requests.get(url, headers=headers)
open("1让板牙象棋捉个正着！“板鸭象棋”是盗版？真相来了！.mp4", 'wb').write(response.content)
url='https://upos-sz-mirrorbd.bilivideo.com/upgcxcode/66/23/32712232366/32712232366-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&oi=1972834773&deadline=1761991188&trid=5f1f21ddbcb448f3ac56160bc925293u&mid=479967744&gen=playurlv3&os=bdbv&uipk=5&platform=pc&nbs=1&og=hw&upsig=726a49b268b7a4d08d2604e8fbeafa07&uparams=e,oi,deadline,trid,mid,gen,os,uipk,platform,nbs,og&bvc=vod&nettype=0&bw=145836&agrr=1&buvid=36D48874-CD56-0F25-B426-954AA9771D7C55518infoc&build=0&dl=0&f=u_0_0&orderid=0,3'
# 导入请求模块
import requests
# 引进请求头（伪装）
headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0',
        'Referer':'https://www.bilibili.com/video/BV1HdnizVEid/?spm_id_from=333.1387.search.video_card.click&vd_source=112cffe2c10bbb0d68b4a3976061a73e'
}
# 使用request
response = requests.get(url, headers=headers)
open("1让板牙象棋捉个正着！“板鸭象棋”是盗版？真相来了！.mp3", 'wb').write(response.content)
#(安装moviepy)把音频和视频合起来
from moviepy.editor import *
#加载视频和音频
video = VideoFileClip('1让板牙象棋捉个正着！“板鸭象棋”是盗版？真相来了！.mp4')
audio = AudioFileClip('1让板牙象棋捉个正着！“板鸭象棋”是盗版？真相来了！.mp3')
#把它们合并（给视频天津背景音乐）
final = video.set_audio(audio)
#导出成品（把最终的数据写入原文件）
final.write_videofile('让板牙象棋捉个正着！“板鸭象棋”是盗版？真相来了！.mp4')
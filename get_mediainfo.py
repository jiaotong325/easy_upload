import os
import json
from datetime import datetime, timezone
import subprocess
def get_mediainfo(video):
    # 分离出文件名和扩展名
    filename, ext = os.path.splitext(video)
    # Mediainfo video.mp4 > video_mediainfo.txt
    print('Getting mediainfo...')
    
    # 没有文件就新建文件
    command1 = f'Mediainfo {video} > {filename}_mediainfo.txt'
    command2 = f'Mediainfo --Output=JSON {video} > {filename}_mediainfo_json.txt'
    subprocess.run(command1, shell=True)
    subprocess.run(command2, shell=True)
    print('Get over...')
    
def generate_simple_mediainfo(filename):
    filename, ext = os.path.splitext(filename)
    # 读取文件内容
    with open(f'{filename}_mediainfo_json.txt', 'r') as f:
        # 读取json文件
        data = json.load(f)
    
    # 获取当前的UTC日期时间
    utc_now = datetime.now(timezone.utc)
    RELEASE_DATE = utc_now.strftime("UTC %Y-%m-%d")
    
    # 还需要根据大小动态调整单位
    RELEASE_SIZE = int(data['media']['track'][0]['FileSize'])/1024/1024
    
    RELEASE_FORMAT = data['media']['track'][0]['Format']
    
    # 动态调整
    DURATION = data['media']['track'][0]['Duration']
    
    OVERALL_BITRATE = data['media']['track'][0]['OverallBitRate']
    
    RESOLUTION = data['media']['track'][1]['Width'] + ' x ' + data['media']['track'][1]['Height']
    VIDEO_CODEC = data['media']['track'][1]['Format'] +" "+ data['media']['track'][1]['Format_Profile']+'@L'+data['media']['track'][1]['Format_Level']+'@'+data['media']['track'][1]['Format_Tier']
    
    FRAME_RATE = data['media']['track'][0]['FrameRate']+' FPS'
    Audio = data['media']['track'][2]['Channels'] +' channels ' + data['media']['track'][2]['Format'] + ' ' + data['media']['track'][2]['Format_AdditionalFeatures'] + str(int(data['media']['track'][2]['BitRate'])/1024)+'kb/s'
    
    UPLOADER = 'CatEDU'
    
    
    # 写入文件bbcode.txt中
    with open(f'{filename}_bbcode.txt', 'w') as f:
        f.write(f'[img]https://pterclub.com/pic/CS.png[/img]\n')
        f.write(f'[quote][size=4][color=royalblue][b]★★★★★ General Information ★★★★★[/b][/color][/size]\n')
        f.write(f'RELEASE.NAME........:\t[珠穆朗玛].Mount.Everest.S01.2022.2160p.WEB-DL.H265.AAC.5.1-CatEDU\n')
        f.write(f'RELEASE.DATE........:\t{RELEASE_DATE}\n')
        f.write(f'RELEASE.SIZE........:\t{RELEASE_SIZE:.2f} MiB\n')
        f.write(f'RELEASE.FORMAT......:\t{RELEASE_FORMAT}\n')
        f.write(f'DURATION.............:\t{DURATION}\n')
        f.write(f'OVERALL.BITRATE..:\t{OVERALL_BITRATE}\n')
        f.write(f'RESOLUTION..........:\t{RESOLUTION}\n')
        f.write(f'VIDEO.CODEC........:\t{VIDEO_CODEC}\n')
        f.write(f'FRAME.RATE..........:\t{FRAME_RATE}\n')
        f.write(f'AUDIO..................:\t{Audio}\n')
        f.write(f'UPLOADER..............:\t{UPLOADER}\n')
        f.write(f'[/quote]\n')
        
        f.write(f'[quote]')
        # 将文件{filename}_mediainfo.txt写入此处
        with open(f'{filename}_mediainfo.txt', 'r') as f1:
            f.write(f1.read())
        f.write(f'[/quote]\n')
        
        f.write(f'[img]https://img.pterclub.com/images/GDJT.png[/img]\n')
        
        
        




        
        
    
    
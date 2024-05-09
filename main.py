# 导入函数
from get_mediainfo import get_mediainfo
from get_mediainfo import generate_simple_mediainfo


def main(video):
    # 生成mediainfo和简化mediainfo
    get_mediainfo(video)
    generate_simple_mediainfo(video)



main('video.mp4')
    
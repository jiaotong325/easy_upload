import requests
from pymediainfo import MediaInfo
import os

# 该路径下的图片均会被上传至 pixhost.to
# 仅支持 png、jpg、jpeg、gif 格式的图片
source_path = ''


# 设置请求头
headers = {
    'Accept': 'application/json'
}

def uoloads(image):
    # 确定 content_type 的值
    if image.lower().endswith('.png'):
        content_type = 'image/png'
    elif image.lower().endswith('.jpg') or image.lower().endswith('.jpeg'):
        content_type = 'image/jpeg'
    elif image.lower().endswith('.gif'):
        content_type = 'image/gif'
    else:
        raise ValueError('Unsupported file format')


    # 设置请求参数
    files = {
        'img': (os.path.basename(image), open(image, 'rb')),
        'content_type': (None, '0'),
        'max_th_size': (None, '420')
    }

    # 发送 POST 请求
    response = requests.post('https://api.pixhost.to/images', files=files, headers=headers)

    # 输出响应结果
    data = response.json()
    print(data)
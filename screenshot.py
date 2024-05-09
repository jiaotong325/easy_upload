import os
# ffmpeg -i 视频文件名.mp4 -vf "thumbnail" -frames:v 1 输出文件名.png

# 需要分析视频时长
# 时长设置为video_duration



def shot(video_name, video_duration, video_n):
    
    
    name = 'video.mp4'
    # 视频时长单位是秒
    duration = 20*60
    # 对视频均匀截取 n张图
    n = 10
    
    # 视频文件名
    video_name = video_name
    # 视频时长
    video_duration = video_duration
    # 截取图片数量
    video_n = n
    
    # 考虑到片头片尾，截取图片的时间需要调整
    
    # 截取图片的时间间隔
    interval = video_duration / video_n
    # 视频文件名不包含扩展名
    video_name = os.path.splitext(video_name)[0]
    # 截取图片的命令
    command = f'ffmpeg -i {video_name}.mp4 -vf "thumbnail" -frames:v 1 {video_name}.png'
    # 执行截取图片的命令
    os.system(command)
    # 保存截取的图片
    for i in range(1, video_n):
        command = f'ffmpeg -ss {i * interval} -i {video_name}.mp4 -vf "thumbnail" -frames:v 1 {video_name}_{i}.png'
        os.system(command)
    print('Shot Done!')


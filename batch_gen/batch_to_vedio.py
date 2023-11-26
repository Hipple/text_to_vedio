# -*- coding: utf-8 -*-
"""
作者：张贵发
日期：2023年06月12日
描述：将生成的语音、图像合成视频
"""

import os
from moviepy.editor import ImageSequenceClip, AudioFileClip, concatenate_videoclips
import numpy as np

import random


def fl_right(gf, t):
    # 获取原始图像帧
    frame = gf(t)

    # 进行滚动效果，将图像向右滚动50像素
    scroll_x = int(t * 2)  # 根据时间t计算滚动的像素数
    new_frame = np.zeros_like(frame)

    # 将原始帧的内容向右滚动50像素，并将结果赋值给新帧
    new_frame[:, scroll_x:] = frame[:, :frame.shape[1] - scroll_x]

    return new_frame

def fl_down(gf, t):
    # 获取原始图像帧
    frame = gf(t)

    # 进行滚动效果，将图像向右滚动50像素
    # scroll_x = int(t * 5)  # 根据时间t计算滚动的像素数
    scroll_y = int(t * 2)  # 根据时间t计算滚动的像素数
    new_frame = np.zeros_like(frame)

    # 将原始帧的内容向右滚动50像素，并将结果赋值给新帧

    new_frame[scroll_y:, :] = frame[:frame.shape[0] - scroll_y, :]

    return new_frame



def fl_up(gf, t):
    # 获取原始图像帧
    frame = gf(t)

    # 进行滚动效果，将图像向下滚动50像素
    height, width = frame.shape[:2]
    scroll_y = int(t * 10)  # 根据时间t计算滚动的像素数
    new_frame = np.zeros_like(frame)

    # 控制滚动的范围，避免滚动超出图像的边界
    if scroll_y < height:
        new_frame[:height-scroll_y, :] = frame[scroll_y:, :]

    return new_frame

def random_fl(gf, t):
    # 定义三个变换函数列表
    fl_functions = [fl_up, fl_down, fl_right]
    # 随机选择一个变换函数
    random_fl_func = random.choice(fl_functions)
    # 调用随机选择的变换函数
    return random_fl_func(gf, t)




def merge_vedio(image_dir_path,audio_dir_path,parent):


    # 将文件名按照顺序排列
    image_files = os.listdir(image_dir_path)
    audio_files = os.listdir(audio_dir_path)
    print(image_files)
    clips = []



    for i in range(len(audio_files)):
        image_path = image_dir_path+'/'+image_files[i]
        audio_path = audio_dir_path+'/'+audio_files[i]

        audio_clip = AudioFileClip(audio_path)
        img_clip = ImageSequenceClip([image_path], audio_clip.duration)

        img_clip = img_clip.set_position(('center', 'center')).fl(fl_up,apply_to=['mask']).set_duration(audio_clip.duration)

        clip = img_clip.set_audio(audio_clip)


        clips.append(clip)

    # 将所有剪辑合并成一个视频
    final_clip = concatenate_videoclips(clips)
    new_parent = image_dir_path.replace("data_image","data_vedio")
    # 导出视频
    # if not os.path.exists(new_parent):
    #     os.makedirs(new_parent)
    new_path = image_dir_path.replace("data_image","data_vedio")
    reulst_path = '/'.join(new_path.rsplit('/', 2)[:-1])+'/'+parent
    if not os.path.exists(reulst_path):
        os.makedirs(reulst_path)
    final_clip.write_videofile(reulst_path+'/'+new_path.rsplit('/', 1)[-1]+".mp4", fps=24,audio_codec="aac")  # 可以根据需要调整fps值

    return new_path+".mp4"



if __name__ == '__main__':
    # lists =os.listdir('../data/data_image/少年歌行第一章/少年歌行第一章')
    # print(lists)
    merge_vedio("../data/data_image/少年歌行第一章/少年歌行第一章","../data/data_audio/少年歌行第一章/少年歌行第一章","ceshi")



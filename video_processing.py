import cv2

videos_src_path = "/Users/shuchangxu/PycharmProjects/face_morpher/res/input.mp4"
frames_save_path = "/Users/shuchangxu/PycharmProjects/face_morpher/res/src_frames/"
width = 640
height = 360
time_interval = 1


def video2frame(video_path, pics_path, frame_width, frame_height, interval):
    """
    将视频按固定间隔读取写入图片
    :param video_src_path: 视频存放路径
    :param frame_save_path:　保存路径
    :param frame_width:　保存帧宽
    :param frame_height:　保存帧高
    :param interval:　保存帧间隔
    :return:　帧图片
    """
    cap = cv2.VideoCapture(video_path)
    frame_index = 0
    frame_count = 0
    if cap.isOpened():
        success = True
    else:
        success = False
        print("读取失败!")

    while True:
        success, frame = cap.read()
        if success:

            if frame_index % interval == 0:
                resize_frame = cv2.resize(frame, (frame_width, frame_height), interpolation=cv2.INTER_AREA)
                cv2.imwrite(pics_path + "%02d.png" % frame_count, resize_frame)
                frame_count += 1

            frame_index += 1
        else:
            break
    cap.release()


if __name__ == '__main__':
    video2frame(videos_src_path, frames_save_path, width, height, time_interval)
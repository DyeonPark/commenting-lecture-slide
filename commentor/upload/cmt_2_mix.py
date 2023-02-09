# * 코드 파일 이름: cmt_2_mix.py
# * 코드 작성자: 박동연, 강소정, 김유진
# * 코드 설명: 동영상 강의 해설 파일을 생성하기 위해 전처리 파일을 조합하여 최종 해설 파일 생성
# * 코드 최종 수정일: 2021/08/21 (박동연)
# * 문의 메일: yeon0729@sookmyung.ac.kr


# 패키지 및 라이브러리 호출
import os
import sys
import time
import datetime
import warnings

from moviepy.editor import VideoFileClip, concatenate_videoclips

pdf2image_module_path = "data/Release-21.03.0/poppler-21.03.0/Library/bin/"
warnings.filterwarnings(action='ignore')  #경고 무시


# 의도한바와 같이 정렬될 수 있도록 파일번호 수정하여 반환하는 함수 (최대 9999장까지 가능)
def set_Filenum_of_Name(filenum):
    fileName = ""

    if (filenum < 10):  # 파일번호가 한자리일때
        fileName = "000" + str(filenum)
    elif (filenum >= 10 and filenum < 100):  # 파일번호가 두자리일때
        fileName = "00" + str(filenum)
    elif (filenum >= 100 and filenum < 1000):  # 파일번호가 세자리일때
        fileName = "0" + str(filenum)
    elif (filenum >= 1000 and filenum < 10000):  # 파일번호가 네자리일때
        fileName = str(filenum)
    else:
        sys.exit(">>> 파일이 너무 큽니다 - 9999장 이상")

    return fileName


def mix_mp4(tts_img_path, lecture_trim_path, mix_path):
    print("\n[lec과 tts 병합 시작] 원본 강의파일(mp4)과 TTS mp4파일 병합을 시작합니다")

    # 디렉토리 유무 검사 및 디렉토리 생성
    try:
        if not os.path.exists(mix_path):  # 디렉토리 없을 시 생성
            os.makedirs(mix_path)
    except OSError:
        print('Error: Creating directory. ' + mix_path)  # 디렉토리 생성 오류

    tts_img_list = os.listdir(tts_img_path)
    tts_img_list = [tts_file for tts_file in tts_img_list if tts_file.endswith(".mp4")]  # tts 가져오기
    tts_img_list.sort()
    print(">>> tts mp3 파일 목록:", tts_img_list)

    lec_list = os.listdir(lecture_trim_path)
    lec_list = [lec_file for lec_file in lec_list if lec_file.endswith(".mp4")]  # lec 가져오기
    lec_list.sort()
    print(">>> lec mp3 파일 목록:", lec_list)

    clip_list = []
    for i, j in zip(tts_img_list, lec_list):
        print(i, "-", j, ": 영상 불러오기")
        clip1 = VideoFileClip(tts_img_path + i)
        clip2 = VideoFileClip(lecture_trim_path + j)

        clip_list.append(clip1)
        clip_list.append(clip2)

    final_clip = concatenate_videoclips(clip_list)
    final_clip.write_videofile(mix_path + "mix.mp4", preset='ultrafast')

    print("[lec과 tts 병합 종료] 원본 강의파일(mp4)과 TTS mp4파일 병합을 종료합니다\n")


# 메인함수
def execute_mix(default_path):

    # 경로 설정 (경로 내에 한글 디렉토리 및 한글 파일이 있으면 제대로 동작하지 않음 유의 !!!!!)
    tts_img_path = default_path + "tts_img/"
    lecture_trim_path = default_path + "lecture_trim/"
    mix_path = default_path + "mix/"

    time_list = []
    total_start = time.time()

    # 모든 오디오 파일 병합 - mix
    tmp_start = time.time()
    mix_mp4(tts_img_path, lecture_trim_path, mix_path)
    tmp_sec = time.time() - tmp_start
    tmp_times = str(datetime.timedelta(seconds=tmp_sec)).split(".")
    time_list.append(tmp_times[0])

    total_sec = time.time() - total_start
    total_times = str(datetime.timedelta(seconds=total_sec)).split(".")

    print("\n■ MIX 시간:", time_list[0])
    print("■□■ 총 소요 시간:", total_times[0])

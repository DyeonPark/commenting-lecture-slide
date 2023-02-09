<h1 align="center"> 
시각장애 학생을 위한 동영상 강의 화면 음성 해설 서비스<br/>
Automatic Voice Commentary System for Online Video Lecture for Visually Impaired Students
  
<br>
  
<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white">
<img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=OpenCV&logoColor=white">
<img src="https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white">
<img src="https://img.shields.io/badge/Google Translate-4285F4?style=flat&logo=Google Translate&logoColor=white">  
<img src="https://img.shields.io/badge/Django-092E20?style=flat&logo=Django&logoColor=white"> 
<h4 align="center">숙명여자대학교 IT공학전공 2021년 1학기 졸업 프로젝트</h4>
</h1>

<br/>

## 프로젝트 배경
<p align="center">
<img src="https://github.com/DyeonPark/commenting-lecture-slide/blob/main/docs/background_img.png" height="250">
</p>

* 코로나 바이러스의 확산 방지를 위해 대다수의 교육기관에서 비대면 강의 시스템을 도입하였음
* 동영상 강의는 비대면 강의 시스템의 많은 부분을 차지하고 있음
* 그러나, 시각장애 학생들은 **동영상 강의의 화면에 무엇이 나오는지 알 수가 없어 강의 내용 이해도가 떨어지는 문제가 발생함**
* 또한 강의자료와 함께 사용하기도 어려워서 현재 수업하는 내용이 **강의자료에서 몇 페이지에 해당하는 지도 알기 어려움**


<h3 align="center"> 따라서 화면 등장하는 강의자료의 페이지 정보를 내용과 함께 해설해주는 시스템을 구축하고, <br/>
  이러한 자동 해설 동영상을 사용하기 용이하도록 전용 웹 플레이어를 함께 제공하고자 함!</h3>

<br/>

## 처리 프로세스
<p align="center">
<img src="https://github.com/DyeonPark/commenting-lecture-slide/blob/main/docs/process_img.png" height="350">
</p>

1. 교수자가 **강의 동영상과 강의자료 파일을 업로드**함
2. 서버에 구축되어 있는 시스템이 **강의 동영상 내 슬라이드 전환 시점을 도출하고, 해당 슬라이드가 강의자료의 몇 번째 페이지**에 해당하는지 유사도 매칭 알고리즘을 통해 파악
3. 강의자료에서 **슬라이드별로 텍스트, 이미지, 표에 대해서 자동으로 해설을 제공**하는 비디오 파일을 생성
4. 앞선 2단계에서 알아낸 슬라이드별 동영상 강의 내 등장시점 정보를 기반으로 직접 생성한 해설 비디오 파일과 원본 강의 **동영상을 조합 → 새로운 해설 비디오 파일 생성**
5. 학생은 **키보드로 간편하게 조작할 수 있는 전용 플레이어**를 사용하여 해설 강의 동영상을 수강

<br/>

## 발표 영상 및 논문

<p align="center">
  <img src="https://github.com/DyeonPark/commenting-lecture-slide/blob/main/docs/video_button.png" height="300">&nbsp;
  <img src="https://github.com/DyeonPark/commenting-lecture-slide/blob/main/docs/paper_img.png" height="300"/>
</p>

* 시연 및 발표 영상 링크: https://youtu.be/qrxdCjk2UBw
* 프로젝트 관련 저술 논문 링크: http://doi.org/10.17210/jhsk.2022.06.17.2.31

<br/>

## 시연 예시 이미지
<p align="center">
  <img src="https://github.com/DyeonPark/commenting-lecture-slide/blob/main/docs/result1_img.png" height="300"/>
</p> 

1. **원본 강의 업로드 및 해설 삽입 (교수자 화면)**: 교수자가 로그인하면 기존 LMS 시스템을 이용했던 것과 동일하게 동영상과 강의자료를 업로드하면, 본 시스템이 자동으로 이를 분석하여 슬라이드마다 해설을 삽입합니다
2. **온라인 강의 플랫폼 홈페이지 (학생 화면)**: 학생이 LMS 시스템에 로그인하면, 기존과 동일하게 강좌목록을 확인할 수 있습니다. 여기서 **'해설 비디오 파일 재생' 버튼을 누르면 자동으로 해설이 제공되는 동영상을 전용 플레이어로 재생**할 수 있습니다
  
<br/>
  
<p align="center">
  <img src="https://github.com/DyeonPark/commenting-lecture-slide/blob/main/docs/result2_img.png" height="300"/>
</p>

3. **원본 강의 동영상(mp4)**: 원본 강의 동영상은 아무런 해설이 제공되지 않는 교수자가 처음에 올린 동영상입니다
4. **강의자료 해설이 제공되는 비디오 플레이어**: 강의자료 화면에 대해서 자동으로 해설이 제공되는 동영상을 효과적으로 이용 및 수강하기 위한 전용 플레이어의 모습입니다. 키보드로 간단하게 동작이 가능하며, 정안인 학생도 이용할 수 있도록 슬라이드 전환 시점 단위로 GUI를 구성하였습니다.

<br/>

## 실행 방법

```bash
python manage.py runserver
```
<br/>

## 설치할 라이브러리
<pre><code> $ pip install opencv-python scenedetect pandas pdf2image fitz pillow scikit-image gtts pdfplumber googletrans pytesseract moviepy pydub mutagen requests </code></pre>

* opencv-python: Python용 OpenCV 설치
* scenedetect: 강의 동영상 내 전환시점 파악을 위한 라이브러리 설치
* pandas: 행렬 기반으로 데이터를 저장하고, csv 파일로 내보내기 위한 라이브러리 설치
* pdf2image: pdf 파일을 jpg로 변환하는 라이브러리 설치
* fitz: 이미지 추출하는 라이브러리 설치
* pillow: 파이썬 이미지 처리하는 라이브러리 설치
* scikit-image: 이미지간 유사도 계산을 위한 라이브러리 설치
* gtts: 텍스트를 음성으로 변환해주는 구글의 tts 라이브러리 설치
* pdfplumber: pdf파일을 텍스트로 변환해주는 라이브러리 설치
* googletrans: 구글 번역으로 영문을 한글으로 번역 설치
* pytesseract: 캡처 이미지에 대해 OCR 기능을 수행하기 위한 라이브러리 설치
* moviepy: mp4 영상 병합을 위한 라이브러리 설치
* pydub: 오디오 파일을 자르고 붙이기 위한 라이브러리 설치
* mutagen: mp3, mp4 파일의 길이를 추출하기 위한 라이브러리 설치]
* requests: 이미지 캡션 REST API 사용을 위한 HTTP 라이브러리 설치

<br/>

## 그 외 설치 및 설정
* PDF 렌더링 라이브러리 poppler 설치: https://poppler.freedesktop.org/ 
* 이후 microsoft azure computer vision 설정 가이드 참고: https://docs.microsoft.com/ko-kr/azure/cognitive-services/computer-vision/quickstarts-sdk/image-analysis-client-library?pivots=programming-language-python&tabs=visual-studio

<br/>

## 설치 환경
브라우저 : Internet Explorer, Firefox (Chrome, Microsoft Edge 제외)

<br/>

## Developers
#### Dongyeon Park: yeon0729@sookmyung.ac.kr
#### Sojeong Kang: thwjdrkd7@naver.com
#### Yujin Kim: heather0220@sookmyung.ac.kr

<br/>

Original Repository: https://github.com/Commentor/commenting-video-lecture

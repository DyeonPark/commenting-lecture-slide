<h1 align="center"> 
시각장애 학생을 위한 온라인 동영상 강의 화면의 음성 해설 서비스<br/>
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
* 코로나 바이러스의 확산 방지를 위해 대다수의 교육기관에서 비대면 강의 시스템을 도입하였음
* 동영상 강의는 비대면 강의 시스템의 많은 부분을 차지하고 있음
* 그러나, 시각장애 학생들은 **돋영상 강의의 화면에 무엇이 나오는지 알 수가 없어 강의 내용 이해도가 떨어지는 문제가 발생함**
* 또한 강의자료와 함께 사용하기도 어려워서 현재 나오는 화면이 강의자료에서 몇 페이지에 해당하는 지도 알 수 없음
→ 따라서

## 프로젝트 설명
강의 동영상 파일에 강의 슬라이드 화면을 읽어주는 해설을 추가한 비디오 파일을 시각장애 학생이 사용하기 용이하도록 전용 웹 플레이어로 재생할 수 있도록 한다

## 발표 영상 링크
https://youtu.be/qrxdCjk2UBw

## 실행 방법

```bash
python manage.py runserver
```

## 설치할 라이브러리
Python용 OpenCV 설치
<pre><code> $ pip install opencv-python </code></pre>

강의 동영상 내 전환시점 파악을 위한 라이브러리 설치
<pre><code> $ pip install scenedetect[opencv] </code></pre>

행렬 기반으로 데이터를 저장하고, csv 파일로 내보내기 위한 라이브러리 설치
<pre><code> $ pip install pandas </code></pre>

pdf 파일을 jpg로 변환하는 라이브러리 설치
<pre><code> $ pip install pdf2image </code></pre>

이미지 추출하는 라이브러리 설치
<pre><code> $ pip install fitz </code></pre>

파이썬 이미지 처리하는 라이브러리 설치
<pre><code> $ pip install PIL </code></pre>

이미지간 유사도 계산을 위한 라이브러리 설치
<pre><code> $ pip install scikit-image </code></pre>

텍스트를 음성으로 변환해주는 구글의 tts 라이브러리 설치
<pre><code> $ pip install gTTS </code></pre>

pdf파일을 텍스트로 변환해주는 라이브러리 설치
<pre><code> $ pip install pdfplumber </code></pre>

구글 번역으로 영문을 한글으로 번역 설치
<pre><code> $ pip install googletrans </code></pre>

캡처 이미지에 대해 OCR 기능을 수행하기 위한 라이브러리 설치
<pre><code> $ pip install pytesseract </code></pre>

mp4 영상 병합을 위한 라이브러리 설치
<pre><code> $ pip install moviepy </code></pre>

오디오 파일을 자르고 붙이기 위한 라이브러리 설치
<pre><code> $ pip install pydub </code></pre>

mp3, mp4 파일의 길이를 추출하기 위한 라이브러리 설치
<pre><code> $ pip install mutagen </code></pre>

PDF 렌더링 라이브러리 poppler 설치
https://poppler.freedesktop.org/ 

이미지 캡션 REST API 사용을 위한 HTTP 라이브러리 설치
<pre><code>$ pip install requests</code></pre>
* 이후 microsoft azure computer vision 설정 가이드 참고
=> https://docs.microsoft.com/ko-kr/azure/cognitive-services/computer-vision/quickstarts-sdk/image-analysis-client-library?pivots=programming-language-python&tabs=visual-studio

## 설치 환경
브라우저 : Internet Explorer, Firefox (Chrome, Microsoft Edge 제외)

## 시연 예시 이미지
원본 강의 업로드 (교수자 화면)
<br>
![image](https://user-images.githubusercontent.com/47679768/134172323-b0bc549e-510e-4ecd-a08a-a5a38300a38f.png)

온라인 강의 플랫폼 홈페이지 (학생 화면)
<br>
![image](https://user-images.githubusercontent.com/47679768/134172390-1cfb1dfc-99e0-4309-9bb1-91243e829b6a.png)


## Developers
#### Dongyeon Park: yeon0729@sookmyung.ac.kr
#### Sojeong Kang: thwjdrkd7@naver.com
#### Yujin Kim: heather0220@sookmyung.ac.kr

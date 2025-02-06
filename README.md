# tts-kor

스트림릿으로 한국어 TTS(Text-to-Speech) 서비스를 제공하는 프로젝트입니다.

## 소개

이 프로젝트는 Facebook의 MMS-TTS 모델을 활용하여 한국어 텍스트를 자연스러운 음성으로 변환하는 웹 서비스입니다. 스트림릿을 통해 사용자 친화적인 인터페이스를 제공합니다.

## 주요 기능

- 한국어 텍스트를 자연스러운 음성으로 변환
- 다양한 음성 스타일 지원
- 실시간 음성 생성 및 재생
- 간편한 웹 인터페이스

## 설치 방법

필요한 패키지를 설치합니다:

```bash
pip install transformers torch scipy uroman streamlit
```

## 실행 방법

```bash
streamlit run app.py
```

## 사용된 모델

이 프로젝트는 [facebook/mms-tts-kor](https://huggingface.co/facebook/mms-tts-kor) 모델을 사용합니다. 이 모델은 Facebook에서 개발한 한국어 TTS 모델로, 다음과 같은 특징이 있습니다:

- 고품질의 자연스러운 음성 생성
- 다양한 음성 스타일과 감정 표현 지원
- Hugging Face 통합으로 손쉬운 사용
- 한국어에 최적화된 음성 합성

## 시스템 요구사항

- Python 3.10 이상
- CUDA 지원 GPU (권장)
- 최소 4GB RAM
- 인터넷 연결 (모델 다운로드용)

## 기술 스택

### 백엔드
- Python 3.10
- PyTorch - 딥러닝 프레임워크
- Transformers - 허깅페이스 ML 모델 지원
- Scipy - 과학적 연산 및 오디오 처리

### 프론트엔드
- Streamlit - 웹 인터페이스 구현
- HTML5 Audio - 오디오 재생

### AI/ML
- Facebook MMS-TTS - 다국어 음성합성 모델
- Hugging Face - AI 모델 저장소 및 파이프라인

### 개발 도구
- Git - 버전 관리
- Python venv - 가상환경 관리

Developed by Blockenters
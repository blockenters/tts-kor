# pip install transformers torch scipy uroman

import streamlit as st
from transformers import VitsModel, AutoTokenizer
import torch
import scipy.io
import os
import base64

# 페이지 설정
st.set_page_config(
    page_title="한국어 TTS",
    page_icon="🎵",
    layout="centered"
)

# CSS 스타일 수정
st.markdown("""
    <style>
    .main-title {
        font-size: 2.5rem;
        color: #1E88E5;
        margin-bottom: 2rem;
        text-align: center;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #424242;
        margin-bottom: 1rem;
    }
    .highlight {
        background-color: #E3F2FD;
        padding: 1.2rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .footer {
        text-align: center;
        color: #757575;
        padding: 2rem 0;
    }
    .common-button {
        background-color: #1E88E5;
        color: white !important;
        padding: 0.8rem 4rem;
        font-size: 1.2rem;
        border-radius: 25px;
        width: 80%;
        margin: 0 auto;
        display: block;
        border: none;
        cursor: pointer;
    }
    .download-button {
        background-color: #4CAF50 !important;
    }
    .stButton>button, .stDownloadButton>button {
        background-color: #1E88E5;
        color: white !important;
        padding: 0.8rem 4rem;
        font-size: 1.2rem;
        border-radius: 25px;
        width: 80%;
        margin: 0 auto;
        display: block;
    }
    .stButton>button span, .stDownloadButton>button span {
        color: white !important;
    }
    .stDownloadButton>button {
        background-color: #4CAF50 !important;
    }
    /* 텍스트 영역 레이블 여백 제거 */
    .stTextArea label {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 헤더
st.markdown('<h1 class="main-title">🎵 한국어 음성 생성기</h1>', unsafe_allow_html=True)

# 소개 섹션 추가
st.markdown("""
    <div class="highlight" style="text-align: center; margin-bottom: 2rem;">
        <h3 style="color: #1E88E5; margin-bottom: 1rem;">🤖 AI 성우가 여러분의 이야기를 들려드립니다!</h3>
        <p style="font-size: 1.1rem; line-height: 1.6; color: #424242;">
            Facebook의 최신 AI 기술로 만든 TTS 서비스예요. 여러분의 글을 자연스러운 목소리로 읽어드립니다. 긴 글도 OK! 감정도 표현할 수 있어요! ✨
        </p>
        <div style="background-color: #E3F2FD; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
            <p style="font-size: 0.9rem; color: #1565C0;">
                💡 <strong>이런 용도로 사용해보세요:</strong><br>
                📚 동화책 읽어주기 🎯 프레젠테이션 음성 나레이션 ✍️ 블로그 포스팅 음성 변환
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)

# 모델 로드
@st.cache_resource
def load_model():
    model = VitsModel.from_pretrained("facebook/mms-tts-kor")
    tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-kor")
    return model, tokenizer

# 모델 로드
model, tokenizer = load_model()

# 메인 입력 섹션
st.markdown("""
    <div class="highlight" style="padding: 0.8rem;">
    <div style="color: #666; font-size: 0.9rem; margin-bottom: 0.3rem;">
        ✏️ 아래 입력창에 변환할 텍스트를 입력하세요
    </div>
    """, unsafe_allow_html=True)
text = st.text_area(
    "",  # 레이블 제거
    placeholder="예시) 안녕하세요. 텍스트를 음성으로 변환해드립니다.",
    value="",
    height=100
)
st.markdown('</div>', unsafe_allow_html=True)

def generate_audio(text):
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        output = model(**inputs).waveform
    return output[0].numpy(), model.config.sampling_rate

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}" style="text-decoration:none;"><button class="common-button download-button">💾 다운로드</button></a>'
    return href

# 사이드바에 사용방법 추가
with st.sidebar:
    st.markdown("""
    <div style="padding: 1rem;">
    <h2 style="color: #1E88E5;">💡 사용 방법</h2>
    <div class="highlight">
    <b>간단 3단계로 음성을 생성하세요:</b><br><br>
    
    1️⃣ 텍스트 입력창에 원하는 한글 텍스트를 입력합니다.<br><br>
    
    2️⃣ '음성 생성하기' 버튼을 클릭합니다.<br><br>
    
    3️⃣ 생성된 음성을 재생하거나 다운로드 받으세요.<br>
    </div>
    </div>
    """, unsafe_allow_html=True)

# 버튼 정렬 개선
st.markdown('<div style="display: flex; justify-content: center; margin: 2rem 0;">', unsafe_allow_html=True)
if st.button("🔊 음성 생성하기", key="generate"):
    if text:
        with st.spinner("🎵 음성을 생성하는 중..."):
            # 음성 생성
            audio_array, sample_rate = generate_audio(text)
            
            # WAV 파일로 저장
            filepath = "output.wav"
            scipy.io.wavfile.write(filepath, rate=sample_rate, data=audio_array)
            
            # 결과 컨테이너
            result_container = st.container()
            with result_container:
                st.markdown('<div class="highlight" style="text-align: center;">', unsafe_allow_html=True)
                st.success("✅ 음성 생성 완료! 플레이 버튼을 눌러 재생해보세요.")
                
                # 오디오 재생 위젯 표시
                st.audio(filepath)
                
                # 다운로드 버튼
                with open(filepath, "rb") as file:
                    st.download_button(
                        label="💾 음성 파일 다운로드",
                        data=file,
                        file_name="output.wav",
                        mime="audio/wav",
                        use_container_width=True
                    )
                st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ 텍스트를 입력해주세요!")
st.markdown('</div>', unsafe_allow_html=True)

# 푸터
st.markdown("""
    <div class="footer">
    <p>💖 Blockenters 💖</p>
    </div>
    """, unsafe_allow_html=True)



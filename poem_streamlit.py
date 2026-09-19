import time
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


model = init_chat_model(
    "gpt-5.6-luna",  # gpt-5.6-luna, gpt-4o, gpt-4o-mini 등 유효한 모델명 사용
    # Kwargs passed to the model:
    timeout=120,
    max_tokens=1000,
    max_retries=10,  # Default; increase for unreliable networks
    api_key = api_key,
)

st.title("_AI 시인_ :sunglasses:")
title = st.text_input("시의 주제를 입력하세요", "가을")
st.write(f"주제: {title}")

if st.button("시 생성"):
    st.write("시를 생성하는 중입니다...")
    with st.spinner("Wait for it...", show_time=False):
        output_parser = StrOutputParser()
        prompt = ChatPromptTemplate.from_messages([
            ("system", "당신은 세상에서 가장 뛰어난 시인입니다. 시를 창작할 때는 감정을 담아 아름답게 표현하세요."),
            ("user", "주제 '{input}'에 대한 시를 작성해 주세요."),
        ])
        chain = prompt | model | output_parser
        response = chain.invoke({"input": title})
    st.success("시 생성 완료!")
    st.write(response)



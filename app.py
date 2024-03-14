from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import streamlit as st 
import streamlit.components.v1 as components

custom_prompt_template =""" 
        You are a professional and creative website develpoer. Make HTML and CSS and Javascript website based on given context. 
        Add professional functionalities to website. Use proper color combination. Use proper fonts. 
        If you want you can create login or logout form also. Smartly use <button> tag at proper place.
        Generate only source code file, no description: {context}
"""

def html_generation(query):
    prompt = PromptTemplate(
        template = custom_prompt_template,
        input_variables = ["context"]
    )
    llm = ChatOpenAI(model="gpt-3.5-turbo-16k", temperature=0.1, max_tokens=2096, api_key="")
    chain = LLMChain(prompt=prompt, llm=llm)
    output = chain.run(context=query)
    print(output)
    return output


if "html" not in st.session_state:
    st.session_state.html = ""
if "text_query" not in st.session_state:
    st.session_state.text_query = ""


def text_run():
    text_query = st.session_state.text_query
    if text_query:
        html_code = html_generation(text_query)
        st.session_state.html = html_code


st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; color: #06113C;'>Prompt2HTML</h1>", unsafe_allow_html=True)


col1, col2 = st.columns([0.5, 0.5], gap='medium')
with col1:
    text_query = st.text_area("Enter your prompt here", height=150)
    if st.button("Run", on_click=text_run):
        st.session_state.text_query = text_query

with col2:
    if st.session_state.html != '':
        with st.expander("See source code"):
            st.code(st.session_state.html)
        with st.container():
            components.html(st.session_state.html, height=900, scrolling=True)

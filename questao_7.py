import streamlit as st
from langchain import OpenAI
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from groq import Groq

def resposta(texto):
    llm = OpenAI(temperature=0, openai_api_key=openai_api_key)    
    ts = CharacterTextSplitter()
    txs = ts.split_text(texto)
    docs = [Document(page_content=t) for t in txs]
    c = load_summarize_chain(llm, chain_type='map_reduce')
    return c.run(docs)

st.set_page_config(page_title='Sumarização')
st.title('Sumarização')

txti = st.text_area('Informe seu texto', '', height=200)

result = []

with st.form('sf', clear_on_submit=True):
    openai_api_key = st.text_input('OPENAI KEY', type='password', disabled=not txti)    
    submmit = st.form_submit_button('Enviar')
    if submmit and openai_api_key.startswith('sk-'):    
        with st.spinner('Executando...'):
            response = resposta(txti)
            result.append(response)
            del openai_api_key            

if len(result):
    st.info(response)
import os
from apikey import apikey
import streamlit as st
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper

os.environ['OPENAI_API_KEY'] = apikey

# App framework
st.title("🦜🔗 LangChain crash course")
prompt = st.text_input("Plug in your prompt here")

# Prompt template
title_template = PromptTemplate(
    input_variables=["topic"],
    template="write me a youtube title about {topic}",
)
script_template = PromptTemplate(
    input_variables=["title", "wikipedia_research"],
    template="write me a youtube video script based on this title: {title}. But also while leveraging this wikipedia research: \"\"\"{wikipedia_research}\"\"\"",
)

# Memory
title_memory = ConversationBufferMemory(input_key="topic", memory_key="chat_history")
script_memory = ConversationBufferMemory(input_key="title", memory_key="chat_history")


# LLMS
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(
    llm=llm,
    prompt=title_template,
    verbose=True,
    output_key="title",
    memory=title_memory,
)
script_chain = LLMChain(
    llm=llm,
    prompt=script_template,
    verbose=True,
    output_key="script",
    memory=script_memory,
)
# sequential_chain= SequentialChain(
#     chains=[title_chain, script_chain],
#     verbose=True,
#     input_variables=["topic"],
#     output_variables=["title", "script"],
# )

wiki = WikipediaAPIWrapper()

if prompt:
    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt)
    script = script_chain.run(title=title, wikipedia_research=wiki_research)

    st.write("Title:", title)
    st.write("Script:", script)

    with st.expander("Title history"):
        st.info(title_memory.buffer)

    with st.expander("Script history"):
        st.info(script_memory.buffer)

    with st.expander("Wikipedia research history"):
        st.info(wiki_research)
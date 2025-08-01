import streamlit as st
from langchain.memory import ConversationBufferMemory
from GetAIChatMessage import GetAIMessage

st.title("⚛ 智能聊天机器人 ⚛")
with st.sidebar:
    api_key = st.text_input("请输入API密钥:",type="password")
    base_url = st.text_input("请输入API端口:")
    st.markdown("[点击此处获取教程](https://ai.nengyongai.cn/study)")
    st.markdown("<br>" * 5, unsafe_allow_html=True)
    st.markdown("&nbsp;" * 5 + "**作者署名**  *Serendipity*", unsafe_allow_html=True)

if "memory" not in st.session_state:
    st.session_state.memory =ConversationBufferMemory(return_messages=True)
    st.session_state.messages =[{"role":"ai","content":"Hi!!我是智能聊天机器人Tulip，有什么能帮到你的吗？"}]
for sentence in st.session_state.messages:
    st.chat_message(sentence["role"]).write(sentence["content"])
prompt = st.chat_input("请输入文本")
if prompt:
    if not api_key:
        st.info("请输入API密钥！")
        st.stop()
    if not base_url:
        st.info("请输入API端口！")
        st.stop()
    st.chat_message("human").write(prompt)
    with st.spinner("让我想想怎么回答你(拍脑壳)"):
        response = GetAIMessage("gpt-4o-mini",api_key,base_url,prompt,st.session_state.memory)
    st.chat_message("ai").write(response)
    st.session_state.messages.append({"role":"human","content":prompt})
    st.session_state.messages.append({"role": "ai", "content": response})




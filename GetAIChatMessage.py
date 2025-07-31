from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain

def GetAIMessage(model,api_key,base_url,prompt,memory):
    model = ChatOpenAI(model=model,api_key=api_key,base_url=base_url)
    chain = ConversationChain(llm=model,memory=memory)
    response = chain.invoke({"input":prompt})
    return response["response"]
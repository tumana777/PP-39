# from typing import TypedDict
# from langgraph.graph import StateGraph, START, END
#
# #=====================================
# # State
# #=====================================
#
# class State(TypedDict):
#     text: str
#     analysis: str
#     answer: str
#
# #=====================================
# # Nodes
# #=====================================
#
# def analyze(state: State):
#     return {
#         "analysis": f"The length of the text is {len(state['text'])}"
#     }
#
# def answer(state: State):
#     return {
#         "answer": f"The answer is: {state['analysis'].upper()}"
#     }
#
# #=====================================
# # Graph
# #=====================================
#
# builder = StateGraph(State)
#
# builder.add_node("analyze", analyze)
# builder.add_node("answer", answer)
#
# builder.add_edge(START, "analyze")
# builder.add_edge("analyze", "answer")
# builder.add_edge("answer", END)
#
# graph = builder.compile()
#
# result = graph.invoke({
#     "text": "Hello, world!"
# })
#
# print(result)

#####################################################################
#####################################################################

from dotenv import load_dotenv
load_dotenv()

from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI

MODEL = "gemini-3.5-flash-lite"

#=====================================
# State
#=====================================

class State(TypedDict):
    text: str
    detected_language: str
    translated_text: str

#=====================================
# Nodes
#=====================================

def detect_language(state: State):

    llm = ChatGoogleGenerativeAI(
        model=MODEL
    )

    prompt = f"""
    You are a language detection model. Detect the language of the following text.
    Text:
    {state['text']}
    return only the language name!
    """

    response = llm.invoke(prompt)

    return {
        "detected_language": response.text
    }

def translate_text(state: State):

    llm = ChatGoogleGenerativeAI(
        model=MODEL
    )

    prompt = f"""
    You are a translation model. Translate the following text to Georgian.
    Text:
    {state['text']}
    return only the translated text!
    """

    response = llm.invoke(prompt)

    return {
        "translated_text": response.text
    }


# #=====================================
# # Graph
# #=====================================

builder = StateGraph(State)

builder.add_node("detect_language", detect_language)
builder.add_node("translate_text", translate_text)

builder.add_edge(START, "detect_language")
builder.add_edge("detect_language", "translate_text")
builder.add_edge("translate_text", END)

graph = builder.compile()

while True:
    text_to_translate = input("Enter the text to translate: ")

    result = graph.invoke({
        "text": text_to_translate
    })

    print(f"Detected language: {result.get('detected_language', 'Cannot detect language.')}")
    print(f"Translated text: {result.get('translated_text', 'Translation failed.')}")











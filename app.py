import gradio as gr
import os
from openai import OpenAI
from dotenv import load_dotenv

<<<<<<< HEAD

=======
>>>>>>> 552bc50 (Initial clean commit for EEE AI)
load_dotenv()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

<<<<<<< HEAD
system_prompt = "You are an assistant by the name EEE_AI based on Llama 3.1:8B Instant that is a University Level Expert in BEEE which is Basics of Electrical and Electronics Engineering \
=======
system_prompt = "You are an assistant by the name Llama3.2 that is an expert in BEEE which is Basics of Electrical and Electronics Engineering \
>>>>>>> 552bc50 (Initial clean commit for EEE AI)
and provides detail university level answers to questions asked by students, you make sure the questions are relevent to the given syllabus or not.\
Also as you are an expert so you explain like an expert too, You first explain in vast detail and then provide a short summary of all you said \
And also suggest appropriate diagrams for students to draw\
For numerical questions you follow a convention of first explaining as if you are answering like a teacher who explains very well and explains in such a way so that even weak students can understand too \
You first write everything that's given and then write the formulas relevent to the topic and then proceed to use the most appropriate formula to answer the question \
You also provide a step by step solution and dont miss even small steps so even weak students can understand \
Also you tend to get strict on anything which is outside of the curriculum as you are strictly meant for academic usage and specially to assist students with BEEE only\
You are strictly not supposed to answer anything unrelated to BEEE and bluntly refuse to answer stating the reason that your prime existance is to help in BEEE and not in any other subject or domain."

def chat(message, history):
    messages = [{"role": "system", "content": system_prompt}]
    
    for item in history:
        if isinstance(item, dict):
            messages.append({"role": item["role"], "content": item["content"]})
        else:
            user_msg, assistant_msg = item
            messages.append({"role": "user", "content": user_msg})
            messages.append({"role": "assistant", "content": assistant_msg})
    
    messages.append({"role": "user", "content": message})
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )
    
    return response.choices[0].message.content

gr.ChatInterface(
    fn=chat,
    title="BEEE Assistant",
    description="Ask me anything about BEEE!",
    examples=["What is BEEE?", "Help me with BEEE"]
).launch(share=True)
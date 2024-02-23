import streamlit as st
from openai import OpenAI
import time

api_key_1 = st.secrets["api_key_1"]
api_key_2 = st.secrets["api_key_2"]

# Initialize the OpenAI clients
client1 = OpenAI(api_key=api_key_1)
client2 = OpenAI(api_key=api_key_2)

# Function to manage the conversation between two bots
def conversation(input_text, original_context):
    if input_text != original_context:
        message = original_context + " " + input_text
    else:
        message = input_text

    # For Bot (Pro stance)
    bot_1_response = client1.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a debate bot. Your role is to take the given topic and take the Pro stance. Your first response should be your own thoughts, and each subsequent response should be in direct response to the other party. Keep replies to 2 sentences. Be a little mean."},
            {"role": "assistant", "content": message}
        ],
        presence_penalty=0.5,
    )

    # Against Bot (Con stance)
    message = original_context + " " + bot_1_response.choices[0].message.content  # Ensure the message is appended correctly
    bot_2_response = client2.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a debate bot. Your role is to take the given topic and take the Con (or against) stance. Your first response should be your own thoughts, and each subsequent response should be in direct response to the other party. Keep replies to 2 sentences. Be a little mean."},
            {"role": "user", "content": message}
        ],
        presence_penalty=0.5,
    )

    return bot_1_response.choices[0].message.content, bot_2_response.choices[0].message.content

# Streamlit UI setup
st.title('AI Debate Bot')
topic = st.text_input('Enter a debate topic:', '')

# Placeholder for real-time transcript updates
transcript_placeholder = st.empty()

if st.button('Start Debate'):
    original_input = topic
    input_text = topic
    debate_transcript = ""

    for i in range(3):  # Adjust the range for longer or shorter debates
        pro_response, con_response = conversation(input_text=input_text, original_context=original_input)
        debate_transcript += f"\nPro: {pro_response}\nCon: {con_response}\n"
        input_text = con_response  # Use the last response as input for the next round
        # Update the placeholder with the latest transcript after each response
        transcript_placeholder.text_area("Debate Transcript", value=debate_transcript, height=300)
        time.sleep(1)  # To simulate real-time response, adjust as needed

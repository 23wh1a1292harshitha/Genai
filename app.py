import streamlit as st
import google.generativeai as genai
import os
from gtts import gTTS
import wikipediaapi

# Google Generative AI API Key Setup
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Wikipedia API Initialization
wiki = wikipediaapi.Wikipedia(language="en", user_agent="MyApp/1.0")

# Function to fetch Wikipedia summary
def get_description_from_wikipedia(topic):
    page = wiki.page(topic)
    return page.summary[:500] if page.exists() else None

# Function to get a description from Gemini
def get_description_from_gemini(topic):
    try:
        model_name = 'models/gemini-1.5-pro'
        model = genai.GenerativeModel(model_name)
        prompt = f"Provide a brief description of the topic: {topic}"
        response = model.generate_content(prompt)
        return response.text
    except google.api_core.exceptions.InvalidArgument as e:
        return f"Gemini Error: Invalid argument - {e}"
    except Exception as e:
        return f"Gemini Error: An unexpected error occurred - {e}"

# Function to convert text to speech
def generate_audio(text):
    try:
        audio_file = "output.mp3"
        tts = gTTS(text=text, lang="en")
        tts.save(audio_file)
        return audio_file
    except Exception as e:
        st.error(f"Error generating audio: {e}")
        return None

# Streamlit UI
def main():
    st.set_page_config(page_title="Shikshak Mahoday with Gemini", layout="wide")

    # Load CSS from file
    with open("style.css", "r") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    st.title("📚 Shikshak Mahoday with Gemini 🤖")

    col1, col2 = st.columns([1, 2])

    with col1:
        topic = st.text_input("Enter Topic:")
        if st.button("Get Description"):
            if topic:
                with st.spinner('Generating description and audio...'):
                    description = get_description_from_wikipedia(topic)
                    if not description:
                        description = get_description_from_gemini(topic)
                    if description:
                        with col2:
                            st.text_area("Description:", description)
                            audio_file = generate_audio(description)
                            if audio_file:
                                st.audio(audio_file)
                    else:
                        st.error("No description found for the topic!")
            else:
                st.warning("Please enter a topic.")

if __name__ == "__main__":
    main()
# Shikshak Mahoday with Gemini 🤖

A Streamlit-based web application that integrates Google Generative AI (Gemini) and Wikipedia API to generate topic descriptions and convert them to audio using Text-to-Speech (gTTS). This project aims to provide an interactive platform for users to explore different topics and listen to descriptions.

## Features

- *Wikipedia Summary*: Fetches a brief summary from Wikipedia on a given topic.
- *Gemini AI Description*: If no Wikipedia summary is found, the app fetches a description from Google's Gemini AI model.
- *Text-to-Speech*: Converts the generated descriptions into an audio file that can be played directly in the app.
- *Interactive UI*: Built with Streamlit, it allows users to input a topic and get a description with audio playback.

## Tech Stack

- *Streamlit*: Framework for building the web application.
- *Google Generative AI (Gemini)*: AI model used to generate topic descriptions.
- *gTTS (Google Text-to-Speech)*: Converts the generated text description into speech.
- *Wikipedia API*: Fetches Wikipedia summaries for given topics.

## Setup Instructions

### Prerequisites

Before you can run the application, ensure you have the following installed:

- *Python 3.x*
- *Streamlit*
- *Google Generative AI (Gemini) API Key*
- *gTTS (Google Text-to-Speech)* library
- *Wikipedia API* library

### Installation

1. Clone the repository to your local machine:

    bash
    git clone https://github.com/your-username/Genai.git
    cd Genai
    

2. Create a virtual environment (optional but recommended):

    bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    

3. Install the required dependencies:

    bash
    pip install -r requirements.txt
    

4. Set up your Google Generative AI API key:

    - Create a .env file in the project directory and add the following line:
    
      
      GOOGLE_API_KEY=your-api-key-here
      

5. Install any other dependencies not in requirements.txt if necessary:
    
    bash
    pip install streamlit google-generativeai wikipedia-api gTTS
    

### Running the App

To start the app locally, run the following command:

```bash
streamlit run app.py

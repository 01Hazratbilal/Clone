import os
import tempfile
from google.cloud import texttospeech
import streamlit as st
import base64

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google.json"

def synthesize_text(text, voice_name):
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code=voice_name[:5],
        name=voice_name,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
    )

    response = client.synthesize_speech(
        input=input_text,
        voice=voice,
        audio_config=audio_config,
    )

    return response.audio_content

st.title("Google Text-to-Speech")

input_text = st.text_area("Enter the text you want to convert to speech:")

# Dropdown menu for selecting a voice
voices_list = [
    "en-AU-Neural2-A",
    "en-AU-Neural2-B",
    "en-AU-Neural2-C",
    "en-AU-Neural2-D",
    "en-AU-News-E",
    "en-AU-News-F",
    "en-AU-News-G",
    "en-AU-Standard-A",
    "en-AU-Standard-B",
    "en-AU-Standard-C",
    "en-AU-Standard-D",
    "en-AU-Wavenet-A",
    "en-AU-Wavenet-B",
    "en-AU-Wavenet-C",
    "en-AU-Wavenet-D",
    "en-IN-Standard-A",
    "en-IN-Standard-B",
    "en-IN-Standard-C",
    "en-IN-Standard-D",
    "en-IN-Wavenet-A",
    "en-IN-Wavenet-B",
    "en-IN-Wavenet-C",
    "en-IN-Wavenet-D",
    "en-GB-Neural2-A",
    "en-GB-Neural2-B",
    "en-GB-Neural2-C",
    "en-GB-Neural2-D",
    "en-GB-Neural2-F",
    "en-GB-News-G",
    "en-GB-News-H",
    "en-GB-News-I",
    "en-GB-News-J",
    "en-GB-News-K",
    "en-GB-News-L",
    "en-GB-News-M",
    "en-GB-Standard-A",
    "en-GB-Standard-B",
    "en-GB-Standard-C",
    "en-GB-Standard-D",
    "en-GB-Standard-F",
    "en-GB-Wavenet-A",
    "en-GB-Wavenet-B",
    "en-GB-Wavenet-C",
    "en-GB-Wavenet-D",
    "en-GB-Wavenet-F",
    "en-US-Neural2-A",
    "en-US-Neural2-C",
    "en-US-Neural2-D",
    "en-US-Neural2-E",
    "en-US-Neural2-F",
    "en-US-Neural2-G",
    "en-US-Neural2-H",
    "en-US-Neural2-I",
    "en-US-Neural2-J",
    "en-US-News-K",
    "en-US-News-L",
    "en-US-News-M",
    "en-US-News-N",
    "en-US-Standard-A",
    "en-US-Standard-B",
    "en-US-Standard-C",
    "en-US-Standard-D",
    "en-US-Standard-E",
    "en-US-Standard-F",
    "en-US-Standard-G",
    "en-US-Standard-H",
    "en-US-Standard-I",
    "en-US-Standard-J",
    "en-US-Studio-M",
    "en-US-Studio-O",
    "en-US-Wavenet-A",
    "en-US-Wavenet-B",
    "en-US-Wavenet-C",
    "en-US-Wavenet-D",
    "en-US-Wavenet-E",
    "en-US-Wavenet-F",
    "en-US-Wavenet-G",
    "en-US-Wavenet-H",
    "en-US-Wavenet-I",
    "en-US-Wavenet-J"

]

voice_selection = st.selectbox("Choose a voice:", voices_list)

submit_button = st.button("Enter")

if input_text and voice_selection:
    audio_content = synthesize_text(input_text, voice_selection)
    audio_file = tempfile.NamedTemporaryFile(delete=False)
    audio_file.write(audio_content)
    audio_file.flush()

    # Display the audio player directly
    st.audio(audio_file.name, format="audio/mp3")

    # Create the download link
    b64_audio = base64.b64encode(audio_content).decode("utf-8")
    href = f'<a href="data:audio/mp3;base64,{b64_audio}" download="{voice_selection}.mp3">Download</a>'
    st.markdown(href, unsafe_allow_html=True)

import speech_recognition as sr
from pydub import AudioSegment
import os
import pandas as pd

def mp3_to_wav(mp3_path):
    sound = AudioSegment.from_mp3(mp3_path)
    wav_path = mp3_path.replace(".mp3", ".wav")
    sound.export(wav_path, format="wav")
    return wav_path

def transcribe(audio_path):
    recognizer = sr.Recognizer()
    wav_path = audio_path
    if not audio_path.lower().endswith(".wav"):
        wav_path = mp3_to_wav(audio_path)
    with sr.AudioFile(wav_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
    except Exception as e:
        text = ""
    if wav_path != audio_path and os.path.exists(wav_path):
        os.remove(wav_path)
    return text

def word_by_word_table(ref_audio_path, user_audio_path):
    ref_text = transcribe(ref_audio_path)
    user_text = transcribe(user_audio_path)
    ref_words = ref_text.strip().split()
    user_words = user_text.strip().split()
    max_len = max(len(ref_words), len(user_words))
    rows = []
    for i in range(max_len):
        ref_word = ref_words[i] if i < len(ref_words) else ""
        user_word = user_words[i] if i < len(user_words) else ""
        match = ref_word.lower() == user_word.lower()
        rows.append({
            "Reference": ref_word,
            "Your Attempt": user_word,
            "Match": "✅" if match else "❌"
        })
    df = pd.DataFrame(rows)
    return df
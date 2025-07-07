import librosa
import matplotlib.pyplot as plt
import pandas as pd
from utils import word_by_word_table
import shutil
import os


def compare_audio(tts_path, user_audio_path):
    if isinstance(tts_path, str):
        y_tts, sr_tts = librosa.load(tts_path, sr=None)
    elif isinstance(tts_path, tuple):
        sr_tts, y_tts = tts_path
    else:
        raise ValueError("Invalid gTTS input type")
    if user_audio_path is None:
        return None
    if isinstance(user_audio_path, str):
        y_user, sr_user = librosa.load(user_audio_path, sr=None)
    elif isinstance(user_audio_path, tuple):
        sr_user, y_user = user_audio_path
    else:
        raise ValueError("Invalid user audio input type")
    min_len = min(len(y_tts), len(y_user))
    y_tts, y_user = y_tts[:min_len], y_user[:min_len]
    fig, ax = plt.subplots(3, 1, figsize=(10, 7))
    ax[0].plot(y_tts)
    ax[0].set_title("Reference (gTTS) Audio")
    ax[1].plot(y_user)
    ax[1].set_title("Your Recorded Audio")
    ax[2].plot(y_tts - y_user, color="red")
    ax[2].set_title("Difference (Reference - Recorded)")
    plt.tight_layout()
    return fig



def compare_both(tts_path, user_audio_path):
    fig = compare_audio(tts_path, user_audio_path)
    table = word_by_word_table(tts_path, user_audio_path)
    return fig, table


def reset_all():
    pycache_path = os.path.join(os.path.dirname(__file__), "__pycache__")
    if os.path.exists(pycache_path):
        shutil.rmtree(pycache_path)
    return "", None, None, None, None
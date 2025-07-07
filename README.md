# Pronunciation Assessment


This is an app designed to practice English pronunciation.

It utilizes `gemma3n:e2b` to generate English sentences (maximum three). It then creates an English audio recording of these sentences, and allows the user to record themselves reading the same sentences (a maximum of three).  After recording, it allows for a comparison between the original English audio and the user's recording, highlighting the words where the user made mistakes.

The model leverages libraries such as `langchain_ollama`, `LangChain`, `Ollama` among others. The app is developed with `Gradio` as the user interface.

The following libraries are required for implementing the app:

* `langchain_ollama`
* `langchain`
* `librosa`
* `matplotlib`
* `pandas`
* `gTTS`
* `SpeechRecognition`
* `pydub`
* `gradio`

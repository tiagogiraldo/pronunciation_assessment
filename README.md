# Pronunciation Assessment

This application is designed to facilitate practice in English pronunciation.

- It generates sentences based on a user-provided topic (maximum of three sentences).  These sentences are accompanied by corresponding audio files.
- The application allows the user to record themselves speaking the generated sentences.
- It compares the audio recordings made by the user with the original audio files.
- The application generates a table highlighting words that are correctly and incorrectly pronounced.

The application is developed using Gradio as the user interface. The following libraries are used in the application's development:

- `langchain_o llama`:  For language model integration and potentially managing the language model.
- `langchain`:  A framework for building applications powered by language models.
- `librosa`:  For audio analysis, manipulation and data visualization.
- `matplotlib`:  For data visualization.
- `pandas`:  For data analysis and manipulation, particularly for tabular data.
- `gTTS`:  Google Text-to-Speech library.
- `SpeechRecognition`:  For speech recognition functionality.
- `pydub`:  For audio editing and manipulation.
- `gradio`:  For building the user interface.

The sentences are generated using a Google LLM model: `gemma3n:e2b`.

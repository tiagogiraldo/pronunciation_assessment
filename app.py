import gradio as gr
from tts import generate_tts, LANGUAGES
from audio_analysis import compare_both, reset_all
from llm import generate_sentences


def gen_sentences_and_audio(topic, n):
    n = max(1, min(int(n), 3))
    sentences = generate_sentences(topic, n)
    sentences_no_quotes = [s.strip().strip('"') for s in sentences]
    text = "\n".join(sentences_no_quotes)
    audio = generate_tts(text, LANGUAGES["English (US)"])
    return text, audio


with gr.Blocks() as app:
    gr.Markdown("## Listen, Record, and Compare Your Pronunciation (in English)")

    with gr.Row():
        topic_in = gr.Textbox(label="Enter a Topic", value="", interactive=True)
        n_sentences_in = gr.Number(label="Number of Sentences", value=1, precision=0, minimum=1, maximum=3,interactive=True)
        gen_text_btn = gr.Button("Generate Sentence(s) and Reference Audio")
    text_in = gr.Textbox(label="Generated Sentence(s) for Reference Audio", interactive=False)
    tts_audio = gr.Audio(label="Reference Audio (gTTS)", interactive=False, type="filepath")
  

    gr.Markdown("**Step 2: Record your version after listening to the reference.**")
    user_audio = gr.Audio(sources=["microphone"], label="Your Recorded Audio", type="filepath")
    compare_btn = gr.Button("Compare")
    reset_btn = gr.Button("Restart / Reset")


    table_out = gr.Dataframe(label="Word-by-Word Comparison", visible=True)
    plot_out = gr.Plot(label="Waveform Comparison Plot")
  
    gen_text_btn.click(
        fn=gen_sentences_and_audio,
        inputs=[topic_in, n_sentences_in],
        outputs=[text_in, tts_audio]
    )

    compare_btn.click(
        fn=compare_both,
        inputs=[tts_audio, user_audio],
        outputs=[plot_out, table_out]
    )
    reset_btn.click(
        fn=reset_all,
        inputs=[],
        outputs=[topic_in, text_in, tts_audio, user_audio, plot_out, table_out]
    )

    

if __name__ == "__main__":
    app.launch()

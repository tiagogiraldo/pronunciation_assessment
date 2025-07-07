from gtts import gTTS
import tempfile

# Language dictionary for dropdown
LANGUAGES = {
    "English (US)": "en",
    "Spanish": "es",
    "French": "fr",
    "Portuguese": "pt",
    "Mandarin (China Mainland)": "zh-CN",
	"Mandarin (Taiwan)": "zh-TW",
}


def generate_tts(text, lang_code):
    tts = gTTS(text, lang=lang_code)
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as fp:
        tts.save(fp.name)
        return fp.name    

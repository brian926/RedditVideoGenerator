import json
import os
import pyttsx3
import requests

voiceoverDir = "Voiceovers"

def off_create_voice_over(fileName, text):
    filePath = f"{voiceoverDir}/{fileName}.mp3"
    engine = pyttsx3.init()
    engine.save_to_file(text, filePath)
    engine.runAndWait()
    return filePath

def create_voice_over(fileName, text):
    filePath = f"{voiceoverDir}/{fileName}.mp3"

    headers = { 'content-type': 'application/json', "xi-api-key": os.getenv("ELEVEN_LABS")}
    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0,
            "similarity_boost": 0
        }
    }
    data = json.dumps(payload)
    voiceId = "21m00Tcm4TlvDq8ikWAM"

    r = requests.post(f"https://api.elevenlabs.io/v1/text-to-speech/{voiceId}", data=data, headers=headers)
    if r.status_code == 200:
        with open(filePath, "wb") as f:
            f.write(r.content)
    else:
        print("FAIL")
    return filePath

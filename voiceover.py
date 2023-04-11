import json
import os
import pyttsx3
import requests
import os
import random

voiceoverDir = "Voiceovers"

def create_voice_over(fileName, text):
    filePath = f"{voiceoverDir}/{fileName}.mp3"
    if(os.path.isfile(filePath)):
        return filePath
    else:
        engine = pyttsx3.init()
        engine.save_to_file(text, filePath)
        engine.runAndWait()
        return filePath

def off_create_voice_over(fileName, text):
    filePath = f"{voiceoverDir}/{fileName}.mp3"
    if(os.path.isfile(filePath)):
        return filePath
    else:
        headers = { 'content-type': 'application/json', "xi-api-key": os.getenv("ELEVEN_LABS")}
        payload = {
            "text": text,
            "voice_settings": {
                "stability": 0.25,
                "similarity_boost": 0.25
            }
        }
        data = json.dumps(payload)
        voiceId = ["EXAVITQu4vr4xnSDxMaL", "21m00Tcm4TlvDq8ikWAM", "AZnzlk1XvdvUeBnXmlld", "MF3mGyEYCl7XYWbV9V6O", "yoZ06aMxZJJ28mfd3POQ"]

        r = requests.post(f"https://api.elevenlabs.io/v1/text-to-speech/{random.choice(voiceId)}", data=data, headers=headers)
        if r.status_code == 200:
            with open(filePath, "wb") as f:
                f.write(r.content)
            r = requests.get("https://api.elevenlabs.io/v1/user/subscription", headers={"xi-api-key": os.getenv("ELEVEN_LABS")})
            res = r.json()
            cur = res["character_count"]
            lim = res["character_limit"]
            print(f"{cur} out of {lim} left: {cur/lim}%")
        else:
            print("FAIL")
        return filePath

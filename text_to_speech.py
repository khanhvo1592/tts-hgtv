import requests
import json
import os
import uuid
# Danh sách các giọng đọc
VOICES = [
    {"name": "Kim Chi", "description": "Nữ miền Nam", "code": "hcm-diemmy"},
    {"name": "Mỹ Tâm", "description": "Nữ miền Nam", "code": "hcm-phuongly"},
    {"name": "Bé Nhí", "description": "Nữ miền Nam", "code": "hcm-thuydung"},
    {"name": "Hứa Khoa", "description": "Nam miền Nam", "code": "hcm-minhquan"},
    {"name": "Mỹ Hảo", "description": "Nữ miền Nam", "code": "hn-leyen"},
    {"name": "Thùy Duyên", "description": "Nữ miền Nam", "code": "hcm-thuyduyen"},
]

def get_voices():
    return VOICES

def text_to_speech_viettel(text, voice, speed, token, upload_folder):
    url = "https://viettelai.vn/tts/speech_synthesis"
    payload = json.dumps({
        "text": text,
        "voice": voice,
        "speed": speed,
        "tts_return_option": 3,
        "token": token,
        "without_filter": False
    })
    headers = {
        'accept': '*/*',
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    if response.status_code == 200:
        filename = f"tts_{uuid.uuid4()}.mp3"
        file_path = os.path.join(upload_folder, filename).replace('\\', '/')
        
        with open(file_path, "wb") as file:
            file.write(response.content)
        
        return filename
    else:
        return None
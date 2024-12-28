#!/bin/bash
cd /home/khanhvo/speech_and_text
source venv/bin/activate
gunicorn --bind 0.0.0.0:8800 app:app

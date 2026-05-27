import os
import threading
import webbrowser
import subprocess
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import speech_recognition as sr
import datetime

app = Flask(__name__)
CORS(app)

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True

is_listening = False
transcript_log = []

def speak(text):
    subprocess.Popen(['say', text])

COMMANDS = {
    "open browser":     lambda: webbrowser.open("https://google.com"),
    "open google":      lambda: webbrowser.open("https://google.com"),
    "open youtube":     lambda: webbrowser.open("https://youtube.com"),
    "open github":      lambda: webbrowser.open("https://github.com"),
    "what time is it":  lambda: speak(datetime.datetime.now().strftime('%I:%M %p')),
    "what is the date": lambda: speak(datetime.datetime.now().strftime('%B %d, %Y')),
    "hello":            lambda: speak("Hello! How can I help you?"),
    "who are you":      lambda: speak("I am NeuralVox, your AI speech intelligence system."),
}

def process_command(text):
    text_lower = text.lower().strip()
    for cmd, action in COMMANDS.items():
        if cmd in text_lower:
            action()
            return f"Command executed: {cmd}"
    if text_lower.startswith("search for "):
        query = text_lower.replace("search for ", "")
        webbrowser.open(f"https://google.com/search?q={query}")
        return f"Searching for: {query}"
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status')
def status():
    return jsonify({"listening": is_listening})

@app.route('/api/listen', methods=['POST'])
def listen():
    global is_listening, transcript_log
    try:
        with sr.Microphone() as source:
            is_listening = True
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=10)
            is_listening = False
        text = recognizer.recognize_google(audio)
        command_result = process_command(text)
        entry = {
            "text": text,
            "timestamp": datetime.datetime.now().strftime("%H:%M:%S"),
            "command": command_result,
            "type": "command" if command_result else "transcript"
        }
        transcript_log.append(entry)
        return jsonify({"success": True, "result": entry})
    except sr.WaitTimeoutError:
        is_listening = False
        return jsonify({"success": False, "error": "No speech detected. Try again."})
    except sr.UnknownValueError:
        is_listening = False
        return jsonify({"success": False, "error": "Could not understand audio."})
    except Exception as e:
        is_listening = False
        return jsonify({"success": False, "error": str(e)})

@app.route('/api/transcript')
def get_transcript():
    return jsonify(transcript_log)

@app.route('/api/clear', methods=['POST'])
def clear_transcript():
    global transcript_log
    transcript_log = []
    return jsonify({"success": True})

@app.route('/api/speak', methods=['POST'])
def speak_text():
    data = request.get_json()
    text = data.get('text', '')
    if text:
        threading.Thread(target=speak, args=(text,), daemon=True).start()
        return jsonify({"success": True})
    return jsonify({"success": False})

if __name__ == '__main__':
    print("\n🎙️  NeuralVox starting...")
    print("📡  Open http://localhost:5000\n")
    app.run(debug=False, port=5000)

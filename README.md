# 🧠 NeuralVox — AI Speech Intelligence

A professional-grade voice recognition system with real-time speech-to-text, intelligent voice commands, live waveform visualization, and text-to-speech output. Built with Python (Flask) backend and a custom JS frontend.

---

## ✨ Features

- 🎙️ **Real-time Speech Recognition** — powered by Google Speech API
- ⚡ **Voice Commands** — open apps, search web, get time/date, and more
- 🌊 **Live Waveform Visualizer** — animated audio feedback
- 📋 **Transcript Log** — full history of everything you've said
- 🔊 **Text-to-Speech** — type anything and hear it spoken back
- ⌨️ **Keyboard Shortcut** — press `Space` to activate mic

---

## 🗣️ Voice Commands

| Command | Action |
|---|---|
| `open browser` | Opens browser |
| `open google` | Opens Google |
| `open youtube` | Opens YouTube |
| `open github` | Opens GitHub |
| `what time is it` | Speaks current time |
| `what is the date` | Speaks today's date |
| `hello` | Greeting response |
| `who are you` | NeuralVox introduction |
| `search for <query>` | Google search |
| `stop listening` | Stops mic |

---

## 🚀 Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/compiledbyutkarsh/NeuralVox.git
cd NeuralVox
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

> **Mac users** — if PyAudio fails:
> ```bash
> brew install portaudio
> pip install pyaudio
> ```

### 3. Run the server
```bash
python app.py
```

### 4. Open in browser
```
http://localhost:5000
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask, Flask-CORS |
| Speech Recognition | SpeechRecognition + Google Speech API |
| Text-to-Speech | pyttsx3 |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Visualization | Canvas API (custom waveform) |

---

## 📁 Project Structure

```
NeuralVox/
├── app.py              # Flask backend + speech logic
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Frontend UI
└── README.md
```

---

## ⚠️ Note
Requires microphone access and an active internet connection for Google Speech API.

---

*Built by [compiledbyutkarsh](https://github.com/compiledbyutkarsh)*

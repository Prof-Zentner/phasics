# λ Phasics — Adaptive Learning Engine

An adaptive physics learning platform for college-level **Waves & Modern Physics**, inspired by GMAT-style computer-adaptive testing.

## Features

- **🎯 Adaptive Engine** — Questions get harder as you improve, easier when you need practice
- **📊 Diagnostic Dashboard** — See per-topic breakdowns and identify weak areas
- **🤖 AI Tutor** — Gemini-powered Socratic tutor with detailed, high-level explanations
- **📝 Multiple Question Types** — Multiple choice, numerical calculations, and conceptual free-response

## Pilot Module

**SHM & Standing Waves** — 16 rigorous questions across 5 difficulty levels:
1. Foundational
2. Developing
3. Proficient
4. Advanced
5. Expert

## Setup

### Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

### Deploy on Streamlit Community Cloud

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Set `app.py` as the main file
5. Deploy!

### Gemini API Key

The AI tutor requires a Gemini API key. Get one free at [ai.google.dev](https://ai.google.dev).

Enter it in the sidebar when running the app, or set it as a Streamlit secret:

```toml
# .streamlit/secrets.toml (for local dev — do NOT commit this)
GEMINI_API_KEY = "your-key-here"
```

## Tech Stack

- **Streamlit** — UI framework
- **Plotly** — Data visualization
- **Google Generative AI** — Gemini-powered tutor
- **Python 3.10+**

## Project Structure

```
phasics/
├── app.py              # Main Streamlit application
├── questions.py        # Adaptive question bank
├── engine.py           # Adaptive difficulty algorithm
├── tutor.py            # Gemini AI tutor module
├── requirements.txt    # Python dependencies
├── .streamlit/
│   └── config.toml     # Streamlit theme configuration
└── README.md
```

## License

MIT

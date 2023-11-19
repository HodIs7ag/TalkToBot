# TalkToBot
Simple voice assistant project that records user speech, converts it to text, interacts with ChatGPT using its API, and converts the response back to voice.

## Features

- **Speech-to-Text:** Converts user speech into text.
- **ChatGPT Interaction:** Utilizes the ChatGPT API for generating responses.
- **Text-to-Speech:** Converts the generated text response back to voice.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/TalkToBot.git
    cd TalkToBot
    ```
2. 'Optional' Create virtual environment
    ```bash
    #Create venv
    python -m venv venv

    #Activate the virtual environment
    source venv/bin/activate  # On Linux/Mac
    venv\Scripts\activate      # On Windows
    ```
3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```
4. Run the Program

    ```bash
    python ChatGPT.py
    ```
from openai import OpenAI
import voiceToText, TextToVoice
from config import API_KEY

CLIENT = OpenAI(api_key=API_KEY)

CHAT_HISTORY = []

def add_to_history(message,role):
    m = {"role":role, "content":message}
    CHAT_HISTORY.append(m)

def get_response(question,):
    
    response = CLIENT.chat.completions.create(
    model="gpt-3.5-turbo",
    messages= CHAT_HISTORY + [
        {"role": "user", "content": question},
    ],
    
    )
    add_to_history(question,"user")

    output = response.choices[0].message.content
    print("\nBot:{}\n\n...".format(output))
    add_to_history(output,"assistant")
    TextToVoice.to_audio(CLIENT, output)
    return output



#main
print("Welcome to TalkToBot\n")
while True:
    user_input = voiceToText.listen()
    if str(user_input).lower() == "stop":
        print("Thanks for using this BOT")
        break
    get_response(user_input)
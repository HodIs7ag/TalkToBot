import sounddevice as sd
import soundfile

def play_audio(file_path):
    data, freq = soundfile.read(file_path, dtype='float32')
    sd.play(data, freq)
    sd.wait()


def to_audio(client,text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text,
        
    )
    output_file = "output.mp3"
    response.stream_to_file(output_file)
    play_audio(output_file)
    return output_file




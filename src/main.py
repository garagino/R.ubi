from listen_and_speak import ListenAndSpeak
from gptApi import GptApi

listen = ListenAndSpeak()


while True:
    try:
        listen.speak(listen.listen())
    except KeyboardInterrupt:
        break


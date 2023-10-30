from rubi import Rubi

rubi = Rubi()

rubi.speak('Olá pessoa! Meu nome é Rubi! E estou aqui para te ajudar!')

while True:
    try:
        rubi.speak(rubi.listen())
    except KeyboardInterrupt:
        break


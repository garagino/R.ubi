from rubi import Rubi

rubi = Rubi()

rubi.speak('Olá pessoa! Meu nome é Rubi! E estou aqui para te ajudar!')

inputs = [['olá', 'oi', 'e ai', 'opa', 'eae', 'eai', 'e ai', 'e ai rubi', 'oi rubi', 'olá rubi', 'opa rubi', 'eae rubi', 'eai rubi', 'e ai rubi'],
          ['que horas são', 'você tem horas', 'você tem hora', 'que horas são', 'que horas são rubi', 'você tem horas rubi', 'você tem hora rubi', 'que horas são rubi'],
          ['que dia é hoje', 'que dia é hoje rubi'],
          ['tudo bem', 'tudo bem rubi', 'tudo bem', 'tudo bem rubi'],
          ['tchau', 'tchau rubi', 'tchau', 'tchau rubi'],
          ['quem é voce', 'quem é voce rubi', 'quem é você', 'quem é você rubi', 'quem é voce', 'quem é voce rubi', 'quem é você', 'quem é você rubi', 'qual seu nome'],
          ['quais as minhas atividades para hoje']
        ]
outputs = [
            ['Olá pessoa!'],
            ['Agora são 20:30'],
            ['Hoje é Sexta-feira, dia 17 de novembro de dois mil e vinte três'],
            ['Estou bem, obrigada por perguntar'],
            ['Até mais'],
            ['Meu nome é Rubi, sou uma assistente virtual ubiqua criada no cesar.'],
            ['Estudar, deixa de ser preguiçoso!']
        ]

while True:
    try:
        rubi.talk(inputs, outputs)
    except KeyboardInterrupt:
        break


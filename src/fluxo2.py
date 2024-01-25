from rubi import Rubi

rubi = Rubi()

# Interação 1
rubi.speak('Bom dia, Sr. Oliveira! Eu me chamo Rubi. Estou aqui para ajudar no que precisar e fazer companhia. Você teve uma boa noite de sono?')

resposta = rubi.listen()

if 'sim' in resposta:
    rubi.speak('Claro, estou aqui para ajudar. Caso o senhor queira conversar basta falar comigo, caso queira ajuda com alguma atividade, também pode me perguntar. Vejo que o senhor acordou a pouco tempo, já tomou seu café da manhã?')

    rubi.listen()

    rubi.speak('O tempo está ensolarado hoje, a estimativa é que não chova ao longo do dia.')

    rubi.listen()

    rubi.speak('Se precisar de alguma coisa, estarei aqui. Lembro que o senhor tem horários para tomar a sua medicação, gostaria de receber um lembrete diário para não esquecer?')

    rubi.listen()

    rubi.speak('Certo! Seu lembrete foi criado, Sr. Oliveira. Você gostaria de algo mais?')

    rubi.listen()

    rubi.speak('Claro, vou atualizá-lo! Ontem o Sport jogou contra o Ibis e ganhou o jogo com o placar de 2 a 0.')

    rubi.listen()

    rubi.speak('De nada, Sr. Oliveira. Não hesite em me chamar quando for preciso.')

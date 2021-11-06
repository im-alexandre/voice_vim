from subprocess import call

import speech_recognition as sr

from audios.cria_audios import cria_audio
from cleusa_funcs.define_function import define_function

NOME = 'Friday'
trigger = NOME.lower()


def monitora_microfone():
    # obtain audio from the microphone
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.energy_threshold = 3000
        microfone.pause_threshold = 1
        microfone.adjust_for_ambient_noise(source)
        print(microfone.energy_threshold)
        print("Aguardando Comando")
        audio = microfone.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        entrada = microfone.recognize_google(audio,
                                             # language='pt-BR'
                                             )
        entrada = entrada.lower()
        print(entrada)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("""Could not request results from Google
        Speech Recognition service; {0}""".format(e))

    else:
        if trigger in entrada:
            print('Comando:', entrada.replace(trigger, ''))
            executa_comandos(entrada)

    return trigger


def executa_comandos(comando: str) -> None:
    if 'define function' in comando:
        cria_audio('defining function', 'function')
        # responde('function')
        define_function()


def main():
    monitora_microfone()


if __name__ == '__main__':
    while True:
        main()

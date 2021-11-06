from subprocess import call

from gtts import gTTS


def cria_audio(texto: str, nome_arquivo: str) -> None:
    tts = gTTS(texto,
               # lang='pt-br'
               )
    tts.save(f'audios/{nome_arquivo}.mp3')
    responde(nome_arquivo)


def responde(arquivo: str) -> None:
    call(['mpg123', '-q', f'audios/{arquivo}.mp3'])


if __name__ == '__main__':
    cria_audio('define function', 'feedback')

from pytube import YouTube
from time import sleep

print('\t Bem vindo ao downloader de videos do youtube!')
print ('-'*80)

link = input('Insira o Link do video que deseja baixar: ')
yt = YouTube(link)
stream = yt.streams.get_highest_resolution()
print('Seu video está sendo baixado...')
sleep(1)
stream.download()
print('Seu video foi baixado com Sucesso!, aproveite!')
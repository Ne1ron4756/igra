import random

def igra():
    cilipiok = random.randint(1,100)
    chiselko = int(input('Попробуй угадай мое число от 1 до 100 если что. '))
    while True:
        if chiselko == cilipiok:
            print('Мега хорош')
            return
        if chiselko > cilipiok:
            chiselko = int(input('Не, многовато взял '))
        elif chiselko < cilipiok:
            chiselko = int(input('Маловато взял '))
igra()
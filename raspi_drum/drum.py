import serial
import pygame
import os

p = os.path.abspath(os.path.dirname(__file__))
pygame.mixer.init()
port = "COM3"
ser = serial.Serial(port, 115200)

state = [0, 0, 0, 0]

a = pygame.mixer.Sound(os.path.join(p, 'hi_hat.wav'))
b = pygame.mixer.Sound(os.path.join(p, 'kick.wav'))
c = pygame.mixer.Sound(os.path.join(p, 'rim.wav'))
d = pygame.mixer.Sound(os.path.join(p, 'snare.wav'))

drum = [a, b, c, d]
data = 1
while True:
    # data = ser.read()
    d = bin(int(data))[5:]
    for idx, c in enumerate(d):
        s = int(c)
        if s and not state[idx]:
            # 소리 출력
            drum[idx].play()
        elif state[idx] and not s:
            # 소리 멈춤
            drum[idx].stop()

        state[idx] = int(c)
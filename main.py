import sys
from konlpy.tag import Kkma
from Chat import Chat

chatting = []

file = open(sys.argv[1], 'r')

while True:
    line = file.readline().strip()
    if not line:
        break
    chatting.append(Chat(line[0][0], line[3:]))

kkma = Kkma()

for chat in chatting:
    print(kkma.pos(chat.string))

file.close()

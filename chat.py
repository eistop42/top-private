import random 

data = {'привет': ['здравствуй!', 'привет'], 'как дела?': ['хорошо', 'нормально'], 'в чем смысл жизни?': [42]}

while True:
    user = input('Введи сообщение:')
    if user == 'пока':
        break
    if user in data.keys():
        ans = data.get(user)
        ans = random.choice(ans)
        print(ans)
    else:
        print('эмм...')

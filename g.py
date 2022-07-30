import random
answer = random.randint(1, 100)
count = 0
while True:
    count = count + 1
    guess = input('請猜1~100其中一數: ')
    guess = int(guess)
    if guess == answer:
        print('你猜中了!')
        print('這是你猜的第', count, '次')
        break
    elif guess < answer:
        print('比答案小')
    elif guess > answer:
        print('比答案大')
    print('這是你猜的第', count, '次')
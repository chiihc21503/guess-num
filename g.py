import random
answer = random.randint(1, 100)
while True:
    guess = input('請猜1~100其中一數: ')
    guess = int(guess)
    if guess == answer:
        print('你猜中了!')
        break
    elif guess < answer:
        print('比答案小')
    elif guess > answer:
        print('比答案大')
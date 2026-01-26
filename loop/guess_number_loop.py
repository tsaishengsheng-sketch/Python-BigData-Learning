"""
檔名：guess_number_loop.py
功能：迴圈演算法練習
學習重點：for/while 迭代、控制流程
"""
import random 
correct = random.randint(1, 100)
guess = eval(input('Guess a number : '))
while True:
    if guess > correct:
        print(guess, '> correct')
    elif guess < correct:
        print(guess, '< correct')
    else:
        print('Correct number is ', correct)
        print('You win!')
        break
    guess = eval(input('Guess a number : '))
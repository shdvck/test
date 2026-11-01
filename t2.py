import random

secret_number = random.randint(1, 10)  # 生成1到10的随机数
guess = 0

while guess != secret_number:
    guess = int(input("之间的数字："))
    if guess < secre:
V
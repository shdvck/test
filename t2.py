import random

secret_number = random.randint(1, 10)  # 生成1到10的随机数
guess = 0

while guess != secret_number:
    guess = int(input("猜一个 1 到 10 之间的数字："))
    if guess < secret_number:
        print("猜小了，再试试！")
    elif guess > secret_number:
        print("猜大了，再试试！")

print("恭喜你，猜对啦！")
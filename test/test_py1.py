import random
#1- 剪刀
#2- 石头
#3--布
number = random.randint(1,3)
user_number= input("请输入一个值: \n1. 剪刀\n2. 石头\n3. 布")
suer_number = int(user_number)
print(f"电脑输入的值是{number}")
if number == user_number:
    print("平局")
else:
    if user_number > number and not (user_number==3 and number==1):
        print("你获胜了！")
    elif user_number ==1 and number ==3:
        print("你获胜了！")
    else:
         print("你失败了！")

# Дано число. Если оно от -10 до 10 не включительно, 
# то увеличить его на 5, иначе уменьшить на 10.

num = int(input("Введите число: "))

if num > -10 and num < 10:
    num = num + 5
else:
    num = num - 10

print(num)
# Система счислений
num = int(input())

num_b = bin(num)  # в двоичную
num_o = oct(num)  # в восьмеричную
num_x = hex(num)  # в шестнадцатиричную

print(num_b[2:])  # срез от номера
print(num_o[2:])
print(num_x[2:].upper())
# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

# n = int(input("Введите 3х значное число: "))
# if 99<n<1000:
#     a = n//100
#     b = n%100//10
#     c = n%10
#     sum = a + b + c
#     print(f"{n} -> {sum} ({a} + {b} + {c})")
# else:
#     print("указано неверное число")


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали
# S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя
# и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше
# журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# s = int(input("Введите сколько корабликов сделали дети вместе "))
# x = s//6
# print(f"{s} -> {x} + {4*x} + {x}")


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались
# за проезд и получали билет с номером. Счастливым билетом называют такой билет с 
# шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. 
# билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
# которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

# n = int(input("Введите 6ти значное число: "))
# if 99999<n<1000000:
#     a = n//1000
#     a1 = a//100
#     a2 = a%100//10
#     a3 = a%10
#     sumA = a1 + a2 +a3
#     b = n%1000
#     b1 = b//100
#     b2 = b%100//10
#     b3 = b%10
#     sumB = b1 + b2 +b3
#     if sumA == sumB:
#         print(f"{n} -> yes")
#     else:
#          print(f"{n} -> no")
# else:
#     print("указано неверное число")


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m 
# долек отломить k долек, если разрешается сделать один разлом по прямой 
# между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

# n = int(input("Введите 1 размер: "))
# m = int(input("Введите 2 размер: "))
# k = int(input("Введите количество долек: "))
# if k < n*m and ((k % n == 0) or (k % m == 0)) :
#     print("YES")
# else :
#     print("NO")

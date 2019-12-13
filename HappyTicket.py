ticket = int(input())
mod6 = ticket % 10
mod5 = ticket // 10 % 10
mod4 = ticket // 100 % 10
mod3 = ticket // 1000 % 10
mod2 = ticket // 10000 % 10
mod1 = ticket // 100000

sum_left = mod1 + mod2 + mod3
sum_right = mod4 + mod5 + mod6

if sum_left == sum_right:
    print("Счастливый")
else:
    print("Обычный")

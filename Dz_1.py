#1
M_name = "Артём"
print(M_name)
#2
M_age = '19'
print("Здравствуй, взрослая жизнь мне", M_age)
#3
Spam = M_name * 5
print (Spam)
#4
name = input('Введите ваше имя\n')
age = int(input("Сколько вам лет\n"))
print ("Здравствуйте,", name)
if age < 18:
    print('Ты еще мал, чтобы понимать мои шутки\n')
elif age >= 18:
    print("Здравствуй, товарищ по несчастью\n")
elif age >= 20:
    print("Здравствуй, старичок. Песочек не мешает, коленки не болят?\n")

#6
print(name[2:-1])
print(name[::-1])
print(name[:3])
print(name[5:])

#7. Список
A = 1 #Срез
result =[]
for i in range(0, len(str(age)), A):
    result.append(int(str(age)[i: i + A]))
print("\nЛист : " + str(result))

#Перебираем значения листа -> плюсуем, множим
div = 1
sm = 0

for i in result:
    div = div * i
    sm = sm + i
print('\nСумма='+str(sm), '\nПроизведение ='+str(div), "\n")

#8
print(name.upper())
print(name.lower())
print(name.capitalize()) # or name.title()
U = name.capitalize()
print(U.swapcase())

#10
pr = int(input("\nСколько будет 2*2+2\n"))
if pr == 6:
    print("Ты прав, а теперь решаем выш мат!")
else:
    print("Эх, брат, гугли порядок действий...")

#9 (Вот тут у меня проблемка)
prob = 0
while 1:
    try:
        if (age < 1) or (age > 150):
            print("ГОДА")
            raise prob
        elif str.isspace(name):
            print("Ошибка ввода\n")
            raise prob
        else:
            print("ИМЯ")
        continue
    except prob as err:
        break
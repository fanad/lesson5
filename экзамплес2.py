personInfo = {'виктор':'+77019999999',
              'нурбол':'+77017777777',
              'азим':'+77019799999'}
name=input("Введите Имя: ")
name = name.lower()

if name in personInfo:
    print(personInfo[name])
else:
    print("Такого имени нет")

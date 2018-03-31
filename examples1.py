file = open('Shop.txt','r',encoding='utf-8')

leastProduct = 99999
leastLine = []

for line in file:
    listValues = line.split(',')
    if int(listValues[5
                      ]) < int(leastProduct):
        leastProduct = int(listValues[5])
        leastLine = listValues

        
print(leastLine)

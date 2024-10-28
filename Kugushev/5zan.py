import numpy as np #иморт библиотеки
'''
arr=np.array([[1,2,3],
    [4,5,6],
    [7,8,9]])#в переменной arr создает таблицу 3 на 3

print(arr[2,2])#выводит 9
'''
'''
#заменяет каждое 3 число 0
da=np.array([1,2,3,4,5,6,7,8,9,10]) #в переменной da создает таблицу 1 на 5
for i in range(10): #создает счет от 0 до 4 в переменной i
    if da[i]%3 ==0:
        da[i]=0
    print(da[i])
 
#создаем случ массив 3 на 3
arrr=np.random.randint(1,100,size=(3,3))
print(arrr)


a = np.array([34, 56, 99, 43, 98, 2])
for i in range(5):
    if a[i]>x:
        x=a[i]

print(x)



a=50
grrib=3
da=a//grrib
print(a-da*grrib)
'''

a=np.array([3,4,2,1,5,6,0])
sum=0
for i in range(len(a)):
    sum=a[0] + i
    print(sum)
    

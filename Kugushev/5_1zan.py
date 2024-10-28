import numpy as np #имортируем numpy
import matplotlib.pyplot as plt #иморт matplotlib

#создаем 1д массив
arr = np.random.randint(1,1001231,size=(50,50))
#отображение массива
plt.imshow(arr,interpolation='nearest')
#убираем оси
plt.axis('off')

plt.show()

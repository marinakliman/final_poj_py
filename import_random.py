import random
import pandas as pd

# Создаем список
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

# Создаем DataFrame
data = pd.DataFrame({'whoAmI': lst})

# Преобразуем в one hot вид
one_hot = pd.DataFrame(0, index=data.index, columns=['robot', 'human'])

for i in data.index:
    one_hot.loc[i, data.loc[i, 'whoAmI']] = 1

# Выводим результат
print(one_hot.head())

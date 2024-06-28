#새로운 열 만들기

import seaborn as sns

#'mpg' dataset를 불러들이면

df=sns.load_dataset('mpg')

print(df.tail(10))
print()
print()

#기존에 존재하는 데이터를 바탕으로 새로운 열을 만들려면
#'mpg' 데이터셋에서 'mpg' 는 연비를, 'weight' 는 무게를, 'ratio = mpg / weight' 열이라면
#'ratio' 열을 만들어 보자

df['ratio'] = (df['mpg'] / df['weight']) * 100
print(df.head())
print()
print()


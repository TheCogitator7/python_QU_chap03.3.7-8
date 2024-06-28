#filtering

import seaborn as sns

#'mpg' dataset 을 불러들임

df=sns.load_dataset('mpg')

#'mpg' dataset의 마지막 10열을 인쇄

print(df.tail(10))
print()
print()

#'cylinders' 열은 자동차의 실린더 개수를 의미

print(df['cylinders'].unique())
print()
print()

#이 중에서 'cylinders'의 개수가 4인 조건을 입력

filter_bool=(df['cylinders'] == 4)
print(filter_bool.tail(10))
print()
print()

#해당 조건을 데이터 프레임에 대입하면
#총 398 개의 열중 204 개의 열만 남게 됨

print(df.loc[filter_bool, ])
print()
print()

#조건이 하나가 아닌 여러 개를 입력할 수도 있음
#실린더 개수가 4개이고, 마력이 100 이상인 데이터를 선택하면

filter_bool_2=(df['cylinders'] == 4) & (df['horsepower'] >= 100)
print(df.loc[filter_bool_2, ['cylinders', 'horsepower', 'name']])
print()
print()


#'name' 이 'ford maverick', 'ford mustang ii', 'chevrolet impala' 인 데이터를 선택하려면?
#불리언 인덱싱을 사용하면
filter_bool_3=(df['name'] == 'ford maverick') | (df['name'] == 'ford mustang ii') | (df['name'] == 'chevrolet impala')
print(df.loc[filter_bool_3, ])
print()
print()

#isin() 메서드를 이용하여 특정 값을 가진 행을 추출
filter_isin = df['name'].isin(['ford maverick', 'ford mustang ii', 'chevrolet impala'])
print(df.loc[filter_isin, ])
print()
print()


#위의 조건을 sort를 이용하여 horsepower 를 기준으로 정렬하면
print(df.loc[filter_isin, ].sort_values('horsepower'))
print()
print()

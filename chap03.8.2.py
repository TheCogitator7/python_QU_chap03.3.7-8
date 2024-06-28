#특정 열의 조건을 기반으로 새로운 열을 만드는 경우
#조건문 함수가 사용된다.
#numpy 패키지의 where() 함수 사용

import numpy as np
import pandas as pd
import seaborn as sns

num=pd.Series([-2, -1, 1, 2])
print(np.where(num >= 0))
print()
print()

#조건 뒤에 두 번째와 세 번째 인자에 값을 추가하면
#조건을 만족하는 부분은 두 번째 인자(양수)를 부여하고
#그렇지 않은 부분은 세 번째(음수)를 부여한다.

df=sns.load_dataset('mpg')

df['horse_power_div']=np.where(df['horsepower'] < 100, '100 미만',
                               np.where((df['horsepower'] >= 100) & (df['horsepower'] < 200), '100 이상',
                                        np.where(df['horsepower'] >= 200, '200 이상', '기타')))

print(df.head(8))


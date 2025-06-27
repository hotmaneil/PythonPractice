from fractions import Fraction

# 建立分數
x=Fraction(3,5)
y=Fraction(3,7)
print(x)
print('分子',x.numerator)
print('分母',x.denominator)

# 分數之間的四則運算，支援通分
print('x+y',x+y)
print('x*y',x*y)
print('x-y',x-y)
print('x*2',x*2)
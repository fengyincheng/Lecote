import math
"""
gcd 最大公约数
lcm 最小公倍数
"""
a=math.gcd(12,16)
b=math.lcm(12,16)
print(a)
print(b)
from functools import reduce
print(reduce(math.gcd,[12,16,20]))
print(reduce(math.lcm,[12,16,20]))

##质数##

# from sympy import isprime
# print(isprime(11))
# print(isprime(12))

# 快速幂算法

pow(3, 13, 1000000007)
#1594323mod1000000007
print(pow(3, 13, 1000000007))

# 取模运算

MOD = 10

def add(a, b):
    return (a + b) % MOD
def sub(a, b):
    return (a - b) % MOD
def mul(a, b):
    return (a * b) % MOD
def inv(x):
    """
    计算x的模逆元,要求MOD为质数
    """
    return pow(x,-1, MOD)
def div(a, b):
    return mul(a, inv(b))

# 环形数组下标处理

def get_index(current, step, length):
    return (current + step) % length
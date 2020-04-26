# 피보나치 수열 알고리즘

fibo_num = 6

def Fibo(n):
    f = [0, 1] # 초기값 세팅
    
    for i in range(2,n):
        add_int = f[i-1] + f[i-2]
        f.append(add_int)
    return f
result = Fibo(fibo_num)
# print(sum(result))

## 순환형태(재귀함수)로 만든다면..
# fib(1) = 1, fib(2) = 1, fib(3) = 2
# fib (6) = fib(5) + fib(4)
# fib (5) = fib(4) + fib(3)
# ...
# 재귀를 형태를 사용하면 팩토리얼 연산이 된다
# 정말 느리다 이건 절대 사용하지 말자...
def fib(n):
    if n <= 1 : return n
    else: return(fib(n-1)+fib(n-2))
result = fib(fibo_num)
print(result)
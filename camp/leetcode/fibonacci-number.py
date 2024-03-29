class Solution:
    def fib(self, n: int) -> int:
        
        fib = [0, 1]
        if n < 2:
            return fib[n]
        for i in range(2,n+1):
            fib.append(fib[-1] + fib[-2])
        return fib[-1]
            
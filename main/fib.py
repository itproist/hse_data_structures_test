def fib(n):
    if not isinstance(n, int) or (n < 1):
        return None
    if (n == 1):
        return 0
        
    a = [0, 1] 
      
    for i in range(2, n): 
        a.append(a[i-1] + a[i-2]) 
    
    return a[-1]
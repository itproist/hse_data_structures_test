def fibonacci(n):
  if n == 1 or n == 2:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

num_terms = int(input("Enter the number of terms: "))


print("Fibonacci Sequence: ")
for i in range(1, num_terms + 1):
  print(fibonacci(i), end=" ")
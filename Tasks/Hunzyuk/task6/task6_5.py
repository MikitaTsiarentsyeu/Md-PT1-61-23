def cash_decor(func):
  cash_dict = {}
  def wrapper(*args):
    if args in cash_dict:
      return cash_dict[args]
    else:
      res = func(*args)
      cash_dict[args] = res
      return res
  return wrapper

@cash_decor
def fibonacci(n):
  if n < 2: return n
  return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(5))
print(fibonacci(10))
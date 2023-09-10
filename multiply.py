def multiply(num):
  def wrapper(n):
    return n * num
  return wrapper

mul2 = multiply(2)
print(mul2(5))

def gen_squares(n):
  return(x**2 for x in range(1, n + 1))

num = int(input("Enter a number: "))
for i in gen_squares(num):
  print(i)

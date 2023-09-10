def gen_fibonacci_numbers(n):
  if n == "":
    n = 10
  ls = [0, 1]
  for i in range(2, int(n)):
    ls.append(ls[i - 1] + ls[i - 2])
  return (i for i in ls)

num = input("Enter a number: ")
for i in gen_fibonacci_numbers(num):
  print(i)


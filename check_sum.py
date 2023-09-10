def check_sum(*arg):
  Sum = 0
  for i in arg:
    Sum += i
  if Sum < 50:
    return "not enough"
  return "verification passed"

print(check_sum(1, 5, 23, 64))

import inspect

def arg_count(*arg):
  return len(arg)

print(arg_count([1, 2, 3], 15, "Hello"))

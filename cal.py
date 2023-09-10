names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = (((i % 32, names[(i - 1) % 7]) for i in range(1, 61) ))

for i in days:
  print(i)

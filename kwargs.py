def keyword(**kwargs):
   ls = sorted(kwargs.keys())
   for key in ls:
     print(key,'=',kwargs[key] ) 

keyword(name = "John", age = 33)

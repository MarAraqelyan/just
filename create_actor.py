def create_actor(**kwargs):
  data = {"name" :"Johnny", "surname" :"Depp", "age" :59}
  if len(kwargs) != 0:
    for args in kwargs:
      data[args] = kwargs[args]
  for key in data:
    print(key,"=",data[key])

create_actor(name = "James", height = 178)
      

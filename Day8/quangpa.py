import json
customers = []
def add_custiomer(data):
  id, name = data.split(',')
  customers.append({
    'id' : id,
    'name' : name
  })
f = open('../Day8/data.txt', 'r')
customers = f.read()
for line in f.readline():
  add_custiomer(line)
print(customers)
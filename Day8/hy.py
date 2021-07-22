customers = []

def add_customer(data):
    id, name = data.split(',')
    customers.append({
        "id" : id,
        "name" : name,
    })

f = open('data.txt', 'r')
for i in f.readlines():
    add_customer(i)

print(customers)
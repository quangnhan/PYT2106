customers = []

def add_customer(data):
    id, name = data.split(',')
    customers.append({
        "id" : id,
        "name" : name,
    })

f = open('Day8/data.txt', 'r')
for line in f.readlines():
    add_customer(line)

print(customers)
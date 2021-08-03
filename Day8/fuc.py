custommer = []

def Add_Customer(data):
    id, name = data.split(', ')
    return {
        'id':id,
        'name':name
    }

for line in open('Day8/data.txt','r').read().split('\n'):
    print(line)
    custommer.append(Add_Customer(line))
print(custommer)
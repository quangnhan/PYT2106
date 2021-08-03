from server import get_server_data

custommer = []

def Add_Customer(data):
    id, name = data.split(', ')
    return {
        'id':id,
        'name':name
    }

def getdata(data):
    intern = data
    for item in intern:
        id, name = item.split(',')
        intern[intern.index(item)] = {'id':id, 'name': name} 
    return intern

'''
for line in open('Day8/data.txt','r').read().split('\n'):
    print(line)
    custommer.append(Add_Customer(line))

print(custommer)
'''

data = get_server_data()

for line in getdata(data):
    custommer.append(line)
print(custommer)


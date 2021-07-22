from server import get_server_data

customers = []

def add_customer(data):
        id, name = data.split(',')
        customers.append({
                'id': id,
                'name': name
            })
        
def get_data():
    with open("Day8/data.txt", 'r') as file:
        return file.readlines()

data = get_server_data()
for i in data: 
    add_customer(i)

print(customers)

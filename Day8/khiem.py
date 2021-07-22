# from server import get_server_data
# custommer = []

# def add_customer(data):
#     id, name = data.split(',')
#     custommer.append({
#         'id': id,
#         'name': name,
#         })

# def get_date():
#     f = open('Day8/data.txt', 'r')
#     return f.readlines()

# # data = get_date()
# data = get_server_data()

# for line in data:
#     add_customer(line)

# print(custommer)

def giai_thua(n):
    if n == 0:
        return  1
    return n*giai_thua(n-1)

print(giai_thua(5))
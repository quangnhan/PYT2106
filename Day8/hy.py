# customers = []

# def add_customer(data):
#     id, name = data.split(',')
#     customers.append({
#         "id" : id,
#         "name" : name,
#     })

# f = open('data.txt', 'r')
# for i in f.readlines():
#     add_customer(i)

# print(customers)

def giaithua(n):
    giai_thua = 1
    if (n ==0 or n ==1 ):
        return giai_thua
    else:
        for i in range(2, n +1):
            giai_thua = giai_thua * i
            return giai_thua

print (giaithua(3))
# class Shop:
#     def __init__(self, name, list_products):
#         self.name = name
#         self.list_products = list_products

#     def get_name(self):
#         return self.name

#     def get_info(self):
#         print (self.name, self.list_products):
#         for item in self.list_products:
#             print(f'---------------\nAmount')

#Initial list
res = []

# Input lengths
lengths = int(input('nhap so luong chuoi: '))

# Add element
for i in range(lengths):
# Input elements
    n = int(input('nhap so trong chuoi:'))
    res.append(n)


def evenNum(res):
    dap_an  = []
    for v in res:
        if v % 2 == 0:
            dap_an.append(v)
    return dap_an

print(evenNum(res))


list1 = [6, -10, -2]
list2 = [-2, 19]

def multiply_two_lists(list1, list2):
    product_list = []
    for s in list2:
        for a in list1:
            product = s * a
            product_list.append(product)
    return product_list




print("List product =", multiply_two_lists(list1, list2))
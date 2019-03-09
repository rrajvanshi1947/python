import heapq

grades = [15,89,95,25,65,75,62,23,56]

print(heapq.nlargest(3, grades))

new_list = [{'name': 'Apple','price': 568}, {'name': 'Google','price': 897}, {'name': 'Microsoft','price': 561}, {'name': 'Facebook','price': 578}]

print(heapq.nsmallest(2, new_list, key = lambda list_item: list_item['price']))
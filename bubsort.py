from dll2 import DoubleLinkedList

def bubble(data):
    n = len(data)
    if n > 1:
        while True:
            sorted = True
            for i in range(1,n):
                if data[i-1]>data[i]:
                    print(f"swapping {data[i-1]} with {data[i]}")
                    data[i-1], data[i] = data[i], data[i-1]
                    sorted = False
            if sorted:
                return data
    return data



def bublist(data):
    node = data.begin.next
    while True:
        node = data.begin.next
        is_sorted = True
        while node:
            if node.prev.value > node.value:
                node.prev.value, node.value = node.value, node.prev.value
                is_sorted = False
            node = node.next
                # print("or here")
        if is_sorted:
            print("here")
            break


print(bubble([3,2,4,5,23,5,464,6,325,73,23,46,54,34,5324,25,34,534]))

dll = DoubleLinkedList()
dll.push(121)
dll.push(23)
dll.push(344)
dll.push(566)
dll.push(34)
dll.push(34)
dll.push(5656)

bublist(dll)
dll.dump()
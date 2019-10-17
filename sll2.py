class SingleLinkedListNode(object):
    def __init__(self, value,nxt):
        self.value = value
        self.next = nxt

class SingleLinkedList(object):
    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        if self.end == None:
            node = SingleLinkedListNode(obj, None)
            self.begin = self.end = node
        elif self.end == self.begin:
            node = SingleLinkedListNode(obj, None)
            self.end.next = node
            self.end = node
        else:
            node = SingleLinkedListNode(obj, None)
            self.end.next = node
            self.end = node

        assert self.end != None

    def printlist(self):
        if self.begin!=None:
            node = self.begin
            while node:
                print(node.value)
                node = node.next
        else:
            print('empty, nothing to print')
    def pop(self):
        if self.begin:

            if self.begin==self.end:
                node  = self.begin
                self.begin = self.end = None
                print('popping {}'.format(node.value))
                return node.value
            else:
                node = self.begin
                self.begin = self.begin.next
                print('popping {}'.format(node.value))
                return node.value
        else:
            print("empty, nothing to pop")

    def count(self):
        count = 0
        node = self.begin
        while node:
            count+=1
            node = node.next
        return count


ll = SingleLinkedList()
print(ll.count())
ll.push(12)
ll.push(22)
print(ll.count())
ll.printlist()
ll.pop()
ll.printlist()
ll.pop()
print(ll.count())
ll.printlist()
ll.pop()
ll.printlist()
ll.push(33)
print(ll.count())
ll.printlist()
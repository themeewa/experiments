class DoubleLinkedListNode(object):
    def __init__(self,value,nxt,prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None

        return f"[{self.value}, {repr(nval)}, {repr(pval)}]"


class DoubleLinkedList(object):

    def __init__(self):
        self.begin=None
        self.end = None

    def push(self, val):
        print(f"push {val}")
        node = DoubleLinkedListNode(val, None, None)
        if self.begin is None:
            self.begin = self.end = node
        else:
            self.end.next = node
            node.prev = self.end
            self.end = node

    def pop(self):
        if self.begin is None:
            print("nothing to pop")
            return None
        elif self.begin == self.end:
            node = self.begin
            self.begin = self.end = None
            print(f"POP{node.value}")
            return node
        else:
            node = self.end
            self.end = self.end.prev
            self.end.next = None
            if self.begin == self.end:
                self.begin.next = None
            print(f"POP{node.value}")
            return node

    def dump(self):
        print("====")
        node = self.begin
        while node:
            print(node)
            node = node.next
        print("xxxx")

# dll = DoubleLinkedList()
# dll.dump()
# dll.push(12)
# dll.dump()
# dll.pop()
# dll.dump()
# dll.pop()
# dll.dump()
# dll.push(23)
# dll.push(34)
# dll.dump()
# dll.pop()
# dll.dump()
# dll.push(34)
# dll.push(5656)
# dll.push("fdf")
# dll.dump()
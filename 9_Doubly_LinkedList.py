class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def insert_empty(self,data):
        if self.head is None:
            self.head = Node(data)

    def insert_at_begin(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = Node(data)
            node.nref = self.head
            self.head.pref = node
            self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = node
            node.pref = n

    def add_after(self, target, data):
        if self.head == None:
            print("Something went wrong")
        else:
            n = self.head
            while n is not None:
                if n.data == target:
                    break
                n = n.nref
            node = Node(data)
            node.nref = n.nref
            node.pref = n
            if n.nref is not None:
                n.nref.pref = node
            n.nref = node

    def add_before(self, target, data):  
        if self.head == None:
            print("Something went wrong")
            return 
        if self.head.data == target:
            node = Node(data)
            self.head.pref = node
            node.nref = self.head
            self.head = node
            return
        n = self.head
        while n.nref is not None:
            if target == n.nref.data:
                break
            n = n.nref
        if n.nref is None:
            print("Given node is not present")
        else:
            node = Node(data)
            node.nref = n
            node.pref = n.pref
            if n.pref is not None:
                n.pref.nref = node
            n.pref = node

    def delete_begin(self):
        if self.head is None:
            print("List is empty")
        else:
            if self.head.nref is None:
                self.head = None
            else:
                self.head.nref.pref = self.head
                self.head = self.head.nref

    def delete_end(self):
        if self.head is None:
            print("List is empty")
        if self.head.nref is None:
            self.head = None
        else:
            n = self.head
            while n.nref.nref is not None:
                n = n.nref
            n.nref = None

    def delete_node_by_value(self, target):
        if self.head is None:
            print("List is empty")
        if self.head.data == target:
            self.head = self.head.nref
            self.head.pref = None
        else:
            n = self.head
            while n.nref is not None:
                if n.data == target:
                    break
                n = n.nref
            if n.nref is None:
                n.pref.nref = None
            n.pref.nref = n.nref
            n.nref.pref = n.pref

    def print_LL(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.nref

    def print_LL_reverse(self):
        print()
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.pref

dl1 = DoublyLL()
dl1.insert_empty(12)
dl1.insert_at_begin(23)
dl1.insert_at_begin(20)
dl1.insert_at_end(40)
dl1.add_after(40, 15)
dl1.print_LL()
print("After delete")
dl1.delete_begin()
dl1.delete_end()
dl1.delete_node_by_value(23)
dl1.print_LL()
dl1.print_LL_reverse()
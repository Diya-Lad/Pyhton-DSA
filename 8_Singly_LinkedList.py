class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_element_to_empty_list(self, data):
        if self.head == None:
            self.head = Node(data)

    def add_element_at_begining(self,data):
        node = Node(data)
        node.ref = self.head
        self.head = node

    def add_element_at_end(self,data):
        node = Node(data)
        l = self.head
        if l is None:
            l = node
        else:
            while l.ref is not None:
                l = l.ref
            l.ref = node

    def add_element_after_the_target_node(self,target,data):
        n = self.head
        node = Node(data)
        flag = False
        while n is not None:
            if n.data == target:
                node.ref = n.ref
                n.ref = node
                flag = True
                break
            n = n.ref
        if flag==False:
            print("Something went wrong")

    def add_element_before_the_target_node(self,target,data):
        n = self.head
        node = Node(data)
        if n.data == target:
            node.ref = n
            self.head = node
            # print("hello")
        else:
            while n.ref is not None:
                if n.ref.data == target:
                    node.ref = n.ref
                    n.ref = node
                    break
                n = n.ref

    def deletion_at_the_begin(self):
        if self.head == None:
            print("List is empty")
        else:
            self.head = self.head.ref

    def deletion_at_the_end(self):
        if self.head == None:
            print("List is empty")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            del n.ref
            n.ref = None

    def delete_node_by_value(self, target):
        if self.head == None:
            print("List is empty")
        else:
            n = self.head
            if n.data == target:
                self.head = self.head.ref
            else:
                while n.ref!=None and n.ref.data != target:
                    n = n.ref
                n.ref = n.ref.ref

    def print_LL(self):
        if self.head is None:
            print("Linked List is empty!!")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

ll1 = LinkedList()
ll1.add_element_to_empty_list(0)
ll1.add_element_at_begining(12)
ll1.add_element_at_begining(20)
ll1.add_element_at_end(60)
ll1.add_element_after_the_target_node(12, 30)
ll1.add_element_before_the_target_node(20, 36)
ll1.print_LL()
# ll1.deletion_at_the_begin()
# ll1.deletion_at_the_end()
ll1.delete_node_by_value(36)
print("After delete")
ll1.print_LL()
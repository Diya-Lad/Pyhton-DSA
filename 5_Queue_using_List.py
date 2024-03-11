# Main operations: enqueue, dequeue, isfULL, isEmpty

# queue = []
# queue.append(10)
# # to insert element at 0th index
# queue.insert(0,20)

# print(queue)

# queue.pop()

# print(not queue)

queue = []
def enqueue():
    element = input("Enter the element: ")
    queue.append(element)
    print(element, "is added in queue")

def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        e = queue.pop(0)
        print("Removed element: ", e)
        # print(queue)

def display():
    print(queue)

while True:
    print("Select the operation 1.push 2.pop 3.quit")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Enter the correct operation!!!")


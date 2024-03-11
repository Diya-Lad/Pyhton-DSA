# # Implement stack using list

# # 1.
# stack = []
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(stack)
# stack.pop()
# print(stack)

# # To check whether stack is empty or not
# print(len(stack) == 0)

# print(not stack)

# # to access last element (top elemnt) of the stack
# stack[-1]

stack = []
def push():
    element = input("Enter the element: ")
    stack.append(element)
    print(stack)

def pop_element():
    if not stack:
        print("Stack is empty")
    else:
        e = stack.pop()
        print("Removed element: ", e)
        print(stack)

while True:
    print("Select the operation 1.push 2.pop 3.quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Enter the correct operation!!!")



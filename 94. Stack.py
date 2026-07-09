stack = []
while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = int(input("Enter element: "))
        stack.append(item)
        print("Element pushed.")
    elif choice == 2:
        if len(stack) == 0:
            print("Stack Underflow")
        else:
            print("Popped Element:", stack.pop())
    elif choice == 3:
        if len(stack) == 0:
            print("Stack is Empty")
        else:
            print("Top Element:", stack[-1])
    elif choice == 4:
        if len(stack) == 0:
            print("Stack is Empty")
        else:
            print("Stack:", stack)
    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid Choice")

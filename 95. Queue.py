queue = []
while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Front")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = int(input("Enter element: "))
        queue.append(item)
        print("Element Enqueued")
    elif choice == 2:
        if len(queue) == 0:
            print("Queue Underflow")
        else:
            print("Dequeued Element:", queue.pop(0))
    elif choice == 3:
        if len(queue) == 0:
            print("Queue is Empty")
        else:
            print("Front Element:", queue[0])
    elif choice == 4:
        if len(queue) == 0:
            print("Queue is Empty")
        else:
            print("Queue:", queue)
    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid Choice")

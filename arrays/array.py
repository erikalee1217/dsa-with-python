# Practicing with arrays using python built-in functions

def arr_test():
    # Create an array
    arr = [1, 6, 12, 17, 28]
    print("initial array = ", arr)

    # Accessing elements
    print("arr[3] = ", arr[3])

    # Updating elements
    arr[2] = 10
    print("array after updating =", arr)

    # Inserting elements
    arr.insert(3, 12)
    print("array after inserting = ", arr) 

    # Appending elements
    arr.append(25)
    print("array after appending = ", arr) 

    # Removing elements
    arr.remove(6)
    print("array after removing = ", arr)

    # Popping elements
    arr.pop()
    print("array after popping = ", arr)

    # Finding the length of the array
    print("the length of the array = ", len(arr)) 

    # Sorting the array
    arr.sort()
    print("array after sorting = ", arr)

    # Reversing the array
    arr.reverse()
    print("array after reversing = ", arr)

def main():
    arr_test()

if __name__ == "__main__":
    main()
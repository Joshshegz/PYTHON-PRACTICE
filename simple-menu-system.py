while True:
    print("Menu:")
    print("1. Calculate Sum")
    print("2. Search for a Word")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        numbers = input("Enter a series of numbers separated by spaces: ")
        num_list = [float(num) for num in numbers.split()]
        total = sum(num_list)
        print(f"The sum of the numbers is: {total}")
    elif choice == '2':
        text = input("Enter a sentence or text: ")
        word_is_there= input("Enter a word to search for: ")
        if word_is_there in text:
            print(f"'{word_is_there}' is found in the text.")
        else:
            print(f"'{word_is_there}' is not found in the text.")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
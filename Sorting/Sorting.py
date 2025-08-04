def alpha():
    def alphabetically(words, n):
        for i in range(n):
            for j in range(n-i-1):
                if words[j].lower() > words[j+1].lower():
                    words[j], words[j+1] = words[j+1], words[j]
        print("Sorted in alphabetic order:", words)
    
    def reverse_alphabetically(words, n):
        for i in range(n):
            for j in range(n-i-1):
                if words[j].lower() < words[j+1].lower():
                    words[j], words[j+1] = words[j+1], words[j]
        print("Sorted in reverse alphabetic order:", words)
    
    def by_length_ascending(words, n):
        for i in range(n):
            for j in range(n-i-1):
                if len(words[j]) > len(words[j+1]):
                    words[j], words[j+1] = words[j+1], words[j]
        print("Sorted by length in ascending order:", words)
    
    def by_length_descending(words, n):
        for i in range(n):
            for j in range(n-i-1):
                if len(words[j]) < len(words[j+1]):
                    words[j], words[j+1] = words[j+1], words[j]
        print("Sorted by length in descending order:", words)
    
    print("Welcome to the String Sorting Program!")
    words = [i for i in input("Enter the list of strings separated by space: ").split()]
    n = len(words)
    print("1. Alphabetically\n2. Reverse Alphabetically\n3. By Length (Ascending)\n4. By Length (Descending)\n")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        alphabetically(words, n)
    elif ch == 2:
        reverse_alphabetically(words, n)
    elif ch == 3:
        by_length_ascending(words, n)
    elif ch == 4:
        by_length_descending(words, n)

def numbers():
    def ascending(nums,n):
        for i in range(n):
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        print("Sorted in ascending order:", nums)
    
    def descending(nums,n):
        for i in range(n):
            for j in range(n-i-1):
                if nums[j] < nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        print("Sorted in descending order:", nums)
    
    print("Welcome to the Number Sorting Program!")
    nums = [int(i) for i in input("Enter the list of numbers separated by space: ").split()]
    n = len(nums)
    print("1. Ascending\n2. Descending\n")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        ascending(nums, n)
    elif ch == 2:
        descending(nums,n)

def main():
    print("Welcome to the Sorting Program!")
    print("1. Sort Strings\n2. Sort Numbers\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        alpha()
    elif choice == 2:
        numbers()
    else:
        print("Invalid choice! Please run the program again.")

main()

# This program sorts strings and numbers based on user choice.
# It provides options to sort 
#     1. strings 
#         a. alphabetically
#         b. reverse alphabetically
#         c. by length
#             i. ascending
#             ii. descending order,
#     2. numbers
#         a. ascending
#         b. descending order.
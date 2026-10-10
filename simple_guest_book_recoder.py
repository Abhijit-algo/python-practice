guest_name = input("Enter your name to sign the guest book: ")

 
with open("guest_book.txt", "a") as file:
    file.write(guest_name + "\n")  

print(f"Thank you, {guest_name}! Your name has been added.")

print("\n--- Everyone in the Guest Book ---")
with open("guest_book.txt", "r") as file:
    print(file.read())

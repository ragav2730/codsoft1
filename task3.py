import random
import string

def generate_p(length):
    # Define character sets
    ch = string.ascii_letters + string.digits 

    # Generate the p8
    p = ''.join(random.choice(ch) for _ in range(length))
    
    return p

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            raise ValueError("The length must be a positive integer.")
        
        p = generate_p(length)
        print(f"Generated Password: {p}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()

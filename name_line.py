"""
You are given the firstname and lastname of a
person on two different lines.
Your task is to read them and print the following:


"""

def print_full_name(a, b):
    full_name = a +" "+ b
    print(f"Hello {full_name}! You just delved into python.")
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

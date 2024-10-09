number = int(input("Enter a number"))

odd_numbers = [x for x in range(number) if x % 2 != 0]

all_num = [x for x in range(number)]

print(f"Odd numbers b4 ({number} : {odd_numbers}")
print(f"\nAll numbers b4 {number} : {all_num}")

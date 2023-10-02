from big_num import BigNum
from data import rand_bigint

big_a = None
big_b = None
result = None


def main():

    global big_a, big_b, result

    while True:
        print("\navailable operations:")
        print("+  addition")
        print("-  subtraction")
        print("*  multiplication")
        print("/  division (returns quotient)")
        print("%  mod")
        print("^  square")
        print("e  exit")
        choice = input("\nenter your choice: ")

        if choice == "e":
            print("exit")
            break
        elif choice not in ["+", "-", "*", "/", "%", "^", "e"]:
            print("incorrect input")
            continue
        elif choice != "^":

            print("\nm - manual")
            print("r - rand")
            input_type = input("\nenter your choice: ")

            if input_type == "m":
                a = input("\nenter first big num: ")
                b = input("enter second big num: ")
                big_a = BigNum(a)
                big_b = BigNum(b)
            elif input_type == "r":
                a = input("\nenter num of digits for a first num: ")
                b = input("enter num of digits for a second num: ")
            else:
                print("\nincorrect input")
                continue

            rand_a = rand_bigint(int(a))
            rand_b = rand_bigint(int(b))
            big_a = BigNum(rand_a)
            big_b = BigNum(rand_b)

            if choice == "+":
                result = big_a + big_b
            elif choice == "-":
                result = big_a - big_b
            elif choice == "*":
                result = big_a * big_b
            elif choice == "/":
                result = big_a // big_b
            elif choice == "%":
                result = big_a % big_b

        elif choice == "^":
            print("m - manual, r - rand")
            input_type = input("\nenter your choice: ")

            if input_type == "m":
                a = input("\nenter big num: ")
                big_a = BigNum(a)

            elif input_type == "r":
                a_num = input("\nenter num of digits for a number: ")
                big_a = rand_bigint(int(a_num))
                print(big_a)
            else:
                print("\nincorrect input")
                break
            result = big_a ** 2
        else:
            print("\nincorrect input")

        print("\n")
        print("a = ", big_a)
        print(choice)
        print("b = ", big_b)
        print("\nresult:", result)


if __name__ == "__main__":
    main()


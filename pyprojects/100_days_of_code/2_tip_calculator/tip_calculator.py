'''
    Program to calculate amounts payable by a number
    of patrons or friends from a bill, inclusive of
    a percentage tip added to bill total.

    @datetime:: September 18, 2024 5:14 am (UTC-5)
    @author:: jacoder
'''


def main():
    calculate_pay_amounts()


def calculate_pay_amounts():
    '''
        Function to calculate and split up how much each 
        of a number of friends/patron is to pay from a
        bill.

        @input: none
        @output: float -> amount payable by each patron.
    '''
    try:
        print("Welcome to the tip calculator!")

        # accept inputs from user and convert the string data type entries
        #to float and int data types (explicit type convertion).
        bill_total = float(input("What was the total bill? $"))
        tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
        split = int(input("How many people to split the bill? "))

        # bill total plus added tip percentage
        grand_total = bill_total + (bill_total * (tip/100))
        print(grand_total)

        split_amount = grand_total / split

        print(f"Each person should pay: ${round(split_amount, 2)}")

    except ValueError:
        print("ValueError occured, check data type conversions. Possible converting from a string to either a float or int datatype.")

    except Exception:
        print("Error occured.")


if __name__ == "__main__":
    main()
# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = input("Please enter your current savings balance: ")
    savings_balance = float(savings_balance)
    
    savings_interest = input("Please enter your current savings interest: ")
    savings_interest = float(savings_interest)

    savings_maturity = input("Please enter the amount of months you will be saving for: ")
    savings_maturity = int(savings_maturity)

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("-" * 40)
    print(f"Savings Account Info:")
    print(f"\t- Savings Balance: ${format(updated_savings_balance, ",.2f")}")
    print(f"\t- Interest Earned: ${format(interest_earned, ",.2f")}")
    print(f"\t- Month Saved: {savings_maturity}")
    print("-" * 40 + "\n")


    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = input("Please enter your current savings balance: ")
    cd_balance = float(cd_balance)
    
    cd_interest = input("Please enter your current savings interest: ")
    cd_interest = float(cd_interest)

    cd_maturity = input("Please enter the amount of months you will be saving for: ")
    cd_maturity = int(cd_maturity)

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("-" * 40)
    print(f"CD Info:")
    print(f"\t- CD Balance: ${format(updated_cd_balance, ",.2f")}")
    print(f"\t- Interest Earned: ${format(interest_earned, ",.2f")}")
    print(f"\t- Month Saved: {cd_maturity}")
    print("-" * 40 + "\n")


if __name__ == "__main__":
    # Call the main function.
    main()
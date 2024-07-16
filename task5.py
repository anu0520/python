def get_total_balance():
    total_balance = 0

    for i in range(1, 5):
        denomination = int(input(f"Enter the {i}st Denomination: "))
        num_notes = int(input(f"Enter the {i}st Denomination number of notes: "))
        total_balance += denomination * num_notes

    return total_balance

# Sample input and output
total_balance = get_total_balance()
print(f"Total Available Balance in ATM: {total_balance}")

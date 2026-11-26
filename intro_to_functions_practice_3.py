price = 13.95

def main():
    tickets = int(input("How many tickets? "))

    total_cost = tickets * price

    print(f"${total_cost}.")

if __name__ == "__main__":
    main()
def main():
    shopping_list = []
    print("Welcome to shopping list")
    while True:
        item_list = input(
            "Enter the item you want to add and type 'done' (without quotations) if you are already done\n>> ").strip().lower()

        if item_list == 'done':
            print("Thank you for shopping list")
            break
        if not item_list:
            print("Please enter a valid item name")
            continue
        shopping_list.append(item_list)
        print(f"Added: {item_list} (total items: {len(shopping_list)})")

    print("\nYour shopping list")
    if item_list:
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    else:
        print("No items added")


if __name__ == "__main__":
    main()


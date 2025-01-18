class CheckOut:
    def __init__(self):
        # original price of product
        self.prices = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15
        }
        # item name: (number_of_item(group), price)
        self.discount_price = {
            "A": (3, 130),
            "B": (2, 45)
        }

    def calculate_total_price(self, items):
        items_count = {}
        error_message = {}
        # Count each item
        for item in items:
            if item not in self.prices:
                error_message[item] = 'This product is invalid'
                continue
            else:
                items_count[item] = items_count.get(item, 0) + 1

        total_price = 0
        # Calculate total price based on item count and possible discounts
        for item, count in items_count.items():
            if item in self.discount_price:
                group_size, price = self.discount_price.get(item)
                total_price += (count // group_size) * price
                total_price += (count % group_size) * self.prices.get(item)
            else:
                total_price += count * self.prices.get(item)

        return items_count, total_price, error_message


if __name__ == '__main__':
    check_out = CheckOut()
    value = input("Enter product codes: ").strip()

    if not value.isalpha():
        print("Invalid input. Please enter product codes using letters (e.g., ABCD).")
        exit()

    # Call funcation for check price 
    number_of_each_item, total_amount, error_message = check_out.calculate_total_price(list(value.upper()))

    # Errors for invalid products
    if len(error_message) > 0:
        print("Following products are invalid:")
        for item, error in error_message.items():
            print(f"{item} - {error}")

    # Display items and their count
    print("\nItem Name  Count")
    for item_name, count in number_of_each_item.items():
        print(f"Item {item_name} - {count}")
    print(f"\nTotal amount: {total_amount}")

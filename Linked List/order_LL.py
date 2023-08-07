class Order:
    def __init__(self, order_number, items):
        self.order_number = order_number
        self.items = items
        self.next = None

class OrderLinkedList:
    def __init__(self):
        self.head = None

    def add_order(self, order):
        new_node = order
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_order(self, order_number):
        if self.head is None:
            return

        if self.head.order_number == order_number:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.order_number == order_number:
                current.next = current.next.next
                return
            current = current.next

    def display_orders(self):
        if self.head is None:
            print("No orders to display.")
            return

        print("\nCurrent Orders:")
        current = self.head
        while current:
            print(f"Order {current.order_number} - Items: {', '.join(current.items)}")
            current = current.next

# Create an order and add it to the list
def create_order():
    order_number = int(input("Enter order number: "))
    items = input("Enter items (comma-separated): ").split(",")
    return Order(order_number, items)

# Main program
def main():
    order_list = OrderLinkedList()

    while True:
        print("\nWelcome to Order Management System:")
        print("1. Add New Order")
        print("2. Remove Order")
        print("3. Display Orders")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            order = create_order()
            order_list.add_order(order)
            print("Order added successfully.")

        elif choice == 2:
            order_number = int(input("Enter order number to remove: "))
            order_list.remove_order(order_number)
            print("Order removed successfully.")

        elif choice == 3:
            order_list.display_orders()

        elif choice == 4:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

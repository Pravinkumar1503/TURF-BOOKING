import datetime

class Delivery:
    def __init__(self, order_id, destination, delivery_date, status="Scheduled"):
        self.order_id = order_id
        self.destination = destination
        self.delivery_date = delivery_date
        self.status = status

    def __str__(self):
        return f"Order {self.order_id} to {self.destination} on {self.delivery_date} - {self.status}"

class DeliverySchedule:
    def __init__(self):
        self.deliveries = []

    def add_delivery(self, order_id, destination, delivery_date):
        delivery = Delivery(order_id, destination, delivery_date)
        self.deliveries.append(delivery)
        print(f"Added: {delivery}")

    def update_status(self, order_id, new_status):
        for delivery in self.deliveries:
            if delivery.order_id == order_id:
                delivery.status = new_status
                print(f"Updated: {delivery}")
                return
        print("Order not found.")

    def view_schedule(self):
        print("Delivery Schedule:")
        for delivery in sorted(self.deliveries, key=lambda d: d.delivery_date):
            print(delivery)

    def deliveries_on_date(self, date):
        print(f"Deliveries on {date}:")
        for delivery in self.deliveries:
            if delivery.delivery_date == date:
                print(delivery)

# Example usage
if __name__ == "__main__":
    schedule = DeliverySchedule()
    schedule.add_delivery("1001", "New York", datetime.date(2024, 6, 10))
    schedule.add_delivery("1002", "Los Angeles", datetime.date(2024, 6, 11))
    schedule.add_delivery("1003", "Chicago", datetime.date(2024, 6, 10))
    schedule.view_schedule()
    schedule.update_status("1002", "Delivered")
    schedule.deliveries_on_date(datetime.date(2024, 6, 10))
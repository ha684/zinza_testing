from models import Order, Product

def create_test_data():
    """Create test data for the three required scenarios and additional edge cases."""
    p1 = Product(product_id="P001", name="Laptop Dell XPS", quantity=1, price=1200.0)
    p2 = Product(product_id="P002", name="Wireless Mouse", quantity=2, price=30.0)
    p3 = Product(product_id="P003", name="Mechanical Keyboard", quantity=1, price=80.0)
    p4 = Product(product_id="P004", name="27-inch Monitor", quantity=1, price=250.0)
    p5 = Product(product_id="P001", name="Laptop Dell XPS", quantity=1, price=1200.0)
    p6 = Product(product_id="P005", name="Noise-Cancelling Headphones", quantity=1, price=100.0)
    p7 = Product(product_id="P006", name="USB-C Hub", quantity=3, price=15.0)

    o1 = Order(order_id="ORD001", delivery_address="123 Main St, Springfield")
    o1.add_product(p1)
    o1.add_product(p2)

    o2 = Order(order_id="ORD002", delivery_address="123 Main St, Springfield")
    o2.add_product(p3)
    o2.add_product(p5)

    o3 = Order(order_id="ORD003", delivery_address="456 Oak Ave, Rivertown")
    o3.add_product(p4)

    o4 = Order(order_id="ORD004", delivery_address="789 Pine Rd, Lakeside")
    o4.add_product(p6)

    o5 = Order(order_id="ORD005", delivery_address="123 Main St, Springfield")
    o5.add_product(p2)
    o5.add_product(p7)

    o6 = Order(order_id="ORD006", delivery_address="456 Oak Ave, Rivertown")
    o6.add_product(p3)
    o6.add_product(p6)

    o7 = Order(order_id="ORD007", delivery_address="101 Birch Ln, Hilltop")

    scenario1 = [o1, o2, o5]

    scenario2 = [o3, o4, o7]

    scenario3 = [o1, o2, o3, o4, o5, o6, o7]

    return scenario1, scenario2, scenario3
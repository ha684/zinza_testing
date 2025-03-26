from dataclasses import dataclass, field
from typing import List, Set


@dataclass
class Product:
    product_id: str
    name: str
    quantity: int
    price: float

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.product_id == other.product_id
    
    def __hash__(self):
        return hash(self.product_id)


@dataclass
class Order:
    order_id: str
    delivery_address: str
    products: List[Product] = field(default_factory=list)

    def add_product(self, product: Product):
        self.products.append(product)


@dataclass
class MergedOrder:
    delivery_address: str
    products: List[Product] = field(default_factory=list)
    order_ids: Set[str] = field(default_factory=set)

    def add_order(self, order: Order):
        self.order_ids.add(order.order_id)
        for product in order.products:
            product_copy = Product(
                product_id=product.product_id,
                name=product.name,
                quantity=product.quantity,
                price=product.price
            )
            self.add_product(product_copy)
    
    def add_product(self, product: Product):
        for existing_product in self.products:
            if existing_product.product_id == product.product_id:
                existing_product.quantity += product.quantity
                return
        self.products.append(product)

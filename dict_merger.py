from typing import Dict, List
from models import Order, MergedOrder


class DictionaryMerger:
    def merge_orders(orders: List[Order]) -> List[MergedOrder]:
        merged_orders_dict: Dict[str, MergedOrder] = {}

        for order in orders:
            address = order.delivery_address

            if address not in merged_orders_dict:
                merged_order = MergedOrder(delivery_address=address)
                merged_orders_dict[address] = merged_order

            merged_orders_dict[address].add_order(order)

        return list(merged_orders_dict.values())

import psycopg2
from typing import List
from models import Order, MergedOrder, Product
import os
class PostgresMerger:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        self.cur = self.conn.cursor()

    def setup_tables(self):
        self.cur.execute("""
            DROP TABLE IF EXISTS Orders;
            DROP TABLE IF EXISTS Products;
            CREATE TABLE Products (
                product_id TEXT PRIMARY KEY,
                name TEXT,
                quantity INTEGER,
                price FLOAT
            );
            CREATE TABLE Orders (
                order_id TEXT PRIMARY KEY,
                delivery_address TEXT,
                product_id TEXT REFERENCES Products(product_id)
            );
        """)
        self.conn.commit()

    def insert_orders(self, orders: List[Order]):
        for order in orders:
            for product in order.products:
                self.cur.execute("""
                    INSERT INTO Products (product_id, name, quantity, price)
                    VALUES (%s, %s, %s, %s)
                    ON CONFLICT (product_id) DO NOTHING;
                """, (product.product_id, product.name, product.quantity, product.price))
                self.cur.execute("""
                    INSERT INTO Orders (order_id, delivery_address, product_id)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (order_id) DO NOTHING;
                """, (order.order_id, order.delivery_address, product.product_id))
        self.conn.commit()

    def merge_orders(self, orders: List[Order]) -> List[MergedOrder]:
        order_ids = [o.order_id for o in orders]
        self.cur.execute("""
            SELECT 
                o.delivery_address,
                array_agg(o.order_id) AS order_ids,
                array_agg(p.product_id) AS product_ids,
                array_agg(p.name) AS product_names,
                array_agg(p.quantity) AS quantities,
                array_agg(p.price) AS prices
            FROM Orders o
            JOIN Products p ON o.product_id = p.product_id
            WHERE o.order_id = ANY(%s)
            GROUP BY o.delivery_address;
        """, (order_ids,))
        
        results = self.cur.fetchall()
        merged_orders = []
        for row in results:
            mo = MergedOrder(row[0])
            mo.order_ids = row[1]
            for pid, name, qty, price in zip(row[2], row[3], row[4], row[5]):
                mo.products.append(Product(pid, name, qty, price))
            merged_orders.append(mo)
        return merged_orders

    def close(self):
        self.cur.close()
        self.conn.close()
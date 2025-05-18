from enum import Enum


class OrderStatus(str, Enum):
    pending = "Pending"
    delivered = "Delivered"
    cancelled = "Cancelled"

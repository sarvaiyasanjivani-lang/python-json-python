import json
from dataclasses import asdict, dataclass


@dataclass
class Product:
    name: str
    price: float
    in_stock: bool


product = Product("Laptop", 77000.0, True)

json_data = json.dumps(asdict(product), indent=2)

print(json_data)

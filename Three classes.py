class Checklist:
    def __init__(self,header: str, entries: list):
        self.header = header
        self.entries = entries

class Customer:
    def __init__(self,id: str, balance: float, discount: int):
        self.id = id
        self.balance = balance
        self.discount = discount

class Cable:
    def __init__(self,model: str,length: float,max_speed: int,bidirectional: bool):
        self.model = model
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectional

# Create a checklist
checklist = Checklist("Groceries", ["milk", "bread", "eggs"])
print(checklist.header)     # Groceries
print(checklist.entries)    # ['milk', 'bread', 'eggs']

# Create a customer
customer = Customer("C123", 250.50, 10)
print(customer.id)          # C123
print(customer.balance)     # 250.5
print(customer.discount)    # 10

# Create a cable
cable = Cable("HDMI", 2.0, 480, True)
print(cable.model)          # HDMI
print(cable.length)         # 2.0
print(cable.max_speed)      # 480
print(cable.bidirectional)  # True
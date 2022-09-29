"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary, contract, contracts, commission, bonus):
        self.name = name
        self.salary = salary
        self.contract = contract
        self.contracts = contracts
        self.commission = commission
        self.bonus = bonus

    def get_pay(self):
        
        return self.salary * self.get_contract() + self.get_empty(self.contracts) * self.get_empty(self.commission) + self.get_empty(self.bonus)

    def get_salaryType(self):
        if self.contract == -1:
            return f" monthly salary of {self.salary}"
        else:
            return f" contract of {self.contract} hours at {self.salary}/hour"
    
    def get_contract(self):
        if self.contract == -1:
            return 1
        else:
            return self.contract

    def get_empty(self, zero):
        if zero == -1:
            return 0
        else:
            return zero

    def get_contracts(self):
        if self.contracts != -1:
            return f" and receives a commission for {self.contracts} contract(s) at {self.commission}/contract"
        else:
            return ""

    def get_bonus(self):
        if self.bonus != -1:
            return f" and receives a bonus commission of {self.bonus}"
        else:
            return ""

    def __str__(self):
        return self.name + " works on a" + self.get_salaryType() + self.get_contracts() + self.get_bonus() + ".  Their total pay is " + str(self.get_pay()) + "."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, -1, -1, -1 , -1)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 25, 100, -1 , -1, -1)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, -1, 4, 200, -1)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 25, 150, 3, 220, -1)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, -1, -1, -1, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 30, 120, -1, -1, 600)

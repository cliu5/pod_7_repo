class Bill:
    def __init__(self):
        self.tax = 0.1
    def set_total(self, total):
        self.total = total
    def set_tip(self, tip):
        self.tip = tip
    def set_people(self, people):
        self.people = people
    def get_tip_amount(self):
        return self.total * (self.tip/100)
    def get_tax(self):
        return self.total * self.tax 
    def split(self):
        return (self.total + self.get_tip_amount() + self.get_tax()) / self.people 

bill = Bill()
bill.set_total(float(input("What is the total bill?: ")))
bill.set_tip(int(input("What % tip would you like to give?: ")))
bill.set_people(int(input("How many people are splitting the bill?: ")))
print(f"Each person owes: ${bill.split()}")
print("Thank you for the business!")

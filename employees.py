import csv
class Employee:
    def __init__(self, first_name, last_name, hourly_rate, hours_worked, amount_due):
        self.first_name = first_name
        self.last_name = last_name
        self.hourly_rate = float(hourly_rate)
        self.hours_worked = float(hours_worked)
        self.amount_due = float(amount_due)
    def values(self):
        return[self.first_name, self.last_name, self.hourly_rate, self.hours_worked, self.amount_due]
employees = []
with open("employees.csv") as emplycsvfile:
    reader = csv.reader(emplycsvfile, skipinitialspace = True)
    next(reader)
    for row in reader:
        current_employee = Employee(*row)
        employees.append(current_employee)
jenny = Employee("Jenny", "Jones", 12.00, 40.00, 0)
employees.append(jenny)
with open("employees_write.csv", mode = "w") as emplycsvfile:
    writer = csv.writer(emplycsvfile, quoting = csv.QUOTE_ALL)
    writer.writerow(["first_name", "last_name", "hourly_rate", "hours_worked", "amount_due"])
    for employee in employees:
        writer.writerow(employee.values())

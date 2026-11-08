class Employee:
    TRANSPORT_ALLOWANCE = 2000

    def __init__(self, employee_id, full_name, department, basic_salary):
        self.employee_id = employee_id
        self.full_name = full_name
        self.department = department
        self.basic_salary = basic_salary

    def housing_allowance(self):
        return self.basic_salary * 0.15

    def gross_pay(self):
        return (
            self.basic_salary
            + self.TRANSPORT_ALLOWANCE
            + self.housing_allowance()
        )

    def tax_rate(self):
        if self.basic_salary < 20000:
            return 0.05
        elif self.basic_salary < 50000:
            return 0.10
        return 0.15

    def tax_deduction(self):
        # The practice tax rate is applied to the basic salary.
        return self.basic_salary * self.tax_rate()

    def net_pay(self):
        return self.gross_pay() - self.tax_deduction()

    def display_details(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.full_name}")
        print(f"Department: {self.department}")

    def display_payslip(self):
        print("\n================ EMPLOYEE PAYSLIP ================")
        self.display_details()
        print(f"Basic salary: KSh {self.basic_salary:,.2f}")
        print(f"Transport allowance: KSh {self.TRANSPORT_ALLOWANCE:,.2f}")
        print(f"Housing allowance: KSh {self.housing_allowance():,.2f}")
        print(f"Gross pay: KSh {self.gross_pay():,.2f}")
        print(f"Tax rate: {self.tax_rate() * 100:.0f}%")
        print(f"Tax deduction: KSh {self.tax_deduction():,.2f}")
        print(f"NET PAY: KSh {self.net_pay():,.2f}")
        print("==================================================")


employees = {}


def add_employee():
    employee_id = input("Employee ID: ").strip().upper()
    if not employee_id:
        print("Employee ID cannot be empty.")
        return
    if employee_id in employees:
        print("Employee ID already exists.")
        return

    name = input("Full name: ").strip()
    department = input("Department: ").strip()
    if not name or not department:
        print("Name and department are required.")
        return

    try:
        salary = float(input("Basic monthly salary (KSh): "))
        if salary <= 0:
            print("Basic salary must be greater than zero.")
            return
    except ValueError:
        print("Enter a valid salary amount.")
        return

    employees[employee_id] = Employee(employee_id, name, department, salary)
    print("Employee registered successfully!")


def find_employee():
    employee_id = input("Employee ID: ").strip().upper()
    employee = employees.get(employee_id)
    if not employee:
        print("Employee not found.")
    return employee


def search_employee():
    employee = find_employee()
    if employee:
        employee.display_details()


def show_payslip():
    employee = find_employee()
    if employee:
        employee.display_payslip()


def payroll_summary():
    if not employees:
        print("No employees are registered.")
        return

    total_payroll = sum(employee.net_pay() for employee in employees.values())
    average_net = total_payroll / len(employees)

    print("\n========== PAYROLL SUMMARY ==========")
    print(f"Employees: {len(employees)}")
    print(f"Total payroll cost (net pay): KSh {total_payroll:,.2f}")
    print(f"Average net salary: KSh {average_net:,.2f}")
    print("=====================================")


def main_menu():
    while True:
        print("\n========== EMPLOYEE PAYROLL CALCULATOR ==========")
        print("1. Register employee")
        print("2. Search employee")
        print("3. View employee payslip")
        print("4. Calculate payroll summary")
        print("5. List all employees")
        print("6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            search_employee()
        elif choice == "3":
            show_payslip()
        elif choice == "4":
            payroll_summary()
        elif choice == "5":
            if not employees:
                print("No employees registered.")
            else:
                for employee in employees.values():
                    print(
                        f"{employee.employee_id} - {employee.full_name} - "
                        f"{employee.department}"
                    )
        elif choice == "6":
            print("Thank you for using the Employee Payroll Calculator!")
            break
        else:
            print("Invalid option. Choose 1-6.")


if __name__ == "__main__":
    main_menu()

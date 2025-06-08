# Step 1: Get number of employees
emp_num = int(input("Number of employees: "))

# Step 2: Initialize total payroll
total_payroll = 0

# Step 3: Loop through each employee
for i in range(emp_num):
    print(f"\nEmployee #{i+1}")
    hourly_rate = int(input("Hourly rate: "))
    num_hours = int(input("Number of hours: "))
    
    salary = hourly_rate * num_hours

    # Step 4: Apply bonus if salary > 1000
    if salary > 1000:
        total_salary = salary + salary * 0.1  # 10% bonus
    else:
        total_salary = salary

    # Step 5: Print and add to total payroll
    print(f"Total salary for employee #{i+1}: Rs. {total_salary}")
    total_payroll += total_salary  # Add to the total

# Step 6: Print total payroll
print(f"\n🧾 Total Payroll: Rs. {total_payroll}")
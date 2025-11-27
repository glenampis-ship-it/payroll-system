Emp = []
‎
‎while True:
‎    print("\n================= PAYROLL SYSTEM =================")
‎    print("1. Add Employee")
‎    print("2. Display All Employees")
‎    print("3. Search Employee")
‎    print("4. Exit\n")
‎    
‎    cho = input("Enter a number (1-4): ")
‎
‎    if cho == "1":
‎        print("\n=== Add Employee ===")
‎
‎        while True:
‎            try:
‎                ID = int(input("Enter ID: "))
‎            except ValueError:
‎                print("Error: ID must be a number.")
‎                continue
‎
‎            dup = False
‎            for em in Emp:
‎                if em["ID"] == ID:
‎                    dup = True
‎                    break
‎
‎            if dup:
‎                print(f"Error: Employee ID {ID} already exists. Please enter a new ID.")
‎            else:
‎                break 
‎
‎        n = input("Enter Name: ")
‎        a = input("Enter Position: ")
‎
‎        # Validate Hourly Rate
‎        while True:
‎            try:
‎                m = float(input("Enter Hourly Rate: "))
‎                if m < 0:
‎                    print("Error: Hourly Rate cannot be negative. Please enter a positive number.")
‎                else:
‎                    break
‎            except ValueError:
‎                print("Error: Please enter a valid number for Hourly Rate.")
‎
‎        while True:
‎            try:
‎                e = float(input("Enter Hours Worked: "))
‎                if e < 0:
‎                    print("Error: Hours Worked cannot be negative. Please enter a positive number.")
‎                else:
‎                    break
‎            except ValueError:
‎                print("Error: Please enter a valid number for Hours Worked.")
‎
‎        sal = m * e
‎
‎        ploy = {
‎            "ID": ID,
‎            "Name": n,
‎            "Position": a,
‎            "Rate": m,
‎            "Hours Worked": e,
‎            "Salary": sal,
‎        }
‎
‎        Emp.append(ploy)
‎        print(f"\nEmployee {n} added successfully!")
‎
‎    elif cho == "2":
‎        print("\n=== Employee List ===")
‎        if len(Emp) == 0:
‎            print("No employees found.")
‎        else:
‎            for pos in Emp:
‎                print("\n-------------------------------------")
‎                print(f"Employee ID: {pos['ID']}")
‎                print(f"Name: {pos['Name']}")
‎                print(f"Position: {pos['Position']}")
‎                print(f"Hourly Rate: {pos['Rate']:.2f}")
‎                print(f"Hours Worked: {pos['Hours Worked']}")
‎                print(f"Total Salary: {pos['Salary']:.2f}")
‎
‎    elif cho == "3":
‎        print("\n==== Search Employee ====")
‎        try:
‎            search = int(input("Enter Employee ID: "))
‎        except ValueError:
‎            print("Error: Please enter a valid numeric ID.")
‎            continue
‎
‎        found = False
‎
‎        for pos in Emp:
‎            if pos["ID"] == search:
‎                print("\nEmployee Found!\n")
‎                print(f"Employee ID: {pos['ID']}")
‎                print(f"Name: {pos['Name']}")
‎                print(f"Position: {pos['Position']}")
‎                print(f"Hourly Rate: {pos['Rate']:.2f}")
‎                print(f"Hours Worked: {pos['Hours Worked']}")
‎                print(f"Total Salary: {pos['Salary']:.2f}")
‎                found = True
‎                break
‎
‎        if not found:
‎            print("Employee not found.")
‎
‎    elif cho == "4":
‎        print("\nGoodbye!")
‎        break
‎
‎    else:
‎        print("\nInvalid Choice.")
import csv
from Employee import Employee


class EmployeeManager:
    
      def load_from_csv(self,filename="employees.csv"):
            try:
                with open(filename, "r", newline="") as file:
                    reader = csv.reader(file)
                    next(reader)  # Skip header row

                    for row in reader:
                        # Create employee objects from the data in CSV
                        id, name, phone, address, email, position, salary = row
                        new_employee = Employee(int(id), name, phone, address, email, position, float(salary))
                        self.employees.append(new_employee)

            except FileNotFoundError:
                    print(f"The file {filename} was not found. Starting with an empty list of employees.")
            except Exception as e:
                    print(f"An error occurred while loading the data from CSV: {e}")       


      def __init__(self):

            self.employees=[]
            self.load_from_csv() 

      def Add_Employee(self):

            #first take employee data
            try:
                  Id=int(input("enter employee id: "))  
                  Name=input("enter employee name: ")
                  Phone=input("enter employee phone: ")
                  Email=input("enter employee email: ")       
                  Address=input("enter employee address: ")
                  Position=input("enter employee position: ")
                  Salary=float(input("enter employee salary: "))

                  #make a new object after taking employee data to make new employee 
                  new_employee=Employee(Id,Name,Phone,Address,Email,Position,Salary)

                  #add the new employee to employees list
                  self.employees.append(new_employee)
                  self.save_to_csv(mode="a")

                  print(f"Employee {new_employee.Name} has been added successfully!")
            except ValueError as ve:

                 print("Invalid input! Please ensure numeric values for ID and Salary.")

            except Exception as e:

                  print(f"An unexpected error occurred: {e}")      

      def List_employees(self):

            #check if list is empty
            if not self.employees:
                  print("no employees found")

            else:
                  for emp in self.employees:
                        print (emp)     


      def save_to_csv(self):
            try:
                  with open("employees.csv",mode="a", newline="") as file:

                        writer=csv.writer(file)        
                        #write file  headers
                        if file.tell() == 0: 
                         writer.writerow(["ID", "Name", "Phone", "Address", "Email", "Position", "Salary"])
                        #write each item in list as a row in the csv file
                        for emp in self.employees:
                              writer.writerow([emp.Id,emp.Name,emp.Phone,emp.Address,emp.Email,emp.Position,emp.Salary]) 
                  print("Data saved successfully to employees.csv.")

            except Exception as e:
                 print(f"An error occurred while saving to csv file: {e}")

      def Delete_Employee(self):
            try:
                emp_id=int(input("Enter the employee id you want to delete: "))
                
                #default value 
                deleted_emp=None

                for emp in self.employees:
                    if emp.Id==emp_id:
                        deleted_emp=emp
                        break

                if deleted_emp:
                    self.employees.remove(deleted_emp)    
                    print(f"Employee {deleted_emp.Name} has been deleted successfully!")

                # Update the CSV after delete employee 
                    self.save_to_csv(mode="w")

                else:
                   print("Employee with the given ID not found.")
                   

            except ValueError:
                print("Invalid input! Please enter a valid employee ID.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

      def Search_Employee(self):
            try:
                emp_id=int(input("Enter the employee id you want to delete: "))
                
                #default value 
                found_emp=None

                for emp in self.employees:
                    if emp.Id==emp_id:
                        found_emp=emp
                        break

                if found_emp:
                    print("Employee found!")
                    print(found_employee)

                else:
                   print("Employee with the given ID not found.")
                   

            except ValueError:
                print("Invalid input! Please enter a valid employee ID.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")        
    
      def Update_Employee(self):
            try:
                emp_id=int(input("Enter the employee id you want to update: "))
                
                #default value 
                updated_emp=None

                for emp in self.employees:
                    if emp.Id==emp_id:
                        updated_emp=emp
                        break

                if updated_emp:
                    print(f"Current details of {updated_emp.Name}:")
                    print(updated_emp)

                    new_name = input(f"Enter new name or press enter to keep : ")
                    if new_name:
                        updated_emp.Name = new_name
                    
                    new_phone = input(f"Enter new phone or press enter to keep: ")
                    if new_phone:
                        updated_emp.Phone = new_phone
                    
                    new_email = input(f"Enter new email or press enter to keep: ")
                    if new_email:
                        updated_emp.Email = new_email
                    
                    new_address = input(f"Enter new address or press enter to keep: ")
                    if new_address:
                        updated_emp.Address = new_address
                    
                    new_position = input(f"Enter new position or press enter to keep: ")
                    if new_position:
                        updated_emp.Position = new_position
                    
                    new_salary = input(f"Enter new salary or press enter to keep: ")
                    if new_salary:
                        updated_emp.Salary = float(new_salary)

                    print(f"Employee {updated_emp.Name}'s details have been updated!")

                    # Update the CSV after modifying employee data
                    self.save_to_csv(mode="w")  


                else:
                   print("Employee with the given ID not found.")
                   

            except ValueError:
                print("Invalid input! Please enter a valid employee ID.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")        
    

     
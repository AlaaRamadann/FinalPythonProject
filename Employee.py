class Employee:

    def __init__(self,Id,Name,Phone,Address,Email,Position,Salary):

            self.Id=Id
            self.Name=Name
            self.Phone=Phone
            self.Address=Address
            self.Email=Email
            self.Position=Position
            self.Salary=Salary

   #function to display data for employee when print it
    def __str__(self):

     return (f"ID: {self.Id}, Name: {self.Name}, Phone: {self.Phone}, Email: {self.Email}\n"
             f"Address: {self.Address}, Position: {self.Position}, Salary: {self.Salary}")
        



  
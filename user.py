class User:
     

    def __init__(self,first_name, last_name, email,password):
       
        self.firstname = first_name
        self.email = email
        self.last_name=last_name
        self.password=password
        

    def get_password(self):
        return self.password
    
    def get_email(self):
        return self.email  
    
    def get_first_name(self):
        return self.firstname 
    
    def get_last_name(self):
        return self.last_name

    
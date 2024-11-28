class Person():
    
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone
    
    def send_message(self,message):
        
        return f"Hello  {self.name} here is a message for you {message}"
    
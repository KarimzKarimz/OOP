from .users import User

class TM(User):
    def __init__(self, name, email, phone, work_email):
        super().__init__(name, email, phone)
        self.work_email = work_email
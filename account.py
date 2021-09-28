import uuid
class Account:
    def __init__(self,id:uuid,number:int, name:str):
        self.id=id
        self.number=number
        self.name=name
    def __str__(self):
        return f"""
        ID: {self.id}
        Account number: {self.number}
        Name: {self.name}
        """
import uuid
import datetime
class Transaction:
    def __init__(self,id:uuid,accountid:uuid, amount:float, note:str, date:datetime):
        self.id=id
        self.accountid=accountid
        self.amount=amount
        self.note=note
        self.date=date
    def __str__(self):
        return f"""
        ID: {self.id}
        Account ID: {self.accountid}
        Amount: {self.amount}
        Note: {self.note}
        Date: {self.date}
        """    

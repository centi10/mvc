import requests
import random

class Connector:
    
    def __init__(self, BASE_URL):
        self.BASE_URL = BASE_URL
        
    def getBalance(self):
        try:
            response = requests.get(self.BASE_URL+'/balance')
            balance = response.json()
        except requests.exceptions.JSONDecodeError:
            print("Server Access Error")
            return '%.2f'%random.randint(0,200000)
        except Exception:
            print('Something went wrong')
            return '%.2f'%random.randint(0,200000)
        return '%.2f'%balance
    
    """
    type is either 'income' or 'expense' string
    """
    def saveExpense(self, amount, type):
        url = self.BASE_URL + '/'+type
        try:
            data = {
                "amount":amount
            }
            response = requests.post(url=url, json=data)
        except requests.exceptions.ConnectionError:
            print("Server Access Error")
            return requests.codes["bad_request"]
        else:
            """
            if status_code is 400 then server accessed with wrong data, 
            if the status_code is 405 then the request method is not allowed. 
            if the status_code is 200 then the transaction is success.
            """
            return response
        
    def dropAllData(self):
        url = self.BASE_URL + '/'+'dropdata'
        try:
            response = requests.post(url=url)
        except requests.exceptions.ConnectionError:
            print('Server Access Error')
            return 404
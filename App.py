#App.py is the View of MVC
import sys
from controller.connector import Connector
        
connector = Connector("http://127.0.0.1:5000")

print('\nEnter ctrl+C to close the program')
# connector.dropAllData()

while True:
    try:
        option = int(input('1: Save Income Amount\n2: Save Expense Amount\n3: Get Balance Amount\nChoose an option with integer(1/2/3): '))
    except ValueError:
        print('Only Integer values are permitted\n')
        continue
    except KeyboardInterrupt:
        sys.exit('\nExiting the program...\n')
    except Exception as e:
        print(str(e))
        continue
    else:
        if option==1:
            try:
                amount = float(input("Enter valid transaction amount: "))
            except ValueError:
                print("Enter a valid amount.")
            except KeyboardInterrupt:
                sys.exit('\nExiting the program...\n')
            except Exception as e:
                print(str(e))
                continue
            else:
                type='income'
                
        elif option==2:
            try:
                amount = float(input("Enter valid transaction amount: "))
            except ValueError:
                print("Enter a valid amount.")
            except KeyboardInterrupt:
                sys.exit('\nExiting the program...\n')
            except Exception as e:
                print(str(e))
                continue
            else:
                type='expense'
                
        elif option==3:
            print('\nBalance amount: RS.'+connector.getBalance()+'\n')
            continue
        
        else:
            print('Choose a valid option\n')
            type=''
            
        if type=='income' or type=='expense':
            res = connector.saveExpense(amount, type)
            if(res.status_code == 200):
                print("Transaction "+str(res.text)+ " is successfully saved.\n")
            else:
                print("Transaction failed.\n")
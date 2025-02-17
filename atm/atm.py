class ATM :
    def __init__(self,pin,balance = 0) :
      self.pin = pin
      self.balance =float( balance )  # Ensure balance is stored as a float

    def authenticate(self) :
      attempts = 3
      while attempts > 0 :
         entered_pin = input('Enter your 4 digit PIN : ')
         if entered_pin == self.pin:
            print('Authentication successful')
            return True
         else:
           attempts -= 1
           print(f'Incorrect PIN . Attempts left : {attempts}')
           print('Too many incorrect attempts! Exiting...')
      return False
    def check_balance (self) :
       print(f'Your current balance is : {self.balance}')

    def withdraw(self):
      try:
        amount =float(input('Enter amount to withdraw :')) 
        if amount > self.balance :
          print('Insufficient balance!')
        elif amount > 0 and amount < self.balance:
           self.balance -= amount
           print(f'{amount:.2f} withdraw successfully! Your new balance is : {self.balance:.2f}')  
        else:
          print('Invalid amount ! Enter a valid amount : ')
      except ValueError:
        print('Invalid input! Please enter numeric value : ')        

    def deposit(self):
        amount = float(input('Enter amount to  deposit : '))
        if amount <=0 :
           print('Invalid amount! Enter a valid amount')
        else :
           self.balance += amount
           print(f'{amount} deposited successfully Your new balance is {self.balance}')
    def start(self) :
       if self.authenticate() :
          while True :
             print('1. Check Balance')
             print('2. Withdraw Money')
             print('3.deposit Money')
             print('4. Exit')
             choice = input('Enter your choice : ')

             if choice == '1':
                self.check_balance()
             elif choice == '2':
                self.withdraw()
             elif choice == '3' :
                self.deposit()
             elif choice  == '4':
                print('Thank You for using the ATM. Have a great day')
                break
             else:
                print('Invalid Choice')

# Initialize the ATM with a predefined PIN('1234') and starting balance Rs:5000
atm = ATM(pin = '1234' , balance = '5000')
atm.start()                   

                               
   


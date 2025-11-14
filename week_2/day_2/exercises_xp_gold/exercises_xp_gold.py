class BankAccount:
    def __init__(self, balance, username, password, authenticated = False):
        self.balance = balance
        self.username = username
        self.passwrd = password
        self.authenticated = authenticated

    def authenticate(self, password):
        if self.passwrd == password:
            self.authenticated = True
            return True
        else:
            return False

    def deposit(self, amount):
        if self.authenticated:
            amount = int(amount)
            if amount <= 0:
                raise Exception('Amount must be a positive integer!')
            self.balance += amount
        else:
            raise Exception('Not authorized!')

    def withdraw(self, amount):
        if self.authenticated:
            amount = int(amount)
            if amount <= 0:
                raise Exception('Amount must be a positive integer!')
            self.balance -= amount
        else:
            raise Exception('Not authorized!')

class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance, username, password, authenticated, minimum_balance = 0):
        super().__init__(balance, username, password, authenticated)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.authenticated:
            amount = int(amount)
            if amount <= 0:
                raise Exception('Amount must be a positive integer!')
            if self.balance - amount < self.minimum_balance:
                raise Exception('Can\'t withdraw! Minimum balance reached.')
            self.balance -= amount
        else:
            raise Exception('Not authorized!')
        
class ATM:
    def __init__(self, account_list, try_limit):
        self.account_list = []
        for account in account_list:
            if isinstance(account, BankAccount):
                self.account_list.append(account)
        try:
            try_limit = int(try_limit)
            self.try_limit = try_limit
            if try_limit < 1:
                raise Exception('Try limit must be a positive integer!')
        except:
            self.try_limit = 2
        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        print('Select action:')
        while self.current_tries < self.try_limit:
            action = input("""
                Login (input 1)
                Exit (input 0)
            """)
            if action == '0':
                break
            elif action == '1':
                username = input('Username: ')
                password = input('Password: ')
                (auth, account) = self.log_in(username, password)
                self.current_tries += 1
                if not auth and self.current_tries >= self.try_limit:
                    print('Max attempts reached! Exiting...')
                    break
                elif auth:
                    self.show_account_menu(account)
                else:
                    continue
            else:
                print('Invalid input! Exiting...')
                break
        self.current_tries = 0

    def log_in(self, username, password):
        auth = False
        account = None
        for account in self.account_list:
            if account.username == username:
                auth = account.authenticate(password)
                account = account
        return (auth, account)
    
    def show_account_menu(self, account):
        print(f'Hello {account.username}')
        while True:
            action = input("""
                Deposit (input 1)
                Withdraw (input 2)
                Exit (input 0)
            """)
            if action == '0':
                self.authenticated = False
                break
            elif action == '1' or action == '2':
                try:
                    amount = input('Give amount! ')
                    if action == '1':
                        account.deposit(amount)
                    else:
                        account.withdraw(amount)
                except:
                    print('Invalid input!')
            else:
                print('Invalid input! Exiting...')
                break

acc1 = BankAccount(balance=1000, username='alice', password='1234')
acc2 = MinimumBalanceAccount(balance=500, username='bob', password='abcd', authenticated=False, minimum_balance=100)

atm = ATM([acc1, acc2], '3')
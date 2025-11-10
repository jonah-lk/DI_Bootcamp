class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []
    
    def call(self, other_phone, outgoing = False):
        print(f'{other_phone.phone_number} call! {'Outgoing' if outgoing else 'Incoming'}')
        self.call_history.append({
                'phone_number': other_phone.phone_number,
                'outgoing': outgoing
            })

    def show_call_history(self):
        for entry in self.call_history:
            print(f'Call: {entry['phone_number']} {'Outgoing' if entry['outgoing'] else 'Incoming'}')

    def send_messages(self, other_phone, message, outgoing = False):
        print(f'A new message: {other_phone.phone_number} {'Outgoing' if outgoing else 'Incoming'}')
        self.messages.append({
            'to': self.phone_number if outgoing else other_phone.phone_number,
            'from': other_phone.phone_number if outgoing else self.phone_number,
            'content': message
        })

    def show_outgoing_messages(self):
        for message in self.messages:
            if message['from'] == self.phone_number:
                print(f'You sent this message "{message['content']}" to {message['to']}')
        
    def show_incoming_messages(self):
        for message in self.messages:
            if message['to'] == self.phone_number:
                print(f'You have received this message "{message['content']}" from {message['from']}')

    def show_messages_from(self, other_phone):
        for message in self.messages:
            if message['from'] == other_phone.phone_number:
                print(f'You have received this message "{message['content']}" from {other_phone.phone_number}')

my_phone = Phone('0699999999')
other_phone = Phone('0612345678')
my_phone.call(other_phone, True)
my_phone.call(other_phone, False)
my_phone.show_call_history()
my_phone.send_messages(other_phone, 'Hello world!', True)
my_phone.send_messages(other_phone, 'Hello world x2!', False)
my_phone.show_outgoing_messages()
my_phone.show_incoming_messages()
my_phone.show_messages_from(other_phone)
print(vars(my_phone).items())
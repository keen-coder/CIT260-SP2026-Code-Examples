class Notification:
    def __init__(self, message):
        self.__message = message

    def get_message(self):
        return self.__message
    
    def send(self):
        print(f"Sending notification: {self.__message}")

    def __repr__(self):
        return f'Notification(message={repr(self.__message)})'
    
class EmailNotification:
    pass

class SMSNotification:
    pass

def main():
    pass

if __name__ == '__main__':
    main()
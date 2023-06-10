from abc import ABC, abstractmethod

#Abstraction
class MessageSender(ABC):

    @abstractmethod
    def send(self, message):
        pass

class EmailSender(ABC):

    def __init__(self, email, smtp) -> None:
        pass
    
    def send(self, message):
        pass

class SmsSender(ABC):

    def __init__(self, number) -> None:
        pass
    
    def send(self, message):
        pass

class Notifier:

    def __init__(self, sender: MessageSender) -> None:
        self.sender = sender

    def send(self, message):
        self.sender.send(message)

# class Notifier:

#     def __init__(self, sender) -> None:
#         self.sender = sender

#     def send_notification(self, message):
#         if isinstance(self.sender, EmailSender):
#             self.sender.send(message, "email", "smtp")
#         if isinstance(self.sender, SmsSender):
#             self.sender.send(message, "number")

# class EmailSender:

#     def send(self, message, email, smtp):
#         print(f"sending email - {message}")

# class SmsSender:

#     def send(self, message, phone_number):
#         print(f"sending sms - {message}")
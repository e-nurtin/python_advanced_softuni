from abc import ABC, abstractmethod


class IReceiver(ABC):
	def __init__(self, receiver):
		self.receiver = receiver
	
	@abstractmethod
	def receiver(self):
		return


class Receiver(IReceiver):
	def receiver(self):
		return ''.join(["I'm ", self.receiver()])


class ISender(ABC):
	def __init__(self, sender):
		self.sender = sender
	
	@abstractmethod
	def send_msg(self):
		pass


class Sender(ISender):
	def send_msg(self):
		return ''.join(["I'm ", self.sender])


class IContent(ABC):
	def __init__(self, text):
		self.text = text
	
	@abstractmethod
	def format(self):
		pass


class MyContent(IContent):
	def format(self):
		return '\n'.join(['<myML>', self.text, '</myML>'])


class HTMLContent(IContent):
	def format(self):
		return '\n'.join(['<html>', self.text, '</html>'])


class IEmail(ABC):
	
	@abstractmethod
	def set_sender(self, sender):
		pass
	
	@abstractmethod
	def set_receiver(self, receiver):
		pass
	
	@abstractmethod
	def set_content(self, content):
		pass


class Email(IEmail):
	
	def __init__(self, protocol):
		self.protocol = protocol
		self.__sender = None
		self.__receiver = None
		self.__content = None
	
	def set_sender(self, sender):
		self.__sender = sender.send_msg()
	
	def set_receiver(self, receiver):
		self.__receiver = receiver
	
	def set_content(self, content):
		self.__content = content.format()
	
	def __repr__(self):
		template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"
		
		return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


email = Email('IM')
sender = Sender('qmal')
email.set_sender(sender)
receiver_ = IReceiver
email.set_receiver('james')
content = MyContent('Hello, there!')
html_content = HTMLContent('Hello, there!')
email.set_content(content)
email.set_content(html_content)
print(email)

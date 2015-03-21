import socket 
import random


class Connection():

	def __init__(self, bot):
		self.server = bot.server
		self.channel = bot.channel
		self.botnick = bot.botnick


	def find(self, target, text):
		if text.find(target) != -1:
			return True
		else:
			return False

	def ping(self):
		ircsock.send("PONG :pingis\n")

	def sendmsg(self, msg):
		ircsock.send("PRIVMSG " + self.channel + " :" + msg + "\n")

	def joinchan(self, chan):
		ircsock.send("JOIN " + chan + "\n")

	def connect(self):
		global ircsock
		ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		ircsock.connect((self.server, 6667))
		ircsock.send("USER " + self.botnick + " " + self.botnick + " " + self.botnick + " :This is gonna be a chatbot.\n")
		ircsock.send("NICK " + self.botnick + "\n")

		self.joinchan(self.channel)

	def parse_message(self, ircmsg):
		if len(ircmsg.split(":")) <= 3:
			try:
				message = ircmsg.split(":")[2]
			except IndexError:
				message = []
		else:
			message = ircmsg.split(":")[2:len(ircmsg.split(":"))]

		# checking to see if the message is a list, which occurs if there were colons in the message #
		if type(message) == type([1]):
			message = ":".join(message)
		try:
			sender = ircmsg.split(":")[1].split("!")[0]
		except IndexError:
			sender = "None"
		print("sender: " + sender)
		print("message: " + message)


	def receive(self):
		ircmsg = ircsock.recv(2048)
		ircmsg = ircmsg.strip("\n\r")
		print(ircmsg)
		if ircmsg.find(" PRIVMSG ") != -1:
			nick = ircmsg.split("!")[0][1:]
			channel = ircmsg.split(" PRIVMSG ")[-1].split(" :")[0]

		if ircmsg.find("PING: ") != -1:
			ping()
		self.parse_message(ircmsg)
		return ircmsg



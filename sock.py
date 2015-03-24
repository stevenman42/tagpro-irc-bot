import socket 
import random


class Connection():

	def __init__(self, bot):
		self.server = bot.server
		self.channel = bot.channel
		self.botnick = bot.botnick
		self.port = bot.port
		self.ircsock = None

	def find(self, target, text):
		if text.find(target) != -1:
			return True
		else:
			return False

	def ping(self):
		self.ircsock.send("PONG :pingis\n")

	def sendmsg(self, msg, channel):
		self.ircsock.send("PRIVMSG " + channel + " :" + msg + "\n")

	def joinchan(self, **kwargs):

		channel = kwargs["channel"]

		try:
			if not channel:
				print("not channel")
				channel = self.channel
		except UnboundLocalError:
			channel = self.channel

		print(channel)

		self.ircsock.send("JOIN " + channel + "\n")

	def connect(self):


		self.ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.ircsock.connect((self.server, self.port))
		self.ircsock.send("USER " + self.botnick + " " + self.botnick + " " + self.botnick + " :This is gonna be a chatbot.\n")
		self.ircsock.send("NICK " + self.botnick + "\n")


		self.joinchan(channel = self.channel)

	def parse_message(self, ircmsg):
		parsed_message = [None, None, None, None]

		if len(ircmsg.split(":")) <= 3:
			try:
				message = ircmsg.split(":")[2]
				channel = "#" + ircmsg.split(":")[1].split("#")[1]
			except IndexError:
				message = []
				channel = ""
		else:
			message = ircmsg.split(":")[2:len(ircmsg.split(":"))]
			channel = ""



		# checking to see if the message is a list, which occurs if there were colons in the message #
		if type(message) == type([1]):
			message = ":".join(message)
		try:
			sender = ircmsg.split(":")[1].split("!")[0]
		except IndexError:
			sender = None


		if sender:
			parsed_message[0] = sender
			parsed_message[1] = message
			parsed_message[2] = channel
			if "PRIVMSG" in ircmsg:
				parsed_message[3] = "PRIVMSG"
		return parsed_message

	def receive(self):
		ircmsg = self.ircsock.recv(2048)
		ircmsg = ircmsg.strip("\n\r")
		if len(ircmsg) > 1:
			# print(ircmsg)
			pass
		if ircmsg.find(" PRIVMSG ") != -1:
			nick = ircmsg.split("!")[0][1:]
			channel = ircmsg.split(" PRIVMSG ")[-1].split(" :")[0]

		if ircmsg.find("PING") != -1:
			self.ping()
		msg = self.parse_message(ircmsg)
		return msg



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

	def commands(self, nick, channel, message):

		if find("hello", message):
			sendmsg("Hi.")

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

	def receive(self):
		ircmsg = ircsock.recv(2048)
		ircmsg = ircmsg.strip("\n\r")
		print(ircmsg)
		if ircmsg.find(" PRIVMSG ") != -1:
			nick = ircmsg.split("!")[0][1:]
			channel = ircmsg.split(" PRIVMSG ")[-1].split(" :")[0]
			commands(nick, channel, ircmsg)

		if ircmsg.find("PING: ") != -1:
			ping()



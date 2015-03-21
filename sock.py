import socket 
import random



def find(target, text):
	if text.find(target) != -1:
		return True
	else:
		return False

def commands(nick, channel, message):

	if message.find(botnick+": shellium") != -1:
		ircsock.send("PRIVMSG %s :%s: shellium is not too shabby.\r\n" % (channel, nick))

	if find("hello", message):
		sendmsg("Hi.")

def ping():
	ircsock.send("PONG :pingis\n")

def sendmsg(msg):
	ircsock.send("PRIVMSG " + channel + " :" + msg + "\n")

def joinchan(chan):
	ircsock.send("JOIN " + chan + "\n")

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667))
ircsock.send("USER " + botnick + " " + botnick + " " + botnick + " :This is gonna be a chatbot.\n")
ircsock.send("NICK " + botnick + "\n")

joinchan(channel)

while 1:
	ircmsg = ircsock.recv(2048)
	ircmsg = ircmsg.strip("\n\r")
	print(ircmsg)
	if ircmsg.find(" PRIVMSG ") != -1:
		nick = ircmsg.split("!")[0][1:]
		channel = ircmsg.split(" PRIVMSG ")[-1].split(" :")[0]
		commands(nick, channel, ircmsg)

	if ircmsg.find("PING: ") != -1:
		ping()

	print("hue")
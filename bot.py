# -*- coding: utf-8 -*-

import random

class Bot:
	"""The basic bot class"""

	def __init__(self, server, channel, botnick, port):
		self.server = server
		self.channel = channel
		self.botnick = botnick
		self.port = port

		self.sender = ""
		self.last_sender = ""
		self.last_last_sender = ""


	def respond(self, connection, parsed_message):

		try:
			self.last_last_sender = self.last_sender
		except UnboundLocalError:
			print("I guess I don't have a last_sender yet")
			self.last_last_sender = ""

		try:
			self.last_sender = self.sender
		except UnboundLocalError:
			print("I guess I don't have a sender yet either")
			self.last_sender = ""

		print("last_sender: " + self.last_sender)
		print("last_last_sender: " + self.last_last_sender)

		self.sender = parsed_message[0]

		message = parsed_message[1]
		channel = parsed_message[2]
		msgtype = parsed_message[3]

		def send(message):
			connection.sendmsg(message, channel)

		if message == "hi " + self.botnick:
			send("huehue")

		if message == "spam":
			send("spam")


		if message == "-yiss":
			yiss = random.randint(0,6)
			if yiss == 0:
				send("ᕕ(ᐛ)ᕗ aww yiss ᕕ(ᐛ)ᕗ")
			elif yiss == 1:
				send("(ღ˘⌣˘ღ) aww yissss (ღ˘⌣˘ღ)")
			elif yiss == 2:
				send( "✧ﾟ･:*ヽ(◕ヮ◕ヽ)  yiss  (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
			elif yiss == 3:
				send("ヽ(‘ ∇‘ )ノ  yiss  ヽ(‘ ∇‘ )ノ")
			elif yiss == 4:
				send("(ﾟヮﾟ)  yiss  (ﾟヮﾟ)")
			elif yiss == 5:
				send("◕ ◡ ◕  yiss  ◕ ◡ ◕")
			elif yiss == 6:
				send("ヽ(ﾟｰﾟ*ヽ) all hail yiss (ﾉ*ﾟｰﾟ)ﾉ")

		elif "-join " in message:
			channel_to_join = message.replace("-join ", "")
			connection.joinchan(channel=channel_to_join) 


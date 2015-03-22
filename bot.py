# -*- coding: utf-8 -*-

import random

class Bot:
	"""The basic bot class"""

	def __init__(self, server, channel, botnick, port):
		self.server = server
		self.channel = channel
		self.botnick = botnick
		self.port = port

	def respond(self, connection, parsed_message):
		sender = parsed_message[0]
		message = parsed_message[1]
		channel = parsed_message[2]
		msgtype = parsed_message[3]

		if message == "hi " + self.botnick:
			connection.sendmsg("huehue")

		if message == "spam":
			connection.sendmsg("spam")


		if message == "-yiss":
			yiss = random.randint(0,6)
			if yiss == 0:
				connection.sendmsg("ᕕ(ᐛ)ᕗ aww yiss ᕕ(ᐛ)ᕗ")
			elif yiss == 1:
				connection.sendmsg("(ღ˘⌣˘ღ) aww yissss (ღ˘⌣˘ღ)")
			elif yiss == 2:
				connection.sendmsg( "✧ﾟ･:*ヽ(◕ヮ◕ヽ)  yiss  (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
			elif yiss == 3:
				connection.sendmsg("ヽ(‘ ∇‘ )ノ  yiss  ヽ(‘ ∇‘ )ノ")
			elif yiss == 4:
				connection.sendmsg("(ﾟヮﾟ)  yiss  (ﾟヮﾟ)")
			elif yiss == 5:
				connection.sendmsg("◕ ◡ ◕  yiss  ◕ ◡ ◕")
			elif yiss == 6:
				connection.sendmsg("ヽ(ﾟｰﾟ*ヽ) all hail yiss (ﾉ*ﾟｰﾟ)ﾉ")

		elif "-join " in message:
			channel_to_join = message.replace("-join ", "")
			connection.connect(channel=channel_to_join) 


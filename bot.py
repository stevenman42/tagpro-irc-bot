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

		self.afk_counter_is_on = False
		self.afk_list = []

		self.response_dict = {"hi " + self.botnick: "hi " + self.last_sender,
								"-yiss": self.yiss_response()
								}

	def yiss_response(self):

		yiss = random.randint(0,6)
		if yiss == 0:
			return ("ᕕ(ᐛ)ᕗ aww yiss ᕕ(ᐛ)ᕗ")
		elif yiss == 1:
			return ("(ღ˘⌣˘ღ) aww yissss (ღ˘⌣˘ღ)")
		elif yiss == 2:
			return ( "✧ﾟ･:*ヽ(◕ヮ◕ヽ)  yiss  (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
		elif yiss == 3:
			return ("ヽ(‘ ∇‘ )ノ  yiss  ヽ(‘ ∇‘ )ノ")
		elif yiss == 4:
			return ("(ﾟヮﾟ)  yiss  (ﾟヮﾟ)")
		elif yiss == 5:
			return ("◕ ◡ ◕  yiss  ◕ ◡ ◕")
		elif yiss == 6:
			return ("ヽ(ﾟｰﾟ*ヽ) all hail yiss (ﾉ*ﾟｰﾟ)ﾉ")





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

		# print("last_sender: " + self.last_sender)
		# print("last_last_sender: " + self.last_last_sender)

		sender = parsed_message[0]

		message = parsed_message[1]
		channel = parsed_message[2]
		msgtype = parsed_message[3]

		try:
			print (sender + ": " + message)
		except TypeError:
			message = ""

		def send(message):
			connection.sendmsg(message, channel)

		def verify_nick(nick):
			if nick in ['defense_bot', 'events']:
				return True
			return False



		# === Settings === #

		if message == "-counter: on" and verify_nick(sender):
			self.afk_counter_is_on = True
			print("turned the counter on")

		if message == "-counter: off" and verify_nick(sender):
			self.afk_counter_is_on = False


		# === End Settings === #

		for name in self.afk_list:
			if name in message:
				send(name + " is afk right now, " + sender)
			if name == sender:
				print("I removed " + name)
				self.afk_list.remove(name)
				send("Welcome back, " + sender)


		if message == "-afk" and self.afk_counter_is_on:
			self.afk_list.append(sender)
			print("I just added " + sender)

		if message in self.response_dict.keys():
			send(self.response_dict[message])





		elif "-join " in message:
			channel_to_join = message.replace("-join ", "")
			connection.joinchan(channel=channel_to_join) 


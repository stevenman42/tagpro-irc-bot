

class Bot:
	"""The basic bot class"""

	def __init__(self, server, channel, botnick, port):
		self.server = server
		self.channel = channel
		self.botnick = botnick
		self.port = port

	def respond(self, parsed_message):
		sender = parsed_message[0]
		message = parsed_message[1]
		channel = parsed_message[2]
		msgtype = parsed_message[3]

		


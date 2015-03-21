

class Bot:
	"""The basic bot class"""

	def __init__(self, server, channel, botnick, port):
		self.server = server
		self.channel = channel
		self.botnick = botnick
		self.port = port
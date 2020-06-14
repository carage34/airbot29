
from irc.bot import SingleServerIRCBot
from requests import get

NAME = "enormesaixe"
OWNER = "air_one29"


class Bot(SingleServerIRCBot):
	def __init__(self):
		self.HOST = "irc.chat.twitch.tv"
		self.PORT = 6667
		self.USERNAME = NAME.lower()
		self.CLIENT_ID = "1utxz63kdn8vmccch4stxn3payttdi"
		self.TOKEN = "ykn6sl6p8kgc0dcjawjpvyjis0vkr9"
		self.CHANNEL = f"#{OWNER}"

		super().__init__([(self.HOST, self.PORT, f"oauth:{self.TOKEN}")], self.USERNAME, self.USERNAME)

	def on_welcome(self, cxn, event):
		for req in ("membership", "tags", "commands"):
			cxn.cap("REQ", f":twitch.tv/{req}")
		cxn.join(self.CHANNEL)
		self.send_message("Now online.")

	def on_pubmsg(self, cxn, event):
		tags = {kvpair["key"]: kvpair["value"] for kvpair in event.tags}
		user = {"name": tags["display-name"], "id": tags["user-id"]}
		message = event.arguments[0]
		print(f"Message from {user['name']}: {message}")

	def send_message(self, message):
		self.connection.privmsg(self.CHANNEL, message)


if __name__ == "__main__":
	bot = Bot()
	bot.start()
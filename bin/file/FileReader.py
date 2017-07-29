def get_bot_settings():
	with open("settings.txt") as f:
		content = f.read().splitlines()
		return content

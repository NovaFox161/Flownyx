from bin.cmds import BotsCommand, HelpCommand


def handle_command(message, client):
	from bin.cmds import FlowCommand

	if message.content.startswith("~"):
		# has correct prefix... test command

		commandRaw = message.content[1:len(message.content)]

		argsRaw = commandRaw.split(" ")

		commandName = argsRaw[0].lower()
		args = argsRaw[1:len(argsRaw) - 1]

		if commandName == "flow":
			FlowCommand.run_command(message, client)
		elif commandName == "bots":
			BotsCommand.run_command(message, client)
		elif commandName == "help":
			HelpCommand.run_command(message, client)

	return True

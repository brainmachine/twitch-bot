
from OSC import OSCServer, OSCClient, OSCMessage
import sys
import types

# Create the OSC Client
client = OSCClient()
client.connect( ("localhost", 9797) )
client.print_tracebacks = False
oscString = "/Twitch/setup"
msg = OSCMessage(oscString.encode("utf-8", "ignore"))
client.send(msg)

def osc(args):
	# TODO: Validate args datatypes
	# args[0] should be string
	# args[1] should be int
	print "received OSC command"
	oscCommand = args[0]
	print(oscCommand)
  	value = int(args[1])
  	print(value)
  	
	usage = '!osc <parameterName> <value>'

	try:
		msg = OSCMessage()
		msg.setAddress('fromTwitch/'+oscCommand)
		msg.append(value)
		client.send(msg)
		return "OSC Message Sent."
	except ValueError:
		return "!osc value error"
	except:
		return usage

osc(["testCommand", 42])

from OSC import OSCServer, OSCClient, OSCMessage
import sys
import types

# Create the OSC Client
client = OSCClient()
client.connect( ("localhost", 9999) )
client.print_tracebacks = False
oscString = "/Twitch/setup"
msg = OSCMessage(oscString.encode("utf-8", "ignore"))
client.send(msg)

def osc(args):
	print "received OSC command"
	oscCommand = args[0]
	print(oscCommand)
  	value = args[1]
  	print(value)
	usage = '!osc <parameterName> <value>'

	try:
		print "trying to broadcast OSC message"
		oscString = '/FromTwitch/'+str(oscCommand)+' '+str(value)
		print(oscString)
		msg = OSCMessage(oscString)
		print(msg)
		client.send(msg)
		return "OSC Message Sent: " + oscString
	except ValueError:
		return "!osc value error"
	except:
		return usage

osc(["testCommand", 42])
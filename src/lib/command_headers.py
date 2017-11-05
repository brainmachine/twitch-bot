from src.config.config import *

commands = {
	'!test': {
		'limit': 3,
		'return': 'This is not a test!'
	},

	'!randomemote': {
		'limit': 180,
		'argc': 0,
		'return': 'command'
	},

	'!wow': {
		'limit': 30,
		'argc': 3,
		'return': 'command'
	}, 
	'!random': {
		'limit': 30,
		'argc': 2,
		'return': 'command'
	},
	'!osc': {
		'limit': 1,
		'argc': 2,
		'return': 'command'
	}
}










for channel in config['channels']:
	for command in commands:
		commands[command][channel] = {}
		commands[command][channel]['last_used'] = 0

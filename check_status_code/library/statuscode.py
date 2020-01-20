#!/usr/bin/python

from ansible.module_utils.basic import *
import requests

def main():
	
	module_args = dict(url=dict(type='str', required=True))
	module = AnsibleModule(argument_spec=module_args,supports_check_mode=True)
	
	x = requests.get(module.params['url'])
	x = x.status_code
	
	response = {"status code": x}
	module.exit_json(changed=False, meta=response)


if __name__ == '__main__':
	main()

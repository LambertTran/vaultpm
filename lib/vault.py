import requests
import logging
import json
import os
from pprint import pprint

logging.getLogger().setLevel(logging.INFO)


class Vault:
	def __init__(self,server):
		self.server = server
		self._unseal_path = "/v1/sys/unseal"
		self._status_path = "/v1/sys/seal-status"
		self._mount_path = "/v1/sys/mounts/"
		self._token = ""
		self._header = {}

	def unseal(self):
		if not self.__isSeal():
			return logging.info("Vault is unseal")
		isSealed = True 
		while isSealed:
			key = input("Please Enter the unseal key: ").strip()
			isSealed = self.__unseal(key)
		print("======== Succesfully Unseal ========")
		return isSealed


	def create_engine(self,name):
		self.__check_vault()
		logging.info("Creating engine name: %s" %name)
		mount_path = self.server + self._mount_path + name
		data = '{"type": "kv"}'
		res = requests.post(mount_path,data=data, headers=self._header)
		return self.__handle_response(res)
		

	def create_key(self,engine,kv_path,key,value):
		self.__check_vault()
		logging.info("Create keys in %s engine" %engine)
		key_path = self.server + "/v1/" + engine + "/apikeys/" + kv_path 
		#data = '{"%s": "%s"}' %(key,value)
		data = json.dumps(dict(zip(key,value)))
		res = requests.post(key_path,data=data, headers=self._header)
		return self.__handle_response(res)
	
			
	def get_key(self,engine,key):
		self.__check_vault()
		key_path = self.server + "/v1/" + engine + "/apikeys/" + key
		res = requests.get(key_path,headers=self._header)
		if (res.status_code not in range(200,300)): 
			return logging.warning(res.text)
		data = res.json()['data']
		result = []
		for key in data:
			result.append([key,data[key]])
		return result
		

    # Private Methods
	def __check_vault(self):
		if self.__isSeal():
			self.unseal()
		self.__get_client_token()


	def __handle_response(self, res):
		if (res.status_code in range(200,300)): 
			logging.info("Done") 
		else:
			logging.warning(res.text)
		return res.status_code


	def __get_client_token(self):
		if 'VAULT_CLIENT_TOKEN' not in os.environ:
			self._token = input("Enter Client Token: ").strip()
		else:
			self._token = os.environ['VAULT_CLIENT_TOKEN']
		self._header = {"X-Vault-Token": self._token } 
		

	def __isSeal(self):
		status_path = self.server + self._status_path
		res = requests.get(status_path)
		return res.json()["sealed"]


	def __unseal(self,key):
		# The data variable below is string, not json or dict
		data ='{"key": "%s" }' %key
		unseal = self.server + self._unseal_path
		res = requests.put(unseal,data)
		if (res.status_code != 200):
			logging.warning(res.text)
			return True # this keep the while loop going
		resData = res.json()
		if (resData['progress'] !=0):
			logging.info('Number of tries: %s/3' %str(resData['progress']))
		return resData['sealed']


#vault = Vault("http://127.0.0.1:8200")
#vault.get_key("qacgov", "key1")
		

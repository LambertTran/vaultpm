

import unittest
import sys

sys.path.append("../lib")

from vault import Vault

DEFAULT_VAULT_ADDR = "http://127.0.0.1:8200"

vault = Vault(DEFAULT_VAULT_ADDR)

class VaultTest(unittest.TestCase):
	def __init__(self,*args, **kwargs):
		super(VaultTest, self).__init__(*args, **kwargs)
		self.engine_name = "test_create_engine"
		self.key_name = "test_key"
		self.k_v = [["key1"],["value1"]]

	def test_create_engine(self):
		resStatus = vault.create_engine(self.engine_name)
		self.assertEqual(resStatus,204)
		
	def test_create_key(self):
		resStatus = vault.create_key(self.engine_name,self.key_name,self.k_v[0],self.k_v[1])
		self.assertEqual(resStatus,204)

	def test_get_key(self):
		resKey = vault.get_key(self.engine_name,self.key_name)[0]
		self.assertEqual(resKey,[self.k_v[0][0],self.k_v[1][0]])

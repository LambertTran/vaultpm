#!/usr/local/bin/python3
import os
import sys
sys.path.append('/opt/lb/vaultpm/lib')
from vault import Vault
import argparse


vault_addr = os.environ['VAULT_ADDR'] if 'VAULT_ADDR' in os.environ else "http://127.0.0.1:8200"

parser = argparse.ArgumentParser(description="Vault - Password Manager")
parser.add_argument("command",help="get or create or createengine")
parser.add_argument("--env",required=True,help="dev, qac,.. ")
parser.add_argument("--key",required=False,help="google, aws,..")
parser.add_argument("--kv",nargs="+",required=False,help="key1=value1 key2=value2")
args = parser.parse_args()

vault = Vault(vault_addr)
if args.command == "get":
	vault.get_key(args.env,args.key)
elif args.command == "createengine":
	vault.create_engine(args.env)
elif args.command == "create":
	k = []
	v = []
	for item in args.kv:
		item = item.split("=")
		k.append(item[0])
		v.append(item[1])
	vault.create_key(args.env,args.key,k,v)
elif args.command == "unseal":
	vault.unseal()
else:
	parser.print_help()

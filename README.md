# Vault

## Variables 
```
export token="<authorize_token>"
export engine="<secret_engine_name>"
export key="<key_name>"
```

## Vault CLI
```
+ vault login <token>

+ vault kv list $engine 
  
+ vault kv get $engine/$key 

+ vault secrets enable -path="$engine" kv
```

## Vault APIs
```
create engine:
+ curl \
    -H "X-Vault-Token: $token" \
    -X POST --data '{ "type": "kv" }' \
    http://127.0.0.1:8200/v1/sys/mounts/$engine

v1:
+ curl \
    -H "X-Vault-Token: $token" -X LIST \
    http://127.0.0.1:8200/v1/$engine | jq
+ curl \
    -H "X-Vault-Token: $token"  \
    http://127.0.0.1:8200/v1/$engine/$key | jq
+ curl -H "X-Vault-Token: $token" \
    -X POST --data '{ "<datakey>": "<value>" }' \
    http://127.0.0.1:8200/v1/$engine/<subpath>/<folder>
v2:
+ curl \
    -H "X-Vault-Token: $token" \
            -X GET \
    http://127.0.0.1:8200/v1/$engine/data/$key | jq
    
```

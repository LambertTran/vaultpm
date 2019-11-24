# Vault

## Vault CLI
```
+ vault kv list < secret engine name >
  
+ vault kv get < secret engine name >/< key name >
```

## Vault APIs
```
v1:
+ curl \
    -H "X-Vault-Token: $token" -X LIST \
    http://127.0.0.1:8200/v1/<secret engine name> | jq
+ curl \
    -H "X-Vault-Token: $token"  \
    http://127.0.0.1:8200/v1/<secret engine name>/<keyname>| jq
v2:
+ curl \
    -H "X-Vault-Token: $token" \
            -X GET \
    http://127.0.0.1:8200/v1/test101/data/hello | jq
    
```

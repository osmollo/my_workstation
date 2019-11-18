#!/bin/bash

## FIX DATA PERMISSIONS
echo "[*] Fix permissions for consul data directory..."
sudo chmod 777 _data/consul
docker restart consul
sleep 5
docker restart vault

## CONFIG LOCAL ENV
echo "[*] Config local environment..."
alias vault='docker-compose exec vault vault "$@"'
export VAULT_ADDR=https://127.0.0.1:8200

## INIT VAULT
echo "[*] Init vault..."
# vault init -address=${VAULT_ADDR} > ./_data/keys.txt
curl -k -XPUT -d '{"secret_shares": 10,"secret_threshold": 5}' ${VAULT_ADDR}/v1/sys/init > ./_data/keys.txt
export VAULT_TOKEN=$( cat _data/keys.txt | jq -r .root_token)

## UNSEAL VAULT
echo "[*] Unseal vault..."
echo "{\"key\": \"$(cat _data/keys.txt | jq -r .keys_base64[1])\"}" > /tmp/key1.json
echo "{\"key\": \"$(cat _data/keys.txt | jq -r .keys_base64[2])\"}" > /tmp/key2.json
echo "{\"key\": \"$(cat _data/keys.txt | jq -r .keys_base64[3])\"}" > /tmp/key3.json
curl -k -X PUT -d@/tmp/key1.json ${VAULT_ADDR}/v1/sys/unseal
curl -k -X PUT -d@/tmp/key2.json ${VAULT_ADDR}/v1/sys/unseal
curl -k -X PUT -d@/tmp/key3.json ${VAULT_ADDR}/v1/sys/unseal

## AUTH
echo "[*] Auth..."
vault auth -address=${VAULT_ADDR} ${VAULT_TOKEN}

## CREATE USER
echo "[*] Create user... Remember to change the defaults!!"
vault auth-enable  -address=${VAULT_ADDR} userpass
vault policy-write -address=${VAULT_ADDR} admin ./config/admin.hcl
vault write -address=${VAULT_ADDR} auth/userpass/users/webui password=webui policies=admin

## CREATE BACKUP TOKEN
echo "[*] Create backup token..."
vault token-create -address=${VAULT_ADDR} -display-name="backup_token" | awk '/token/{i++}i==2' | awk '{print "backup_token: " $2}' >> ./_data/keys.txt

## MOUNTS
echo "[*] Creating new mount point..."
vault mounts -address=${VAULT_ADDR}
vault mount  -address=${VAULT_ADDR} -path=assessment -description="Secrets used in the assessment" generic
vault write  -address=${VAULT_ADDR} assessment/server1_ad value1=name value2=pwd

## READ/WRITE
# $ vault write -address=${VAULT_ADDR} secret/api-key value=12345678
# $ vault read -address=${VAULT_ADDR} secret/api-key

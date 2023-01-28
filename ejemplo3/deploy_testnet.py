from contract import MyContract
from pyteal import *
from beaker import *
import os
from dotenv import load_dotenv

from algosdk import mnemonic
from algosdk import account

from algosdk.atomic_transaction_composer import AccountTransactionSigner
from beaker.client import ApplicationClient, Network
from beaker.client.api_providers import AlgoNode

load_dotenv()

PASSPHRASE = os.environ.get("PASSPHRASE")
print(PASSPHRASE)

MyContract().dump("artifacts")

pk_signer = AccountTransactionSigner(mnemonic.to_private_key(PASSPHRASE))
user_address = account.address_from_private_key(pk_signer.private_key)
print(user_address)


app_client = ApplicationClient(
    client = AlgoNode(Network.TestNet).algod(),
    app = MyContract(),
    signer = pk_signer
)


app_id, app_addr, txid = app_client.create()

open("./artifacts/app_id", "w").write(str(app_id))


print(
    f"""Applicación desplegada txid {txid}
    App ID: {app_id}
    Address: {app_addr}
   """
)
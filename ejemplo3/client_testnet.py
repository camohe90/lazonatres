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

text_file = open("./artifacts/app_id", "r")
app_id = int(text_file.read())
text_file.close()

pk_signer = AccountTransactionSigner(mnemonic.to_private_key(PASSPHRASE))


app_client = ApplicationClient(
    client = AlgoNode(Network.TestNet).algod(),
    app = MyContract(),
    app_id = app_id,
    signer = pk_signer
)

result = app_client.call(MyContract.hello, name= "Alejandro")
print(result.return_value)
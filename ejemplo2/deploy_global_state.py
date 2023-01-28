from contract_globa import SaveInfo
from beaker import *

SaveInfo().dump("artifacts")

account = sandbox.get_accounts()[0]

app_client = client.ApplicationClient(
    client = sandbox.get_algod_client(),
    app = SaveInfo(),
    signer = account.signer
)

app_id, app_addr, txid = app_client.create()

open("./artifacts/app_id","w").write(str(app_id))

print(
    f""" Id de la transacción {txid},
    App Id: {app_id}
    address: {app_addr}

"""
)


from pyteal import *
from beaker import *

class MyContract(Application):
    
    @external
    def hello(self, name:abi.String, *, output:abi.String):
        return output.set(Concat(Bytes("Hello World "), name.get()))
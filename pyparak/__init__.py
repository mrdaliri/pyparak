from pay_ir.api.client import PayIrClient


class BaseGateway(object):
    def send(self, *args, **kwargs):
        raise NotImplementedError()

    def verify(self, *args, **kwargs):
        raise NotImplementedError()


class PayIrGateway(BaseGateway):
    def __init__(self, api_key):
        self.client = PayIrClient(api_key)

    def send(self, *args, **kwargs):
        self.client.init_transaction(**kwargs)

    def verify(self, *args, **kwargs):
        self.client.verify_transaction(**kwargs)

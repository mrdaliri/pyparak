
class BaseGateway(object):
    def send(self):
        raise NotImplementedError()

    def verify(self):
        raise NotImplementedError()


class PayirGateway(BaseGateway):
    def send(self):
        pass

    def verify(self):
        pass

from zeep import Client


class BaseGateway(object):
    def send(self, data):
        raise NotImplementedError()

    def verify(self):
        raise NotImplementedError()


class ZarinpalGateway(BaseGateway):

    def __init__(self):
        self.client = Client('https://sandbox.zarinpal.com/pg/services/WebGate/wsdl')

    def send(self, data):
        result = self.client.service.PaymentRequest(data['merchant'], data['amount'], data['description'],
                                                    data['email'], data['mobile'], data['callback'])

        if result.Status == 100 and len(result.Authority) == 36:
            return {'authority': result.Authority,
                    'url': 'https://sandbox.zarinpal.com/pg/StartPay/{0}'.format(result.Authority)}
        else:
            raise Exception(self.error_code(result.Status))

    def verify(self, data):
        result = self.client.service.PaymentVerificationWithExtra(data['merchant'], data['authority'], data['amount'])
        if result.Status == 100:
            return {'status': result.Status, 'reference_id': result.RefID}
        else:
            raise Exception(self.error_code(result.Status))

    def confirm(self, data):
        if data['query_params']['Status'] == 'OK':
            verify_data = {'merchant': data['merchant'], 'amount': data['payment'].amount,
                           'authority': data['payment'].authority}
            return self.verify(verify_data)

        else:
            raise Exception(self.error_code(-22))

    def error_code(self, code):
        switcher = {
            101: "Transaction submitted.",
            -42: "Time out validation",
            -22: "Transaction canceled by user",
            -11: "request not found",
            -3: "Payment value error",
            -1: "ّInformation send is incomplete",
        }
        return switcher.get(code, "error not found")

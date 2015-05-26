import xml.etree.ElementTree as ET
import urllib
import urllib2
from xmltodict import parse

PGS_TOKEN = 'C888EE7F420841CF92D0B0063EDDFC7D'
PGS_EMAIL = 'pagseguro@panfleteria.com.br'


class PagSeguroTransactions(object):

    def __init__(self, initial_date, final_date):
        self.initial_date = initial_date
        self.final_date = final_date
        self.ws_endpoint = 'https://ws.pagseguro.uol.com.br/v2/transactions'
        self.transactions = list()

    def get_transactions(self):
        data = {
            'initialDate': self.initial_date,
            'finalDate': self.final_date,
            'token': PGS_TOKEN,
            'email': PGS_EMAIL
        }
        encode_data = urllib.urlencode(data)
        request = self.ws_endpoint + '?' + encode_data
        response = urllib2.urlopen(request)
        xml = response.read()
        root = ET.fromstring(xml)
        transactions = root.iter('transactions')
        total = 0
        try:
            for transaction in transactions:
                for element in transaction:
                    code = element.find('code').text
                    gorss_amount = element.find('grossAmount').text
                    print code, gorss_amount
                    tran_ = PagSeguroTransaction(code)
                    tran_.get_details()
            #         total = float(tran_.get_details()) + total
            # print total
        except Exception as e:
            print e


class PagSeguroTransaction:

    def __init__(self, code):
        self.ws_endpoint = 'https://ws.pagseguro.uol.com.br/v3/transactions'
        self.code = code

    def get_details(self):
        data = {
            'token': PGS_TOKEN,
            'email': PGS_EMAIL
        }
        encode_data = urllib.urlencode(data)
        request = self.ws_endpoint + '/' + self.code + '/' + '?' + encode_data
        print request
        response = urllib2.urlopen(request)
        xml_transaction = response.read()
        xml2dict = parse(xml_transaction)
        print xml2dict['transaction']['reference']
        # transation_root = ET.fromstring(xml_transaction)
        # return transation_root.find('grossAmount').text


class PagSeguroAbandonedTransactions(PagSeguroTransactions):

    def __init__(self, initial_date, final_date):
        super(PagSeguroAbandonedTransactions, self).__init__(initial_date, final_date)
        self.ws_endpoint = 'https://ws.pagseguro.uol.com.br/v2/transactions/abandoned'

    def get_transactions(self):
        super(PagSeguroAbandonedTransactions, self).get_transactions()


if __name__ == '__main__':
    transactions = PagSeguroAbandonedTransactions('2015-05-22T00:00', '2015-05-25T00:00')
    transactions.get_transactions()

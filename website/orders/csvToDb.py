
import pandas

from website.orders.models import Order

dataSet = pandas.read_csv('media/s.csv', sep = ',', names = ['internalID', 'orderCreationTime',
                                                             'merchantID', 'status', 'amount',
                                                             'currency', 'orderID', 'orderType',
                                                             'orderDescription'])
maxRange = dataSet['internalID'].count()
for count in range(maxRange):
    obj, created = Order.objects.get_or_create(
        internalID = dataSet['internalID'][count],
        orderCreationTime = dataSet['orderCreationTime'][count],
        merchantID = dataSet['merchantID'][count],
        status = dataSet['status'][count],
        amount = dataSet['amount'][count],
        currency = dataSet['currency'][count],
        orderID = dataSet['orderID'][count],
        orderType = dataSet['orderType'][count],
        orderDescription = dataSet['orderDescription'][count],
    )

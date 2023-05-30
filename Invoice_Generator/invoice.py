from datetime import datetime, date
from pyinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item, Transaction
from pyinvoice.templates import SimpleInvoice

doc = SimpleInvoice('invoice.pdf')


doc.is_paid = True

doc.invoice_info = InvoiceInfo(1122, datetime.now(), datetime.now())  


doc.service_provider_info = ServiceProviderInfo(
    name='Fresh Fruits Shop',
    city='Pathanamthitta',
    state='Kerala',
)


doc.client_info = ClientInfo(name='Bibin', email='bibin@gmail.com')


doc.add_item(Item('Apple', '', 1, '55'))
doc.add_item(Item('Orange', '', 2, '50'))
doc.add_item(Item('Mango', '', 3, '60'))


doc.set_item_tax_rate(18)  
doc.set_bottom_tip("Thank you for shopping with us!")
doc.finish()

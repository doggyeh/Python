"""Create a SalesOrder in Python and upload to Microsoft Dynamics NAV
You'll need your own NAV Web Service URL, UserName, and Password.
Here's the detailed guide http://doggyeh.blogspot.sg/2016/08/create-salesorder-in-python-and-upload.html"""

from datetime import datetime
from os.path import expanduser
from pytz import timezone
from suds.client import Client
from suds.transport.https import WindowsHttpAuthenticated
from suds import WebFault

def upload_error(msg):
    """Record that upload sales_order to NAV FAILED"""
    now_utc = datetime.now(timezone('UTC'))
    now_sg = now_utc.astimezone(timezone('Asia/Singapore'))
    with open(expanduser("~") + '/Documents/nav_record.txt', 'a+') as f:
        f.write(("[%s]" % now_sg) + msg)
    print msg

def sales_order_lines(client, product_sales):
    """Generate sales order lines."""
    lines = client.factory.create('Sales_Order_Line_List')
    for p in product_sales:
        product = product_sales[p]
        line = client.factory.create('Sales_Order_Line')
        line.Type = 'Item'
        line.No = product['code']
        line.Reserve = 'Optional'
        line.Quantity = product['qty']
        line.Line_Amount = product['price']
        line.IC_Partner_Ref_Type = '_blank_'
        line.Unit_Price = product['unit_price']
        lines[0].append(line)
    return lines


def new_sales_order(client, nav_info):
    """Generate a new sales_order"""
    sales_order = client.factory.create('SalesOrder')
    sales_order.Status = "Open"
    sales_order.No_Series = "DSO"
    sales_order.Shipping_Advice = "Partial"
    sales_order.Job_Queue_Status = "_blank_"
    sales_order.Location_Code = nav_info['location']
    sales_order.Sell_to_Customer_No = nav_info['customer']
    sales_order.Remarks = "Generated by Robin: %s %s" % (nav_info['name'], nav_info['date'][:10])
    return sales_order

def upload(setting, product_sales, nav_info):
    ntlm = WindowsHttpAuthenticated(username=setting.nav_username, password=setting.nav_password)
    client = Client(setting.nav_url, transport=ntlm)

    # Create SalesOrder
    sales_order = new_sales_order(client, nav_info)
    result = None
    try:
        result = client.service.Create(sales_order)
        #result = client.service.Read('SO16-NAV029066')
        print result
    except WebFault as detail:
        upload_error('Create failed with %s, ERROR: %s\n' % (nav_info, detail))
        return
    sales_order = result
    now_utc = datetime.now(timezone('UTC'))
    now_sg = now_utc.astimezone(timezone('Asia/Singapore'))
    with open(expanduser("~") + '/Documents/nav_record.txt', 'a+') as f:
        f.write("[%s]Create success with %s, SalesOrder.No = %s\n" % (now_sg, nav_info, sales_order.No))

    # Update SalesOrder lines
    lines = sales_order_lines(client, product_sales)
    sales_order.SalesLines = lines
    result = None
    try:
        result = client.service.Update(sales_order)
    except WebFault as detail:
        upload_error('Update failed with %s, ERROR: %s\n' % (nav_info, detail))

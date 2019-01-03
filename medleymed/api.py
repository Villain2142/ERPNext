from __future__ import unicode_literals
import frappe
import json
import frappe.utils
from frappe.utils import cstr, flt, getdate, comma_and, cint
from frappe import _
from frappe.model.utils import get_fetch_values
from frappe.model.mapper import get_mapped_doc
from erpnext.stock.stock_balance import update_bin_qty, get_reserved_qty
from frappe.desk.notifications import clear_doctype_notifications
from frappe.contacts.doctype.address.address import get_company_address
from erpnext.controllers.selling_controller import SellingController
from erpnext.accounts.doctype.subscription.subscription import get_next_schedule_date
from erpnext.selling.doctype.customer.customer import check_credit_limit
import requests

# # @frappe.whitelist(allo w_guest=True)
# def ping():
# 	return "pong"

# @frappe.whitelist(allow_guest=True)
def get_orders():

	url = "http://172.27.2.46:8006/order/api/getproxyorders/"
	headers = {
		"content-type": "application/json",
		"cache-control": "no-cache",
	}

	response = requests.post(url,data=json.dumps({"dist_id":"MMRX-B2B-INHYD-DI-18"}),headers=headers)

	data = json.loads(response.text)
	print json.dumps(data, indent=4)
	print json.loads(response.text)

	return data["orders"]

# @frappe.whitelist(allow_guest=True)
def createSalesOrder():
	try :
		data = get_orders()

		for order in data:
			so = frappe.new_doc("Sales Order")
			so.customer = order["customer"]
			so.transaction_date = order["transaction_date"]
			so.delivery_date = order["delivery_date"]
			so.medley_orderid = order["medley_orderid"]
			
			for item in order["item_list"]:
				obj = {
					'qty': item['qty'],
					'item_code': item['item_code'],
				}
				so.append("items",obj)
			so.save(ignore_permissions=True)
			frappe.db.commit
	except Exception as e :
		print e


# createSalesOrder()




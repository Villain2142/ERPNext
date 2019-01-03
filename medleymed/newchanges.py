from __future__ import unicode_literals
import frappe
from frappe.model.mapper import get_mapped_doc
from frappe.utils import flt, add_days
import frappe.permissions
import unittest
from erpnext.selling.doctype.sales_order.sales_order \
	import make_material_request, make_delivery_note, make_sales_invoice, WarehouseRequired
from frappe import throw, _
import json
import sys 
import requests





def create_material_request(doc,method=None):

	mr = frappe.new_doc("Material Request")
	mr.customer = doc.customer
	mr.transaction_date = doc.transaction_date
	mr.schedule_date = doc.delivery_date
	
	mr.medleyorderid = doc.medley_orderid
	mr.naming_series = doc.medley_orderid

	
	try:

		for item in doc.items:
			negative_stock = (item.actual_qty - item.reserved_qty) 
			x = negative_stock-item.qty
			if negative_stock <= 0:
				negative_stock = 0
			else :
				negative_stock

			if x<0:
				doc.material_request_type = "Purchase"
				mr.append("items",
				{
				"qty": -(negative_stock - item.qty),
				"item_code": item.item_code,
				"item_name": item.item_name
				})
				
			if (item.qty-x)> 0:

				doc.material_request_type = "Material Transfer"
				mr.append("items",
				{
				"qty": -(item.qty-x),
				"item_code": item.item_code,
				"item_name": item.item_name
				})
				
			else:

				pass

		mr.flags.ignore_permissions = True

		mr.save()

	except Exception as e:
		print e
		


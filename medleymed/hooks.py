# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "medleymed"
app_title = "Medleymed"
app_publisher = "Medleymed"
app_description = "custom changes"
app_icon = "octicon octicon-file-directory"
app_color = "black"
app_email = "custom@medleymed.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/medleymed/css/medleymed.css"
# app_include_js = "/assets/medleymed/js/medleymed.js"
app_include_css = [
    "/assets/medleymed/css/bdtheme.css",
    "/assets/medleymed/css/skin-blue.css",
    "/assets/medleymed/css/custom.css",
    "/assets/medleymed/css/temp.css",
]
app_include_js = [
    "/assets/medleymed/js/bdtheme.js",
    "/assets/medleymed/js/custom.js",
    "/assets/js/medleymed-template.min.js",
]


# include js, css files in header of web template
web_include_css = "/assets/medleymed/css/bdtheme-web.css"
# web_include_css = "/assets/medleymed/css/medleymed.css"
# web_include_js = "/assets/medleymed/js/medleymed.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "medleymed.utils.get_home_page"

# Generators
# ----------
doc_events = {
"Sales Order" : {
		"on_submit":["medleymed.medleymed.newchanges.create_material_request"]
		}
}

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "medleymed.install.before_install"
# after_install = "medleymed.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "medleymed.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"medleymed.tasks.all"
# 	],
# 	"daily": [
# 		"medleymed.tasks.daily"
# 	],
# 	"hourly": [
# 		"medleymed.tasks.hourly"
# 	],
# 	"weekly": [
# 		"medleymed.tasks.weekly"
# 	]
# 	"monthly": [
# 		"medleymed.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "medleymed.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "medleymed.event.get_events"
# }


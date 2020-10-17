"""
This file is part of the MerchantAPI package.

(c) Miva Inc <https://www.miva.com/>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.
"""

import requests
import logging
import merchantapi.request
import merchantapi.response
from . credentials import MerchantApiTestCredentials
from merchantapi.client import Client
from merchantapi.abstract import Response
from merchantapi.logging import FileLogger
from pathlib import Path
from http.client import HTTPConnection


FILE_LOGGER = None


def configure_logging():
	if MerchantApiTestCredentials.DEBUG_OUTPUT is True:
		HTTPConnection.debuglevel = 1
		logging.basicConfig()
		logging.getLogger().setLevel(logging.DEBUG)
		log = logging.getLogger("requests.packages.urllib3")
		log.setLevel(logging.DEBUG)
		log.propagate = True


def configure_permissions():
	if MerchantApiTestCredentials.AUTO_PROVISION_PERMISSIONS is True:
		enable_api_function_access('Provision_Domain')
		enable_api_function_access('Provision_Store', MerchantApiTestCredentials.MERCHANT_API_STORE_CODE)
		enable_api_function_access('PrintQueueJobList_Load_Query', MerchantApiTestCredentials.MERCHANT_API_STORE_CODE)
		enable_api_function_access('PrintQueueList_Load_Query', MerchantApiTestCredentials.MERCHANT_API_STORE_CODE)
		enable_api_function_access('PrintQueueJob_Delete', MerchantApiTestCredentials.MERCHANT_API_STORE_CODE)


def init_client():
	global FILE_LOGGER

	if MerchantApiTestCredentials.LOG_FILE is not None and isinstance(MerchantApiTestCredentials.LOG_FILE, str) and len(MerchantApiTestCredentials.LOG_FILE):
		if FILE_LOGGER is None:
			FILE_LOGGER = FileLogger(MerchantApiTestCredentials.LOG_FILE)

	client = Client(MerchantApiTestCredentials.MERCHANT_API_ENDPOINT, MerchantApiTestCredentials.MERCHANT_API_API_TOKEN, MerchantApiTestCredentials.MERCHANT_API_SIGNING_KEY, {
		'default_store_code': MerchantApiTestCredentials.MERCHANT_API_STORE_CODE,
		'ssl_verify': MerchantApiTestCredentials.SSL_VERIFY
	})

	if FILE_LOGGER is not None:
		client.set_logger(FILE_LOGGER)

	return client


def validate_response_object(response, expectedtype=None):
	assert response is not None
	assert isinstance(response, Response)
	if expectedtype is not None:
		assert isinstance(response, expectedtype)


def validate_response_success(response, expectedtype=None):
	validate_response_object(response, expectedtype)

	if MerchantApiTestCredentials.VERBOSE_OUTPUT and response.is_error():
		print('%s: %s' % (response.get_error_code(), response.get_error_message()))

	assert response.is_success()


def validate_response_error(response, expectedtype=None):
	validate_response_object(response, expectedtype)
	assert response.is_error()


def read_test_file(file: str):
	filepath = MerchantApiTestCredentials.TEST_DATA_PATH + '/' + file
	fp = open(filepath, 'rb')
	ret = fp.read()
	fp.close()
	return ret


def upload_image(file: str):
	filepath = MerchantApiTestCredentials.TEST_DATA_PATH + '/' + file

	data = dict()
	data['Session_Type'] = 'admin'
	data['Function'] = 'Image_Upload'
	data['Username'] = MerchantApiTestCredentials.MERCHANT_ADMIN_USER
	data['Password'] = MerchantApiTestCredentials.MERCHANT_ADMIN_PASSWORD
	data['TemporarySession'] = 1
	data['Store_Code'] = MerchantApiTestCredentials.MERCHANT_API_STORE_CODE

	if filepath.endswith('.png'):
		type = 'image/png'
	elif filepath.endswith('.jpg') or filepath.endswith('.jpeg'):
		type = 'image/jpeg'

	files = {'Image': (Path(filepath).name, open(filepath, 'rb'), type, {})}

	response = requests.post(url=MerchantApiTestCredentials.MERCHANT_API_ENDPOINT, files=files, data=data)

	json = response.json()

	assert 'success' in json and json['success'] in (True, 1)


def enable_api_function_access(function_name: str, store_code: str = None):
	list_response = send_admin_request( 'APITokenList_Load_Query', {
		'Filter': [
			{
				'name':	'search',
				'value':
				[
					{
						'field':		'token',
						'operator':		'EQ',
						'value':		MerchantApiTestCredentials.MERCHANT_API_API_TOKEN
					}
				]
			}
		]
	}, True)

	list_result = list_response.json()

	assert list_result['success'] in (True, 1)
	assert list_result['data']['data'][0]['token'] == MerchantApiTestCredentials.MERCHANT_API_API_TOKEN

	if isinstance(store_code, str) and len(store_code):
		list_response = send_admin_request( 'StoreList_Load_Query', {
			'Filter': [
				{
					'name':	'search',
					'value':
					[
						{
							'field':		'code',
							'operator':		'EQ',
							'value':		MerchantApiTestCredentials.MERCHANT_API_STORE_CODE
						}
					]
				}
			]
		}, False)
		
		assert list_response['success'] in (True, 1)
		assert list_response['data']['data'][0]['id'] > 0

		store_id = list_response['data']['data'][0]['id']
	else:
		store_id = 0

	response = send_admin_request( 'APITokenFunction_Insert', {
		'APIToken_ID': list_result['data']['data'][0]['id'],
		'APIToken_Store_ID': store_id,
		'APIToken_Function': function_name
	}, True)


def send_admin_request(func: str, data: dict, domain: bool = False):
	if not isinstance(data, dict):
		data = dict()

	data['Session_Type'] = 'admin'
	data['Function'] = func
	data['Username'] = MerchantApiTestCredentials.MERCHANT_ADMIN_USER
	data['Password'] = MerchantApiTestCredentials.MERCHANT_ADMIN_PASSWORD
	data['TemporarySession'] = 1

	if domain is not True and 'Store_Code' not in data:
		data['Store_Code'] = MerchantApiTestCredentials.MERCHANT_API_STORE_CODE
	elif domain is True and 'Store_Code' in data:
		del data['Store_Code']

	return requests.post(url=MerchantApiTestCredentials.MERCHANT_API_ENDPOINT, json=data)


def load_modules_by_feature(feature: str, include: list = None):
	response = send_admin_request('ModuleList_Load_Features', {'Module_Features': feature})

	data = response.json()

	if isinstance(include, list):
		ret = []
		for d in data['data']:
			if d['code'] in include:
				ret.append(d)
		return ret

	return data['data']


def get_product(code: str):
	request = merchantapi.request.ProductListLoadQuery(init_client())

	filters = request.filter_expression()\
		.equal('code', code)

	request.set_filters(filters) \
		.set_on_demand_columns(request.get_available_on_demand_columns()) \
		.add_on_demand_column('CustomField_Values:*')

	response = request.send()

	validate_response_success(response, merchantapi.response.ProductListLoadQuery)

	return response.get_products()[0] if len(response.get_products()) else None


def get_category(code: str):
	request = merchantapi.request.CategoryListLoadQuery(init_client())

	filters = request.filter_expression()\
		.equal('code', code)

	request.set_filters(filters) \
		.set_on_demand_columns(request.get_available_on_demand_columns()) \
		.add_on_demand_column('CustomField_Values:*')

	response = request.send()

	validate_response_success(response, merchantapi.response.CategoryListLoadQuery)

	return response.get_categories()[0] if len(response.get_categories()) else None


def get_coupon(code: str):
	request = merchantapi.request.CouponListLoadQuery(init_client())

	filters = request.filter_expression()\
		.equal('code', code)

	request.set_filters(filters)

	response = request.send()

	validate_response_success(response, merchantapi.response.CouponListLoadQuery)

	return response.get_coupons()[0] if len(response.get_coupons()) else None


def get_customer(login: str):
	request = merchantapi.request.CustomerListLoadQuery(init_client())

	filters = request.filter_expression()\
		.equal('login', login)

	request.set_filters(filters) \
		.set_on_demand_columns(request.get_available_on_demand_columns())\
		.add_on_demand_column('CustomField_Values:*')

	response = request.send()

	validate_response_success(response, merchantapi.response.CustomerListLoadQuery)

	return response.get_customers()[0] if len(response.get_customers()) else None


def get_price_group(name: str):
	request = merchantapi.request.PriceGroupListLoadQuery(init_client())

	filters = request.filter_expression()\
		.equal('name', name)

	request.set_filters(filters)

	response = request.send()

	validate_response_success(response, merchantapi.response.PriceGroupListLoadQuery)

	return response.get_price_groups()[0] if len(response.get_price_groups()) else None


def get_branch(name: str):
	request = merchantapi.request.BranchListLoadQuery(init_client())

	filters = request.filter_expression()\
		.equal('name', name)

	request.set_filters(filters)

	response = request.send()

	validate_response_success(response, merchantapi.response.BranchListLoadQuery)

	return response.get_branches()[0] if len(response.get_branches()) else None


def delete_branch(name: str):
	request = merchantapi.request.BranchDelete(init_client())

	request.set_branch_name(name)

	response = request.send()

	validate_response_object(response, merchantapi.response.BranchDelete)


def get_note(field: str, value):
	request = merchantapi.request.NoteListLoadQuery(init_client())

	filters = request.filter_expression()\
		.equal(field, value)

	request.set_filters(filters)

	response = request.send()

	validate_response_success(response, merchantapi.response.NoteListLoadQuery)

	return response.get_notes()[0] if len(response.get_notes()) else None


def get_order(id: int):
	request = merchantapi.request.OrderListLoadQuery(init_client())

	filters = request.filter_expression()\
		.equal('id', id)

	request.set_filters(filters) \
		.set_on_demand_columns(request.get_available_on_demand_columns())\
		.add_on_demand_column('CustomField_Values:*')

	response = request.send()

	validate_response_success(response, merchantapi.response.OrderListLoadQuery)

	return response.get_orders()[0] if len(response.get_orders()) else None


def provision_store(file: str):
	request = merchantapi.request.ProvisionStore(init_client())
	full_path = '%s/%s' % (MerchantApiTestCredentials.TEST_DATA_PATH, file)

	with open(full_path, 'r') as f:
		content = f.read()

	request.set_xml(content)

	response = request.send()

	validate_response_success(response, merchantapi.response.ProvisionStore)

	if MerchantApiTestCredentials.VERBOSE_OUTPUT:
		for message in response.get_provision_messages():
			print('[%s] Line %d Tag %s - %s' % (message.get_date_time_stamp(), message.get_line_number(), message.get_tag(), message.get_message()))


def provision_domain(file: str):
	request = merchantapi.request.ProvisionDomain(init_client())
	full_path = '%s/%s' % (MerchantApiTestCredentials.TEST_DATA_PATH, file)

	with open(full_path, 'r') as f:
		content = f.read()

	request.set_xml(content)

	response = request.send()

	validate_response_success(response, merchantapi.response.ProvisionDomain)

	if MerchantApiTestCredentials.VERBOSE_OUTPUT:
		for message in response.get_provision_messages():
			print('[%s] Line %d Tag %s - %s' % (message.get_date_time_stamp(), message.get_line_number(), message.get_tag(), message.get_message()))


def create_print_queue(name: str):
	response = send_admin_request('PrintQueue_Insert', {'PrintQueue_Description': name})
	data = response.json()
	assert 'success' in data


def create_branch(name: str, color: str, parent: merchantapi.model.Branch):
	assert parent is not None

	request = merchantapi.request.BranchCreate(init_client(), parent)

	request.set_name(name)
	request.set_color(color)

	response = request.send()

	validate_response_success(response, merchantapi.response.BranchCreate)

	return response.get_branch()


def get_branch_template_version(filename: str, branch: merchantapi.model.Branch):
	request = merchantapi.request.BranchTemplateVersionListLoadQuery(init_client(), branch)

	request.set_filters(request.filter_expression().equal('filename', filename))
	request.set_on_demand_columns(request.get_available_on_demand_columns())

	response = request.send()

	validate_response_success(response, merchantapi.response.BranchTemplateVersionListLoadQuery)

	return response.get_branch_template_versions()[0] if len(response.get_branch_template_versions()) > 0 else None

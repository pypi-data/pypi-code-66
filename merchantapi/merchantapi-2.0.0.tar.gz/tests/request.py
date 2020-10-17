"""
This file is part of the MerchantAPI package.

(c) Miva Inc <https://www.miva.com/>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.
"""

import time
import random
from . import helper
import merchantapi.request
import merchantapi.response
import merchantapi.model
import merchantapi.multicall

helper.configure_logging()
helper.configure_permissions()


def test_availability_group_business_account_update_assigned():
	"""
	Tests the AvailabilityGroupBusinessAccount_Update_Assigned API Call
	"""

	helper.provision_store('AvailabilityGroupBusinessAccount_Update_Assigned.xml')

	availability_group_business_account_update_assigned_test_assignment()
	availability_group_business_account_update_assigned_test_unassignment()
	availability_group_business_account_update_assigned_test_invalid_assign()
	availability_group_business_account_update_assigned_test_invalid_availability_group()
	availability_group_business_account_update_assigned_test_invalid_business_account()


def availability_group_business_account_update_assigned_test_assignment():
	request = merchantapi.request.AvailabilityGroupBusinessAccountUpdateAssigned(helper.init_client())

	request.set_availability_group_name('AvailabilityGrpBusAccUpdateAssignedTest')\
		.set_business_account_title('AvailabilityGrpBusAccUpdateAssignedTest_BusinessAccount')\
		.set_assigned(True)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.AvailabilityGroupBusinessAccountUpdateAssigned)


def availability_group_business_account_update_assigned_test_unassignment():
	request = merchantapi.request.AvailabilityGroupBusinessAccountUpdateAssigned(helper.init_client())

	request.set_availability_group_name('AvailabilityGrpBusAccUpdateAssignedTest')\
		.set_business_account_title('AvailabilityGrpBusAccUpdateAssignedTest_BusinessAccount')\
		.set_assigned(False)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.AvailabilityGroupBusinessAccountUpdateAssigned)


def availability_group_business_account_update_assigned_test_invalid_assign():
	request = merchantapi.request.AvailabilityGroupBusinessAccountUpdateAssigned(helper.init_client())

	# noinspection PyTypeChecker
	request.set_availability_group_name('AvailabilityGrpBusAccUpdateAssignedTest')\
		.set_business_account_title('AvailabilityGrpBusAccUpdateAssignedTest_BusinessAccount')\
		.set_assigned('foobar')

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.AvailabilityGroupBusinessAccountUpdateAssigned)


def availability_group_business_account_update_assigned_test_invalid_availability_group():
	request = merchantapi.request.AvailabilityGroupBusinessAccountUpdateAssigned(helper.init_client())

	request.set_availability_group_name('InvalidAvailabilityGroup')\
		.set_business_account_title('AvailabilityGrpBusAccUpdateAssignedTest_BusinessAccount')\
		.set_assigned(True)

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.AvailabilityGroupBusinessAccountUpdateAssigned)


def availability_group_business_account_update_assigned_test_invalid_business_account():
	request = merchantapi.request.AvailabilityGroupBusinessAccountUpdateAssigned(helper.init_client())

	request.set_availability_group_name('AvailabilityGrpBusAccUpdateAssignedTest')\
		.set_business_account_title('InvalidBusinessAccount')\
		.set_assigned(True)

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.AvailabilityGroupBusinessAccountUpdateAssigned)


def test_availability_group_customer_update_assigned():
	"""
	Tests the AvailabilityGroupCustomer_Update_Assigned API Call
	"""

	helper.provision_store('AvailabilityGroupCustomer_Update_Assigned.xml')

	availability_group_customer_update_assigned_test_assignment()
	availability_group_customer_update_assigned_test_unassignment()
	availability_group_customer_update_assigned_test_invalid_assign()
	availability_group_customer_update_assigned_test_invalid_availability_group()
	availability_group_customer_update_assigned_test_invalid_customer()


def availability_group_customer_update_assigned_test_assignment():
	request = merchantapi.request.AvailabilityGroupCustomerUpdateAssigned(helper.init_client())

	request.set_availability_group_name('AvailabilityGrpCustUpdateAssigned')\
		.set_customer_login('AvailabilityGrpCustUpdateAssigned')\
		.set_assigned(True)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.AvailabilityGroupCustomerUpdateAssigned)


def availability_group_customer_update_assigned_test_unassignment():
	request = merchantapi.request.AvailabilityGroupCustomerUpdateAssigned(helper.init_client())

	request.set_availability_group_name('AvailabilityGrpCustUpdateAssigned')\
		.set_customer_login('AvailabilityGrpCustUpdateAssigned')\
		.set_assigned(False)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.AvailabilityGroupCustomerUpdateAssigned)


def availability_group_customer_update_assigned_test_invalid_assign():
	request = merchantapi.request.AvailabilityGroupCustomerUpdateAssigned(helper.init_client())

	# noinspection PyTypeChecker
	request.set_availability_group_name('AvailabilityGrpCustUpdateAssigned')\
		.set_customer_login('AvailabilityGrpCustUpdateAssigned')\
		.set_assigned('foobar')

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.AvailabilityGroupCustomerUpdateAssigned)


def availability_group_customer_update_assigned_test_invalid_availability_group():
	request = merchantapi.request.AvailabilityGroupCustomerUpdateAssigned(helper.init_client())

	request.set_availability_group_name('InvalidAvailabilityGroup')\
		.set_customer_login('AvailabilityGrpCustUpdateAssigned')\
		.set_assigned(False)

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.AvailabilityGroupCustomerUpdateAssigned)


def availability_group_customer_update_assigned_test_invalid_customer():
	request = merchantapi.request.AvailabilityGroupCustomerUpdateAssigned(helper.init_client())

	request.set_availability_group_name('AvailabilityGrpCustUpdateAssigned')\
		.set_customer_login('InvalidAvailabilityGroupCustomer')\
		.set_assigned(False)

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.AvailabilityGroupCustomerUpdateAssigned)


def test_availability_group_list_load_query():
	"""
	Tests the AvailabilityGroupList_Load_Query API Call
	"""

	helper.provision_store('AvailabilityGroupList_Load_Query.xml')

	availability_group_list_load_query_test_list_load()


def availability_group_list_load_query_test_list_load():
	request = merchantapi.request.AvailabilityGroupListLoadQuery(helper.init_client())

	request.set_filters(request.filter_expression().like('name', 'AvailabilityGroupListLoadQueryTest_%'))

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.AvailabilityGroupListLoadQuery)

	assert isinstance(response.get_availability_groups(), list)

	for i, ag in enumerate(response.get_availability_groups()):
		assert isinstance(ag, merchantapi.model.AvailabilityGroup)
		assert ag.get_name() == ('AvailabilityGroupListLoadQueryTest_%d' % int(i+1))


def test_availability_group_payment_method_update_assigned():
	"""
	Tests the AvailabilityGroupPaymentMethod_Update_Assigned API Call
	"""

	helper.provision_store('AvailabilityGroupPaymentMethod_Update_Assigned.xml')

	availability_group_payment_method_update_assigned_test_assignment()
	availability_group_payment_method_update_assigned_test_unassignment()
	availability_group_payment_method_update_assigned_test_invalid_assign()
	availability_group_payment_method_update_assigned_test_invalid_availability_group()


def availability_group_payment_method_update_assigned_test_assignment():
	request = merchantapi.request.AvailabilityGroupPaymentMethodUpdateAssigned(helper.init_client())

	request.set_availability_group_name('AvailabilityGrpPayMethUpdateAssignedTest')\
		.set_module_code('COD')\
		.set_method_code('COD')\
		.set_assigned(True)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.AvailabilityGroupPaymentMethodUpdateAssigned)


def availability_group_payment_method_update_assigned_test_unassignment():
	request = merchantapi.request.AvailabilityGroupPaymentMethodUpdateAssigned(helper.init_client())

	request.set_availability_group_name('AvailabilityGrpPayMethUpdateAssignedTest')\
		.set_module_code('COD')\
		.set_method_code('COD')\
		.set_assigned(False)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.AvailabilityGroupPaymentMethodUpdateAssigned)


def availability_group_payment_method_update_assigned_test_invalid_assign():
	request = merchantapi.request.AvailabilityGroupPaymentMethodUpdateAssigned(helper.init_client())

	# noinspection PyTypeChecker
	request.set_availability_group_name('AvailabilityGrpPayMethUpdateAssignedTest')\
		.set_module_code('COD')\
		.set_method_code('COD')\
		.set_assigned('foobar')

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.AvailabilityGroupPaymentMethodUpdateAssigned)


def availability_group_payment_method_update_assigned_test_invalid_availability_group():
	request = merchantapi.request.AvailabilityGroupPaymentMethodUpdateAssigned(helper.init_client())

	request.set_availability_group_name('InvalidAvailabilityGroup')\
		.set_module_code('COD')\
		.set_method_code('COD')\
		.set_assigned(False)

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.AvailabilityGroupPaymentMethodUpdateAssigned)


def test_availability_group_product_update_assigned():
	"""
	Tests the AvailabilityGroupProduct_Update_Assigned API Call
	"""

	helper.provision_store('AvailabilityGroupProduct_Update_Assigned.xml')

	availability_group_product_update_assigned_test_assignment()
	availability_group_product_update_assigned_test_unassignment()
	availability_group_product_update_assigned_test_invalid_assign()
	availability_group_product_update_assigned_test_invalid_availability_group()
	availability_group_product_update_assigned_test_invalid_product()


def availability_group_product_update_assigned_test_assignment():
	request = merchantapi.request.AvailabilityGroupProductUpdateAssigned(helper.init_client())

	request.set_availability_group_name('AvailabilityGrpProdUpdateAssignedTest')\
		.set_product_code('AvailabilityGrpProdUpdateAssignedTest_Product')\
		.set_assigned(True)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.AvailabilityGroupProductUpdateAssigned)


def availability_group_product_update_assigned_test_unassignment():
	request = merchantapi.request.AvailabilityGroupProductUpdateAssigned(helper.init_client())

	request.set_availability_group_name('AvailabilityGrpProdUpdateAssignedTest')\
		.set_product_code('AvailabilityGrpProdUpdateAssignedTest_Product')\
		.set_assigned(False)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.AvailabilityGroupProductUpdateAssigned)


def availability_group_product_update_assigned_test_invalid_assign():
	request = merchantapi.request.AvailabilityGroupProductUpdateAssigned(helper.init_client())

	# noinspection PyTypeChecker
	request.set_availability_group_name('AvailabilityGrpProdUpdateAssignedTest')\
		.set_product_code('AvailabilityGrpProdUpdateAssignedTest_Product')\
		.set_assigned('foobar')

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.AvailabilityGroupProductUpdateAssigned)


def availability_group_product_update_assigned_test_invalid_availability_group():
	request = merchantapi.request.AvailabilityGroupProductUpdateAssigned(helper.init_client())

	request.set_availability_group_name('InvalidAvailabilityGroup')\
		.set_product_code('AvailabilityGrpProdUpdateAssignedTest_Product')\
		.set_assigned(False)

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.AvailabilityGroupProductUpdateAssigned)


def availability_group_product_update_assigned_test_invalid_product():
	request = merchantapi.request.AvailabilityGroupProductUpdateAssigned(helper.init_client())

	request.set_availability_group_name('AvailabilityGrpProdUpdateAssignedTest')\
		.set_product_code('InvalidProduct')\
		.set_assigned(False)

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.AvailabilityGroupProductUpdateAssigned)


def test_availability_group_shipping_method_update_assigned():
	"""
	Tests the AvailabilityGroupShippingMethod_Update_Assigned API Call
	"""

	helper.provision_store('AvailabilityGroupShippingMethod_Update_Assigned.xml')

	availability_group_shipping_method_update_assigned_test_assignment()
	availability_group_shipping_method_update_assigned_test_unassignment()
	availability_group_shipping_method_update_assigned_test_invalid_assign()
	availability_group_shipping_method_update_assigned_test_invalid_availability_group()


def availability_group_shipping_method_update_assigned_test_assignment():
	request = merchantapi.request.AvailabilityGroupShippingMethodUpdateAssigned(helper.init_client())

	request.set_availability_group_name('AvailabilityGrpShpMethUpdateAssignedTest')\
		.set_module_code('flatrate')\
		.set_method_code('AvailabilityGrpShpMethUpdateAssignedTest_Method')\
		.set_assigned(True)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.AvailabilityGroupShippingMethodUpdateAssigned)


def availability_group_shipping_method_update_assigned_test_unassignment():
	request = merchantapi.request.AvailabilityGroupShippingMethodUpdateAssigned(helper.init_client())

	request.set_availability_group_name('AvailabilityGrpShpMethUpdateAssignedTest')\
		.set_module_code('flatrate')\
		.set_method_code('AvailabilityGrpShpMethUpdateAssignedTest_Method')\
		.set_assigned(False)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.AvailabilityGroupShippingMethodUpdateAssigned)


def availability_group_shipping_method_update_assigned_test_invalid_assign():
	request = merchantapi.request.AvailabilityGroupShippingMethodUpdateAssigned(helper.init_client())

	# noinspection PyTypeChecker
	request.set_availability_group_name('AvailabilityGrpShpMethUpdateAssignedTest')\
		.set_module_code('flatrate')\
		.set_method_code('AvailabilityGrpShpMethUpdateAssignedTest_Method')\
		.set_assigned('foobar')

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.AvailabilityGroupShippingMethodUpdateAssigned)


def availability_group_shipping_method_update_assigned_test_invalid_availability_group():
	request = merchantapi.request.AvailabilityGroupShippingMethodUpdateAssigned(helper.init_client())

	request.set_availability_group_name('InvalidAvailabilityGroup')\
		.set_module_code('flatrate')\
		.set_method_code('AvailabilityGrpShpMethUpdateAssignedTest_Method')\
		.set_assigned(True)

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.AvailabilityGroupShippingMethodUpdateAssigned)


def test_category_list_load_parent():
	"""
	Tests the CategoryList_Load_Parent API Call
	"""

	helper.provision_store('CategoryList_Load_Parent.xml')

	category_list_load_parent_test_list_load()


def category_list_load_parent_test_list_load():
	parentcat = helper.get_category('CategoryListLoadParentTest_Parent')

	assert parentcat is not None
	assert isinstance(parentcat, merchantapi.model.Category)

	request = merchantapi.request.CategoryListLoadParent(helper.init_client(), parentcat)

	assert request.get_parent_id() == parentcat.get_id()

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CategoryListLoadParent)

	assert len(response.get_categories()) == 3

	for i, category in enumerate(response.get_categories()):
		assert isinstance(category, merchantapi.model.Category)
		assert category.get_code() == 'CategoryListLoadParentTest_Child_%d' % int(i+1)
		assert category.get_name() == 'CategoryListLoadParentTest_Child_%d' % int(i+1)
		assert category.get_active() is True


def test_category_list_load_query():
	"""
	Tests the CategoryList_Load_Query API Call
	"""

	helper.provision_store('CategoryList_Load_Query.xml')
	helper.upload_image('graphics/CategoryListLoadQuery1.jpg')
	helper.upload_image('graphics/CategoryListLoadQuery2.jpg')
	helper.upload_image('graphics/CategoryListLoadQuery3.jpg')
	helper.upload_image('graphics/CategoryListLoadQuery4.jpg')
	helper.upload_image('graphics/CategoryListLoadQuery5.jpg')
	helper.upload_image('graphics/CategoryListLoadQuery6.jpg')
	helper.upload_image('graphics/CategoryListLoadQuery7.jpg')

	category_list_load_query_test_list_load()
	category_list_load_query_test_list_load_with_custom_fields()


def category_list_load_query_test_list_load():
	request = merchantapi.request.CategoryListLoadQuery(helper.init_client())

	request.set_filters(request.filter_expression().like('code', 'CategoryListLoadQueryTest_%'))

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CategoryListLoadQuery)

	assert isinstance(response.get_categories(), list)
	assert len(response.get_categories()) == 7

	for i, category in enumerate(response.get_categories()):
		assert isinstance(category, merchantapi.model.Category)
		assert category.get_code() == 'CategoryListLoadQueryTest_%d' % int(i+1)
		assert category.get_name() == 'CategoryListLoadQueryTest_%d' % int(i+1)


def category_list_load_query_test_list_load_with_custom_fields():
	request = merchantapi.request.CategoryListLoadQuery(helper.init_client())

	request.set_filters(request.filter_expression().like('code', 'CategoryListLoadQueryTest_%'))\
		.add_on_demand_column('CustomField_Values:customfields:CategoryListLoadQueryTest_checkbox')\
		.add_on_demand_column('CustomField_Values:customfields:CategoryListLoadQueryTest_imageupload')\
		.add_on_demand_column('CustomField_Values:customfields:CategoryListLoadQueryTest_text')\
		.add_on_demand_column('CustomField_Values:customfields:CategoryListLoadQueryTest_textarea')\
		.add_on_demand_column('CustomField_Values:customfields:CategoryListLoadQueryTest_dropdown')\
		.set_sort('code', merchantapi.request.CategoryListLoadQuery.SORT_ASCENDING)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CategoryListLoadQuery)

	assert isinstance(response.get_categories(), list)
	assert len(response.get_categories()) == 7

	for i, category in enumerate(response.get_categories()):
		assert isinstance(category, merchantapi.model.Category)
		assert category.get_code() == 'CategoryListLoadQueryTest_%d' % int(i+1)
		assert category.get_name() == 'CategoryListLoadQueryTest_%d' % int(i+1)

		assert isinstance(category.get_custom_field_values(), merchantapi.model.CustomFieldValues)

		assert category.get_custom_field_values().has_value('CategoryListLoadQueryTest_checkbox', 'customfields') is True
		assert category.get_custom_field_values().get_value('CategoryListLoadQueryTest_checkbox', 'customfields') == '1'

		assert category.get_custom_field_values().has_value('CategoryListLoadQueryTest_imageupload', 'customfields') is True
		assert category.get_custom_field_values().get_value('CategoryListLoadQueryTest_imageupload', 'customfields') == 'graphics/00000001/CategoryListLoadQuery%d.jpg' % int(i+1)

		assert category.get_custom_field_values().has_value('CategoryListLoadQueryTest_text', 'customfields') is True
		assert category.get_custom_field_values().get_value('CategoryListLoadQueryTest_text', 'customfields') == 'CategoryListLoadQueryTest_%d' % int(i+1)

		assert category.get_custom_field_values().has_value('CategoryListLoadQueryTest_dropdown', 'customfields') is True
		assert category.get_custom_field_values().get_value('CategoryListLoadQueryTest_dropdown', 'customfields') == 'Option%d' % int(i+1)


def test_category_product_update_assigned():
	"""
	Tests the CategoryProduct_Update_Assigned API Call
	"""

	helper.provision_store('CategoryProduct_Update_Assigned.xml')

	category_product_update_assigned_test_assignment()
	category_product_update_assigned_test_unassignment()
	category_product_update_assigned_test_invalid_assign()
	category_product_update_assigned_test_invalid_category()
	category_product_update_assigned_test_invalid_product()


def category_product_update_assigned_test_assignment():
	request = merchantapi.request.CategoryProductUpdateAssigned(helper.init_client())

	request.set_edit_category('CategoryProductUpdateAssignedTest_Category')\
		.set_edit_product('CategoryProductUpdateAssignedTest_Product')\
		.set_assigned(True)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CategoryProductUpdateAssigned)


def category_product_update_assigned_test_unassignment():
	request = merchantapi.request.CategoryProductUpdateAssigned(helper.init_client())

	request.set_edit_category('CategoryProductUpdateAssignedTest_Category')\
		.set_edit_product('CategoryProductUpdateAssignedTest_Product')\
		.set_assigned(False)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CategoryProductUpdateAssigned)


def category_product_update_assigned_test_invalid_assign():
	request = merchantapi.request.CategoryProductUpdateAssigned(helper.init_client())

	# noinspection PyTypeChecker
	request.set_edit_category('CategoryProductUpdateAssignedTest_Category')\
		.set_edit_product('CategoryProductUpdateAssignedTest_Product')\
		.set_assigned('foobar')

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.CategoryProductUpdateAssigned)


def category_product_update_assigned_test_invalid_category():
	request = merchantapi.request.CategoryProductUpdateAssigned(helper.init_client())

	request.set_edit_category('InvalidCategory')\
		.set_edit_product('CategoryProductUpdateAssignedTest_Product')\
		.set_assigned(True)

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.CategoryProductUpdateAssigned)


def category_product_update_assigned_test_invalid_product():
	request = merchantapi.request.CategoryProductUpdateAssigned(helper.init_client())

	request.set_edit_category('CategoryProductUpdateAssignedTest_Category')\
		.set_edit_product('InvalidProduct')\
		.set_assigned(True)

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.CategoryProductUpdateAssigned)


def test_category_insert():
	"""
	Tests the Category_Insert API Call
	"""

	helper.provision_store('Category_Insert.xml')

	category_insert_test_insertion()
	category_insert_test_insertion_with_custom_fields()


def category_insert_test_insertion():
	request = merchantapi.request.CategoryInsert(helper.init_client())

	request.set_category_code('CategoryInsertTest_1')\
		.set_category_name('CategoryInsertTest_1 Name')\
		.set_category_page_title('CategoryInsertTest_1 Page Title')\
		.set_category_active(True)\
		.set_category_parent_category('')\
		.set_category_alternate_display_page('')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CategoryInsert)

	check = helper.get_category('CategoryInsertTest_1')

	assert isinstance(check, merchantapi.model.Category)
	assert check.get_code() == 'CategoryInsertTest_1'
	assert check.get_name() == 'CategoryInsertTest_1 Name'
	assert check.get_page_title() == 'CategoryInsertTest_1 Page Title'
	assert check.get_active() is True
	assert check.get_id() > 0


def category_insert_test_insertion_with_custom_fields():
	request = merchantapi.request.CategoryInsert(helper.init_client())

	request.set_category_code('CategoryInsertTest_2')\
		.set_category_name('CategoryInsertTest_2 Name')\
		.set_category_page_title('CategoryInsertTest_2 Page Title')\
		.set_category_active(True)\
		.set_category_parent_category('')\
		.set_category_alternate_display_page('')

	request.get_custom_field_values() \
		.add_value('CategoryInsertTest_checkbox', 'True', 'customfields') \
		.add_value('CategoryInsertTest_imageupload', 'graphics/00000001/CategoryInsert.jpg', 'customfields') \
		.add_value('CategoryInsertTest_text', 'CategoryInsertTest_2', 'customfields') \
		.add_value('CategoryInsertTest_textarea', 'CategoryInsertTest_2', 'customfields') \
		.add_value('CategoryInsertTest_dropdown', 'Option2', 'customfields')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CategoryInsert)

	check = helper.get_category('CategoryInsertTest_2')

	assert isinstance(check, merchantapi.model.Category)
	assert check.get_code() == 'CategoryInsertTest_2'
	assert check.get_name() == 'CategoryInsertTest_2 Name'
	assert check.get_page_title() == 'CategoryInsertTest_2 Page Title'
	assert check.get_active() is True
	assert check.get_id() > 0

	assert isinstance(check.get_custom_field_values(), merchantapi.model.CustomFieldValues)

	assert check.get_custom_field_values().has_value('CategoryInsertTest_checkbox', 'customfields') is True
	assert check.get_custom_field_values().get_value('CategoryInsertTest_checkbox', 'customfields') == '1'

	assert check.get_custom_field_values().has_value('CategoryInsertTest_imageupload', 'customfields') is True
	assert check.get_custom_field_values().get_value('CategoryInsertTest_imageupload', 'customfields') == 'graphics/00000001/CategoryInsert.jpg'

	assert check.get_custom_field_values().has_value('CategoryInsertTest_text', 'customfields') is True
	assert check.get_custom_field_values().get_value('CategoryInsertTest_text', 'customfields') == 'CategoryInsertTest_2'

	assert check.get_custom_field_values().has_value('CategoryInsertTest_textarea', 'customfields') is True
	assert check.get_custom_field_values().get_value('CategoryInsertTest_textarea', 'customfields') == 'CategoryInsertTest_2'

	assert check.get_custom_field_values().has_value('CategoryInsertTest_dropdown', 'customfields') is True
	assert check.get_custom_field_values().get_value('CategoryInsertTest_dropdown', 'customfields') == 'Option2'


def test_category_delete():
	"""
	Tests the Category_Delete API Call
	"""

	helper.provision_store('Category_Delete.xml')

	category_delete_test_deletion()
	category_delete_test_invalid_category()


def category_delete_test_deletion():
	request = merchantapi.request.CategoryDelete(helper.init_client())

	request.set_edit_category('CategoryDeleteTest')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CategoryDelete)

	check = helper.get_category('CategoryDelete')
	assert check is None


def category_delete_test_invalid_category():
	request = merchantapi.request.CategoryDelete(helper.init_client())

	request.set_edit_category('InvalidCategory')

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.CategoryDelete)


def test_category_update():
	"""
	Tests the Category_Update API Call
	"""

	helper.provision_store('Category_Update.xml')

	category_update_test_update()


def category_update_test_update():
	request = merchantapi.request.CategoryUpdate(helper.init_client())

	request.set_edit_category('CategoryUpdateTest_01')\
		.set_category_name('CategoryUpdateTest_01 New Name')\
		.set_category_active(False)\
		.set_category_page_title('CategoryUpdateTest_01 New Page Title')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CategoryUpdate)

	check = helper.get_category('CategoryUpdateTest_01')

	assert check is not None
	assert check.get_code() == 'CategoryUpdateTest_01'
	assert check.get_name() == 'CategoryUpdateTest_01 New Name'
	assert check.get_page_title() == 'CategoryUpdateTest_01 New Page Title'
	assert check.get_active() is False


def test_coupon_list_delete():
	"""
	Tests the CouponList_Delete API Call
	"""

	helper.provision_store('CouponList_Delete.xml')

	coupon_list_delete_test_deletion()


def coupon_list_delete_test_deletion():
	listrequest = merchantapi.request.CouponListLoadQuery(helper.init_client())

	listrequest.set_filters(listrequest.filter_expression().like('code', 'CouponListDeleteTest_%'))

	listresponse = listrequest.send()

	helper.validate_response_success(listresponse, merchantapi.response.CouponListLoadQuery)

	assert len(listresponse.get_coupons()) == 3

	request = merchantapi.request.CouponListDelete(helper.init_client())

	for coupon in listresponse.get_coupons():
		request.add_coupon(coupon)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CouponListDelete)


def test_coupon_list_load_query():
	"""
	Tests the CouponList_Load_Query API Call
	"""

	helper.provision_store('CouponList_Load_Query.xml')

	coupon_list_load_query_test_list_load()


def coupon_list_load_query_test_list_load():
	request = merchantapi.request.CouponListLoadQuery(helper.init_client())

	request.set_filters(request.filter_expression().like('code', 'CouponListLoadQueryTest_%'))

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CouponListLoadQuery)

	assert isinstance(response.get_coupons(), list)
	assert len(response.get_coupons()) == 3

	for i, coupon in enumerate(response.get_coupons()):
		assert isinstance(coupon, merchantapi.model.Coupon)
		assert coupon.get_code() == 'CouponListLoadQueryTest_%d' % int(i+1)


def test_coupon_price_group_update_assigned():
	"""
	Tests the CouponPriceGroup_Update_Assigned API Call
	"""

	helper.provision_store('CouponPriceGroup_Update_Assigned.xml')

	coupon_price_group_update_assigned_test_assignment()
	coupon_price_group_update_assigned_test_unassignment()
	coupon_price_group_update_assigned_test_invalid_assign()
	coupon_price_group_update_assigned_invalid_price_group()
	coupon_price_group_update_assigned_invalid_coupon()


def coupon_price_group_update_assigned_test_assignment():
	request = merchantapi.request.CouponPriceGroupUpdateAssigned(helper.init_client())

	request.set_coupon_code('CouponPriceGroupUpdateAssignedTest_Coupon')\
		.set_price_group_name('CouponPriceGroupUpdateAssignedTest_PriceGroup_1')\
		.set_assigned(True)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CouponPriceGroupUpdateAssigned)


def coupon_price_group_update_assigned_test_unassignment():
	request = merchantapi.request.CouponPriceGroupUpdateAssigned(helper.init_client())

	request.set_coupon_code('CouponPriceGroupUpdateAssignedTest_Coupon')\
		.set_price_group_name('CouponPriceGroupUpdateAssignedTest_PriceGroup_1')\
		.set_assigned(False)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CouponPriceGroupUpdateAssigned)


def coupon_price_group_update_assigned_test_invalid_assign():
	request = merchantapi.request.CouponPriceGroupUpdateAssigned(helper.init_client())

	# noinspection PyTypeChecker
	request.set_coupon_code('CouponPriceGroupUpdateAssignedTest_Coupon')\
		.set_price_group_name('CouponPriceGroupUpdateAssignedTest_PriceGroup_1')\
		.set_assigned('foobar')

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.CouponPriceGroupUpdateAssigned)


def coupon_price_group_update_assigned_invalid_price_group():
	request = merchantapi.request.CouponPriceGroupUpdateAssigned(helper.init_client())

	request.set_coupon_code('CouponPriceGroupUpdateAssignedTest_Coupon')\
		.set_price_group_name('InvalidPriceGroup')\
		.set_assigned(True)

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.CouponPriceGroupUpdateAssigned)


def coupon_price_group_update_assigned_invalid_coupon():
	request = merchantapi.request.CouponPriceGroupUpdateAssigned(helper.init_client())

	request.set_coupon_code('InvalidCoupon')\
		.set_price_group_name('CouponPriceGroupUpdateAssignedTest_PriceGroup_1')\
		.set_assigned(True)

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.CouponPriceGroupUpdateAssigned)


def test_coupon_insert():
	"""
	Tests the Coupon_Insert API Call
	"""

	helper.provision_store('Coupon_Insert.xml')

	coupon_insert_test_insertion()
	coupon_insert_test_insertion_with_price_group()
	coupon_insert_test_duplicate_code()
	coupon_insert_test_invalid_price_group()


def coupon_insert_test_insertion():
	request = merchantapi.request.CouponInsert(helper.init_client())

	start_time = int(time.time() / 1000) - 1000
	end_time = int(time.time() / 1000) + 100000

	request.set_code('CouponInsertTest_1')\
		.set_description('CouponInsertTest_1 Description')\
		.set_customer_scope(merchantapi.model.Coupon.CUSTOMER_SCOPE_ALL_SHOPPERS)\
		.set_date_time_start(start_time)\
		.set_date_time_end(end_time)\
		.set_max_per(1)\
		.set_max_use(2)\
		.set_active(True)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CouponInsert)

	coupon = helper.get_coupon('CouponInsertTest_1')

	assert isinstance(coupon, merchantapi.model.Coupon)
	assert coupon.get_code() == 'CouponInsertTest_1'
	assert coupon.get_description() == 'CouponInsertTest_1 Description'
	assert coupon.get_customer_scope() == merchantapi.model.Coupon.CUSTOMER_SCOPE_ALL_SHOPPERS
	assert coupon.get_date_time_start() == start_time
	assert coupon.get_date_time_end() == end_time
	assert coupon.get_max_per() == 1
	assert coupon.get_max_use() == 2
	assert coupon.get_active() is True


def coupon_insert_test_insertion_with_price_group():
	price_group = helper.get_price_group('CouponInsertTest_PriceGroup')

	assert isinstance(price_group, merchantapi.model.PriceGroup)
	assert price_group.get_id() > 0

	request = merchantapi.request.CouponInsert(helper.init_client())

	start_time = int(time.time() / 1000) - 1000
	end_time = int(time.time() / 1000) + 100000

	request.set_code('CouponInsertTest_2')\
		.set_description('CouponInsertTest_2 Description')\
		.set_customer_scope(merchantapi.model.Coupon.CUSTOMER_SCOPE_ALL_SHOPPERS)\
		.set_date_time_start(start_time)\
		.set_date_time_end(end_time)\
		.set_max_per(1)\
		.set_max_use(2)\
		.set_active(True)\
		.set_price_group_id(price_group.get_id())

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CouponInsert)

	coupon = helper.get_coupon('CouponInsertTest_2')

	assert isinstance(coupon, merchantapi.model.Coupon)
	assert coupon.get_code() == 'CouponInsertTest_2'
	assert coupon.get_description() == 'CouponInsertTest_2 Description'
	assert coupon.get_customer_scope() == merchantapi.model.Coupon.CUSTOMER_SCOPE_ALL_SHOPPERS
	assert coupon.get_date_time_start() == start_time
	assert coupon.get_date_time_end() == end_time
	assert coupon.get_max_per() == 1
	assert coupon.get_max_use() == 2
	assert coupon.get_active() is True


def coupon_insert_test_duplicate_code():
	request = merchantapi.request.CouponInsert(helper.init_client())

	request.set_code('CouponInsertTest_Duplicate')

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.CouponInsert)


def coupon_insert_test_invalid_price_group():
	request = merchantapi.request.CouponInsert(helper.init_client())

	start_time = int(time.time() / 1000) - 1000
	end_time = int(time.time() / 1000) + 100000

	request.set_code('CouponInsertTest_2')\
		.set_description('CouponInsertTest_2 Description')\
		.set_customer_scope(merchantapi.model.Coupon.CUSTOMER_SCOPE_ALL_SHOPPERS)\
		.set_date_time_start(start_time)\
		.set_date_time_end(end_time)\
		.set_max_per(1)\
		.set_max_use(2)\
		.set_active(True)\
		.set_price_group_id(8569545)

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.CouponInsert)


def test_coupon_update():
	"""
	Tests the Coupon_Update API Call
	"""

	helper.provision_store('Coupon_Update.xml')

	coupon_update_test_update()


def coupon_update_test_update():
	request = merchantapi.request.CouponUpdate(helper.init_client())

	request.set_edit_coupon('CouponUpdateTest')\
		.set_max_use(1000)\
		.set_max_per(2)\
		.set_active(True)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CouponUpdate)

	coupon = helper.get_coupon('CouponUpdateTest')

	assert isinstance(coupon, merchantapi.model.Coupon)
	assert coupon.get_code() == 'CouponUpdateTest'
	assert coupon.get_max_per() == 2
	assert coupon.get_max_use() == 1000
	assert coupon.get_active() is True


def test_customer_list_load_query():
	"""
	Tests the CustomerList_Load_Query API Call
	"""

	helper.provision_store('CustomerList_Load_Query.xml')
	helper.upload_image('graphics/CustomerListLoadQuery1.jpg')
	helper.upload_image('graphics/CustomerListLoadQuery2.jpg')
	helper.upload_image('graphics/CustomerListLoadQuery3.jpg')
	helper.upload_image('graphics/CustomerListLoadQuery4.jpg')
	helper.upload_image('graphics/CustomerListLoadQuery5.jpg')
	helper.upload_image('graphics/CustomerListLoadQuery6.jpg')
	helper.upload_image('graphics/CustomerListLoadQuery7.jpg')

	customer_list_load_query_test_list_load()
	customer_list_load_query_test_list_load_with_custom_fields()


def customer_list_load_query_test_list_load():
	request = merchantapi.request.CustomerListLoadQuery(helper.init_client())

	request.set_filters(request.filter_expression().like('login', 'CustomerListLoadQueryTest_%'))

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CustomerListLoadQuery)

	assert isinstance(response.get_customers(), list)
	assert len(response.get_customers()) == 7

	for i, customer in enumerate(response.get_customers()):
		assert isinstance(customer, merchantapi.model.Customer)
		assert customer.get_login() == 'CustomerListLoadQueryTest_%d' % int(i+1)


def customer_list_load_query_test_list_load_with_custom_fields():
	request = merchantapi.request.CustomerListLoadQuery(helper.init_client())

	request.set_filters(request.filter_expression().like('login', 'CustomerListLoadQueryTest_%'))\
		.add_on_demand_column('CustomField_Values:customfields:CustomerListLoadQueryTest_checkbox')\
		.add_on_demand_column('CustomField_Values:customfields:CustomerListLoadQueryTest_imageupload')\
		.add_on_demand_column('CustomField_Values:customfields:CustomerListLoadQueryTest_text')\
		.add_on_demand_column('CustomField_Values:customfields:CustomerListLoadQueryTest_textarea')\
		.add_on_demand_column('CustomField_Values:customfields:CustomerListLoadQueryTest_dropdown')\
		.set_sort('login', merchantapi.request.CustomerListLoadQuery.SORT_ASCENDING)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CustomerListLoadQuery)

	assert isinstance(response.get_customers(), list)
	assert len(response.get_customers()) == 7

	for i, customer in enumerate(response.get_customers()):
		assert isinstance(customer, merchantapi.model.Customer)
		assert customer.get_login() == 'CustomerListLoadQueryTest_%d' % int(i+1)
		assert isinstance(customer.get_custom_field_values(), merchantapi.model.CustomFieldValues)
		assert customer.get_custom_field_values().has_value('CustomerListLoadQueryTest_checkbox', 'customfields') is True
		assert customer.get_custom_field_values().get_value('CustomerListLoadQueryTest_checkbox', 'customfields') == '1'
		assert customer.get_custom_field_values().has_value('CustomerListLoadQueryTest_imageupload', 'customfields') is True
		assert customer.get_custom_field_values().get_value('CustomerListLoadQueryTest_imageupload', 'customfields') == 'graphics/00000001/CustomerListLoadQuery%d.jpg' % int(i+1)
		assert customer.get_custom_field_values().has_value('CustomerListLoadQueryTest_text', 'customfields') is True
		assert customer.get_custom_field_values().get_value('CustomerListLoadQueryTest_text', 'customfields') == 'CustomerListLoadQueryTest_%d' % int(i+1)
		assert customer.get_custom_field_values().has_value('CustomerListLoadQueryTest_textarea', 'customfields') is True
		assert customer.get_custom_field_values().get_value('CustomerListLoadQueryTest_textarea', 'customfields') == 'CustomerListLoadQueryTest_%d' % int(i+1)
		assert customer.get_custom_field_values().has_value('CustomerListLoadQueryTest_dropdown', 'customfields') is True
		assert customer.get_custom_field_values().get_value('CustomerListLoadQueryTest_dropdown', 'customfields') == 'Option%d' % int(i+1)


def test_customer_delete():
	"""
	Tests the Customer_Delete API Call
	"""

	helper.provision_store('Customer_Delete.xml')

	customer_delete_test_deletion()
	customer_delete_test_invalid_customer()


def customer_delete_test_deletion():
	request = merchantapi.request.CustomerDelete(helper.init_client())

	request.set_edit_customer('CustomerDeleteTest')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CustomerDelete)

	customer = helper.get_customer('CustomerDeleteTest')

	assert customer is None


def customer_delete_test_invalid_customer():
	request = merchantapi.request.CustomerDelete(helper.init_client())

	request.set_edit_customer('InvalidCustomerLogin')

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.CustomerDelete)


def test_customer_insert():
	"""
	Tests the Customer_Insert API Call
	"""

	helper.provision_store('Customer_Insert.xml')

	customer_insert_test_insertion()
	customer_insert_test_insertion_with_custom_fields()
	customer_insert_test_duplicate_customer()


def customer_insert_test_insertion():
	request = merchantapi.request.CustomerInsert(helper.init_client())

	request.set_customer_login('CustomerInsertTest_1') \
		.set_customer_password('P@ssw0rd') \
		.set_customer_password_email('test@coolcommerce.net') \
		.set_customer_bill_first_name('John') \
		.set_customer_bill_last_name('Doe') \
		.set_customer_bill_address1('1234 Some St') \
		.set_customer_bill_address2('Unit 100') \
		.set_customer_bill_city('San Diego') \
		.set_customer_bill_state('CA') \
		.set_customer_bill_zip('92009') \
		.set_customer_bill_country('USA') \
		.set_customer_bill_company('Miva Inc') \
		.set_customer_bill_phone('6191231234') \
		.set_customer_bill_fax('6191234321') \
		.set_customer_bill_email('test@coolcommerce.net') \
		.set_customer_ship_first_name('John') \
		.set_customer_ship_last_name('Deer') \
		.set_customer_ship_address1('4321 Some St') \
		.set_customer_ship_address2('Unit 200') \
		.set_customer_ship_city('San Diego') \
		.set_customer_ship_state('CA') \
		.set_customer_ship_zip('92009') \
		.set_customer_ship_phone('6191231234') \
		.set_customer_ship_fax('6191234321') \
		.set_customer_ship_email('test@coolcommerce.net') \
		.set_customer_ship_country('USA') \
		.set_customer_ship_company('Miva Inc')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CustomerInsert)

	customer = response.get_customer()

	assert isinstance(customer, merchantapi.model.Customer)
	assert customer.get_password_email() == 'test@coolcommerce.net'
	assert customer.get_bill_first_name() == 'John'
	assert customer.get_bill_last_name() == 'Doe'
	assert customer.get_bill_address1() == '1234 Some St'
	assert customer.get_bill_address2() == 'Unit 100'
	assert customer.get_bill_city() == 'San Diego'
	assert customer.get_bill_state() == 'CA'
	assert customer.get_bill_zip() == '92009'
	assert customer.get_bill_country() == 'USA'
	assert customer.get_bill_company() == 'Miva Inc'
	assert customer.get_bill_phone() == '6191231234'
	assert customer.get_bill_fax() == '6191234321'
	assert customer.get_bill_email() == 'test@coolcommerce.net'
	assert customer.get_ship_first_name() == 'John'
	assert customer.get_ship_last_name() == 'Deer'
	assert customer.get_ship_address1() == '4321 Some St'
	assert customer.get_ship_address2() == 'Unit 200'
	assert customer.get_ship_city() == 'San Diego'
	assert customer.get_ship_state() == 'CA'
	assert customer.get_ship_zip() == '92009'
	assert customer.get_ship_phone() == '6191231234'
	assert customer.get_ship_fax() == '6191234321'
	assert customer.get_ship_email() == 'test@coolcommerce.net'
	assert customer.get_ship_country() == 'USA'
	assert customer.get_ship_company() == 'Miva Inc'


def customer_insert_test_insertion_with_custom_fields():
	request = merchantapi.request.CustomerInsert(helper.init_client())

	request.set_customer_login('CustomerInsertTest_2') \
		.set_customer_password('P@ssw0rd') \
		.set_customer_password_email('test@coolcommerce.net') \
		.set_customer_bill_first_name('John') \
		.set_customer_bill_last_name('Doe') \
		.set_customer_bill_address1('1234 Some St') \
		.set_customer_bill_address2('Unit 100') \
		.set_customer_bill_city('San Diego') \
		.set_customer_bill_state('CA') \
		.set_customer_bill_zip('92009') \
		.set_customer_bill_country('USA') \
		.set_customer_bill_company('Miva Inc') \
		.set_customer_bill_phone('6191231234') \
		.set_customer_bill_fax('6191234321') \
		.set_customer_bill_email('test@coolcommerce.net') \
		.set_customer_ship_first_name('John') \
		.set_customer_ship_last_name('Deer') \
		.set_customer_ship_address1('4321 Some St') \
		.set_customer_ship_address2('Unit 200') \
		.set_customer_ship_city('San Diego') \
		.set_customer_ship_state('CA') \
		.set_customer_ship_zip('92009') \
		.set_customer_ship_phone('6191231234') \
		.set_customer_ship_fax('6191234321') \
		.set_customer_ship_email('test@coolcommerce.net') \
		.set_customer_ship_country('USA') \
		.set_customer_ship_company('Miva Inc')

	request.get_custom_field_values()\
		.add_value('CustomerInsertTest_checkbox', 'True', 'customfields')\
		.add_value('CustomerInsertTest_imageupload', 'graphics/00000001/CustomerInsert.jpg', 'customfields')\
		.add_value('CustomerInsertTest_text', 'CustomerInsertTest_2', 'customfields')\
		.add_value('CustomerInsertTest_textarea', 'CustomerInsertTest_2', 'customfields')\
		.add_value('CustomerInsertTest_dropdown', 'Option2', 'customfields')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CustomerInsert)

	customer = helper.get_customer('CustomerInsertTest_2')

	assert isinstance(customer, merchantapi.model.Customer)
	assert customer.get_password_email() == 'test@coolcommerce.net'
	assert customer.get_bill_first_name() == 'John'
	assert customer.get_bill_last_name() == 'Doe'
	assert customer.get_bill_address1() == '1234 Some St'
	assert customer.get_bill_address2() == 'Unit 100'
	assert customer.get_bill_city() == 'San Diego'
	assert customer.get_bill_state() == 'CA'
	assert customer.get_bill_zip() == '92009'
	assert customer.get_bill_country() == 'USA'
	assert customer.get_bill_company() == 'Miva Inc'
	assert customer.get_bill_phone() == '6191231234'
	assert customer.get_bill_fax() == '6191234321'
	assert customer.get_bill_email() == 'test@coolcommerce.net'
	assert customer.get_ship_first_name() == 'John'
	assert customer.get_ship_last_name() == 'Deer'
	assert customer.get_ship_address1() == '4321 Some St'
	assert customer.get_ship_address2() == 'Unit 200'
	assert customer.get_ship_city() == 'San Diego'
	assert customer.get_ship_state() == 'CA'
	assert customer.get_ship_zip() == '92009'
	assert customer.get_ship_phone() == '6191231234'
	assert customer.get_ship_fax() == '6191234321'
	assert customer.get_ship_email() == 'test@coolcommerce.net'
	assert customer.get_ship_country() == 'USA'
	assert customer.get_ship_company() == 'Miva Inc'

	assert isinstance(customer.get_custom_field_values(), merchantapi.model.CustomFieldValues)
	assert customer.get_custom_field_values().has_value('CustomerInsertTest_checkbox', 'customfields') is True
	assert customer.get_custom_field_values().get_value('CustomerInsertTest_checkbox', 'customfields') == '1'
	assert customer.get_custom_field_values().has_value('CustomerInsertTest_imageupload', 'customfields') is True
	assert customer.get_custom_field_values().get_value('CustomerInsertTest_imageupload', 'customfields') == 'graphics/00000001/CustomerInsert.jpg'
	assert customer.get_custom_field_values().has_value('CustomerInsertTest_text', 'customfields') is True
	assert customer.get_custom_field_values().get_value('CustomerInsertTest_text', 'customfields') == 'CustomerInsertTest_2'
	assert customer.get_custom_field_values().has_value('CustomerInsertTest_textarea', 'customfields') is True
	assert customer.get_custom_field_values().get_value('CustomerInsertTest_textarea', 'customfields') == 'CustomerInsertTest_2'
	assert customer.get_custom_field_values().has_value('CustomerInsertTest_dropdown', 'customfields') is True
	assert customer.get_custom_field_values().get_value('CustomerInsertTest_dropdown', 'customfields') == 'Option2'


def customer_insert_test_duplicate_customer():
	request = merchantapi.request.CustomerInsert(helper.init_client())

	request.set_customer_login('CustomerInsertTest_Duplicate') \
		.set_customer_password('P@ssw0rd') \
		.set_customer_password_email('test@coolcommerce.net') \

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.CustomerInsert)


def test_customer_update():
	"""
	Tests the Customer_Update API Call
	"""

	helper.provision_store('Customer_Update.xml')

	customer_update_test_update()


def customer_update_test_update():
	request = merchantapi.request.CustomerUpdate(helper.init_client())

	request.set_edit_customer('CustomerUpdateTest_01') \
		.set_customer_password_email('test@coolcommerce.net') \
		.set_customer_bill_first_name('John') \
		.set_customer_bill_last_name('Doe') \
		.set_customer_bill_address1('1234 Some St') \
		.set_customer_bill_address2('Unit 100') \
		.set_customer_bill_city('San Diego') \
		.set_customer_bill_state('CA') \
		.set_customer_bill_zip('92009') \
		.set_customer_bill_country('USA') \
		.set_customer_bill_company('Miva Inc') \
		.set_customer_bill_phone('6191231234') \
		.set_customer_bill_fax('6191234321') \
		.set_customer_bill_email('test@coolcommerce.net') \
		.set_customer_ship_first_name('John') \
		.set_customer_ship_last_name('Deer') \
		.set_customer_ship_address1('4321 Some St') \
		.set_customer_ship_address2('Unit 200') \
		.set_customer_ship_city('San Diego') \
		.set_customer_ship_state('CA') \
		.set_customer_ship_zip('92009') \
		.set_customer_ship_phone('6191231234') \
		.set_customer_ship_fax('6191234321') \
		.set_customer_ship_email('test@coolcommerce.net') \
		.set_customer_ship_country('USA') \
		.set_customer_ship_company('Miva Inc')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CustomerUpdate)

	customer = helper.get_customer('CustomerUpdateTest_01')

	assert isinstance(customer, merchantapi.model.Customer)
	assert customer.get_password_email() == 'test@coolcommerce.net'
	assert customer.get_bill_first_name() == 'John'
	assert customer.get_bill_last_name() == 'Doe'
	assert customer.get_bill_address1() == '1234 Some St'
	assert customer.get_bill_address2() == 'Unit 100'
	assert customer.get_bill_city() == 'San Diego'
	assert customer.get_bill_state() == 'CA'
	assert customer.get_bill_zip() == '92009'
	assert customer.get_bill_country() == 'USA'
	assert customer.get_bill_company() == 'Miva Inc'
	assert customer.get_bill_phone() == '6191231234'
	assert customer.get_bill_fax() == '6191234321'
	assert customer.get_bill_email() == 'test@coolcommerce.net'
	assert customer.get_ship_first_name() == 'John'
	assert customer.get_ship_last_name() == 'Deer'
	assert customer.get_ship_address1() == '4321 Some St'
	assert customer.get_ship_address2() == 'Unit 200'
	assert customer.get_ship_city() == 'San Diego'
	assert customer.get_ship_state() == 'CA'
	assert customer.get_ship_zip() == '92009'
	assert customer.get_ship_phone() == '6191231234'
	assert customer.get_ship_fax() == '6191234321'
	assert customer.get_ship_email() == 'test@coolcommerce.net'
	assert customer.get_ship_country() == 'USA'
	assert customer.get_ship_company() == 'Miva Inc'


def test_customer_payment_card_register():
	"""
	Tests the CustomerPaymentCard_Register API Call
	"""

	helper.provision_store('CustomerPaymentCard_Register.xml')

	customer_payment_card_register_test_register_card()


def customer_payment_card_register_test_register_card():
	request = merchantapi.request.CustomerPaymentCardRegister(helper.init_client())

	request.set_customer_login('CustomerPaymentCardRegisterTest')\
		.set_first_name('John')\
		.set_last_name('Doe')\
		.set_card_type('Visa')\
		.set_card_number('4111111111111111')\
		.set_expiration_month(8)\
		.set_expiration_year(2025)\
		.set_address1('1234 Test St')\
		.set_address2('Unit 123')\
		.set_city('San Diego')\
		.set_state('CA')\
		.set_zip('92009')\
		.set_country('US')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CustomerPaymentCardRegister)

	card = response.get_customer_payment_card()

	assert isinstance(card, merchantapi.model.CustomerPaymentCard)
	assert card.get_token() is not None
	assert card.get_first_name() == 'John'
	assert card.get_last_name() == 'Doe'
	assert card.get_type() == 'Visa'
	assert card.get_last_four() == '1111'
	assert card.get_expiration_month() == 8
	assert card.get_expiration_year() == 2025
	assert card.get_address1() == '1234 Test St'
	assert card.get_address2() == 'Unit 123'
	assert card.get_city() == 'San Diego'
	assert card.get_state() == 'CA'
	assert card.get_zip() == '92009'
	assert card.get_country() == 'US'


def test_module():
	"""
	Tests the Module API Call
	"""

	module_test_invalid_module()


def module_test_invalid_module():
	request = merchantapi.request.Module(helper.init_client())

	request.set_module_code('InvalidModule')\
		.set_module_function('InvalidModuleFunction')

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.Module)


def test_note_list_load_query():
	"""
	Tests the NoteList_Load_Query API Call
	"""

	helper.provision_store('NoteList_Load_Query.xml')

	note_list_load_query_test_list_load()


def note_list_load_query_test_list_load():
	request = merchantapi.request.NoteListLoadQuery(helper.init_client())

	request.set_filters(
		request.filter_expression()
		.equal('cust_login', 'NoteListLoadQuery_Customer_1')
		.and_equal('order_id', 10520)
		.and_equal('business_title', 'NoteListLoadQuery_BusinessAccount_1')
	)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.NoteListLoadQuery)

	assert isinstance(response.get_notes(), list)
	assert len(response.get_notes()) == 6

	for note in response.get_notes():
		assert isinstance(note, merchantapi.model.Note)
		assert note.get_business_title() == 'NoteListLoadQuery_BusinessAccount_1'
		assert note.get_customer_login() == 'NoteListLoadQuery_Customer_1'
		assert note.get_order_id() == 10520
		assert note.get_note_text() == 'This note should be customer NoteListLoadQuery_Customer_1 and order 10520 and business NoteListLoadQuery_BusinessAccount_1'


def test_note_delete():
	"""
	Tests the Note_Delete API Call
	"""

	helper.provision_store('Note_Delete.xml')

	note_delete_test_deletion_by_business_account()
	note_delete_test_deletion_by_customer()


def note_delete_test_deletion_by_business_account():
	note = helper.get_note('business_title', 'NoteDeleteTest_BusinessAccount')

	assert isinstance(note, merchantapi.model.Note)

	request = merchantapi.request.NoteDelete(helper.init_client(), note)

	assert request.get_note_id() == note.get_id()

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.NoteDelete)


def note_delete_test_deletion_by_customer():
	note = helper.get_note('cust_login', 'NoteDeleteTest_Customer')

	assert isinstance(note, merchantapi.model.Note)

	request = merchantapi.request.NoteDelete(helper.init_client(), note)

	assert request.get_note_id() == note.get_id()

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.NoteDelete)


def test_note_insert():
	"""
	Tests the Note_Insert API Call
	"""

	helper.provision_store('Note_Insert.xml')

	note_insert_test_insertion_by_customer()
	note_insert_test_insertion_by_order()
	note_insert_test_invalid_customer()
	note_insert_test_invalid_order()


def note_insert_test_insertion_by_customer():
	customer = helper.get_customer('NoteInsertTest_Customer')

	assert isinstance(customer, merchantapi.model.Customer)

	request = merchantapi.request.NoteInsert(helper.init_client())

	request.set_customer_id(customer.get_id())\
		.set_note_text('API Inserted Customer Note')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.NoteInsert)


def note_insert_test_insertion_by_order():
	request = merchantapi.request.NoteInsert(helper.init_client())

	request.set_order_id(592745)\
		.set_note_text('API Inserted Customer Note')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.NoteInsert)


def note_insert_test_invalid_customer():
	request = merchantapi.request.NoteInsert(helper.init_client())

	request.set_customer_id(int(time.time()))\
		.set_note_text('API Inserted Customer Note')

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.NoteInsert)


def note_insert_test_invalid_order():
	request = merchantapi.request.NoteInsert(helper.init_client())

	request.set_order_id(int(time.time()))\
		.set_note_text('API Inserted Customer Note')

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.NoteInsert)


def test_note_update():
	"""
	Tests the Note_Update API Call
	"""

	helper.provision_store('Note_Update.xml')

	note_update_test_update()


def note_update_test_update():
	notes_request = merchantapi.request.NoteListLoadQuery(helper.init_client())

	notes_request.set_filters(
		notes_request.filter_expression()
		.equal('cust_login', 'NoteUpdateTest_Customer')
		.or_equal('business_title', 'NoteUpdateTest_BusinessAccount')
		.or_equal('order_id', 978375551)
	)

	notes_response = notes_request.send()

	helper.validate_response_success(notes_response, merchantapi.response.NoteListLoadQuery)

	notes = notes_response.get_notes()

	assert isinstance(notes, list)
	assert len(notes) > 2

	request = merchantapi.request.NoteUpdate(helper.init_client())
	note_text = 'New Note Text %d' % int(time.time())

	request.set_note_id(notes[0].get_id())\
		.set_note_text(note_text)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.NoteUpdate)

	note = helper.get_note('id', notes[0].get_id())

	assert isinstance(note, merchantapi.model.Note)
	assert note.get_note_text() == note_text


def test_order_custom_field_list_load():
	"""
	Tests the OrderCustomFieldList_Load API Call
	"""

	helper.provision_store('OrderCustomFieldList_Load.xml')

	order_custom_field_list_load_test_list_load()


def order_custom_field_list_load_test_list_load():
	request = merchantapi.request.OrderCustomFieldListLoad(helper.init_client())

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderCustomFieldListLoad)

	assert isinstance(response.get_order_custom_fields(), list)
	assert len(response.get_order_custom_fields()) > 1

	for ocf in response.get_order_custom_fields():
		assert isinstance(ocf, merchantapi.model.OrderCustomField)


def test_order_custom_fields_update():
	"""
	Tests the OrderCustomFields_Update API Call
	"""

	helper.provision_store('OrderCustomFields_Update.xml')

	order_custom_fields_update_test_update()


def order_custom_fields_update_test_update():
	request = merchantapi.request.OrderCustomFieldsUpdate(helper.init_client())

	request.set_order_id(65191651)

	request.get_custom_field_values()\
		.add_value('OrderCustomFieldsUpdate_Field_1', 'foobar')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderCustomFieldsUpdate)

	order = helper.get_order(65191651)

	assert isinstance(order, merchantapi.model.Order)
	assert isinstance(order.get_custom_field_values(), merchantapi.model.CustomFieldValues)
	assert order.get_custom_field_values().get_value('OrderCustomFieldsUpdate_Field_1') == 'foobar'


def test_order_item_list_back_order():
	"""
	Tests the OrderItemList_BackOrder API Call
	"""

	helper.provision_store('OrderItemList_BackOrder.xml')

	order_item_list_back_order_test_backorder()
	order_item_list_back_order_test_add_items_from_orderitem_instance()


def order_item_list_back_order_test_backorder():
	order = helper.get_order(678566)

	assert isinstance(order, merchantapi.model.Order)

	isdate = int(time.time()) + int(random.random() + 1000)

	request = merchantapi.request.OrderItemListBackOrder(helper.init_client(), order)

	assert request.get_order_id() == order.get_id()

	request.set_date_in_stock(isdate)

	for item in order.get_items():
		request.add_line_id(item.get_line_id())

	assert len(order.get_items()) == len(request.get_line_ids())

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderItemListBackOrder)

	checkorder = helper.get_order(678566)

	assert isinstance(checkorder, merchantapi.model.Order)
	assert checkorder.get_date_in_stock() == isdate

	for item in checkorder.get_items():
		assert item.get_status() == merchantapi.model.OrderItem.ORDER_ITEM_STATUS_BACKORDERED


def order_item_list_back_order_test_add_items_from_orderitem_instance():
	item1 = merchantapi.model.OrderItem({'line_id': 123})
	item2 = merchantapi.model.OrderItem({'line_id': 456})

	request = merchantapi.request.OrderItemListBackOrder(helper.init_client())

	request.add_order_item(item1)\
		.add_order_item(item2)

	lines = request.get_line_ids()

	assert isinstance(lines, list)
	assert len(lines) == 2
	assert 123 in lines
	assert 456 in lines


def test_order_item_list_cancel():
	"""
	Tests the OrderItemList_Cancel API Call
	"""

	helper.provision_store('OrderItemList_Cancel.xml')

	order_item_list_cancel_test_cancel()
	order_item_list_cancel_test_add_items_from_orderitem_instance()


def order_item_list_cancel_test_cancel():
	order = helper.get_order(678567)

	assert isinstance(order, merchantapi.model.Order)
	assert isinstance(order.get_items(), list)
	assert len(order.get_items()) == 4

	request = merchantapi.request.OrderItemListCancel(helper.init_client(), order)

	assert request.get_order_id() == order.get_id()

	request.set_reason('API Test')

	for item in order.get_items():
		request.add_line_id(item.get_line_id())

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderItemListCancel)

	order = helper.get_order(678567)

	assert isinstance(order, merchantapi.model.Order)
	assert isinstance(order.get_items(), list)
	assert len(order.get_items()) == 4

	for item in order.get_items():
		assert isinstance(item, merchantapi.model.OrderItem)
		assert item.get_status() == merchantapi.model.OrderItem.ORDER_ITEM_STATUS_CANCELLED
		assert isinstance(item.get_options(), list)
		assert len(item.get_options()) == 1
		assert item.get_options()[0].get_attribute_code() == 'Cancellation Reason'
		assert item.get_options()[0].get_value() == 'API Test'


def order_item_list_cancel_test_add_items_from_orderitem_instance():
	item1 = merchantapi.model.OrderItem({'line_id': 123})
	item2 = merchantapi.model.OrderItem({'line_id': 456})

	request = merchantapi.request.OrderItemListCancel(helper.init_client())

	request.add_order_item(item1)\
		.add_order_item(item2)

	lines = request.get_line_ids()

	assert isinstance(lines, list)
	assert len(lines) == 2
	assert 123 in lines
	assert 456 in lines


def test_order_item_list_create_shipment():
	"""
	Tests the OrderItemList_CreateShipment API Call
	"""

	helper.provision_store('OrderItemList_CreateShipment.xml')

	order_item_list_create_shipment_test_create_shipment()
	order_item_list_create_shipment_test_add_items_from_orderitem_instance()


def order_item_list_create_shipment_test_create_shipment():
	order = helper.get_order(678570)

	assert isinstance(order, merchantapi.model.Order)

	request = merchantapi.request.OrderItemListCreateShipment(helper.init_client(), order)

	assert request.get_order_id() == order.get_id()

	for item in order.get_items():
		request.add_line_id(item.get_line_id())

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderItemListCreateShipment)

	assert isinstance(response.get_order_shipment(), merchantapi.model.OrderShipment)
	assert order.get_id() == response.get_order_shipment().get_order_id()
	assert response.get_order_shipment().get_id() > 0


def order_item_list_create_shipment_test_add_items_from_orderitem_instance():
	item1 = merchantapi.model.OrderItem({'line_id': 123})
	item2 = merchantapi.model.OrderItem({'line_id': 456})

	request = merchantapi.request.OrderItemListCreateShipment(helper.init_client())

	request.add_order_item(item1)\
		.add_order_item(item2)

	lines = request.get_line_ids()

	assert isinstance(lines, list)
	assert len(lines) == 2
	assert 123 in lines
	assert 456 in lines


def test_order_item_list_delete():
	"""
	Tests the OrderItemList_Delete API Call
	"""

	helper.provision_store('OrderItemList_Delete.xml')

	order_item_list_delete_test_deletion()
	order_item_list_delete_test_add_items_from_orderitem_instance()


def order_item_list_delete_test_deletion():
	order = helper.get_order(678568)

	assert isinstance(order, merchantapi.model.Order)
	assert isinstance(order.get_items(), list)
	assert len(order.get_items()) == 4

	request = merchantapi.request.OrderItemListDelete(helper.init_client(), order)

	assert request.get_order_id() == order.get_id()

	for item in order.get_items():
		request.add_line_id(item.get_line_id())

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderItemListDelete)

	order = helper.get_order(678568)

	assert isinstance(order, merchantapi.model.Order)
	assert isinstance(order.get_items(), list)
	assert len(order.get_items()) == 0


def order_item_list_delete_test_add_items_from_orderitem_instance():
	item1 = merchantapi.model.OrderItem({'line_id': 123})
	item2 = merchantapi.model.OrderItem({'line_id': 456})

	request = merchantapi.request.OrderItemListDelete(helper.init_client())

	request.add_order_item(item1)\
		.add_order_item(item2)

	lines = request.get_line_ids()

	assert isinstance(lines, list)
	assert len(lines) == 2
	assert 123 in lines
	assert 456 in lines


def test_order_item_add():
	"""
	Tests the OrderItem_Add API Call
	"""

	helper.provision_store('OrderItem_Add.xml')

	order_item_add_test_insertion()
	order_item_add_test_add_product()
	order_item_add_test_add_product_with_option()
	order_item_add_test_insertion_with_attribute()
	order_item_add_test_insertion_with_invalid_attribute()


def order_item_add_test_insertion():
	request = merchantapi.request.OrderItemAdd(helper.init_client())

	request.set_order_id(678565)\
		.set_code('OrderItemAddTest_Foo')\
		.set_quantity(2)\
		.set_price(10.00)\
		.set_taxable(True)\
		.set_weight(1.00)\
		.set_sku('OrderItemAddTest_Foo_SKU')\
		.set_name('OrderItemAddTest - Foo')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderItemAdd)

	assert isinstance(response.get_order_total(), merchantapi.model.OrderTotal)
	assert response.get_order_total().get_total() == 20.00
	assert response.get_order_total().get_formatted_total() == '$20.00'

	order = helper.get_order(678565)

	assert isinstance(order, merchantapi.model.Order)
	assert isinstance(order.get_items(), list)
	assert len(order.get_items()) == 1

	item = order.get_items()[0]

	assert isinstance(item, merchantapi.model.OrderItem)
	assert item.get_code() == 'OrderItemAddTest_Foo'
	assert item.get_quantity() == 2
	assert item.get_price() == 10.00
	assert item.get_weight() == 1.00
	assert item.get_sku() == 'OrderItemAddTest_Foo_SKU'
	assert item.get_name() == 'OrderItemAddTest - Foo'


def order_item_add_test_add_product():
	request = merchantapi.request.OrderItemAdd(helper.init_client())

	request.set_order_id(678566) \
		.set_code('OrderItemAddTest_Product') \
		.set_quantity(1) \
		.set_price(9.99) \
		.set_name('OrderItemAddTest_Product')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderItemAdd)

	assert isinstance(response.get_order_total(), merchantapi.model.OrderTotal)
	assert response.get_order_total().get_total() == 9.99
	assert response.get_order_total().get_formatted_total() == '$9.99'

	order = helper.get_order(678566)

	assert isinstance(order, merchantapi.model.Order)
	assert isinstance(order.get_items(), list)
	assert len(order.get_items()) == 1

	item = order.get_items()[0]

	assert isinstance(item, merchantapi.model.OrderItem)
	assert item.get_code() == 'OrderItemAddTest_Product'
	assert item.get_quantity() == 1
	assert item.get_name() == 'OrderItemAddTest_Product'


def order_item_add_test_add_product_with_option():
	request = merchantapi.request.OrderItemAdd(helper.init_client())

	request.set_order_id(678567) \
		.set_code('OrderItemAddTest_Product_2') \
		.set_quantity(1) \
		.set_price(12.99) \
		.set_name('OrderItemAddTest_Product_2')

	option = merchantapi.model.OrderItemOption()

	option.set_attribute_code('color')\
		.set_value('red')

	request.add_option(option)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderItemAdd)

	assert isinstance(response.get_order_total(), merchantapi.model.OrderTotal)
	assert response.get_order_total().get_total() == 12.99
	assert response.get_order_total().get_formatted_total() == '$12.99'


def order_item_add_test_insertion_with_attribute():
	request = merchantapi.request.OrderItemAdd(helper.init_client())

	request.set_order_id(678568) \
		.set_code('OrderItemAddTest_ItemWOptions') \
		.set_quantity(1) \
		.set_price(12.99) \
		.set_name('OrderItemAddTest_ItemWOptions')

	option = merchantapi.model.OrderItemOption()

	option.set_attribute_code('foo')\
		.set_value('bar')\
		.set_price(3.29)\
		.set_weight(1.25)

	request.add_option(option)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderItemAdd)

	assert isinstance(response.get_order_total(), merchantapi.model.OrderTotal)
	assert response.get_order_total().get_total() == 16.28
	assert response.get_order_total().get_formatted_total() == '$16.28'


def order_item_add_test_insertion_with_invalid_attribute():
	request = merchantapi.request.OrderItemAdd(helper.init_client())

	request.set_order_id(678568) \
		.set_code('OrderItemAddTest_ItemWOptions') \
		.set_quantity(1) \
		.set_price(12.99) \
		.set_name('OrderItemAddTest_ItemWOptions')

	option = merchantapi.model.OrderItemOption()

	option.set_attribute_code('')\
		.set_value('')

	request.add_option(option)

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.OrderItemAdd)


def test_order_item_update():
	"""
	Tests the OrderItem_Update API Call
	"""

	helper.provision_store('OrderItem_Update.xml')

	order_item_update_test_update()
	order_item_update_test_update_with_existing_attribute()


def order_item_update_test_update():
	order = helper.get_order(678569)

	assert isinstance(order, merchantapi.model.Order)
	assert isinstance(order.get_items(), list)
	assert len(order.get_items()) == 2

	item1 = order.get_items()[0]

	request = merchantapi.request.OrderItemUpdate(helper.init_client(), item1)

	assert request.get_line_id() == item1.get_line_id()

	request.set_order_id(order.get_id())\
		.set_line_id(item1.get_line_id())\
		.set_quantity(item1.get_quantity() + 1)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderItemUpdate)


def order_item_update_test_update_with_existing_attribute():
	order = helper.get_order(678570)

	assert isinstance(order, merchantapi.model.Order)
	assert isinstance(order.get_items(), list)
	assert len(order.get_items()) == 1

	item1 = order.get_items()[0]

	request = merchantapi.request.OrderItemUpdate(helper.init_client(), item1)

	assert request.get_line_id() == item1.get_line_id()
	assert isinstance(item1.get_options(), list)
	assert len(item1.get_options()) == 1
	assert isinstance(item1.get_options()[0], merchantapi.model.OrderItemOption)

	request.set_order_id(order.get_id())\
		.set_line_id(item1.get_line_id())\
		.set_quantity(item1.get_quantity() + 2)

	request.get_options()[0].set_value('BIN')\
		.set_price(29.99)\
		.set_weight(15.00)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderItemUpdate)

	order = helper.get_order(678570)

	assert isinstance(order, merchantapi.model.Order)
	assert isinstance(order.get_items(), list)
	assert len(order.get_items()) == 1

	item = order.get_items()[0]

	assert isinstance(item, merchantapi.model.OrderItem)
	assert isinstance(item.get_options(), list)
	assert len(item.get_options()) == 1

	option = item.get_options()[0]

	assert isinstance(option, merchantapi.model.OrderItemOption)
	assert option.get_price() == 29.99
	assert option.get_weight() == 15.00


def test_order_list_load_query():
	"""
	Tests the OrderList_Load_Query API Call
	"""

	helper.provision_store('OrderList_Load_Query.xml')
	helper.upload_image('graphics/OrderListLoadQuery1.jpg')
	helper.upload_image('graphics/OrderListLoadQuery2.jpg')
	helper.upload_image('graphics/OrderListLoadQuery3.jpg')
	helper.upload_image('graphics/OrderListLoadQuery4.jpg')
	helper.upload_image('graphics/OrderListLoadQuery5.jpg')
	helper.upload_image('graphics/OrderListLoadQuery6.jpg')
	helper.upload_image('graphics/OrderListLoadQuery7.jpg')

	order_list_load_query_test_list_load()
	order_list_load_query_test_list_load_with_custom_fields()


def order_list_load_query_test_list_load():
	request = merchantapi.request.OrderListLoadQuery(helper.init_client())

	request.set_filters(request.filter_expression().equal('cust_login', 'OrderListLoadQueryTest_Cust1')) \
		.add_on_demand_column('cust_login')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderListLoadQuery)

	assert isinstance(response.get_orders(), list)
	assert len(response.get_orders()) == 7

	for order in response.get_orders():
		assert isinstance(order, merchantapi.model.Order)
		assert order.get_customer_login() == 'OrderListLoadQueryTest_Cust1'
		assert order.get_id() in [678571, 678572, 678573, 678574, 678575, 678576, 678577]


def order_list_load_query_test_list_load_with_custom_fields():
	request = merchantapi.request.OrderListLoadQuery(helper.init_client())

	request.set_filters(request.filter_expression().equal('cust_login', 'OrderListLoadQueryTest_Cust1')) \
		.set_on_demand_columns([
			'ship_method',
			'cust_login',
			'cust_pw_email',
			'business_title',
			'payment_module',
			'customer',
			'items',
			'charges',
			'coupons',
			'discounts',
			'payments',
			'notes'
		]) \
		.add_on_demand_column('CustomField_Values:customfields:OrderListLoadQueryTest_checkbox') \
		.add_on_demand_column('CustomField_Values:customfields:OrderListLoadQueryTest_imageupload') \
		.add_on_demand_column('CustomField_Values:customfields:OrderListLoadQueryTest_text') \
		.add_on_demand_column('CustomField_Values:customfields:OrderListLoadQueryTest_textarea') \
		.add_on_demand_column('CustomField_Values:customfields:OrderListLoadQueryTest_dropdown')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderListLoadQuery)

	assert isinstance(response.get_orders(), list)
	assert len(response.get_orders()) == 7

	for i, order in enumerate(response.get_orders()):
		assert isinstance(order, merchantapi.model.Order)
		assert order.get_customer_login() == 'OrderListLoadQueryTest_Cust1'
		assert order.get_id() in [678571, 678572, 678573, 678574, 678575, 678576, 678577]
		assert order.get_custom_field_values().has_value('OrderListLoadQueryTest_checkbox', 'customfields') is True
		assert order.get_custom_field_values().get_value('OrderListLoadQueryTest_checkbox', 'customfields') == '1'
		assert order.get_custom_field_values().has_value('OrderListLoadQueryTest_imageupload', 'customfields') is True
		assert order.get_custom_field_values().get_value('OrderListLoadQueryTest_imageupload', 'customfields') == 'graphics/00000001/OrderListLoadQuery%d.jpg' % int(i+1)
		assert order.get_custom_field_values().has_value('OrderListLoadQueryTest_text', 'customfields') is True
		assert order.get_custom_field_values().get_value('OrderListLoadQueryTest_text', 'customfields') == 'OrderListLoadQueryTest_%d' % int(i + 1)
		assert order.get_custom_field_values().has_value('OrderListLoadQueryTest_textarea', 'customfields') is True
		assert order.get_custom_field_values().get_value('OrderListLoadQueryTest_textarea', 'customfields') == 'OrderListLoadQueryTest_%d' % int(i + 1)
		assert order.get_custom_field_values().has_value('OrderListLoadQueryTest_dropdown', 'customfields') is True
		assert order.get_custom_field_values().get_value('OrderListLoadQueryTest_dropdown', 'customfields') == 'Option%d' % int(i + 1)


def test_order_shipment_list_update():
	"""
	Tests the OrderShipmentList_Update API Call
	"""

	helper.provision_store('OrderShipmentList_Update.xml')

	order_shipment_list_update_test_update()


def order_shipment_list_update_test_update():
	request = merchantapi.request.OrderShipmentListUpdate(helper.init_client())
	update = merchantapi.model.OrderShipmentUpdate()

	update.set_cost(1.00) \
		.set_mark_shipped(True) \
		.set_shipment_id(100) \
		.set_tracking_number('Z12312312313') \
		.set_tracking_type('UPS')

	request.add_shipment_update(update)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderShipmentListUpdate)


def test_order_create():
	"""
	Tests the Order_Create API Call
	"""

	helper.provision_store('Order_Create.xml')

	order_create_test_creation()
	order_create_test_creation_with_customer()
	order_create_test_invalid_customer()
	order_create_test_with_customer_info()
	order_create_test_creation_with_everything()


def order_create_test_creation():
	request = merchantapi.request.OrderCreate(helper.init_client())

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderCreate)

	assert isinstance(response.get_order(), merchantapi.model.Order)
	assert response.get_order().get_id() > 0


def order_create_test_creation_with_customer():
	request = merchantapi.request.OrderCreate(helper.init_client())

	request.set_customer_login('OrderCreateTest_Cust_1')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderCreate)

	assert isinstance(response.get_order(), merchantapi.model.Order)
	assert response.get_order().get_id() > 0
	assert response.get_order().get_customer_id() > 0


def order_create_test_invalid_customer():
	request = merchantapi.request.OrderCreate(helper.init_client())

	request.set_customer_login('InvalidCustomer')

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.OrderCreate)


def order_create_test_with_customer_info():
	request = merchantapi.request.OrderCreate(helper.init_client())

	request.set_ship_first_name('Joe') \
		.set_ship_last_name('Dirt') \
		.set_ship_email('test@coolcommerce.net') \
		.set_ship_phone('6191231234') \
		.set_ship_fax('6191234321') \
		.set_ship_company('Dierte Inc') \
		.set_ship_address1('1234 Test Ave') \
		.set_ship_address2('Unit 100') \
		.set_ship_city('San Diego') \
		.set_ship_state('CA') \
		.set_ship_zip('92009') \
		.set_ship_country('USA') \
		.set_ship_residential(True) \
		.set_bill_first_name('Joe') \
		.set_bill_last_name('Dirt') \
		.set_bill_email('test@coolcommerce.net') \
		.set_bill_phone('6191231234') \
		.set_bill_fax('6191234321') \
		.set_bill_company('Dierte Inc') \
		.set_bill_address1('1234 Test Ave') \
		.set_bill_address2('Unit 100') \
		.set_bill_city('San Diego') \
		.set_bill_state('CA') \
		.set_bill_zip('92009') \
		.set_bill_country('US') \
		.set_calculate_charges(False) \
		.set_trigger_fulfillment_modules(False)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderCreate)

	assert isinstance(response.get_order(), merchantapi.model.Order)
	assert response.get_order().get_id() > 0
	assert isinstance(response.get_order(), merchantapi.model.Order)
	assert response.get_order().get_id() > 0
	assert response.get_order().get_ship_first_name() == 'Joe'
	assert response.get_order().get_ship_last_name() == 'Dirt'
	assert response.get_order().get_ship_email() == 'test@coolcommerce.net'
	assert response.get_order().get_ship_phone() == '6191231234'
	assert response.get_order().get_ship_fax() == '6191234321'
	assert response.get_order().get_ship_company() == 'Dierte Inc'
	assert response.get_order().get_ship_address1() == '1234 Test Ave'
	assert response.get_order().get_ship_address2() == 'Unit 100'
	assert response.get_order().get_ship_city() == 'San Diego'
	assert response.get_order().get_ship_state() == 'CA'
	assert response.get_order().get_ship_zip() == '92009'
	assert response.get_order().get_ship_country() == 'USA'
	assert response.get_order().get_ship_residential() is True
	assert response.get_order().get_bill_first_name() == 'Joe'
	assert response.get_order().get_bill_last_name() == 'Dirt'
	assert response.get_order().get_bill_email() == 'test@coolcommerce.net'
	assert response.get_order().get_bill_phone() == '6191231234'
	assert response.get_order().get_bill_fax() == '6191234321'
	assert response.get_order().get_bill_company() == 'Dierte Inc'
	assert response.get_order().get_bill_address1() == '1234 Test Ave'
	assert response.get_order().get_bill_address2() == 'Unit 100'
	assert response.get_order().get_bill_city() == 'San Diego'
	assert response.get_order().get_bill_state() == 'CA'
	assert response.get_order().get_bill_zip() == '92009'
	assert response.get_order().get_bill_country() == 'US'


def order_create_test_creation_with_everything():
	request = merchantapi.request.OrderCreate(helper.init_client())
	charge = merchantapi.model.OrderCharge()
	item = merchantapi.model.OrderItem()
	item_opt = merchantapi.model.OrderItemOption()
	product = merchantapi.model.OrderProduct()
	prod_attr = merchantapi.model.OrderProductAttribute()

	charge.set_description('foo') \
		.set_amount(29.99) \
		.set_type('API')

	item.set_name('Test Custom Line') \
		.set_code('CUSTOM_LINE') \
		.set_price(15.00) \
		.set_quantity(1)

	item_opt.set_attribute_code('option')\
		.set_value('option_data') \
		.set_price(5.00) \
		.set_weight(1.00)

	item.add_option(item_opt)

	product.set_code('OrderCreateTest_Prod_3') \
		.set_quantity(1)

	prod_attr.set_code('color') \
		.set_value('red')

	product.add_attribute(prod_attr)

	request.set_customer_login('OrderCreateTest_Cust_2') \
		.set_calculate_charges(False) \
		.set_trigger_fulfillment_modules(False) \
		.add_charge(charge) \
		.add_item(item) \
		.add_product(product)

	request.get_custom_field_values() \
		.add_value('OrderCreateTest_1', 'foo') \
		.add_value('OrderCreateTest_2', 'bar') \
		.add_value('OrderCreateTest_3', 'baz', 'customfields')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderCreate)

	assert isinstance(response.get_order(), merchantapi.model.Order)
	assert response.get_order().get_id() > 0

	order = helper.get_order(response.get_order().get_id())

	assert isinstance(order, merchantapi.model.Order)
	assert order.get_id() == response.get_order().get_id()
	assert order.get_customer_login() == 'OrderCreateTest_Cust_2'
	assert isinstance(order.get_items(), list)
	assert len(order.get_items()) == 2

	item1 = order.get_items()[0]

	assert item1.get_code() == 'CUSTOM_LINE'
	assert item1.get_price() == 15.00
	assert isinstance(item1.get_options(), list)
	assert len(item1.get_options()) == 1

	item1_option1 = item1.get_options()[0]

	assert item1_option1.get_attribute_code() == 'option'
	assert item1_option1.get_value() == 'option_data'
	assert item1_option1.get_price() == 5.00
	assert item1_option1.get_weight() == 1.00

	item2 = order.get_items()[1]

	assert item2.get_code() == 'OrderCreateTest_Prod_3'
	assert item2.get_price() == 4.00
	assert isinstance(item2.get_options(), list)
	assert len(item2.get_options()) == 1

	item2_option1 = item2.get_options()[0]

	assert item2_option1.get_attribute_code() == 'color'
	assert item2_option1.get_value() == 'red'
	assert item2_option1.get_price() == 5.99
	assert item2_option1.get_weight() == 1.21

	assert isinstance(order.get_charges(), list)
	assert len(order.get_charges()) == 1

	charge = order.get_charges()[0]

	assert isinstance(charge, merchantapi.model.OrderCharge)
	assert charge.get_description() == 'foo'
	assert charge.get_amount() == 29.99
	assert charge.get_type() == 'API'

	assert isinstance(order.get_customer(), merchantapi.model.Customer)
	assert order.get_customer().get_login() == 'OrderCreateTest_Cust_2'
	assert isinstance(order.get_custom_field_values(), merchantapi.model.CustomFieldValues)
	assert order.get_custom_field_values().get_value('OrderCreateTest_1') == 'foo'
	assert order.get_custom_field_values().get_value('OrderCreateTest_2') == 'bar'
	assert order.get_custom_field_values().get_value('OrderCreateTest_3') == 'baz'


def test_order_delete():
	"""
	Tests the Order_Delete API Call
	"""

	order_delete_test_deletion()


def order_delete_test_deletion():
	createrequest = merchantapi.request.OrderCreate(helper.init_client())

	createresponse = createrequest.send()

	helper.validate_response_success(createresponse, merchantapi.response.OrderCreate)

	assert isinstance(createresponse.get_order(), merchantapi.model.Order)
	assert createresponse.get_order().get_id() > 0

	request = merchantapi.request.OrderDelete(helper.init_client(), createresponse.get_order())

	assert request.get_order_id() == createresponse.get_order().get_id()

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderDelete)


def test_order_update_customer_information():
	"""
	Tests the Order_Update_Customer_Information API Call
	"""

	helper.provision_store('Order_Update_Customer_Information.xml')

	order_update_customer_information_test_update()


def order_update_customer_information_test_update():
	order = helper.get_order(678571)
	assert isinstance(order, merchantapi.model.Order)
	assert order.get_id() > 0

	request = merchantapi.request.OrderUpdateCustomerInformation(helper.init_client())

	request.set_order_id(order.get_id()) \
		.set_ship_first_name('Joe') \
		.set_ship_last_name('Dirt') \
		.set_ship_email('test@coolcommerce.net') \
		.set_ship_phone('6191231234') \
		.set_ship_fax('6191234321') \
		.set_ship_company('Dierte Inc') \
		.set_ship_address1('1234 Test Ave') \
		.set_ship_address2('Unit 100') \
		.set_ship_city('San Diego') \
		.set_ship_state('CA') \
		.set_ship_zip('92009') \
		.set_ship_country('USA') \
		.set_ship_residential(True) \
		.set_bill_first_name('Joe') \
		.set_bill_last_name('Dirt') \
		.set_bill_email('test@coolcommerce.net') \
		.set_bill_phone('6191231234') \
		.set_bill_fax('6191234321') \
		.set_bill_company('Dierte Inc') \
		.set_bill_address1('1234 Test Ave') \
		.set_bill_address2('Unit 100') \
		.set_bill_city('San Diego') \
		.set_bill_state('CA') \
		.set_bill_zip('92009') \
		.set_bill_country('US')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderUpdateCustomerInformation)

	checkorder = helper.get_order(678571)

	assert isinstance(checkorder, merchantapi.model.Order)
	assert order.get_ship_first_name() != checkorder.get_ship_first_name()
	assert order.get_ship_last_name() != checkorder.get_ship_last_name()
	assert order.get_ship_phone() != checkorder.get_ship_phone()
	assert order.get_ship_fax() != checkorder.get_ship_fax()
	assert order.get_ship_city() != checkorder.get_ship_city()
	assert order.get_ship_state() != checkorder.get_ship_state()
	assert order.get_ship_zip() != checkorder.get_ship_zip()
	assert order.get_ship_country() != checkorder.get_ship_country()
	assert order.get_ship_address1() != checkorder.get_ship_address1()
	assert order.get_ship_address2() != checkorder.get_ship_address2()
	assert order.get_bill_first_name() != checkorder.get_bill_first_name()
	assert order.get_bill_last_name() != checkorder.get_bill_last_name()
	assert order.get_bill_phone() != checkorder.get_bill_phone()
	assert order.get_bill_fax() != checkorder.get_bill_fax()
	assert order.get_bill_city() != checkorder.get_bill_city()
	assert order.get_bill_state() != checkorder.get_bill_state()
	assert order.get_bill_zip() != checkorder.get_bill_zip()
	assert order.get_bill_country() != checkorder.get_bill_country()
	assert order.get_bill_address1() != checkorder.get_bill_address1()
	assert order.get_bill_address2() != checkorder.get_bill_address2()


def test_price_group_customer_update_assigned():
	"""
	Tests the PriceGroupCustomer_Update_Assigned API Call
	"""

	helper.provision_store('PriceGroupCustomer_Update_Assigned.xml')

	price_group_customer_update_assigned_test_assignment()
	price_group_customer_update_assigned_test_unassignment()
	price_group_customer_update_assigned_test_invalid_assign()
	price_group_customer_update_assigned_test_invalid_price_group()
	price_group_customer_update_assigned_test_invalid_customer()


def price_group_customer_update_assigned_test_assignment():
	request = merchantapi.request.PriceGroupCustomerUpdateAssigned(helper.init_client())

	request.set_customer_login('PriceGroupCustomerUpdateAssignedTest_01')\
		.set_price_group_name('PriceGroupCustomerUpdateAssignedTest')\
		.set_assigned(True)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.PriceGroupCustomerUpdateAssigned)


def price_group_customer_update_assigned_test_unassignment():
	request = merchantapi.request.PriceGroupCustomerUpdateAssigned(helper.init_client())

	request.set_customer_login('PriceGroupCustomerUpdateAssignedTest_01')\
		.set_price_group_name('PriceGroupCustomerUpdateAssignedTest')\
		.set_assigned(False)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.PriceGroupCustomerUpdateAssigned)


def price_group_customer_update_assigned_test_invalid_assign():
	request = merchantapi.request.PriceGroupCustomerUpdateAssigned(helper.init_client())

	# noinspection PyTypeChecker
	request.set_customer_login('PriceGroupCustomerUpdateAssignedTest_01')\
		.set_price_group_name('PriceGroupCustomerUpdateAssignedTest')\
		.set_assigned('foobar')

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.PriceGroupCustomerUpdateAssigned)


def price_group_customer_update_assigned_test_invalid_price_group():
	request = merchantapi.request.PriceGroupCustomerUpdateAssigned(helper.init_client())

	request.set_customer_login('PriceGroupCustomerUpdateAssignedTest_01')\
		.set_price_group_name('InvalidPriceGroup')\
		.set_assigned(False)

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.PriceGroupCustomerUpdateAssigned)


def price_group_customer_update_assigned_test_invalid_customer():
	request = merchantapi.request.PriceGroupCustomerUpdateAssigned(helper.init_client())

	request.set_customer_login('InvalidCustomer')\
		.set_price_group_name('PriceGroupCustomerUpdateAssignedTest')\
		.set_assigned(False)

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.PriceGroupCustomerUpdateAssigned)


def test_price_group_list_load_query():
	"""
	Tests the PriceGroupList_Load_Query API Call
	"""

	helper.provision_store('PriceGroupList_Load_Query.xml')

	price_group_list_load_query_test_list_load()


def price_group_list_load_query_test_list_load():
	request = merchantapi.request.PriceGroupListLoadQuery(helper.init_client())

	request.set_filters(request.filter_expression().like('name', 'PriceGroupListLoadQueryTest_%')) \
		.set_sort('id', merchantapi.request.PriceGroupListLoadQuery.SORT_ASCENDING)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.PriceGroupListLoadQuery)

	assert isinstance(response.get_price_groups(), list)
	assert len(response.get_price_groups()) == 14

	for i, pg in enumerate(response.get_price_groups()):
		assert isinstance(pg, merchantapi.model.PriceGroup)
		assert pg.get_name() == 'PriceGroupListLoadQueryTest_%d' % int(i+1)


def test_price_group_product_update_assigned():
	"""
	Tests the PriceGroupProduct_Update_Assigned API Call
	"""

	helper.provision_store('PriceGroupProduct_Update_Assigned.xml')

	price_group_product_update_assigned_test_assignment()
	price_group_product_update_assigned_test_unassignment()
	price_group_product_update_assigned_test_invalid_assign()
	price_group_product_update_assigned_test_invalid_price_group()
	price_group_product_update_assigned_test_invalid_product()


def price_group_product_update_assigned_test_assignment():
	request = merchantapi.request.PriceGroupProductUpdateAssigned(helper.init_client())

	request.set_product_code('PriceGroupProductUpdateAssignedTest_1')\
		.set_price_group_name('PriceGroupProductUpdateAssignedTest')\
		.set_assigned(True)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.PriceGroupProductUpdateAssigned)


def price_group_product_update_assigned_test_unassignment():
	request = merchantapi.request.PriceGroupProductUpdateAssigned(helper.init_client())

	request.set_product_code('PriceGroupProductUpdateAssignedTest_1')\
		.set_price_group_name('PriceGroupProductUpdateAssignedTest')\
		.set_assigned(False)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.PriceGroupProductUpdateAssigned)


def price_group_product_update_assigned_test_invalid_assign():
	request = merchantapi.request.PriceGroupProductUpdateAssigned(helper.init_client())

	# noinspection PyTypeChecker
	request.set_product_code('PriceGroupProductUpdateAssignedTest_1')\
		.set_price_group_name('PriceGroupProductUpdateAssignedTest')\
		.set_assigned('foobar')

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.PriceGroupProductUpdateAssigned)


def price_group_product_update_assigned_test_invalid_price_group():
	request = merchantapi.request.PriceGroupProductUpdateAssigned(helper.init_client())

	request.set_product_code('PriceGroupProductUpdateAssignedTest_1')\
		.set_price_group_name('InvalidPriceGroup')\
		.set_assigned(True)

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.PriceGroupProductUpdateAssigned)


def price_group_product_update_assigned_test_invalid_product():
	request = merchantapi.request.PriceGroupProductUpdateAssigned(helper.init_client())

	request.set_product_code('InvalidProduct')\
		.set_price_group_name('PriceGroupProductUpdateAssignedTest')\
		.set_assigned(True)

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.PriceGroupProductUpdateAssigned)


def test_product_image_add():
	"""
	Tests the ProductImage_Add API Call
	"""

	helper.upload_image('graphics/ProductImageAdd.jpg')
	helper.provision_store('ProductImage_Add.xml')

	product_image_add_test_add()
	product_image_add_test_invalid_product()
	product_image_add_test_invalid_product_path()


def product_image_add_test_add():
	request = merchantapi.request.ProductImageAdd(helper.init_client())

	request.set_product_code('ProductImageAddTest') \
		.set_filepath('graphics/00000001/1/ProductImageAdd.jpg') \
		.set_image_type_id(0)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.ProductImageAdd)


def product_image_add_test_invalid_product():
	request = merchantapi.request.ProductImageAdd(helper.init_client())

	request.set_product_code('InvalidProductImageAddTest') \
		.set_filepath('graphics/00000001/1/ProductImageAdd.jpg') \
		.set_image_type_id(0)

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.ProductImageAdd)


def product_image_add_test_invalid_product_path():
	request = merchantapi.request.ProductImageAdd(helper.init_client())

	request.set_product_code('ProductImageAddTest') \
		.set_filepath('graphics/00000001/InvalidImage.jpg') \
		.set_image_type_id(0)

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.ProductImageAdd)


def test_product_image_delete():
	"""
	Tests the ProductImage_Delete API Call
	"""

	helper.provision_store('ProductImage_Delete_Cleanup_v10.xml')
	helper.upload_image('graphics/ProductImageDelete.jpg')
	helper.provision_store('ProductImage_Delete_v10.xml')

	product_image_delete_test_deletion()


def product_image_delete_test_deletion():
	product = helper.get_product('ProductImageDeleteTest')

	assert isinstance(product, merchantapi.model.Product)
	assert isinstance(product.get_product_image_data(), list)
	assert len(product.get_product_image_data()) == 1

	request = merchantapi.request.ProductImageDelete(helper.init_client(), product.get_product_image_data()[0])

	assert request.get_product_image_id() == product.get_product_image_data()[0].get_id()

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.ProductImageDelete)


def test_product_list_adjust_inventory():
	"""
	Tests the ProductList_Adjust_Inventory API Call
	"""

	helper.provision_store('ProductList_Adjust_Inventory.xml')

	product_list_adjust_inventory_test_adjustment()


def product_list_adjust_inventory_test_adjustment():
	product = helper.get_product('ProductListAdjustInventoryTest_1')

	request = merchantapi.request.ProductListAdjustInventory(helper.init_client())
	adjustment = merchantapi.model.ProductInventoryAdjustment()

	adjustment.set_product_id(product.get_id()) \
		.set_adjustment(100)

	request.add_inventory_adjustment(adjustment)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.ProductListAdjustInventory)


def test_product_list_load_query():
	"""
	Tests the ProductList_Load_Query API Call
	"""

	helper.upload_image('graphics/ProductListLoadQuery1.jpg')
	helper.upload_image('graphics/ProductListLoadQuery2.jpg')
	helper.upload_image('graphics/ProductListLoadQuery3.jpg')
	helper.upload_image('graphics/ProductListLoadQuery4.jpg')
	helper.upload_image('graphics/ProductListLoadQuery5.jpg')
	helper.upload_image('graphics/ProductListLoadQuery6.jpg')
	helper.upload_image('graphics/ProductListLoadQuery7.jpg')
	helper.provision_store('ProductList_Load_Query_v10.xml')

	product_list_load_query_test_list_load()
	product_list_load_query_test_list_load_with_custom_fields()


def product_list_load_query_test_list_load():
	request = merchantapi.request.ProductListLoadQuery(helper.init_client())

	request.set_filters(
		request.filter_expression()
		.like('code', 'ProductListLoadQueryTest_%')
		.and_not_like('code', 'ProductListLoadQueryTest_Rel_%')
	)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.ProductListLoadQuery)

	assert isinstance(response.get_products(), list)
	assert len(response.get_products()) == 7

	for i, product in enumerate(response.get_products()):
		assert isinstance(product, merchantapi.model.Product)
		assert product.get_code() == 'ProductListLoadQueryTest_%d' % int(i+1)
		assert product.get_price() == 2.00
		assert product.get_cost() == 1.00
		assert product.get_weight() == 1.00
		assert product.get_active() is False
		assert product.get_taxable() is False


def product_list_load_query_test_list_load_with_custom_fields():
	request = merchantapi.request.ProductListLoadQuery(helper.init_client())

	request.set_filters(
		request.filter_expression()
			.like('code', 'ProductListLoadQueryTest_%')
			.and_not_like('code', 'ProductListLoadQueryTest_Rel_%')
	)

	request.set_on_demand_columns(request.get_available_on_demand_columns()) \
		.add_on_demand_column('CustomField_Values:customfields:ProductListLoadQueryTest_checkbox') \
		.add_on_demand_column('CustomField_Values:customfields:ProductListLoadQueryTest_imageupload') \
		.add_on_demand_column('CustomField_Values:customfields:ProductListLoadQueryTest_text') \
		.add_on_demand_column('CustomField_Values:customfields:ProductListLoadQueryTest_textarea') \
		.add_on_demand_column('CustomField_Values:customfields:ProductListLoadQueryTest_dropdown') \
		.add_on_demand_column('CustomField_Values:customfields:ProductListLoadQueryTest_multitext')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.ProductListLoadQuery)

	assert isinstance(response.get_products(), list)
	assert len(response.get_products()) == 7

	for i, product in enumerate(response.get_products()):
		assert isinstance(product, merchantapi.model.Product)
		assert product.get_code() == 'ProductListLoadQueryTest_%d' % int(i+1)
		assert product.get_price() == 2.00
		assert product.get_cost() == 1.00
		assert product.get_weight() == 1.00
		assert product.get_active() is False
		assert product.get_taxable() is False

		if product.get_code() in ['ProductListLoadQueryTest_1', 'ProductListLoadQueryTest_2']:
			assert isinstance(product.get_attributes(), list)
			assert len(product.get_attributes()) > 0

			for attribute in product.get_attributes():
				assert isinstance(attribute, merchantapi.model.ProductAttribute)

				if attribute.get_type() == 'select':
					assert isinstance(attribute.get_options(), list)
					assert len(attribute.get_options()) > 0

					for option in attribute.get_options():
						assert isinstance(option, merchantapi.model.ProductOption)

		assert isinstance(product.get_related_products(), list)
		assert len(product.get_related_products()) > 0

		for related in product.get_related_products():
			assert isinstance(related, merchantapi.model.RelatedProduct)
			assert related.get_code() in [
				'ProductListLoadQueryTest_Rel_1',
				'ProductListLoadQueryTest_Rel_2',
				'ProductListLoadQueryTest_Rel_3',
				'ProductListLoadQueryTest_Rel_4',
				'ProductListLoadQueryTest_Rel_5',
				'ProductListLoadQueryTest_Rel_6',
				'ProductListLoadQueryTest_Rel_7'
			]

		assert isinstance(product.get_categories(), list)
		assert len(product.get_categories()) > 0

		for category in product.get_categories():
			assert isinstance(category, merchantapi.model.Category)
			assert category.get_code() in [
				'ProductListLoadQueryTest_1',
				'ProductListLoadQueryTest_2',
				'ProductListLoadQueryTest_3',
				'ProductListLoadQueryTest_4',
				'ProductListLoadQueryTest_5',
				'ProductListLoadQueryTest_6',
				'ProductListLoadQueryTest_7'
			]

		assert isinstance(product.get_product_image_data(), list)
		assert len(product.get_product_image_data()) > 0

		for imagedata in product.get_product_image_data():
			assert isinstance(imagedata, merchantapi.model.ProductImageData)
			assert imagedata.get_image() in [
				'graphics/00000001/1/ProductListLoadQuery1.jpg',
				'graphics/00000001/1/ProductListLoadQuery2.jpg',
				'graphics/00000001/1/ProductListLoadQuery3.jpg',
				'graphics/00000001/1/ProductListLoadQuery4.jpg',
				'graphics/00000001/1/ProductListLoadQuery5.jpg',
				'graphics/00000001/1/ProductListLoadQuery6.jpg',
				'graphics/00000001/1/ProductListLoadQuery7.jpg'
			]

		assert isinstance(product.get_custom_field_values(), merchantapi.model.CustomFieldValues)
		assert product.get_custom_field_values().has_value('ProductListLoadQueryTest_checkbox', 'customfields') is True
		assert product.get_custom_field_values().has_value('ProductListLoadQueryTest_imageupload', 'customfields') is True
		assert product.get_custom_field_values().has_value('ProductListLoadQueryTest_text', 'customfields') is True
		assert product.get_custom_field_values().has_value('ProductListLoadQueryTest_textarea', 'customfields') is True
		assert product.get_custom_field_values().has_value('ProductListLoadQueryTest_dropdown', 'customfields') is True
		assert product.get_custom_field_values().has_value('ProductListLoadQueryTest_multitext', 'customfields') is True


def test_product_variant_list_load_product():
	"""
	Tests the ProductVariantList_Load_Product API Call
	"""

	helper.provision_store('ProductVariantList_Load_Product.xml')

	product_variant_list_load_product_test_load()


def product_variant_list_load_product_test_load():
	request = merchantapi.request.ProductVariantListLoadProduct(helper.init_client())

	request.set_edit_product('ProductVariantListLoadProduct') \
		.set_include_default_variant(True)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.ProductVariantListLoadProduct)

	assert isinstance(response.get_product_variants(), list)
	assert len(response.get_product_variants()) == 48

	for pv in response.get_product_variants():
		assert isinstance(pv, merchantapi.model.ProductVariant)
		assert isinstance(pv.get_parts(), list)
		assert len(pv.get_parts()) == 2

		for part in pv.get_parts():
			assert isinstance(part, merchantapi.model.ProductVariantPart)
			assert part.get_product_id() > 0
			assert 'PVLLP_' in part.get_product_code()

		assert isinstance(pv.get_dimensions(), list)
		assert len(pv.get_dimensions()) > 3

		for dimension in pv.get_dimensions():
			assert isinstance(dimension, merchantapi.model.ProductVariantDimension)
			assert dimension.get_attribute_id() > 0


def test_product_insert():
	"""
	Tests the Product_Insert API Call
	"""

	helper.provision_store('Product_Insert.xml')
	helper.upload_image('graphics/ProductInsert.jpg')

	product_insert_test_insertion()
	product_insert_test_insertion_with_custom_fields()
	product_insert_test_duplicate()


def product_insert_test_insertion():
	request = merchantapi.request.ProductInsert(helper.init_client())

	request.set_product_code('ProductInsertTest_1') \
		.set_product_sku('ProductInsertTest_1_Sku') \
		.set_product_name('API Inserted Product 1') \
		.set_product_active(True) \
		.set_product_price(7.50) \
		.set_product_cost(7.50)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.ProductInsert)

	product = helper.get_product('ProductInsertTest_1')

	assert isinstance(product, merchantapi.model.Product)
	assert product.get_code() == 'ProductInsertTest_1'
	assert product.get_sku() == 'ProductInsertTest_1_Sku'
	assert product.get_name() == 'API Inserted Product 1'
	assert product.get_price() == 7.50
	assert product.get_cost() == 7.50
	assert product.get_id() > 0


def product_insert_test_insertion_with_custom_fields():
	request = merchantapi.request.ProductInsert(helper.init_client())

	request.set_product_code('ProductInsertTest_2') \
		.set_product_sku('ProductInsertTest_2_Sku') \
		.set_product_name('API Inserted Product 2') \
		.set_product_active(True) \
		.set_product_price(7.50) \
		.set_product_cost(7.50)

	request.get_custom_field_values() \
		.add_value('ProductInsertTest_checkbox', 'True', 'customfields') \
		.add_value('ProductInsertTest_imageupload', 'graphics/00000001/ProductInsert.jpg', 'customfields') \
		.add_value('ProductInsertTest_text', 'ProductInsertTest_2', 'customfields') \
		.add_value('ProductInsertTest_textarea', 'ProductInsertTest_2', 'customfields') \
		.add_value('ProductInsertTest_dropdown', 'Option2', 'customfields')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.ProductInsert)

	product = helper.get_product('ProductInsertTest_2')

	assert isinstance(product, merchantapi.model.Product)
	assert product.get_code() == 'ProductInsertTest_2'
	assert product.get_sku() == 'ProductInsertTest_2_Sku'
	assert product.get_name() == 'API Inserted Product 2'
	assert product.get_price() == 7.50
	assert product.get_cost() == 7.50
	assert product.get_id() > 0
	assert product.get_custom_field_values().has_value('ProductInsertTest_checkbox', 'customfields') is True
	assert product.get_custom_field_values().get_value('ProductInsertTest_checkbox', 'customfields') == '1'
	assert product.get_custom_field_values().has_value('ProductInsertTest_imageupload', 'customfields') is True
	assert product.get_custom_field_values().get_value('ProductInsertTest_imageupload', 'customfields') == 'graphics/00000001/ProductInsert.jpg'
	assert product.get_custom_field_values().has_value('ProductInsertTest_text', 'customfields') is True
	assert product.get_custom_field_values().get_value('ProductInsertTest_text', 'customfields') == 'ProductInsertTest_2'
	assert product.get_custom_field_values().has_value('ProductInsertTest_textarea', 'customfields') is True
	assert product.get_custom_field_values().get_value('ProductInsertTest_textarea', 'customfields') == 'ProductInsertTest_2'
	assert product.get_custom_field_values().has_value('ProductInsertTest_dropdown', 'customfields') is True
	assert product.get_custom_field_values().get_value('ProductInsertTest_dropdown', 'customfields') == 'Option2'


def product_insert_test_duplicate():
	request = merchantapi.request.ProductInsert(helper.init_client())

	request.set_product_code('ProductInsertTest_Duplicate') \
		.set_product_sku('ProductInsertTest_Duplicate_Sku') \
		.set_product_name('API Inserted Product Duplicate') \
		.set_product_active(True) \
		.set_product_price(7.50) \
		.set_product_cost(7.50)

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.ProductInsert)


def test_product_delete():
	"""
	Tests the Product_Delete API Call
	"""

	helper.provision_store('Product_Delete.xml')

	product_delete_test_deletion_by_id()
	product_delete_test_deletion_by_code()
	product_delete_test_deletion_by_sku()
	product_delete_test_deletion_by_edit_product()


def product_delete_test_deletion_by_id():
	product = helper.get_product('ProductDeleteTest_ID')

	assert isinstance(product, merchantapi.model.Product)

	request = merchantapi.request.ProductDelete(helper.init_client())

	request.set_product_id(product.get_id())

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.ProductDelete)

	check = helper.get_product('ProductDeleteTest_ID')

	assert check is None


def product_delete_test_deletion_by_code():
	request = merchantapi.request.ProductDelete(helper.init_client())

	request.set_product_code('ProductDeleteTest_CODE')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.ProductDelete)

	check = helper.get_product('ProductDeleteTest_CODE')

	assert check is None


def product_delete_test_deletion_by_sku():
	request = merchantapi.request.ProductDelete(helper.init_client())

	request.set_product_sku('ProductDeleteTest_SKU')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.ProductDelete)

	check = helper.get_product('ProductDeleteTest_SKU')

	assert check is None


def product_delete_test_deletion_by_edit_product():
	request = merchantapi.request.ProductDelete(helper.init_client())

	request.set_edit_product('ProductDeleteTest_EDIT_PRODUCT')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.ProductDelete)

	check = helper.get_product('ProductDeleteTest_EDIT_PRODUCT')

	assert check is None


def test_product_update():
	"""
	Tests the Product_Update API Call
	"""

	helper.provision_store('Product_Update.xml')

	product_update_test_update()
	product_update_test_update_code()


def product_update_test_update():
	request = merchantapi.request.ProductUpdate(helper.init_client())

	request.set_edit_product('ProductUpdateTest_1') \
		.set_product_name('ProductUpdateTest_1 New Name') \
		.set_product_price(39.99) \
		.set_product_cost(29.99) \
		.set_product_active(True) \
		.set_product_taxable(True) \
		.set_product_sku('ProductUpdateTest_1_Changed_SKU') \
		.set_product_page_title('ProductUpdateTest_1 Changed Page Title')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.ProductUpdate)

	product = helper.get_product('ProductUpdateTest_1')

	assert isinstance(product, merchantapi.model.Product)
	assert product.get_name() == 'ProductUpdateTest_1 New Name'
	assert product.get_price() == 39.99
	assert product.get_cost() == 29.99
	assert product.get_active() is True
	assert product.get_taxable() is True
	assert product.get_sku() == 'ProductUpdateTest_1_Changed_SKU'
	assert product.get_page_title() == 'ProductUpdateTest_1 Changed Page Title'


def product_update_test_update_code():
	request = merchantapi.request.ProductUpdate(helper.init_client())

	request.set_edit_product('ProductUpdateTest_3') \
		.set_product_code('ProductUpdateTest_3_Changed')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.ProductUpdate)

	product = helper.get_product('ProductUpdateTest_3_Changed')

	assert isinstance(product, merchantapi.model.Product)
	assert product.get_code() == 'ProductUpdateTest_3_Changed'


def test_customer_address_list_load_query():
	"""
	Tests the CustomerAddressList_Load_Query API Call
	"""

	helper.provision_store('CustomerAddressList_Load_Query.xml')

	customer_address_list_load_query_test_list_load()
	customer_address_list_load_query_test_list_load_filtered()


def customer_address_list_load_query_test_list_load():
	customer = helper.get_customer('CustomerAddressListLoadQueryTest')

	assert isinstance(customer, merchantapi.model.Customer)
	assert customer.get_login() == 'CustomerAddressListLoadQueryTest'
	assert customer.get_id() > 0

	request = merchantapi.request.CustomerAddressListLoadQuery(helper.init_client())

	request.set_customer_login('CustomerAddressListLoadQueryTest')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CustomerAddressListLoadQuery)

	assert isinstance(response.get_customer_addresses(), list)
	assert len(response.get_customer_addresses()) == 3

	for i, address in enumerate(response.get_customer_addresses()):
		assert isinstance(address, merchantapi.model.CustomerAddress)
		assert address.get_customer_id() == customer.get_id()


def customer_address_list_load_query_test_list_load_filtered():
	customer = helper.get_customer('CustomerAddressListLoadQueryTest')

	assert isinstance(customer, merchantapi.model.Customer)
	assert customer.get_login() == 'CustomerAddressListLoadQueryTest'
	assert customer.get_id() > 0

	request = merchantapi.request.CustomerAddressListLoadQuery(helper.init_client())

	request.set_customer_login('CustomerAddressListLoadQueryTest')
	request.set_filters(request.filter_expression().equal('fname', 'Joe'))

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CustomerAddressListLoadQuery)

	assert isinstance(response.get_customer_addresses(), list)
	assert len(response.get_customer_addresses()) == 1

	for i, address in enumerate(response.get_customer_addresses()):
		assert isinstance(address, merchantapi.model.CustomerAddress)
		assert address.get_customer_id() == customer.get_id()
		assert address.get_first_name() == 'Joe'


def test_print_queue_list_load_query():
	"""
	Tests the PrintQueueList_Load_Query API Call
	"""

	print_queue_list_load_query_test_list_load()


def print_queue_list_load_query_test_list_load():
	request = merchantapi.request.PrintQueueListLoadQuery(helper.init_client())

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.PrintQueueListLoadQuery)

	assert isinstance(response.get_print_queues(), list)

	for pq in response.get_print_queues():
		assert isinstance(pq, merchantapi.model.PrintQueue)


def test_print_queue_job_list_load_query():
	"""
	Tests the PrintQueueJobList_Load_Query API Call
	"""

	print_queue_job_list_load_query_test_list_load()
	print_queue_job_list_load_query_test_invalid_queue()


def print_queue_job_list_load_query_test_list_load():
	helper.create_print_queue('PrintQueueJobListLoadQueryTest')

	request = merchantapi.request.PrintQueueJobListLoadQuery(helper.init_client())

	request.set_edit_print_queue('PrintQueueJobListLoadQueryTest')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.PrintQueueJobListLoadQuery)

	assert isinstance(response.get_print_queue_jobs(), list)

	for pqj in response.get_print_queue_jobs():
		assert isinstance(pqj, merchantapi.model.PrintQueueJob)


def print_queue_job_list_load_query_test_invalid_queue():
	request = merchantapi.request.PrintQueueJobListLoadQuery(helper.init_client())

	request.set_edit_print_queue('InvalidPrintQueue')

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.PrintQueueJobListLoadQuery)


def test_print_queue_job_delete():
	"""
	Tests the PrintQueueJob_Delete API Call
	"""

	print_queue_job_delete_test_deletion()


def print_queue_job_delete_test_deletion():
	helper.create_print_queue('PrintQueueJobDeleteTest')

	insert_request = merchantapi.request.PrintQueueJobInsert(helper.init_client())

	insert_request.set_edit_print_queue('PrintQueueJobDeleteTest') \
		.set_print_queue_description('Description') \
		.set_print_queue_job_format('Format') \
		.set_print_queue_job_data('Data')

	insert_response = insert_request.send()

	helper.validate_response_success(insert_response, merchantapi.response.PrintQueueJobInsert)

	assert insert_response.get_id() > 0

	request = merchantapi.request.PrintQueueJobDelete(helper.init_client())

	request.set_print_queue_job_id(insert_response.get_id())

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.PrintQueueJobDelete)


def test_print_queue_job_insert():
	"""
	Tests the PrintQueueJob_Insert API Call
	"""

	print_queue_job_insert_test_insertion()


def print_queue_job_insert_test_insertion():
	helper.create_print_queue('PrintQueueJobInsertTest')

	request = merchantapi.request.PrintQueueJobInsert(helper.init_client())

	request.set_edit_print_queue('PrintQueueJobInsertTest') \
		.set_print_queue_description('Description') \
		.set_print_queue_job_format('Format') \
		.set_print_queue_job_data('Data')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.PrintQueueJobInsert)

	assert response.get_id() > 0


def test_print_queue_job_status():
	"""
	Tests the PrintQueueJob_Status API Call
	"""

	print_queue_job_status_test_get_status()


def print_queue_job_status_test_get_status():
	helper.create_print_queue('PrintQueueJobStatusTest')

	insert_request = merchantapi.request.PrintQueueJobInsert(helper.init_client())

	insert_request.set_edit_print_queue('PrintQueueJobStatusTest') \
		.set_print_queue_description('Description') \
		.set_print_queue_job_format('Format') \
		.set_print_queue_job_data('Data')

	insert_response = insert_request.send()

	helper.validate_response_success(insert_response, merchantapi.response.PrintQueueJobInsert)

	assert insert_response.get_id() > 0

	request = merchantapi.request.PrintQueueJobStatus(helper.init_client())

	request.set_print_queue_job_id(insert_response.get_id())

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.PrintQueueJobStatus)

	assert response.get_status() not in (None, '')


def test_payment_method_list_load():
	"""
	Tests the PaymentMethodList_Load API Call
	"""

	helper.provision_store('PaymentMethodList_Load.xml')

	payment_method_list_load_test_list_load()


def payment_method_list_load_test_list_load():
	modules = helper.load_modules_by_feature('payment', ['cod', 'check'])

	assert isinstance(modules, list)
	assert len(modules) == 2

	request = merchantapi.request.PaymentMethodListLoad(helper.init_client())

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.PaymentMethodListLoad)

	assert isinstance(response.get_payment_methods(), list)
	assert len(response.get_payment_methods()) >= 2

	for pm in response.get_payment_methods():
		assert isinstance(pm, merchantapi.model.PaymentMethod)
		assert pm.get_module_api() > 0
		assert pm.get_module_id() > 0
		assert pm.get_method_code() not in (None, '')
		assert pm.get_method_name() not in (None, '')

	for module in modules:
		match = None

		for pm in response.get_payment_methods():
			if pm.get_module_id() == module['id']:
				match = pm

		assert match is not None


def test_order_create_from_order():
	"""
	Tests the Order_Create_FromOrder API Call
	"""

	helper.provision_store('Order_Create_FromOrder.xml')

	order_create_from_order_test_create()
	order_create_from_order_test_invalid_order()


def order_create_from_order_test_create():
	order = helper.get_order(10520)

	assert isinstance(order, merchantapi.model.Order)
	assert order.get_id() == 10520

	request = merchantapi.request.OrderCreateFromOrder(helper.init_client(), order)

	assert request.get_order_id() == order.get_id()

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderCreateFromOrder)

	assert isinstance(response.get_order(), merchantapi.model.Order)
	assert response.get_order().get_id() > 0
	assert response.get_order().get_id() != 10520


def order_create_from_order_test_invalid_order():
	request = merchantapi.request.OrderCreateFromOrder(helper.init_client())

	request.set_order_id(8980999)

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.OrderCreateFromOrder)


def test_customer_payment_card_list_load_query():
	"""
	Tests the CustomerPaymentCardList_Load_Query API Call
	"""

	helper.provision_store('MivaPay.xml')
	helper.provision_store('CustomerPaymentCardList_Load_Query.xml')

	customer_payment_card_list_load_query_test_list_load()


def customer_payment_card_list_load_query_test_list_load():
	cards = ['4788250000028291', '4055011111111111', '5454545454545454', '5405222222222226']
	lastfours = ['8291', '1111', '5454', '2226']

	mrequest = merchantapi.multicall.MultiCallRequest(helper.init_client())

	for card in cards:
		card_request = merchantapi.request.CustomerPaymentCardRegister(None)

		card_request.set_customer_login('CustomerPaymentCardList_Load_Query') \
			.set_first_name('John') \
			.set_last_name('Doe') \
			.set_card_type('MasterCard' if card[0] == 5 else 'Visa') \
			.set_card_number(card) \
			.set_expiration_month(8) \
			.set_expiration_year(2025) \
			.set_address1('1234 Test St') \
			.set_address2('Unit 123') \
			.set_city('San Diego') \
			.set_state('CA') \
			.set_zip('92009') \
			.set_country('USA')

		mrequest.add_request(card_request)

	mresponse = mrequest.send()

	helper.validate_response_success(mresponse, merchantapi.multicall.MultiCallResponse)

	assert isinstance(mresponse.get_responses(), list)

	for resp in mresponse.get_responses():
		helper.validate_response_success(resp, merchantapi.response.CustomerPaymentCardRegister)

	request = merchantapi.request.CustomerPaymentCardListLoadQuery(helper.init_client())

	request.set_customer_login('CustomerPaymentCardList_Load_Query')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CustomerPaymentCardListLoadQuery)

	assert isinstance(response.get_customer_payment_cards(), list)
	assert len(response.get_customer_payment_cards()) == 4

	for card in response.get_customer_payment_cards():
		assert card.get_last_four() in lastfours


def test_category_product_list_load_query():
	"""
	Tests the CategoryProductList_Load_Query API Call
	"""

	helper.provision_store('CategoryProductList_Load_Query.xml')

	category_product_list_load_query_test_list_load()


def category_product_list_load_query_test_list_load():
	request = merchantapi.request.CategoryProductListLoadQuery(helper.init_client())

	request.set_edit_category('CategoryProductListLoadQueryTest_Category') \
		.set_assigned(True) \
		.set_unassigned(False)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CategoryProductListLoadQuery)

	assert isinstance(response.get_category_products(), list)
	assert len(response.get_category_products()) == 3

	for i, cp in enumerate(response.get_category_products()):
		assert isinstance(cp, merchantapi.model.CategoryProduct)
		assert cp.get_code() == 'CategoryProductListLoadQueryTest_Product_%d' % int(i+1)


def test_coupon_price_group_list_load_query():
	"""
	Tests the CouponPriceGroupList_Load_Query API Call
	"""

	helper.provision_store('CouponPriceGroupList_Load_Query.xml')

	coupon_price_group_list_load_query_test_list_load()


def coupon_price_group_list_load_query_test_list_load():
	request = merchantapi.request.CouponPriceGroupListLoadQuery(helper.init_client())

	request.set_coupon_code('CouponPriceGroupListLoadQueryTest_Coupon') \
		.set_assigned(True) \
		.set_unassigned(False)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CouponPriceGroupListLoadQuery)

	assert isinstance(response.get_coupon_price_groups(), list)
	assert len(response.get_coupon_price_groups()) == 3

	for i, cp in enumerate(response.get_coupon_price_groups()):
		assert isinstance(cp, merchantapi.model.CouponPriceGroup)
		assert cp.get_name() == 'CouponPriceGroupListLoadQueryTest_PriceGroup_%d' % int(i+1)


def test_price_group_product_list_load_query():
	"""
	Tests the PriceGroupProductList_Load_Query API Call
	"""

	helper.provision_store('PriceGroupProductList_Load_Query.xml')

	price_group_product_list_load_query_test_list_load()


def price_group_product_list_load_query_test_list_load():
	request = merchantapi.request.PriceGroupProductListLoadQuery(helper.init_client())

	request.set_price_group_name('PriceGroupProductListLoadQueryTest') \
		.set_assigned(True) \
		.set_unassigned(False)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.PriceGroupProductListLoadQuery)

	assert isinstance(response.get_price_group_products(), list)
	assert len(response.get_price_group_products()) == 5

	for i, pgp in enumerate(response.get_price_group_products()):
		assert isinstance(pgp, merchantapi.model.PriceGroupProduct)
		assert pgp.get_code() == 'PriceGroupProductListLoadQueryTest_0%d' % int(i+1)
		assert pgp.get_name() == 'PriceGroupProductListLoadQueryTest_0%d' % int(i+1)


def test_customer_price_group_list_load_query():
	"""
	Tests the CustomerPriceGroupList_Load_Query API Call
	"""

	helper.provision_store('CustomerPriceGroupList_Load_Query.xml')

	customer_price_group_list_load_query_test_list_load()


def customer_price_group_list_load_query_test_list_load():
	request = merchantapi.request.CustomerPriceGroupListLoadQuery(helper.init_client())

	request.set_customer_login('CustomerPriceGroupListLoadQueryTest') \
		.set_assigned(True) \
		.set_unassigned(False)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CustomerPriceGroupListLoadQuery)

	assert isinstance(response.get_customer_price_groups(), list)
	assert len(response.get_customer_price_groups()) == 3

	for i, customerpricegroup in enumerate(response.get_customer_price_groups()):
		assert isinstance(customerpricegroup, merchantapi.model.CustomerPriceGroup)
		assert customerpricegroup.get_name() == 'CustomerPriceGroupListLoadQueryTest_%d' % int(i+1)
		assert customerpricegroup.get_description() == 'CustomerPriceGroupListLoadQueryTest_%d' % int(i+1)
		assert customerpricegroup.get_customer_scope() == merchantapi.model.CustomerPriceGroup.ELIGIBILITY_CUSTOMER
		assert customerpricegroup.get_module().get_code() == 'discount_product'


def test_price_group_customer_list_load_query():
	"""
	Tests the PriceGroupCustomerList_Load_Query API Call
	"""

	helper.provision_store('PriceGroupCustomerList_Load_Query.xml')

	price_group_customer_list_load_query_test_list_load()


def price_group_customer_list_load_query_test_list_load():
	request = merchantapi.request.PriceGroupCustomerListLoadQuery(helper.init_client())

	request.set_price_group_name('PriceGroupCustomerListLoadQueryTest') \
		.set_assigned(True) \
		.set_unassigned(False)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.PriceGroupCustomerListLoadQuery)

	assert isinstance(response.get_price_group_customers(), list)
	assert len(response.get_price_group_customers()) == 5

	for i, pgc in enumerate(response.get_price_group_customers()):
		assert isinstance(pgc, merchantapi.model.PriceGroupCustomer)
		assert pgc.get_login() == 'PriceGroupCustomerListLoadQueryTest_0%d' % int(i+1)
		assert pgc.get_business_title() == 'PriceGroupCustomerListLoadQueryTest'
		assert pgc.get_assigned() is True


def test_branch_copy():
	"""
	Tests the Branch_Copy API Call
	"""

	branch_copy_test_copy()


def branch_copy_test_copy():
	helper.delete_branch('Production Copy 1')

	default_branch = helper.get_branch('Production')

	assert default_branch is not None

	create_request = merchantapi.request.BranchCreate(helper.init_client(), default_branch)
	create_request.set_name('Production Copy 1')
	create_request.set_color(default_branch.get_color())

	create_response = create_request.send()

	helper.validate_response_success(create_response, merchantapi.response.BranchCreate)

	request = merchantapi.request.BranchCopy(helper.init_client(), default_branch)

	request.set_destination_branch_id(create_response.get_branch().get_id())

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.BranchCopy)

	assert isinstance(response.get_changeset(), merchantapi.model.Changeset)

	assert response.get_changeset().get_id() > 0
	assert response.get_changeset().get_branch_id() > 0


def test_branch_create():
	"""
	Tests the Branch_Create API Call
	"""

	branch_create_test_create()


def branch_create_test_create():
	helper.delete_branch('Production Copy')

	branch = helper.get_branch('Production')

	assert branch is not None

	request = merchantapi.request.BranchCreate(helper.init_client(), branch)

	request.set_name('Production Copy')
	request.set_color('#000000')

	assert branch.get_id() == request.get_parent_branch_id()

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.BranchCreate)

	assert isinstance(response.get_branch(), merchantapi.model.Branch)


def test_branch_delete():
	"""
	Tests the Branch_Delete API Call
	"""

	branch_delete_test_deletion()


def branch_delete_test_deletion():
	branch = helper.get_branch('Production Copy')

	if branch is None:
		copybranch = helper.get_branch('Production')
		assert isinstance(copybranch, merchantapi.model.Branch)
		copyrequest = merchantapi.request.BranchCreate(helper.init_client(), copybranch)
		copyrequest.set_name('Production Copy')
		copyrequest.set_color('#000000')

		copyresponse = copyrequest.send()
		helper.validate_response_success(copyresponse, merchantapi.response.BranchCreate)

		branch = copyresponse.get_branch()

	request = merchantapi.request.BranchDelete(helper.init_client(), branch)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.BranchDelete)


def test_changeset_create():
	"""
	Tests the Changeset_Create API Call
	"""

	changeset_create_test_creation()


def changeset_create_test_creation():
	branch = helper.get_branch('Production')

	assert branch is not None

	request = merchantapi.request.ChangesetCreate(helper.init_client(), branch)

	assert request.get_branch_id() == branch.get_id()

	# Load a Changeset
	load_changeset_request = merchantapi.request.ChangesetListLoadQuery(helper.init_client(), branch)
	load_changeset_response = load_changeset_request.send()

	helper.validate_response_success(load_changeset_response, merchantapi.response.ChangesetListLoadQuery)

	assert isinstance(load_changeset_response.get_changesets(), list)
	assert len(load_changeset_response.get_changesets()) > 0

	changeset = load_changeset_response.get_changesets()[0]

	assert isinstance(changeset, merchantapi.model.Changeset)

	# Load a Template
	load_template_request = merchantapi.request.BranchTemplateVersionListLoadQuery(helper.init_client(), branch)

	load_template_request.set_filters(load_template_request.filter_expression().equal('filename', 'sfnt.mvc'))
	load_template_request.set_on_demand_columns(load_template_request.get_available_on_demand_columns())
	load_template_request.set_changeset_id(changeset.get_id())

	load_template_response = load_template_request.send()

	helper.validate_response_success(load_template_response, merchantapi.response.BranchTemplateVersionListLoadQuery)

	assert isinstance(load_template_response.get_branch_template_versions(), list)
	assert len(load_template_response.get_branch_template_versions()) > 0

	version = load_template_response.get_branch_template_versions()[0]

	assert isinstance(version, merchantapi.model.BranchTemplateVersion)

	# Add a Change
	change1 = merchantapi.model.TemplateChange()

	source = version.get_source()

	assert isinstance(source, str)
	assert len(source) > 0

	if '<body class="SFNT">HELLO_WORLD' in source:
		change1.set_template_filename('sfnt.mvc').set_source(source.replace('<body class="SFNT">HELLO_WORLD', '<body class="SFNT">'))
	else:
		change1.set_template_filename('sfnt.mvc').set_source(source.replace('<body class="SFNT">', '<body class="SFNT">HELLO_WORLD'))

	request.add_template_change(change1)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.ChangesetCreate)

	assert isinstance(response.get_changeset(), merchantapi.model.Changeset)


def test_branch_list_load_query():
	"""
	Tests the BranchList_Load_Query API Call
	"""

	branch_list_load_query_test_list_load()


def branch_list_load_query_test_list_load():
	request = merchantapi.request.BranchListLoadQuery(helper.init_client())

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.BranchListLoadQuery)

	assert len(response.get_branches()) > 0

	for e in response.get_branches():
		assert isinstance(e, merchantapi.model.Branch)



def test_branch_list_delete():
	"""
	Tests the BranchList_Delete API Call
	"""

	branch_list_delete_test()


def branch_list_delete_test():
	helper.delete_branch('Production Copy')
	helper.delete_branch('Production Copy 1')
	helper.delete_branch('Production Copy 2')

	production_branch = helper.get_branch('Production')

	branch1 = helper.create_branch('Production Copy', '#000000', production_branch)
	branch2 = helper.create_branch('Production Copy 1', '#000000', production_branch)
	branch3 = helper.create_branch('Production Copy 2', '#000000', production_branch)

	request = merchantapi.request.BranchListDelete(helper.init_client())

	request.add_branch(branch1)
	request.add_branch(branch2)
	request.add_branch(branch3)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.BranchListDelete)

	assert response.get_processed() == 3


def test_branch_template_version_list_load_query():
	"""
	Tests the BranchTemplateVersionList_Load_Query API Call
	"""

	branch_template_version_list_load_query_test_list_load()


def branch_template_version_list_load_query_test_list_load():
	branch = helper.get_branch('Production')

	assert branch is not None

	request = merchantapi.request.BranchTemplateVersionListLoadQuery(helper.init_client(), branch)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.BranchTemplateVersionListLoadQuery)

	assert len(response.get_branch_template_versions()) > 0

	for e in response.get_branch_template_versions():
		assert isinstance(e, merchantapi.model.BranchTemplateVersion)


def test_changeset_template_version_list_load_query():
	"""
	Tests the ChangesetTemplateVersionList_Load_Query API Call
	"""

	changeset_template_version_list_load_query_test_list_load()


def changeset_template_version_list_load_query_test_list_load():
	helper.delete_branch('Production Copy')

	production_branch = helper.get_branch('Production')

	assert production_branch is not None

	branch = helper.create_branch('Production Copy', '#000000', production_branch)

	assert branch is not None
	
	# Load a Changeset
	load_changeset_request = merchantapi.request.ChangesetListLoadQuery(helper.init_client(), branch)
	load_changeset_response = load_changeset_request.send()

	helper.validate_response_success(load_changeset_response, merchantapi.response.ChangesetListLoadQuery)

	assert isinstance(load_changeset_response.get_changesets(), list)
	assert len(load_changeset_response.get_changesets()) > 0

	changeset = load_changeset_response.get_changesets()[0]

	assert isinstance(changeset, merchantapi.model.Changeset)

	request = merchantapi.request.ChangesetTemplateVersionListLoadQuery(helper.init_client(), changeset)
	
	assert changeset.get_id() == request.get_changeset_id()

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.ChangesetTemplateVersionListLoadQuery)

	assert len(response.get_changeset_template_versions()) > 0

	for e in response.get_changeset_template_versions():
		assert isinstance(e, merchantapi.model.ChangesetTemplateVersion)


def test_changeset_list_load_query():
	"""
	Tests the ChangesetTemplateVersionList_Load_Query API Call
	"""

	changeset_list_load_query_test_list_load()


def changeset_list_load_query_test_list_load():
	request = merchantapi.request.ChangesetListLoadQuery(helper.init_client())

	request.set_branch_name('Production')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.ChangesetListLoadQuery)

	assert len(response.get_changesets()) > 0

	for e in response.get_changesets():
		assert isinstance(e, merchantapi.model.Changeset)


def test_changeset_list_merge():
	"""
	Tests the ChangesetList_Merge API Call
	"""

	changeset_list_merge_test_merge()


def changeset_list_merge_test_merge():
	helper.delete_branch('Production Copy')

	production_branch = helper.get_branch('Production')

	assert production_branch is not None

	branch = helper.create_branch('Production Copy', '#000000', production_branch)

	assert branch is not None

	# Create 3 seperate Changes

	create_changeset_request1 = merchantapi.request.ChangesetCreate(helper.init_client(), branch)
	create_changeset_request2 = merchantapi.request.ChangesetCreate(helper.init_client(), branch)
	create_changeset_request3 = merchantapi.request.ChangesetCreate(helper.init_client(), branch)

	template1 = helper.get_branch_template_version('sfnt.mvc', branch)
	template2 = helper.get_branch_template_version('prod.mvc', branch)
	template3 = helper.get_branch_template_version('ctgy.mvc', branch)

	change1 = merchantapi.model.TemplateChange()
	change2 = merchantapi.model.TemplateChange()
	change3 = merchantapi.model.TemplateChange()

	change1.set_template_filename('sfnt.mvc').set_source(template1.get_source().replace('<body class="SFNT">', '<body class="SFNT">HELLO_WORLD'))
	change2.set_template_filename('prod.mvc').set_source(template2.get_source().replace('<body class="PROD">', '<body class="PROD">HELLO_WORLD'))
	change3.set_template_filename('ctgy.mvc').set_source(template3.get_source().replace('<body class="CTGY">', '<body class="CTGY">HELLO_WORLD'))

	create_changeset_request1.add_template_change(change1)
	create_changeset_request2.add_template_change(change2)
	create_changeset_request3.add_template_change(change3)

	create_changeset_response1 = create_changeset_request1.send()
	create_changeset_response2 = create_changeset_request2.send()
	create_changeset_response3 = create_changeset_request3.send()

	helper.validate_response_success(create_changeset_response1, merchantapi.response.ChangesetCreate)
	helper.validate_response_success(create_changeset_response2, merchantapi.response.ChangesetCreate)
	helper.validate_response_success(create_changeset_response3, merchantapi.response.ChangesetCreate)

	assert isinstance(create_changeset_response1.get_changeset(), merchantapi.model.Changeset)
	assert isinstance(create_changeset_response2.get_changeset(), merchantapi.model.Changeset)
	assert isinstance(create_changeset_response3.get_changeset(), merchantapi.model.Changeset)

	# Now merge the changes into one change

	request = merchantapi.request.ChangesetListMerge(helper.init_client(), branch)

	request.add_changeset(create_changeset_response1.get_changeset())
	request.add_changeset(create_changeset_response2.get_changeset())
	request.add_changeset(create_changeset_response3.get_changeset())

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.ChangesetListMerge)

	assert isinstance(response.get_changeset(), merchantapi.model.Changeset)


def test_changeset_change_list_load_query():
	"""
	Tests the ChangesetChangeList_Load_Query API Call
	"""

	changeset_change_list_load_query_test_list_load()


def changeset_change_list_load_query_test_list_load():
	helper.delete_branch('Production Copy')

	production_branch = helper.get_branch('Production')

	assert production_branch is not None

	branch = helper.create_branch('Production Copy', '#000000', production_branch)

	assert branch is not None

	# Create 3 Changes in one changeset

	create_changeset_request = merchantapi.request.ChangesetCreate(helper.init_client(), branch)

	template1 = helper.get_branch_template_version('sfnt.mvc', branch)
	template2 = helper.get_branch_template_version('prod.mvc', branch)
	template3 = helper.get_branch_template_version('ctgy.mvc', branch)

	change1 = merchantapi.model.TemplateChange()
	change2 = merchantapi.model.TemplateChange()
	change3 = merchantapi.model.TemplateChange()

	change1.set_template_filename('sfnt.mvc').set_source(template1.get_source().replace('<body class="SFNT">', '<body class="SFNT">HELLO_WORLD'))
	change2.set_template_filename('prod.mvc').set_source(template2.get_source().replace('<body class="PROD">', '<body class="PROD">HELLO_WORLD'))
	change3.set_template_filename('ctgy.mvc').set_source(template3.get_source().replace('<body class="CTGY">', '<body class="CTGY">HELLO_WORLD'))

	create_changeset_request.add_template_change(change1)
	create_changeset_request.add_template_change(change2)
	create_changeset_request.add_template_change(change3)

	create_changeset_response = create_changeset_request.send()

	helper.validate_response_success(create_changeset_response, merchantapi.response.ChangesetCreate)

	changeset = create_changeset_response.get_changeset()

	assert isinstance(changeset, merchantapi.model.Changeset)

	request = merchantapi.request.ChangesetChangeListLoadQuery(helper.init_client(), changeset)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.ChangesetChangeListLoadQuery)

	assert len(response.get_changeset_changes()) == 3

	for change in response.get_changeset_changes():
		assert isinstance(change, merchantapi.model.ChangesetChange)


def test_branch_css_resource_version_list_load_query():
	"""
	Tests the BranchCSSResourceVersionList_Load_Query API Call
	"""

	branch_css_resource_version_list_load_query_test_list_load()


def branch_css_resource_version_list_load_query_test_list_load():
	helper.delete_branch('Production Copy')

	production_branch = helper.get_branch('Production')

	assert production_branch is not None

	branch = helper.create_branch('Production Copy', '#000000', production_branch)

	assert branch is not None

	request = merchantapi.request.BranchCSSResourceVersionListLoadQuery(helper.init_client(), branch)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.BranchCSSResourceVersionListLoadQuery)

	assert len(response.get_branch_css_resource_versions()) > 0

	for version in response.get_branch_css_resource_versions():
		assert isinstance(version, merchantapi.model.CSSResourceVersion)


def test_branch_java_script_resource_version_list_load_query():
	"""
	Tests the BranchJavaScriptResourceVersionList_Load_Query API Call
	"""

	branch_java_script_resource_version_list_load_query_test_list_load()


def branch_java_script_resource_version_list_load_query_test_list_load():
	helper.delete_branch('Production Copy')

	production_branch = helper.get_branch('Production')

	assert production_branch is not None

	branch = helper.create_branch('Production Copy', '#000000', production_branch)

	assert branch is not None

	request = merchantapi.request.BranchJavaScriptResourceVersionListLoadQuery(helper.init_client(), branch)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.BranchJavaScriptResourceVersionListLoadQuery)

	assert len(response.get_branch_java_script_resource_versions()) > 0

	for version in response.get_branch_java_script_resource_versions():
		assert isinstance(version, merchantapi.model.JavaScriptResourceVersion)


def test_changeset_css_resource_version_list_load_query():
	"""
	Tests the ChangesetCSSResourceVersionList_Load_Query API Call
	"""

	helper.provision_store('ChangesetCSSResourceVersionList_Load_Query.xml')

	changeset_css_resource_version_list_load_query_test_list_load()


def changeset_css_resource_version_list_load_query_test_list_load():
	helper.delete_branch('Production Copy')

	default_branch = helper.get_branch('Production')

	assert default_branch is not None

	branch = helper.create_branch('Production Copy', default_branch.get_color(), default_branch)

	assert branch is not None

	changeset_request = merchantapi.request.ChangesetListLoadQuery(helper.init_client())
	changeset_request.set_branch_id(branch.get_id())

	changeset_response = changeset_request.send()

	helper.validate_response_success(changeset_response, merchantapi.response.ChangesetListLoadQuery)

	assert len(changeset_response.get_changesets()) == 1
	assert changeset_response.get_changesets()[0].get_id() > 0

	request = merchantapi.request.ChangesetCSSResourceVersionListLoadQuery(helper.init_client())
	request.set_changeset_id(changeset_response.get_changesets()[0].get_id())

	request.set_filters(
		request.filter_expression()
			.like('code', 'ChangesetCSSResourceVersionListLoadQuery%')
	)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.ChangesetCSSResourceVersionListLoadQuery)

	assert len(response.get_changeset_css_resource_versions()) == 6

	for version in response.get_changeset_css_resource_versions():
		assert isinstance(version, merchantapi.model.CSSResourceVersion)

		assert len(version.get_attributes()) > 0

		for attribute in version.get_attributes():
			assert isinstance(attribute, merchantapi.model.CSSResourceVersionAttribute)


def test_changeset_java_script_resource_version_list_load_query():
	"""
	Tests the ChangesetJavaScriptResourceVersionList_Load_Query API Call
	"""

	helper.provision_store('ChangesetJavaScriptResourceVersionList_Load_Query.xml')

	changeset_java_script_resource_version_list_load_query_test_list_load()


def changeset_java_script_resource_version_list_load_query_test_list_load():
	helper.delete_branch('Production Copy 1')

	default_branch = helper.get_branch('Production')

	assert default_branch is not None

	create_request = merchantapi.request.BranchCreate(helper.init_client(), default_branch)
	create_request.set_name('Production Copy 1')
	create_request.set_color(default_branch.get_color())

	create_response = create_request.send()

	helper.validate_response_success(create_response, merchantapi.response.BranchCreate)

	changeset_request = merchantapi.request.ChangesetListLoadQuery(helper.init_client())
	changeset_request.set_branch_id(create_response.get_branch().get_id())

	changeset_response = changeset_request.send()

	helper.validate_response_success(changeset_response, merchantapi.response.ChangesetListLoadQuery)

	assert len(changeset_response.get_changesets()) == 1
	assert changeset_response.get_changesets()[0].get_id() > 0

	request = merchantapi.request.ChangesetJavaScriptResourceVersionListLoadQuery(helper.init_client())
	request.set_changeset_id(changeset_response.get_changesets()[0].get_id())

	request.set_filters(
		request.filter_expression()
			.like('code', 'ChangesetJavaScriptResourceVersionListLoadQuery%')
	)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.ChangesetJavaScriptResourceVersionListLoadQuery)

	assert len(response.get_changeset_java_script_resource_versions()) == 6

	for version in response.get_changeset_java_script_resource_versions():
		assert isinstance(version, merchantapi.model.ChangesetJavaScriptResourceVersion)

		assert len(version.get_attributes()) > 0

		for attribute in version.get_attributes():
			assert isinstance(attribute, merchantapi.model.JavaScriptResourceVersionAttribute)


def test_branch_property_version_list_load_query():
	"""
	Tests the BranchPropertyVersionList_Load_Query API Call
	"""

	branch_property_version_list_load_query_test_list_load()


def branch_property_version_list_load_query_test_list_load():
	helper.delete_branch('Production Copy')

	default_branch = helper.get_branch('Production')

	assert default_branch is not None

	branch = helper.create_branch('Production Copy', default_branch.get_color(), default_branch)

	assert branch is not None

	request = merchantapi.request.BranchPropertyVersionListLoadQuery(helper.init_client(), branch)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.BranchPropertyVersionListLoadQuery)

	assert len(response.get_branch_property_versions()) > 0

	for v in response.get_branch_property_versions():
		assert isinstance(v, merchantapi.model.BranchPropertyVersion)


def test_changeset_property_version_list_load_query():
	"""
	Tests the ChangesetPropertyVersionList_Load_Query API Call
	"""

	changeset_property_version_list_load_query_test_list_load()


def changeset_property_version_list_load_query_test_list_load():
	helper.delete_branch('Production Copy')

	default_branch = helper.get_branch('Production')

	assert default_branch is not None

	branch = helper.create_branch('Production Copy', default_branch.get_color(), default_branch)

	assert branch is not None

	changeset_request = merchantapi.request.ChangesetListLoadQuery(helper.init_client(), branch)
	changeset_response = changeset_request.send()

	helper.validate_response_success(changeset_response, merchantapi.response.ChangesetListLoadQuery)

	assert len(changeset_response.get_changesets()) == 1
	assert changeset_response.get_changesets()[0].get_id() > 0

	request = merchantapi.request.ChangesetPropertyVersionListLoadQuery(helper.init_client(), changeset_response.get_changesets()[0])

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.ChangesetPropertyVersionListLoadQuery)

	assert len(response.get_changeset_property_versions()) > 0

	for v in response.get_changeset_property_versions():
		assert isinstance(v, merchantapi.model.ChangesetPropertyVersion)


def test_order_price_group_update_assigned():
	"""
	Tests the OrderPriceGroup_Update_Assigned API Call
	"""

	helper.provision_store('OrderPriceGroup_Update_Assigned.xml')

	order_price_group_update_assigned_test_assignment()
	order_price_group_update_assigned_test_unassignment()


def order_price_group_update_assigned_test_assignment():
	order = helper.get_order(3651499)

	assert order is not None

	request = merchantapi.request.OrderPriceGroupUpdateAssigned(helper.init_client(), order)

	assert order.get_id() == request.get_order_id()

	request.set_price_group_name('OrderPriceGroup_Update_Assigned_1')
	request.set_assigned(True)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderPriceGroupUpdateAssigned)

	check_request = merchantapi.request.OrderPriceGroupListLoadQuery(helper.init_client(), order)
	check_request.set_filters(
		check_request.filter_expression()
		.equal('name', 'OrderPriceGroup_Update_Assigned_1')
	)

	assert order.get_id() == check_request.get_order_id()

	check_request.set_assigned(True)
	check_request.set_unassigned(False)

	check_response = check_request.send()

	helper.validate_response_success(check_response, merchantapi.response.OrderPriceGroupListLoadQuery)

	assert len(check_response.get_order_price_groups()) == 1
	assert check_response.get_order_price_groups()[0].get_name() == 'OrderPriceGroup_Update_Assigned_1'


def order_price_group_update_assigned_test_unassignment():
	order = helper.get_order(3651499)

	assert order is not None

	request = merchantapi.request.OrderPriceGroupUpdateAssigned(helper.init_client(), order)

	assert order.get_id() == request.get_order_id()

	request.set_price_group_name('OrderPriceGroup_Update_Assigned_2')
	request.set_assigned(False)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderPriceGroupUpdateAssigned)

	check_request = merchantapi.request.OrderPriceGroupListLoadQuery(helper.init_client(), order)

	check_request.set_filters(
		check_request.filter_expression()
		.equal('name', 'OrderPriceGroup_Update_Assigned_2')
	)

	assert order.get_id() == check_request.get_order_id()

	check_request.set_assigned(False)
	check_request.set_unassigned(True)

	check_response = check_request.send()

	helper.validate_response_success(check_response, merchantapi.response.OrderPriceGroupListLoadQuery)

	assert len(check_response.get_order_price_groups()) == 1
	assert check_response.get_order_price_groups()[0].get_name() == 'OrderPriceGroup_Update_Assigned_2'


def test_order_price_group_list_load_query():
	"""
	Tests the OrderPriceGroupList_Load_Query API Call
	"""

	helper.provision_store('OrderPriceGroupList_Load_Query.xml')

	order_price_group_list_load_query_test_list_load()


def order_price_group_list_load_query_test_list_load():
	order = helper.get_order(3651498)

	assert order is not None

	request = merchantapi.request.OrderPriceGroupListLoadQuery(helper.init_client(), order)

	request.set_assigned(True)
	request.set_unassigned(False)

	assert order.get_id() == request.get_order_id()

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderPriceGroupListLoadQuery)

	assert len(response.get_order_price_groups()) == 2
	for order_price_group in response.get_order_price_groups():
		assert isinstance(order_price_group, merchantapi.model.OrderPriceGroup)
		assert order_price_group.get_name() in ('OrderPriceGroupListLoadQuery_1', 'OrderPriceGroupListLoadQuery_2')


def test_order_coupon_update_assigned():
	"""
	Tests the OrderPriceGroup_Update_Assigned API Call
	"""

	helper.provision_store('OrderCoupon_Update_Assigned.xml')

	order_coupon_update_assigned_test_assignment()
	order_coupon_update_assigned_test_unassignment()


def order_coupon_update_assigned_test_assignment():
	order = helper.get_order(3651500)

	assert order is not None

	request = merchantapi.request.OrderCouponUpdateAssigned(helper.init_client(), order)

	assert order.get_id() == request.get_order_id()

	request.set_coupon_code('OrderCouponUpdateAssigned_1')
	request.set_assigned(True)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderCouponUpdateAssigned)

	check_request = merchantapi.request.OrderCouponListLoadQuery(helper.init_client(), order)

	assert order.get_id() == check_request.get_order_id()

	check_request.set_assigned(True)
	check_request.set_unassigned(False)
	check_request.set_filters(
		check_request.filter_expression()
		.equal('code', 'OrderCouponUpdateAssigned_1')
	)

	check_response = check_request.send()

	helper.validate_response_success(check_response, merchantapi.response.OrderCouponListLoadQuery)

	assert len(check_response.get_order_coupons()) == 1
	assert check_response.get_order_coupons()[0].get_code() == 'OrderCouponUpdateAssigned_1'


def order_coupon_update_assigned_test_unassignment():
	order = helper.get_order(3651500)

	assert order is not None

	request = merchantapi.request.OrderCouponUpdateAssigned(helper.init_client(), order)

	assert order.get_id() == request.get_order_id()

	request.set_coupon_code('OrderCouponUpdateAssigned_2')
	request.set_assigned(False)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderCouponUpdateAssigned)

	check_request = merchantapi.request.OrderCouponListLoadQuery(helper.init_client(), order)

	check_request.set_filters(
		check_request.filter_expression()
		.equal('code', 'OrderCouponUpdateAssigned_2')
	)

	assert order.get_id() == check_request.get_order_id()

	check_request.set_assigned(False)
	check_request.set_unassigned(True)

	check_response = check_request.send()

	helper.validate_response_success(check_response, merchantapi.response.OrderCouponListLoadQuery)

	assert len(check_response.get_order_coupons()) == 1
	assert check_response.get_order_coupons()[0].get_code() == 'OrderCouponUpdateAssigned_2'


def test_order_coupon_list_load_query():
	"""
	Tests the OrderCouponList_Load_Query API Call
	"""

	helper.provision_store('OrderCouponList_Load_Query.xml')

	order_coupon_list_load_query_test_list_load()


def order_coupon_list_load_query_test_list_load():
	order = helper.get_order(3651501)

	assert order is not None

	request = merchantapi.request.OrderCouponListLoadQuery(helper.init_client(), order)

	request.set_assigned(True)
	request.set_unassigned(False)

	assert order.get_id() == request.get_order_id()

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderCouponListLoadQuery)

	assert len(response.get_order_coupons()) == 3
	for order_coupon in response.get_order_coupons():
		assert isinstance(order_coupon, merchantapi.model.OrderCoupon)
		assert order_coupon.get_code() in ('OrderCouponList_Load_Query_1', 'OrderCouponList_Load_Query_2', 'OrderCouponList_Load_Query_3')


def test_customer_history_list_load_query():
	"""
	Tests the CustomerCreditHistoryList_Load_Query API Call
	"""

	helper.provision_store('CustomerCreditHistoryList_Load_Query.xml')

	customer_history_list_load_query_test_list_load()


def customer_history_list_load_query_test_list_load():
	customer = helper.get_customer('CustomerHistoryListLoadQuery')

	assert customer is not None

	for i in range(0, 3):
		insert_request = merchantapi.request.CustomerCreditHistoryInsert(helper.init_client(), customer)
		insert_request.set_amount(1.99)
		insert_request.set_description('DESCRIPTION')
		insert_request.set_transaction_reference('REFERENCE')
		helper.validate_response_success(insert_request.send(), merchantapi.response.CustomerCreditHistoryInsert)

	request = merchantapi.request.CustomerCreditHistoryListLoadQuery(helper.init_client(), customer)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CustomerCreditHistoryListLoadQuery)

	assert len(response.get_customer_credit_history()) == 3
	for history in response.get_customer_credit_history():
		assert isinstance(history, merchantapi.model.CustomerCreditHistory)
		assert history.get_description() == 'DESCRIPTION'
		assert history.get_transaction_reference() == 'REFERENCE'
		assert history.get_amount() == 1.99


def test_customer_history_insert():
	"""
	Tests the CustomerCreditHistory_Insert API Call
	"""

	helper.provision_store('CustomerCreditHistory_Insert.xml')

	customer_history_insert_test_insertion()


def customer_history_insert_test_insertion():
	customer = helper.get_customer('CustomerCreditHistoryInsert')

	assert customer is not None

	request = merchantapi.request.CustomerCreditHistoryInsert(helper.init_client(), customer)

	assert request.get_customer_id() == customer.get_id()

	request.set_amount(1.99)
	request.set_description('DESCRIPTION')
	request.set_transaction_reference('REFERENCE')

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CustomerCreditHistoryInsert)


def test_customer_history_delete():
	"""
	Tests the CustomerCreditHistory_Delete API Call
	"""

	helper.provision_store('CustomerCreditHistory_Delete.xml')

	customer_history_delete_test_deletion()


def customer_history_delete_test_deletion():
	customer = helper.get_customer('CustomerCreditHistoryDelete')

	assert customer is not None

	add_request = merchantapi.request.CustomerCreditHistoryInsert(helper.init_client(), customer)

	assert add_request.get_customer_id() == customer.get_id()

	add_request.set_amount(1.99)
	add_request.set_description('DESCRIPTION')
	add_request.set_transaction_reference('REFERENCE')

	add_response = add_request.send()

	helper.validate_response_success(add_response, merchantapi.response.CustomerCreditHistoryInsert)

	load_request = merchantapi.request.CustomerCreditHistoryListLoadQuery(helper.init_client(), customer)

	load_response = load_request.send()

	helper.validate_response_success(load_response, merchantapi.response.CustomerCreditHistoryListLoadQuery)

	assert len(load_response.get_customer_credit_history()) == 1

	history = load_response.get_customer_credit_history()[0]

	assert isinstance(history, merchantapi.model.CustomerCreditHistory)

	request = merchantapi.request.CustomerCreditHistoryDelete(helper.init_client(), history)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.CustomerCreditHistoryDelete)


def test_order_item_list_create_return():
	"""
	Tests the OrderItemList_CreateReturn API Call
	"""

	helper.provision_store('OrderItemList_CreateReturn.xml')

	order_item_list_create_return_create_return()
	order_item_list_create_return_invalid_order()
	order_item_list_create_return_invalid_line_ids()


def order_item_list_create_return_create_return():
	order = helper.get_order(529555)

	assert order is not None

	request = merchantapi.request.OrderItemListCreateReturn(helper.init_client(), order)

	assert request.get_order_id() == order.get_id()

	for item in order.get_items():
		request.add_order_item(item)

	assert len(request.get_line_ids()) == len(order.get_items())

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderItemListCreateReturn)

	assert isinstance(response.get_order_return(), merchantapi.model.OrderReturn)
	assert response.get_order_return().get_status() == merchantapi.model.OrderReturn.ORDER_RETURN_STATUS_ISSUED


def order_item_list_create_return_invalid_order():
	request = merchantapi.request.OrderItemListCreateReturn(helper.init_client())
	request.set_order_id(999999999)

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.OrderItemListCreateReturn)


def order_item_list_create_return_invalid_line_ids():
	request = merchantapi.request.OrderItemListCreateReturn(helper.init_client())
	request.set_order_id(529555)

	response = request.send()

	helper.validate_response_error(response, merchantapi.response.OrderItemListCreateReturn)


def test_order_return_list_received():
	"""
	Tests the OrderReturnList_Received API Call
	"""

	helper.provision_store('OrderReturnList_Received.xml')

	order_return_list_received_test_received_return()


def order_return_list_received_test_received_return():
	order = helper.get_order(529556)

	assert order is not None

	create_request = merchantapi.request.OrderItemListCreateReturn(helper.init_client(), order)

	assert create_request.get_order_id() == order.get_id()

	for item in order.get_items():
		create_request.add_order_item(item)

	assert len(create_request.get_line_ids()) == len(order.get_items())

	create_response = create_request.send()

	helper.validate_response_success(create_response, merchantapi.response.OrderItemListCreateReturn)

	assert isinstance(create_response.get_order_return(), merchantapi.model.OrderReturn)
	assert create_response.get_order_return().get_status() == merchantapi.model.OrderReturn.ORDER_RETURN_STATUS_ISSUED

	request = merchantapi.request.OrderReturnListReceived(helper.init_client())

	for item in order.get_items():
		received_return = merchantapi.model.ReceivedReturn()
		received_return.set_return_id(create_response.get_order_return().get_id())
		received_return.set_adjust_inventory(1)

		request.add_received_return(received_return)

	response = request.send()

	helper.validate_response_success(response, merchantapi.response.OrderReturnListReceived)

	check_order = helper.get_order(order.get_id())

	assert check_order is not None

	for item in check_order.get_items():
		assert item.get_status() ==  merchantapi.model.OrderReturn.ORDER_RETURN_STATUS_RECEIVED


def test_template_version_settings():
	"""
	Tests the TemplateVersionSettings model within various API Calls
	"""

	template_version_settings_test_serialization()
	template_version_settings_test_deserialization()


def template_version_settings_test_serialization():
	data = {
		"foo": {
			"bar": "bin",
			"baz": 1,
			"bin": 1.99
		},
		"bar": {
			"array": [
				"foo",
				"bar"
			]
		},
		"baz": "bar"
	}

	model = merchantapi.model.TemplateVersionSettings(data)

	serialized = model.to_dict()

	assert isinstance(serialized, dict)

	assert 'foo' in serialized
	assert 'bar' in serialized
	assert 'baz' in serialized

	assert serialized['foo']['bar'] == 'bin'
	assert serialized['foo']['baz'] == 1
	assert serialized['foo']['bin'] == 1.99
	assert serialized['bar']['array'][0] == 'foo'
	assert serialized['bar']['array'][1] == 'bar'
	assert serialized['baz'] == 'bar'


def template_version_settings_test_deserialization():
	data = {
		"foo": {
			"bar": "bin",
			"baz": 1,
			"bin": 1.99
		},
		"bar": {
			"array": [
				"foo",
				"bar"
			]
		},
		"baz": "bar"
	}

	model = merchantapi.model.TemplateVersionSettings(data)

	assert model.is_dict() is True
	assert model.is_scalar() is False
	assert model.is_list() is False

	assert model.has_item('foo') is True
	assert model.item_has_property('foo', 'bar') is True
	assert model.item_has_property('foo', 'baz') is True
	assert model.item_has_property('foo', 'bin') is True
	assert model.get_item_property('foo', 'bar') == "bin"
	assert model.get_item_property('foo', 'baz') == 1
	assert model.get_item_property('foo', 'bin') == 1.99

	assert model.has_item('bar') is True
	assert model.item_has_property('bar', 'array') is True
	assert isinstance(model.get_item_property('bar', 'array'), list)

	assert model.has_item('baz') is True
	assert model.item_has_property('baz', 'NONE') is False
	assert model.get_item('baz') == 'bar'


def test_resource_group_list_load_query():
	"""
	Tests the ResourceGroupList_Load_Query  API Call
	"""

	resource_group_list_load_query_test_list_load()


def resource_group_list_load_query_test_list_load():
	helper.delete_branch('Production Copy 1')

	default_branch = helper.get_branch('Production')

	assert default_branch is not None

	create_request = merchantapi.request.BranchCreate(helper.init_client(), default_branch)
	create_request.set_name('Production Copy 1')
	create_request.set_color(default_branch.get_color())

	create_response = create_request.send()

	helper.validate_response_success(create_response, merchantapi.response.BranchCreate)

	changeset_request = merchantapi.request.ChangesetListLoadQuery(helper.init_client())
	changeset_request.set_branch_id(create_response.get_branch().get_id())

	changeset_response = changeset_request.send()

	helper.validate_response_success(changeset_response, merchantapi.response.ChangesetListLoadQuery)

	assert len(changeset_response.get_changesets()) == 1
	assert changeset_response.get_changesets()[0].get_id() > 0

	request = merchantapi.request.ResourceGroupListLoadQuery(helper.init_client(), create_response.get_branch())
	request.set_on_demand_columns(request.get_available_on_demand_columns())
	request.set_changeset_id(changeset_response.get_changesets()[0].get_id())
	
	response = request.send()

	helper.validate_response_success(response, merchantapi.response.ResourceGroupListLoadQuery)


def test_miva_merchant_verison():
	"""
	Tests the ResourceGroupList_Load_Query  API Call
	"""

	request = merchantapi.request.MivaMerchantVersion(helper.init_client())
	
	response = request.send()

	helper.validate_response_success(response, merchantapi.response.MivaMerchantVersion)

	assert isinstance(response.get_merchant_version(), merchantapi.model.MerchantVersion)

	assert isinstance(response.get_merchant_version().get_version(), str) and len(response.get_merchant_version().get_version())
	assert isinstance(response.get_merchant_version().get_major(), int) and response.get_merchant_version().get_major() >= 10
	assert isinstance(response.get_merchant_version().get_minor(), int) and response.get_merchant_version().get_minor() >= 0
	assert isinstance(response.get_merchant_version().get_bugfix(), int) and response.get_merchant_version().get_bugfix() >= 0


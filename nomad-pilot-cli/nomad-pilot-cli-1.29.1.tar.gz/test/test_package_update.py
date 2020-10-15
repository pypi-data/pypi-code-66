# coding: utf-8

"""
    Nomad Pilot

    This is the API descriptor for the Nomad Pilot API, responsible for shipping and logistics processing. Developed by `Samarkand Global <https://samarkand.global>`_ in partnership with `SF Express <https://www.sf- express.com/cn/sc/>`_, `eSinotrans <http://www.esinotrans.com/haitao.html>`_. Read the documentation online at `Nomad API Suite <https://api.samarkand.io/>`_ and Check out the detailed `changelog <https://gitlab.com/samarkand-nomad/nomad_readme/-/raw/master/history/nomad_pilot.md>`_. - Install for node with ``npm install nomad_pilot_cli`` - Install for python with ``pip install nomad-pilot-cli``  # noqa: E501

    The version of the OpenAPI document: 1.29.1
    Contact: paul@samarkand.global
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import nomad_pilot_cli
from nomad_pilot_cli.models.package_update import PackageUpdate  # noqa: E501
from nomad_pilot_cli.rest import ApiException

class TestPackageUpdate(unittest.TestCase):
    """PackageUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PackageUpdate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = nomad_pilot_cli.models.package_update.PackageUpdate()  # noqa: E501
        if include_optional :
            return PackageUpdate(
                dimension = nomad_pilot_cli.models.dimension.Dimension(
                    weight = 1.337, 
                    height = 1.337, 
                    length = 1.337, 
                    width = 1.337, ), 
                ship_from = nomad_pilot_cli.models.address.Address(
                    first_name = 'John', 
                    last_name = '0', 
                    address1 = '0', 
                    address2 = '0', 
                    county = '0', 
                    city = '0', 
                    state = '0', 
                    country = '0', 
                    zip = '0', 
                    tin = '0', 
                    phone = '0', 
                    country_code = '142', 
                    id_card = '0', 
                    email = '0', 
                    company = '0', 
                    ecommerce_website_user_id = '0', ), 
                ship_to = nomad_pilot_cli.models.address.Address(
                    first_name = 'John', 
                    last_name = '0', 
                    address1 = '0', 
                    address2 = '0', 
                    county = '0', 
                    city = '0', 
                    state = '0', 
                    country = '0', 
                    zip = '0', 
                    tin = '0', 
                    phone = '0', 
                    country_code = '142', 
                    id_card = '0', 
                    email = '0', 
                    company = '0', 
                    ecommerce_website_user_id = '0', ), 
                bill = nomad_pilot_cli.models.address.Address(
                    first_name = 'John', 
                    last_name = '0', 
                    address1 = '0', 
                    address2 = '0', 
                    county = '0', 
                    city = '0', 
                    state = '0', 
                    country = '0', 
                    zip = '0', 
                    tin = '0', 
                    phone = '0', 
                    country_code = '142', 
                    id_card = '0', 
                    email = '0', 
                    company = '0', 
                    ecommerce_website_user_id = '0', ), 
                order_ref = '0', 
                seller_order_ref = '0', 
                tracking_reference = '0', 
                order_time = '0', 
                gross_weight = 1.337, 
                net_weight = 1.337, 
                total_price = 1.337, 
                currency = 'RMB', 
                mass_unit = 'Kilogram', 
                length_unit = 'Centimetre', 
                domestic_delivery_company = 'YTO', 
                created_at = '2019-07-12T13:13:52.004637+01:00', 
                updated_at = '2019-07-12T13:13:52.004637+01:00', 
                pay_method = 'EASIPAY', 
                pay_merchant_name = 'Paypal', 
                pay_amount = 611.08, 
                pay_id = '2014030120394812', 
                paid_at = '2019-07-12T13:13:52.004637+01:00', 
                products_total_tax = 53.28, 
                shipping_cost = 25.0, 
                non_cash_deduction_amount = 0.0, 
                customer_note = 'This package is very important.', 
                cancel_reason = 'The customers updated the address.', 
                warehouse_code = '718595286704', 
                customer_id_ref = '0', 
                insurance_fee = 2.5, 
                express_type = 'BC', 
                payment_pay_id = '191028195204000214', 
                platform_name = 'youzan', 
                check_point = '0', 
                items = [
                    nomad_pilot_cli.models.package_item.PackageItem(
                        name = '0', 
                        name_cn = '0', 
                        barcode = '0', 
                        sku_number = 'SMK123', 
                        quantity = 7, 
                        price = 21.3, 
                        brand = '0', 
                        quantity_uom = '50G', 
                        hs_code = '0', 
                        country_of_origin = '0', 
                        goldjet = nomad_pilot_cli.models.goldjet.Goldjet(
                            goods_ptcode = '0', ), 
                        gross_weight = 1.337, 
                        net_weight = 1.337, 
                        customs_unit_code = '142, 007, 瓶, ...', 
                        customs_unit_code_package = '142, 011, 140', 
                        customs_unit_code_weight = '035', 
                        customs_filing_id = '0', 
                        spec = '25mm', 
                        model = 'iPhone XR', 
                        ingredients = '发酵乳杆菌Lc40（CECT5716），麦芽糊精，蔗糖，抗坏血酸钠', )
                    ]
            )
        else :
            return PackageUpdate(
                tracking_reference = '0',
        )

    def testPackageUpdate(self):
        """Test PackageUpdate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

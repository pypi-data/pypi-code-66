# Copyright (C) 2019 Majormode.  All rights reserved.
#
# This software is the confidential and proprietary information of
# Majormode or one of its subsidiaries.  You shall not disclose this
# confidential information and shall use it only in accordance with the
# terms of the license agreement or other applicable agreement you
# entered into with Majormode.
#
# MAJORMODE MAKES NO REPRESENTATIONS OR WARRANTIES ABOUT THE SUITABILITY
# OF THE SOFTWARE, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
# TO THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE, OR NON-INFRINGEMENT.  MAJORMODE SHALL NOT BE LIABLE FOR ANY
# LOSSES OR DAMAGES SUFFERED BY LICENSEE AS A RESULT OF USING, MODIFYING
# OR DISTRIBUTING THIS SOFTWARE OR ITS DERIVATIVES.

from majormode.perseus.client.service.base_service import BaseService
from majormode.perseus.model.locale import DEFAULT_LOCALE
from majormode.perseus.model.obj import Object


class SchoolService(BaseService):
    BaseService._declare_custom_exceptions({
    })

    def get_school_buses_locations(self, school_id):
        """

        :param school_id:

        :return:
        """
        return Object.from_json(
            self.send_request(
                http_method=self.HttpMethod.GET,
                path='/school/(school_id)/tracker/location',
                url_bits={
                    'school_id': school_id
                },
                authentication_required=True,
                signature_required=True))

    def search_schools(
            self,
            area_id=None,
            include_education_grades=False,
            ip_address=None,
            keywords=None,
            location=None,
            limit=None,
            locale=DEFAULT_LOCALE,
            offset=0):
        """
        Return a list of schools that have joined the School Bus Program and
        that correspond to the specified criteria.


        :param area_id: Identification of a geographical area to return
            schools.

        :param include_education_grades: Indicate whether to include the
            education grades that this school supports.

        :param ip_address: IPv4 address of the machine of the user, a tuple
            consisting of four decimal numbers, each ranging from ``0`` to
            ``255``.

        :param keywords: A list of keywords to search schools for.

        :param limit: Constrain the number of places to return to the
            specified number.  If not specified, the default value is
            ``BaseService.DEFAULT_RESULT_SET_SIZE``.  The maximum value is
            ``BaseService.MAXIMUM_RESULT_SET_LIMIT``.

        :param locale: An instance ``Locale`` to return textual information,
            such as the names of countries and the names of schools.

        :param location: An instance ``GeoPoint`` that indicates the user's
            location.

        :param offset: Require to skip that many records before beginning to
            return records to the client.  Default value is ``0``.  If both
            ``offset`` and ``limit`` are specified, then ``offset`` records
            are skipped before starting to count the limit records that are
            returned.


        @return: An object containing the following attributes:

        """
        return Object.from_json(
            self.send_request(
                http_method=self.HttpMethod.GET,
                path='/school',
                arguments={
                    'area_id': area_id,
                    'include_education_grades': include_education_grades,
                    'ip_address': ip_address and '.'.join([str(byte) for byte in ip_address]),
                    'keywords': keywords and ','.join(keywords if isinstance(keywords, (list, set, tuple)) else [keywords]),
                    'limit': limit,
                    'll': location and f'{location.latitude},{location.longitude}',
                    'locale': locale,
                    'offset': offset
                },
                authentication_required=False,
                signature_required=True))

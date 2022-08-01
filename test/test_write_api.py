"""
    Ory Keto API

    Documentation for all of Ory Keto's REST APIs. gRPC is documented separately.   # noqa: E501

    The version of the OpenAPI document: v0.9.0-alpha.0
    Contact: hi@ory.sh
    Generated by: https://openapi-generator.tech
"""


import unittest

import ory_keto_client
from ory_keto_client.api.write_api import WriteApi  # noqa: E501


class TestWriteApi(unittest.TestCase):
    """WriteApi unit test stubs"""

    def setUp(self):
        self.api = WriteApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_relation_tuple(self):
        """Test case for create_relation_tuple

        Create a Relation Tuple  # noqa: E501
        """
        pass

    def test_delete_relation_tuples(self):
        """Test case for delete_relation_tuples

        Delete Relation Tuples  # noqa: E501
        """
        pass

    def test_patch_relation_tuples(self):
        """Test case for patch_relation_tuples

        Patch Multiple Relation Tuples  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

import unittest
from leaky.utils.tests import BaseTestCase


class TestGeneral(BaseTestCase):
    """ Generic tests for invoices and assets """

    def test_00_all_empty(self):
        assert not self.execute("{products(first:1){edges{node{id}}}}")['products']['edges'], "Products detected: Database shouldbe empty"
        assert not self.execute("{reviews(first:1){edges{node{id}}}}")['reviews']['edges'], "Reviews detected: Database shouldbe empty"
        assert not self.execute("{reviewComments(first:1){edges{node{id}}}}")['reviewComments']['edges'], "ReviewComments detected: Database shouldbe empty"
        assert not self.execute("{assets(first:1){edges{node{id}}}}", tenant_name="test")['assets']['edges'], "Assets detected: Database shouldbe empty"
        assert not self.execute("{assetTags(first:1){edges{node{id}}}}", tenant_name="test")['assetTags']['edges'], "AssetTags detected: Database shouldbe empty"
        assert not self.execute("{invoices(first:1){edges{node{id}}}}", tenant_name="test")['invoices']['edges'], "Invoices detected: Database shouldbe empty"

    def test_01_create_update_store(self):
        pass

    def test_02_create_update_product(self):
        pass

    def test_03_create_update_custom_product(self):
        pass

    def test_04_create_update_asset_policy(self):
        pass

    def test_05_create_update_asset_from_product(self):
        pass

    def test_06_create_update_asset_from_custom_product(self):
        pass

    def test_07_create_update_custom_asset_from_product(self):
        pass

    def test_08_create_update_custom_asset_from_custom_product(self):
        pass

    def test_09_invoice_subscription(self):
        pass

    def test_10_create_update_invoice(self):
        pass

    def test_11_create_update_asset_tags(self):
        pass

    def test_12_create_update_invoice_after_tagging(self):
        pass

    def test_13_asset_timeline(self):
        pass

    def test_14_ordering(self):
        pass


if __name__ == '__main__':
    unittest.main()

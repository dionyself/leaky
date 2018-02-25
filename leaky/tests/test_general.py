import unittest
from leaky.utils.tests import BaseTestCase


class TestGeneral(BaseTestCase):
    """ Generic tests for invoices and assets """

    def test_00_all_empty(self):
        nodes = ['products', 'reviews', 'reviewComments', 'assets', 'assetTags', 'invoices']
        tenant_nodes = ['assets', 'assetTags', 'invoices']
        for node in nodes:
            assert not self.execute(
                "{%s(first:1){edges{node{id}}}}" % node, tenant_name=(node in tenant_nodes) and "test" or "public")[node]['edges'], \
                "{} detected: Database shouldbe empty".format(node)

    def test_01_create_update_corporation(self):
        result = self.execute("""mutation {createCorporation(
            name: "general_corp",
            description: "test general description",
            properties: {},
            relatedCorporationId: 0,
            userId: 0,
            phone: "5-555-5555",
            isActive: true,
            isDeleted: false) {
                corporationId
                ok}
            }""", tenant_name="test")
        assert result['createCorporation']['corporationId'] == 2
        assert result['createCorporation']['ok']

        result = self.execute("""mutation {updateCorporation(
            id: 2,
            name: "general corp",
            description: "test",
            properties: {asf: 1},
            relatedCorporationId: 1,
            phone: "5-555-5556",
            isActive: false,
            isDeleted: false) {
                corporationId
                ok}
        }""", tenant_name="test")
        assert result['updateCorporation']['corporationId'] == 2
        assert result['updateCorporation']['ok']
        result = self.execute("""{corporations(first:1, description:"test") { edges {
            node {
                id
                name
                description
                properties
                phone
                createdAt
                updatedAt
                isActive
                isDeleted
            }
        }}}""", tenant_name="test")
        assert result['corporations']['edges'][0]['node']["name"] == 'general corp'
        assert result['corporations']['edges'][0]['node']["description"] == 'test'
        assert result['corporations']['edges'][0]['node']["properties"]["asf"] == 1
        assert result['corporations']['edges'][0]['node']["phone"] == '5-555-5556'
        assert result['corporations']['edges'][0]['node']["createdAt"] < result['corporations']['edges'][0]['node']["updatedAt"]
        assert result['corporations']['edges'][0]['node']["isActive"] == False
        assert result['corporations']['edges'][0]['node']["isDeleted"] == False

    def test_02_create_update_user(self):
        pass

    def test_03_create_update_store(self):
        pass

    def test_04_create_update_product(self):
        pass

    def test_05_create_update_custom_product(self):
        pass

    def test_06_create_update_asset_policy(self):
        pass

    def test_07_create_update_asset_from_product(self):
        pass

    def test_08_create_update_asset_from_custom_product(self):
        pass

    def test_09_create_update_custom_asset_from_product(self):
        pass

    def test_10_create_update_custom_asset_from_custom_product(self):
        pass

    def test_11_invoice_subscription(self):
        pass

    def test_12_create_update_invoice(self):
        pass

    def test_13_create_update_asset_tags(self):
        pass

    def test_14_create_update_invoice_after_tagging(self):
        pass

    def test_15_shipping_proccess(self):
        pass

    def test_16_asset_timeline(self):
        pass

    def test_17_case_pre_shipping_process(self):
        pass

    def test_18_invoice_timeline(self):
        pass

    def test_19_case_post_shipping_process(self):
        pass

    def test_20_ordering(self):
        pass

    def test_21_daily_reports(self):
        pass

    def test_22_weekly_reports(self):
        pass

    def test_23_anual_reports(self):
        pass

    def test_23_daily_recommends(self):
        pass

    def test_24_daily_recommends_subscriptions(self):
        pass

    def test_23_weekly_recommends(self):
        pass

    def test_24_weekly_recommends_subscriptions(self):
        pass

    def test_23_anual_recommends(self):
        pass

    def test_24_anuals_recommends_subscriptions(self):
        pass

class TestGeneralPermissions(BaseTestCase):
    """ Generic tests for permissions """
    pass

class TestReviewSystem(BaseTestCase):
    """ Generic tests for review system """
    pass


if __name__ == '__main__':
    unittest.main()

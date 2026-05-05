import unittest
from aep_core import AEPNode

class TestAEPNode(unittest.TestCase):
    def test_init(self):
        node = AEPNode(node_id="test_node", port=8080)
        self.assertEqual(node.node_id, "test_node")
        self.assertEqual(node.port, 8080)
        self.assertEqual(node.capabilities, {})
        self.assertEqual(node.schema, {})

    def test_register_action_without_schema(self):
        node = AEPNode(node_id="test_node")
        def dummy_action(params):
            pass

        node.register_action("test_action", dummy_action)

        self.assertIn("test_action", node.capabilities)
        self.assertEqual(node.capabilities["test_action"], dummy_action)
        self.assertIn("test_action", node.schema)
        self.assertEqual(node.schema["test_action"], {"type": "object", "properties": {}})

    def test_register_action_with_schema(self):
        node = AEPNode(node_id="test_node")
        def dummy_action(params):
            pass
        schema = {"type": "object", "properties": {"param1": {"type": "string"}}}

        node.register_action("test_action", dummy_action, schema=schema)

        self.assertIn("test_action", node.capabilities)
        self.assertEqual(node.capabilities["test_action"], dummy_action)
        self.assertIn("test_action", node.schema)
        self.assertEqual(node.schema["test_action"], schema)

if __name__ == '__main__':
    unittest.main()

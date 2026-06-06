import unittest
from aep_core import AEPNode

class TestAEPNode(unittest.TestCase):
    def setUp(self):
        self.node = AEPNode("test_node")

    def test_register_action_default_schema(self):
        def my_callback(params):
            pass

        self.node.register_action("test_action", my_callback)

        # Verify action is in capabilities
        self.assertIn("test_action", self.node.capabilities)
        self.assertEqual(self.node.capabilities["test_action"], my_callback)

        # Verify default schema
        expected_schema = {"type": "object", "properties": {}}
        self.assertIn("test_action", self.node.schema)
        self.assertEqual(self.node.schema["test_action"], expected_schema)

    def test_register_action_custom_schema(self):
        def my_callback(params):
            pass

        custom_schema = {
            "type": "object",
            "properties": {
                "param1": {"type": "string"}
            }
        }

        self.node.register_action("custom_action", my_callback, schema=custom_schema)

        # Verify action is in capabilities
        self.assertIn("custom_action", self.node.capabilities)
        self.assertEqual(self.node.capabilities["custom_action"], my_callback)

        # Verify custom schema
        self.assertIn("custom_action", self.node.schema)
        self.assertEqual(self.node.schema["custom_action"], custom_schema)

if __name__ == "__main__":
    unittest.main()

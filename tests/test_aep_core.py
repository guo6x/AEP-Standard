import unittest
from aep_core import AEPNode

class TestAEPNode(unittest.TestCase):
    def setUp(self):
        self.node = AEPNode("test-node")

    def test_register_action_with_schema(self):
        def my_callback(_params):
            pass

        schema = {
            "type": "object",
            "properties": {
                "value": {"type": "integer"}
            }
        }

        self.node.register_action("set_value", my_callback, schema=schema)

        self.assertIn("set_value", self.node.capabilities)
        self.assertEqual(self.node.capabilities["set_value"], my_callback)
        self.assertIn("set_value", self.node.schema)
        self.assertEqual(self.node.schema["set_value"], schema)

    def test_register_action_without_schema(self):
        def my_callback(_params):
            pass

        self.node.register_action("simple_action", my_callback)

        expected_default_schema = {"type": "object", "properties": {}}

        self.assertIn("simple_action", self.node.capabilities)
        self.assertEqual(self.node.capabilities["simple_action"], my_callback)
        self.assertIn("simple_action", self.node.schema)
        self.assertEqual(self.node.schema["simple_action"], expected_default_schema)

    def test_register_multiple_actions(self):
        def action1(_params): pass
        def action2(_params): pass

        self.node.register_action("action1", action1)
        self.node.register_action("action2", action2)

        self.assertEqual(len(self.node.capabilities), 2)
        self.assertIn("action1", self.node.capabilities)
        self.assertIn("action2", self.node.capabilities)

if __name__ == "__main__":
    unittest.main()

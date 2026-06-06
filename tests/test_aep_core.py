import pytest
from aep_core import AEPNode

def test_register_action_default_schema():
    node = AEPNode(node_id="test_node")

    def my_callback(params):
        pass

    node.register_action("test_action", my_callback)

    assert "test_action" in node.capabilities
    assert node.capabilities["test_action"] == my_callback
    assert "test_action" in node.schema
    assert node.schema["test_action"] == {"type": "object", "properties": {}}

def test_register_action_custom_schema():
    node = AEPNode(node_id="test_node")
    custom_schema = {
        "type": "object",
        "properties": {
            "value": {"type": "integer"}
        }
    }

    def my_callback(params):
        pass

    node.register_action("test_action", my_callback, schema=custom_schema)

    assert "test_action" in node.capabilities
    assert node.capabilities["test_action"] == my_callback
    assert "test_action" in node.schema
    assert node.schema["test_action"] == custom_schema

def test_register_action_overwrite():
    node = AEPNode(node_id="test_node")

    def callback1(params):
        pass

    def callback2(params):
        pass

    node.register_action("test_action", callback1)
    assert node.capabilities["test_action"] == callback1

    node.register_action("test_action", callback2, schema={"type": "string"})
    assert node.capabilities["test_action"] == callback2
    assert node.schema["test_action"] == {"type": "string"}

def test_register_multiple_actions():
    node = AEPNode(node_id="test_node")

    def action1(params):
        pass

    def action2(params):
        pass

    node.register_action("action1", action1)
    node.register_action("action2", action2, schema={"type": "number"})

    assert len(node.capabilities) == 2
    assert "action1" in node.capabilities
    assert "action2" in node.capabilities
    assert node.schema["action1"] == {"type": "object", "properties": {}}
    assert node.schema["action2"] == {"type": "number"}

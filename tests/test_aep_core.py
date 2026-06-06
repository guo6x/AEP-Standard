from aep_core import AEPNode

def test_register_action():
    node = AEPNode(node_id="test_node")

    def dummy_callback(params):
        pass

    node.register_action("test_action", dummy_callback)

    assert "test_action" in node.capabilities
    assert node.capabilities["test_action"] == dummy_callback

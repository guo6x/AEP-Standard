import unittest
from unittest.mock import patch, MagicMock
import json
import sys
import os

# Add src to sys.path
sys.path.append(os.path.join(os.getcwd(), 'src'))

from aep_core import AEPNode

class TestAEPNodeHeartbeat(unittest.TestCase):
    @patch('socket.socket')
    @patch('time.sleep', side_effect=InterruptedError) # To break the while True loop
    def test_broadcast_heartbeat_content(self, mock_sleep, mock_socket):
        mock_udp = MagicMock()
        mock_socket.return_value = mock_udp

        node = AEPNode(node_id="test_node")
        node.register_action("test_action", lambda x: None, schema={"type": "object"})

        try:
            node._broadcast_heartbeat()
        except InterruptedError:
            pass

        # Check if sendto was called
        self.assertTrue(mock_udp.sendto.called)

        # Verify the content of the payload
        args, kwargs = mock_udp.sendto.call_args
        payload_bytes = args[0]
        destination = args[1]

        self.assertEqual(destination, ('255.255.255.255', 8888))

        payload = json.loads(payload_bytes.decode('utf-8'))
        self.assertEqual(payload['node_id'], "test_node")
        self.assertEqual(payload['ip_address'], "127.0.0.1")
        self.assertIn("test_action", payload['capabilities'])

if __name__ == '__main__':
    unittest.main()

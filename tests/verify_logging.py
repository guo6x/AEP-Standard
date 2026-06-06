import unittest
from unittest.mock import MagicMock, patch
import sys
import os
import io
from contextlib import redirect_stdout

# Add src to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

class TestAEPNodeLogging(unittest.TestCase):
    @patch('aep_core.network')
    @patch('socket.socket')
    def test_wlan_error_logging(self, mock_socket, mock_network):
        from aep_core import AEPNode

        # Setup mock network to raise exception
        mock_network.STA_IF = 0
        mock_network.WLAN.side_effect = Exception("Mocked WLAN Failure")

        node = AEPNode("test-node")

        f = io.StringIO()
        with redirect_stdout(f):
            # Manually trigger _broadcast_heartbeat logic (it has a while True, so we mock time.sleep to break)
            with patch('time.sleep', side_effect=InterruptedError):
                try:
                    node._broadcast_heartbeat()
                except InterruptedError:
                    pass

        output = f.getvalue()
        self.assertIn("[AEP Core] WLAN Error: Mocked WLAN Failure", output)

    @patch('aep_core.network', None)
    @patch('socket.socket')
    def test_udp_broadcast_setup_error_logging(self, mock_socket):
        from aep_core import AEPNode

        mock_socket_inst = mock_socket.return_value
        mock_socket_inst.setsockopt.side_effect = Exception("Mocked Socket Opt Failure")

        node = AEPNode("test-node")

        f = io.StringIO()
        with redirect_stdout(f):
            with patch('time.sleep', side_effect=InterruptedError):
                try:
                    node._broadcast_heartbeat()
                except InterruptedError:
                    pass

        output = f.getvalue()
        self.assertIn("[AEP Core] UDP Broadcast Setup Error: Mocked Socket Opt Failure", output)

    @patch('aep_core.network', None)
    @patch('socket.socket')
    def test_heartbeat_send_error_logging(self, mock_socket):
        from aep_core import AEPNode

        mock_socket_inst = mock_socket.return_value
        mock_socket_inst.sendto.side_effect = Exception("Mocked SendTo Failure")

        node = AEPNode("test-node")

        f = io.StringIO()
        with redirect_stdout(f):
            # We need it to loop at least once then fail
            with patch('time.sleep', side_effect=InterruptedError):
                try:
                    node._broadcast_heartbeat()
                except InterruptedError:
                    pass

        output = f.getvalue()
        self.assertIn("[AEP Core] Heartbeat Send Error: Mocked SendTo Failure", output)

if __name__ == '__main__':
    unittest.main()

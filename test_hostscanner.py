# test_hostscanner.py
"""
Tests for HostScanner module.
"""

import unittest
from hostscanner import HostScanner

class TestHostScanner(unittest.TestCase):
    """Test cases for HostScanner class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HostScanner()
        self.assertIsInstance(instance, HostScanner)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HostScanner()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

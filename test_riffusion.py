# test_riffusion.py
"""
Tests for Riffusion module.
"""

import unittest
from riffusion import Riffusion

class TestRiffusion(unittest.TestCase):
    """Test cases for Riffusion class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = Riffusion()
        self.assertIsInstance(instance, Riffusion)
        
    def test_run_method(self):
        """Test the run method."""
        instance = Riffusion()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

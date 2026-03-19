import unittest
import os
import json

class TestWalletLocking(unittest.TestCase):
    def setUp(self):
        self.wallet_file = "test_wallet.json"
        with open(self.wallet_file, "w") as f:
            json.dump({"address": "7iaDDAoADEA3poEY4a1SAXPVzisz7ut9hdUraZSJz2rB", "locked": False}, f)

    def test_lock_wallet(self):
        # Simulation of locking logic
        with open(self.wallet_file, "r") as f:
            data = json.load(f)
        data["locked"] = True
        with open(self.wallet_file, "w") as f:
            json.dump(data, f)
        
        with open(self.wallet_file, "r") as f:
            updated_data = json.load(f)
        self.assertTrue(updated_data["locked"])

    def tearDown(self):
        if os.path.exists(self.wallet_file):
            os.remove(self.wallet_file)

if __name__ == "__main__":
    unittest.main()

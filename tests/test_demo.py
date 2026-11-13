import sys
import unittest
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from order_check_demo import Order, totals

class OrderCheckTests(unittest.TestCase):
    def test_one_mismatch_per_receipt(self):
        order=Order("DEMO-001","Marketplace A",{"SKU1":1})
        for _ in range(10):
            self.assertEqual(order.scan("WRONG"),"SALAH ARTIKEL")
        self.assertEqual(totals([order])["tidak_match"],1)
        self.assertEqual(order.scan("SKU1"),"COCOK")
        self.assertEqual(totals([order])["tidak_match"],0)

    def test_partial_and_complete_qty(self):
        order=Order("DEMO-002","Marketplace B",{"SKU1":2})
        self.assertEqual(order.status,"BELUM SCAN")
        order.scan("SKU1")
        self.assertEqual(order.status,"SEBAGIAN")
        order.scan("SKU1")
        self.assertTrue(order.complete)
        self.assertEqual(totals([order])["resi_selesai"],1)
        self.assertEqual(totals([order])["baris_selesai"],1)

    def test_cancel_does_not_finish(self):
        order=Order("DEMO-003","Marketplace C",{"SKU1":1}, cancelled="CANCEL STOCK KOSONG")
        self.assertEqual(order.scan("SKU1"),"PESANAN CANCEL")
        self.assertEqual(totals([order])["resi_selesai"],0)

if __name__=="__main__": unittest.main()

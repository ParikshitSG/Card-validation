import credit_card_validation as ccr
import unittest

class TestCreditCardValidation(unittest.TestCase):

    def test_checksum_len1(self):
        self.assertEqual(ccr.checksum('8'),8)

    def test_checksum_len2(self):
        self.assertEqual(ccr.checksum('12'),4)

    def test_checksum_len3(self):
        self.assertEqual(ccr.checksum('9'),9)

    def test_checksum_len4(self):
        self.assertEqual(ccr.checksum('383'),3)

    def test_checksum_len13(self):
        self.assertEqual(ccr.checksum('4346537657597'),9)

    def test_checksum_len14(self):
        self.assertEqual(ccr.checksum('27184931073326'),1)

    def test_valid(self):
        self.assertEqual(ccr.is_valid('356938035643809'), True)

    def test_invalid1(self):
        self.assertEqual(not ccr.is_valid('4222222222222222'), True)

    def test_invalid2(self):
        self.assertEqual(not ccr.is_valid('4222222222a22222') , True)

    def test_brand_invalid(self):
        self.assertEqual(ccr.get_brand('4222222222222222',"324"),"Invalid card number")

    def test_brand_valid_visa(self):
        self.assertEqual(ccr.get_brand('4532127071054225',"324"),"This is a Visa card")

    def test_brand_valid_mastercard(self):
        self.assertEqual(ccr.get_brand('5553760583414254',"324"),"This is a Mastercard")

    def test_brand_valid_discover(self):
        self.assertEqual(ccr.get_brand('6011244304345315',"324"),"This is a Discover card")

    def test_brand_valid_diners_club_carte_blanche(self):
        self.assertEqual(ccr.get_brand('30205863084058',"324"),"This is a Diners Club Carte Blanche card")

    def test_brand_valid_diners_club_carte_blanche2(self):
        self.assertEqual(ccr.get_brand('36340633332133',"324"),"This is a Diners Club Carte Blanche card")    

    def test_brand_valid_amex(self):
        self.assertEqual(ccr.get_brand('379614703832171',"6542"),"This is a American Express card")

    def test_cvv_invalid(self):
    	self.assertEqual(ccr.get_brand('30205863084058',"1a3"),"Invalid cvv!")

    def test_cvv_invalid2(self):
    	self.assertEqual(ccr.get_brand('4532127071054225',"54632"),"Unknown card brand")

if __name__=="__main__":
    unittest.main()
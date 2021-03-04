import credit_card_validation as ccr

def test_checksum_len1():
    assert ccr.checksum('8') == 8

def test_checksum_len2():
    assert ccr.checksum('12') == 3

def test_checksum_len3():
    assert ccr.checksum('9') == 9

def test_checksum_len4():
    assert ccr.checksum('383') == 5

def test_checksum_len13():
    assert ccr.checksum('4346537657597') == 9

def test_checksum_len14():
    assert ccr.checksum('27184931073326') == 1

def test_valid():
    assert ccr.is_valid('356938035643809')

def test_invalid1():
    assert not ccr.is_valid('4222222222222222')

def test_invalid2():
    assert not ccr.is_valid('4222222222a22222')

# ["Visa", "Mastercard", "American Express" ,"Discover", "Diners Club Carte Blanche"]

def test_brand_valid_visa():
    assert ccr.get_brand('4532127071054225',"324") == "This is a Visa card"

def test_brand_valid_visa():
    assert ccr.get_brand('4957170651679745522',"324") == "This is a Visa card"

def test_brand_valid_mastercard():
    assert ccr.get_brand('5553760583414254',"324") == "This is a Mastercard"

def test_brand_valid_discover():
    assert ccr.get_brand('6011244304345315',"324") == "This is a Discover card"

def test_brand_valid_diners_club_carte_blanche():
    assert ccr.get_brand('30205863084058',"324") == "This is a Diners Club Carte Blanche card"

def test_brand_valid_amex():
    assert ccr.get_brand('379614703832171',"6542") == "This is a American Express card"

def test_cvv_invalid():
	assert ccr.get_brand('4222222222a22222',"1a3") == "Invalid cvv!"

def test_cvv_invalid2():
	assert ccr.get_brand('4532127071054225',"54632") == "Unknown card brand"
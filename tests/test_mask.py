from src.mask import Mask

mask_1 = Mask()


def test_how_many_split():
    assert mask_1.how_many_split("Visa Platinum 8990922113665229") == "Visa Platinum"
    assert mask_1.how_many_split("Visa 8990922113665229") == "Visa"
    assert mask_1.how_many_split("") == ""


def test_check_number():
    assert mask_1.check_number("Visa Platinum 8990922113665229") == "8990922113665229"


def test_mask_number():
    assert mask_1.mask_number("Visa Platinum 8990922113665229") == "Visa Platinum 8990 92** **** 5229"
    assert mask_1.mask_number("Счет 72082042523231456215") == "Счет **6215"

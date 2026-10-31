
import pytest
from marathon_registration import entry_fee, start_wave, finisher_status


# 1. ENTRY FEE TESTS

def test_entry_fee_invalid_race():
    with pytest.raises(ValueError, match="unknown race"):
        entry_fee("ultra", 25, False, False)


def test_entry_fee_age_below_12():
    with pytest.raises(ValueError, match="too young"):
        entry_fee("5k", 10, False, False)


def test_entry_fee_underage_for_half_marathon():
    with pytest.raises(ValueError, match="too young for this distance"):
        entry_fee("half", 16, False, False)


def test_entry_fee_normal():
    assert entry_fee("5k", 30, False, False) == 500


def test_entry_fee_early_bird():
    assert entry_fee("10k", 30, True, False) == 600


def test_entry_fee_senior_discount():
    assert entry_fee("5k", 65, False, False) == 250


def test_entry_fee_with_tshirt():
    assert entry_fee("5k", 30, False, True) == 800


def test_entry_fee_all_discounts():
    assert entry_fee("full", 70, True, True) == 975


# 2. START WAVE TESTS

def test_start_wave_none():
    assert start_wave(None, "full") == "D"


def test_start_wave_a():
    assert start_wave(180, "full") == "A"


def test_start_wave_b():
    assert start_wave(200, "full") == "B"


def test_start_wave_c():
    assert start_wave(241, "full") == "C"


def test_start_wave_non_full():
    assert start_wave(100, "10k") == "B"


# 3. FINISHER STATUS TESTS

def test_disqualified_runner():
    assert finisher_status(60, "5k", 1) == "DSQ"


def test_full_marathon_finisher():
    assert finisher_status(360, "full", 0) == "finisher"


def test_full_marathon_dnf():
    assert finisher_status(361, "full", 0) == "DNF"


def test_half_marathon_finisher():
    assert finisher_status(180, "half", 0) == "finisher"


def test_5k_finisher():
    assert finisher_status(90, "5k", 0) == "finisher"


def test_5k_dnf():
    assert finisher_status(91, "5k", 0) == "DNF"

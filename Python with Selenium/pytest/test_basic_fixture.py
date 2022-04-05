import pytest

def test_comparewithAA(supply_AA_BB_CC):
    zz=35
    assert supply_AA_BB_CC[0]==zz,"aa nd zz failed"

def test_comparewithBB(supply_AA_BB_CC):
    zz=35
    assert supply_AA_BB_CC[1]==zz,"bb nd zz failed"

def test_comparewithCC(supply_AA_BB_CC):
    zz=35
    assert supply_AA_BB_CC[2]==zz,"cc nd zz failed"
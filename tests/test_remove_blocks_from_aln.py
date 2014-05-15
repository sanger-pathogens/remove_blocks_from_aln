import sys
sys.path[0] = './scripts'

print sys.path

from remove_blocks_from_aln import *
import filecmp, os
import pytest

def test_tab_parse():
    exp = [[9, 500, 'f'], [999, 2000, 'r'], [5069, 5095, 'f'], [8162, 8182, 'f'], [9568, 9588, 'f']]
    got = parse_tab( "tests/test_data/small_test.tab" )
    assert got == exp
    
def test_get_ref():
    exp = "OOOOOOOOOOOOOOOO"
    got = get_ref_sequence( "im_your_ref", "tests/test_data/fake_ref.aln" )
    assert got == exp
    
def test_adjusting_regions():
    exp = [[1,7, 'f'], [11,21, 'r']]
    ref = "AAA----TT--GGGGG-----CC"
    regions = [[1,3, 'f'], [5,10, 'r']]
    got = adjust_regions( regions, ref )
    print got
    assert got == exp
    
def test_masking():
    exp = 'AB----GHIJKLMNOPQRST-----Z'
    regions = [[2,6],[20,25]]
    seq = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    got = mask_regions(regions, seq, "-")
    assert got == exp
    
def test_cutting():
    exp = 'ABGHIJKLMNOPQRSTZ'
    regions = [[2,6],[20,25]]
    seq = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    got = cut_regions(regions, seq)
    assert got == exp
    
def test_keeping():
    exp = 'FEDGUVWXY'
    regions = [[2,6,'r'],[20,25, 'f']]
    seq = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    got = keep_regions(regions, seq)
    assert got == exp
    
def test_validation():
    exp = 20
    got = validate_aln("tests/test_data/good.aln")
    assert exp == got
    
    with pytest.raises(SystemExit):
        validate_aln("tests/test_data/bad.aln")
    
def test_run1():
    alnfile = "tests/test_data/tiny_test.aln"
    tabfile = "tests/test_data/tiny_test.2.tab"
    outfile = "test_run1.aln"
    keepremove = 'r'
    reference = ''
    refrem = True
    symbol = 'X'
    run(alnfile, outfile, tabfile, keepremove, reference, refrem, symbol)
    assert os.path.exists("test_run1.aln")
    assert filecmp.cmp( "test_run1.aln", "tests/test_data/test_run1.exp" )
    os.remove("test_run1.aln")
    
def test_run2():
    alnfile = "tests/test_data/tiny_test.aln"
    tabfile = "tests/test_data/tiny_test.tab"
    outfile = "test_run2.aln"
    keepremove = 'c'
    reference = ''
    refrem = True
    symbol = 'X'
    run(alnfile, outfile, tabfile, keepremove, reference, refrem, symbol)
    assert os.path.exists("test_run2.aln")
    assert filecmp.cmp( "test_run2.aln", "tests/test_data/test_run2.exp" )
    os.remove("test_run2.aln")
    
def test_run3():
    alnfile = "tests/test_data/tiny_test.aln"
    tabfile = "tests/test_data/tiny_test.tab"
    outfile = "test_run3.aln"
    keepremove = 'k'
    reference = ''
    refrem = True
    symbol = 'X'
    run(alnfile, outfile, tabfile, keepremove, reference, refrem, symbol)
    assert os.path.exists("test_run3.aln")
    assert filecmp.cmp( "test_run3.aln", "tests/test_data/test_run3.exp" )
    os.remove("test_run3.aln")
    
def test_run4():
    alnfile = "tests/test_data/tiny_test.gapped.aln"
    tabfile = "tests/test_data/tiny_test.gapped.tab"
    outfile = "test_run4.aln"
    reference = 'reference'
    refrem = True
    keepremove = 'r'
    symbol = 'N'
    run(alnfile, outfile, tabfile, keepremove, reference, refrem, symbol)
    assert os.path.exists("test_run4.aln")
    assert filecmp.cmp( "test_run4.aln", "tests/test_data/test_run4.exp" )
    os.remove("test_run4.aln")
    
def test_run5():
    alnfile = "tests/test_data/tiny_test.gapped.aln"
    tabfile = "tests/test_data/tiny_test.gapped.tab"
    outfile = "test_run5.aln"
    reference = 'reference'
    refrem = False
    keepremove = 'r'
    symbol = 'N'
    run(alnfile, outfile, tabfile, keepremove, reference, refrem, symbol)
    assert os.path.exists("test_run5.aln")
    assert filecmp.cmp( "test_run5.aln", "tests/test_data/test_run5.exp" )
    os.remove("test_run5.aln")
   
    
    
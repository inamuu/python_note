# cofing:utf-8

from apps.main import main

import pytest

def test_main_1():
    record = 'hoge'
    assert main(record) == 'test_hoge'

def test_main_2():
    record = 'hoge'
    assert main(record) != record

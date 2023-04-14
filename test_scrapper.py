import pytest
import unittest
from scrapper import getVKMembers
from scrapper import allCountOffset

def test_getVkMembers():
   ds = getVKMembers('bsuir_official', count=1000, offset=0)
   assert ds is not None

def test_allCountOffset():
   ds = allCountOffset(getVKMembers, 'bsuir_official')
   assert ds is not None




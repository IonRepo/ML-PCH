#!/usr/bin/env python
import unittest

from libraries.utils import composition_concentration as composition_concentration

class TestCompositionConcentration(unittest.TestCase):
    """Class for testing the identificaiton of composition and concentration from a formula.
    """
        
    def test_only_letters_1(self):
        """Checks that both capital letters are recognized.
        """
        
        compound = 'AB'
        composition, concentration = composition_concentration(compound)
        
        composition   = composition.split()
        concentration = concentration.split()
        
        self.assertEqual(composition,   ['A', 'B'])
        self.assertEqual(concentration, ['1', '1'])
    
    def test_only_letters_2(self):
        """Checks that white spaces are not a problem.
        """
        
        compound = 'A B'
        composition, concentration = composition_concentration(compound)
        
        composition   = composition.split()
        concentration = concentration.split()
        
        self.assertEqual(composition,   ['A', 'B'])
        self.assertEqual(concentration, ['1', '1'])
    
    def test_only_letters_3(self):
        """Checks that lowercase letters are part of the compound name.
        """
        
        compound = 'AaBb'
        composition, concentration = composition_concentration(compound)
        
        composition   = composition.split()
        concentration = concentration.split()
        
        self.assertEqual(composition,   ['Aa', 'Bb'])
        self.assertEqual(concentration, ['1', '1'])
    
    def test_only_letters_4(self):
        """Checks that more spaces and compounds are not problematic.
        """
        
        compound = 'Aa   Bb C'
        composition, concentration = composition_concentration(compound)
        
        composition   = composition.split()
        concentration = concentration.split()
        
        self.assertEqual(composition,   ['Aa', 'Bb', 'C'])
        self.assertEqual(concentration, ['1', '1', '1'])
    
    def test_only_numbers_1(self):
        """Checks that only numbers are not allowed.
        """
        
        compound = '2345'
        composition, concentration = composition_concentration(compound)
        
        composition   = composition.split()
        concentration = concentration.split()
        
        self.assertEqual(composition,   [])
        self.assertEqual(concentration, [])
    
    def test_only_numbers_2(self):
        """Checks that spaces do not change that.
        """
        
        compound = '2345  234'
        composition, concentration = composition_concentration(compound)
        
        composition   = composition.split()
        concentration = concentration.split()
        
        self.assertEqual(composition,   [])
        self.assertEqual(concentration, [])
    
    def test_erroneous_characters(self):
        """Checks that erroneous characters are not allowed.
        """
        
        compound = '23x45 < 234'
        composition, concentration = composition_concentration(compound)
        
        composition   = composition.split()
        concentration = concentration.split()
        
        self.assertEqual(composition,   [])
        self.assertEqual(concentration, [])
    
    def test_complete_case(self):
        """Checks that a prototypical case is identified correctly.
        """
        
        compound = 'A3B12CDe32'
        composition, concentration = composition_concentration(compound)
        
        composition   = composition.split()
        concentration = concentration.split()
        
        self.assertEqual(composition,   ['A', 'B', 'C', 'De'])
        self.assertEqual(concentration, ['3', '12', '1', '32'])

#!/usr/bin/env python
import unittest
import numpy  as np
import pandas as pd

from libraries.utils import get_expected_energy

class TestExpectedEnergy(unittest.TestCase):
    """Class for testing the computation of the expected energy.
    """
        
    def test_normal(self):
        """Checks the energy computation for a normal triangle.
        """
        
        test_r = [0.35, 0.35]
        energies = pd.DataFrame([-3, -8, -9],
                                 columns=['formation_energy'],
                                 index=['a', 'b', 'c'])
        
        energy = get_expected_energy(energies,
                                     np.array(['a', 'b', 'c']),
                                     np.array([[0.1, 0.1],
                                               [0.6, 0.1],
                                               [0.1, 0.6]]),
                                     'a', 'b', 'c',
                                     test_r)
        
        self.assertEqual(energy, -8.5)
        
    def test_equal_1(self):
        """Checks the energy computation for collinear points, being the extra one equal to the greatest.
        """
        
        test_r = [0.25, 0.15]
        energies = pd.DataFrame([1, 2, 2],
                                 columns=['formation_energy'],
                                 index=['a', 'b', 'c'])
        
        energy = get_expected_energy(energies,
                                     np.array(['a', 'b', 'c']),
                                     np.array([[0.3, 0.2],
                                               [0.2, 0.1],
                                               [0.5, 0.4]]),
                                     'a', 'b', 'c',
                                     test_r)

        self.assertEqual(energy, 1.5)
        
    def test_equal_2(self):
        """Checks the energy computation for collinear points, being the extra one equal to the lowest.
        """
        
        test_r = [0.25, 0.15]
        energies = pd.DataFrame([1, 2, 1],
                                 columns=['formation_energy'],
                                 index=['a', 'b', 'c'])
        
        energy = get_expected_energy(energies,
                                     np.array(['a', 'b', 'c']),
                                     np.array([[0.3, 0.2],
                                               [0.2, 0.1],
                                               [0.5, 0.4]]),
                                     'a', 'b', 'c',
                                     test_r)

        self.assertEqual(energy, 1.5)
        
    def test_greater(self):
        """Checks the energy computation for collinear points, being the extra one greater that the greatest.
        """
        
        test_r = [0.25, 0.15]
        energies = pd.DataFrame([1, 2, 3],
                                 columns=['formation_energy'],
                                 index=['a', 'b', 'c'])
        
        energy = get_expected_energy(energies,
                                     np.array(['a', 'b', 'c']),
                                     np.array([[0.3, 0.2],
                                               [0.2, 0.1],
                                               [0.5, 0.4]]),
                                     'a', 'b', 'c',
                                     test_r)

        self.assertEqual(energy, 1.5)
        
    def test_middle(self):
        """Checks the energy computation for collinear points, being the extra one in the middle.
        """
        
        test_r = [0.25, 0.15]
        energies = pd.DataFrame([1, 2, 1.5],
                                 columns=['formation_energy'],
                                 index=['a', 'b', 'c'])
        
        energy = get_expected_energy(energies,
                                     np.array(['a', 'b', 'c']),
                                     np.array([[0.3, 0.2],
                                               [0.2, 0.1],
                                               [0.5, 0.4]]),
                                     'a', 'b', 'c',
                                     test_r)

        self.assertEqual(energy, 1.5)
        
    def test_lower(self):
        """Checks the energy computation for collinear points, being the extra one lower than the lowest.
        """
        
        test_r = [0.25, 0.15]
        energies = pd.DataFrame([1, 2, 0.5],
                                 columns=['formation_energy'],
                                 index=['a', 'b', 'c'])
        
        energy = get_expected_energy(energies,
                                     np.array(['a', 'b', 'c']),
                                     np.array([[0.3, 0.2],
                                               [0.2, 0.1],
                                               [0.5, 0.4]]),
                                     'a', 'b', 'c',
                                     test_r)

        self.assertEqual(energy, 1.5)
        
    def test_permutation_1(self):
        """Checks the energy computation for collinear points, with permutation 1.
        """
        
        test_r = [0.25, 0.15]
        energies = pd.DataFrame([1, 2, 0.5],
                                 columns=['formation_energy'],
                                 index=['a', 'b', 'c'])
        
        energy = get_expected_energy(energies,
                                     np.array(['a', 'b', 'c']),
                                     np.array([[0.3, 0.2],
                                               [0.2, 0.1],
                                               [0.5, 0.4]]),
                                     'a', 'c', 'b',
                                     test_r)

        self.assertEqual(energy, 1.5)
        
    def test_permutation_2(self):
        """Checks the energy computation for collinear points, with permutation 2.
        """
        
        test_r = [0.25, 0.15]
        energies = pd.DataFrame([1, 2, 0.5],
                                 columns=['formation_energy'],
                                 index=['a', 'b', 'c'])
        
        energy = get_expected_energy(energies,
                                     np.array(['a', 'b', 'c']),
                                     np.array([[0.3, 0.2],
                                               [0.2, 0.1],
                                               [0.5, 0.4]]),
                                     'c', 'b', 'a',
                                     test_r)

        self.assertEqual(energy, 1.5)
        
    def test_permutation_3(self):
        """Checks the energy computation for collinear points, with permutation 3.
        """
        
        test_r = [0.4, 0.3]
        energies = pd.DataFrame([1, 2, 0.5],
                                 columns=['formation_energy'],
                                 index=['a', 'b', 'c'])
        
        energy = get_expected_energy(energies,
                                     np.array(['a', 'b', 'c']),
                                     np.array([[0.3, 0.2],
                                               [0.2, 0.1],
                                               [0.5, 0.4]]),
                                     'a', 'b', 'c',
                                     test_r)

        self.assertEqual(energy, 0.75)

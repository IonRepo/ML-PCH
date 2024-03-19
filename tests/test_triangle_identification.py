#!/usr/bin/env python
import unittest
import numpy as np

from libraries.utils import is_in_triangle

class TestTriagleIdentification(unittest.TestCase):
    """Class for testing the recognition of a point being or not inside a triangle.
    """
        
    def test_normal_1(self):
        """Checks that, for a normal triangle, an inner point is inside.
        """
        
        test_r = [0.25, 0.4]
        
        assertion = is_in_triangle(np.array(['a', 'b', 'c']),
                                        [[0.3, 0.2],
                                         [0.2, 0.1],
                                         [0.25, 0.7]],
                                        'a', 'b', 'c',
                                        test_r)
        
        self.assertTrue(assertion)
    
    def test_normal_2(self):
        """Checks that, for a normal triangle, a point in the edge is inside.
        """
        
        test_r = [0.25, 0.15]
        
        assertion = is_in_triangle(np.array(['a', 'b', 'c']),
                                        [[0.3, 0.2],
                                         [0.2, 0.1],
                                         [0.25, 0.7]],
                                        'a', 'b', 'c',
                                        test_r)
        
        self.assertTrue(assertion)
    
    def test_normal_3(self):
        """Checks that, for a normal triangle, a point in the corner is inside.
        """
        
        test_r = [0.3, 0.2]
        
        assertion = is_in_triangle(np.array(['a', 'b', 'c']),
                                        [[0.3, 0.2],
                                         [0.2, 0.1],
                                         [0.25, 0.7]],
                                        'a', 'b', 'c',
                                        test_r)
        
        self.assertTrue(assertion)
    
    def test_normal_4(self):
        """Checks that, for a normal triangle, an outter point is outside.
        """
        
        test_r = [0.3, 0.4]
        
        assertion = is_in_triangle(np.array(['a', 'b', 'c']),
                                        [[0.3, 0.2],
                                         [0.2, 0.1],
                                         [0.25, 0.7]],
                                        'a', 'b', 'c',
                                        test_r)
        
        self.assertFalse(assertion)

    def test_narrow_1(self):
        """Checks that, for a narrow triangle, an inner point is inside.
        """
        
        test_r = [0.25, 0.2]
        
        assertion = is_in_triangle(np.array(['a', 'b', 'c']),
                                        [[0.3, 0.2],
                                         [0.2, 0.1],
                                         [0.3, 0.4]],
                                        'a', 'b', 'c',
                                        test_r)
        
        self.assertTrue(assertion)
    
    def test_narrow_2(self):
        """Checks that, for a narrow triangle, a point in the edge is inside.
        """
        
        test_r = [0.25, 0.15]
        
        assertion = is_in_triangle(np.array(['a', 'b', 'c']),
                                        [[0.3, 0.2],
                                         [0.2, 0.1],
                                         [0.3, 0.4]],
                                        'a', 'b', 'c',
                                        test_r)
        
        self.assertTrue(assertion)
    
    def test_narrow_3(self):
        """Checks that, for a narrow triangle, a point in the corner is inside.
        """
        
        test_r = [0.3, 0.2]
        
        assertion = is_in_triangle(np.array(['a', 'b', 'c']),
                                        [[0.3, 0.2],
                                         [0.2, 0.1],
                                         [0.3, 0.4]],
                                        'a', 'b', 'c',
                                        test_r)
        
        self.assertTrue(assertion)
    
    def test_narrow_4(self):
        """Checks that, for a narrow triangle, an outter point is outside.
        """
        
        test_r = [0.6, 0.5]
        
        assertion = is_in_triangle(np.array(['a', 'b', 'c']),
                                        [[0.3, 0.2],
                                         [0.2, 0.1],
                                         [0.3, 0.4]],
                                        'a', 'b', 'c',
                                        test_r)
        
        self.assertFalse(assertion)

    def test_line_1_1(self):
        """Checks that, for a line, a point in the edge is inside with a first disposition.
        """
        
        test_r = [0.25, 0.15]
        
        assertion = is_in_triangle(np.array(['a', 'b', 'c']),
                                        [[0.3, 0.2],
                                         [0.2, 0.1],
                                         [0.5, 0.4]],
                                        'a', 'b', 'c',
                                        test_r)
        
        self.assertTrue(assertion)
    
    def test_line_1_2(self):
        """Checks that, for a line, a point in the edge is inside with a second disposition.
        """
        
        test_r = [0.25, 0.15]
        
        assertion = is_in_triangle(np.array(['a', 'b', 'c']),
                                        [[0.2, 0.1],
                                         [0.3, 0.2],
                                         [0.5, 0.4]],
                                        'a', 'b', 'c',
                                        test_r)
        
        self.assertTrue(assertion)
    
    def test_line_1_3(self):
        """Checks that, for a line, a point in the edge is inside with a third disposition.
        """
        
        test_r = [0.25, 0.15]
        
        assertion = is_in_triangle(np.array(['a', 'b', 'c']),
                                        [[0.3, 0.2],
                                         [0.5, 0.4],
                                         [0.2, 0.1]],
                                        'a', 'b', 'c',
                                        test_r)
        
        self.assertTrue(assertion)
    
    def test_line_2_1(self):
        """Checks that, for a line, an outter point is outside with a first disposition.
        """
        
        test_r = [0.3, 0.4]
        
        assertion = is_in_triangle(np.array(['a', 'b', 'c']),
                                        [[0.3, 0.2],
                                         [0.2, 0.1],
                                         [0.5, 0.4]],
                                        'a', 'b', 'c',
                                        test_r)
        
        self.assertFalse(assertion)
    
    def test_line_2_2(self):
        """Checks that, for a line, an outter point is outside with a second disposition.
        """
        
        test_r = [0.3, 0.4]
        
        assertion = is_in_triangle(np.array(['a', 'b', 'c']),
                                        [[0.2, 0.1],
                                         [0.3, 0.2],
                                         [0.5, 0.4]],
                                        'a', 'b', 'c',
                                        test_r)
        
        self.assertFalse(assertion)
    
    def test_line_2_3(self):
        """Checks that, for a line, an outter point is outside with a third disposition.
        """
        
        test_r = [0.3, 0.4]
        
        assertion = is_in_triangle(np.array(['a', 'b', 'c']),
                                        [[0.3, 0.2],
                                         [0.5, 0.4],
                                         [0.2, 0.1]],
                                        'a', 'b', 'c',
                                        test_r)
        
        self.assertFalse(assertion)
    
    def test_line_3_1(self):
        """Checks that, for a line, an outter point in the same line is outside with a first disposition.
        """
                
        test_r = [0.6, 0.5]
        
        assertion = is_in_triangle(np.array(['a', 'b', 'c']),
                                        [[0.3, 0.2],
                                         [0.2, 0.1],
                                         [0.5, 0.4]],
                                        'a', 'b', 'c',
                                        test_r)
        
        self.assertFalse(assertion)
    
    def test_line_3_2(self):
        """Checks that, for a line, an outter point in the same line is outside with a second disposition.
        """
                
        test_r = [0.6, 0.5]
        
        assertion = is_in_triangle(np.array(['a', 'b', 'c']),
                                        [[0.2, 0.1],
                                         [0.3, 0.2],
                                         [0.5, 0.4]],
                                        'a', 'b', 'c',
                                        test_r)
        
        self.assertFalse(assertion)
    
    def test_line_3_3(self):
        """Checks that, for a line, an outter point in the same line is outside with a third disposition.
        """
                
        test_r = [0.6, 0.5]
        
        assertion = is_in_triangle(np.array(['a', 'b', 'c']),
                                        [[0.3, 0.2],
                                         [0.5, 0.4],
                                         [0.2, 0.1]],
                                        'a', 'b', 'c',
                                        test_r)
        
        self.assertFalse(assertion)

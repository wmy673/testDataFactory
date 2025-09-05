import unittest

class TestMathFunctions(unittest.TestCase):
    """
    示例单元测试类，测试基本的数学函数。
    """

    def test_add(self):
        """测试加法"""
        self.assertEqual(1 + 1, 2)

    def test_subtract(self):
        """测试减法"""
        self.assertEqual(5 - 3, 2)

    def test_multiply(self):
        """测试乘法"""
        self.assertEqual(3 * 4, 12)

    def test_divide(self):
        """测试除法"""
        self.assertAlmostEqual(10 / 2, 5)

    def test_zero_division(self):
        """测试除以零抛出异常"""
        with self.assertRaises(ZeroDivisionError):
            _ = 1 / 0

if __name__ == "__main__":
    unittest.main()

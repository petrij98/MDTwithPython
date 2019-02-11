import unittest
import random
import my_code

class TestMyCode(unittest.TestCase):

    def test(self):
        for n in range(100):
            self.r_list = random.sample(range(1,30), random.randrange(2,30))
            self.r_int = random.randrange(1,len(self.r_list))
            self.r_list_c = []
            for i in range(0,len(self.r_list)):
                if ((i + 1) % self.r_int) == 0:
                    self.r_list_c .append(self.r_list[i])
            self.assertAlmostEqual(my_code.problem_01(self.r_list, self.r_int),self.r_list_c, \
                msg=("???"))

if __name__ == '__main__':
    unittest.main()
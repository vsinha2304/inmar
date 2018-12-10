import unittest, inmar_chess as ic


class TestChessMovement(unittest.TestCase):

		

	def test_invalid_rook_output(self):
		res = ic.rook_movement("d2")
		self.assertNotEqual(res,['a1'])


	def test_invalid_knight_output(self):
                res = ic.knight_movement("d2")
                self.assertNotEqual(res,['a1'])


	def test_invalid_queen_output(self):
                res = ic.queen_movement("d2")
                self.assertNotEqual(res,['a1'])



	def test_valid_rook_output(self):
                valid_res = ic.rook_movement("d2")
                self.assertEqual(valid_res,['d1', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'a2', 'b2', 'c2', 'e2', 'f2', 'g2', 'h2'])


        def test_valid_knight_output(self):
                res = ic.knight_movement("d2")
                self.assertEqual(res,['c4', 'e4', 'b3', 'b1', 'f3', 'f1'])


        def test_valid_queen_output(self):
                res = ic.queen_movement("d2")
                self.assertEqual(res,['d1', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'a2', 'b2', 'c2', 'e2', 'f2', 'g2', 'h2', 'e3', 'f4', 'g5', 'h6'])

if __name__ == '__main__':
	unittest.main()

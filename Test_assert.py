'''
author : Jaydatt Patel


syntax : assert expression, error statement

.assertEqual(a, b)	a == b
.assertTrue(x)	bool(x) is True
.assertFalse(x)	bool(x) is False
.assertIs(a, b)	a is b
.assertIsNone(x)	x is None
.assertIn(a, b)	a in b
.assertIsInstance(a, b)	isinstance(a, b)
.assertNotIn(a, b)	a not in b
.assertNotIsInstance(a,b)	not isinstance(a, b)
.assertIsNot(a, b)	a is not b

'''

def square(x):
    return x*x
print('Test: square(10) == 100 ')
assert (square(10) == 100) , 'It should be 100'
print('Pass')

print('Test: square(10) == 101 ')
assert square(10) == 101 ,  'It should be 100' # runtime error and terminate program
print('Pass')

print('Test: square(10) == 101 ')
assert square(10) == 101 ,  'It should be 100' # runtime error and terminate program
print('Pass')
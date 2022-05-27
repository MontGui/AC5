from unittest import TestCase, main
from calc import app


class Testes(TestCase):
    def test_power(self):
        tester = app.test_client(self)
        response = tester.post('/calculadora', data=dict(number1='10', number2='2', operation='power'))
        self.assertEqual(response.status, '200 OK')
        self.assertTrue(b'100.0' in response.data)

    def test_square_root(self):
        tester = app.test_client(self)
        response = tester.post('/calculadora', data=dict(number1='81', operation='square_root'))
        self.assertEqual(response.status, '200 OK')
        self.assertTrue(b'9.0' in response.data)

    def test_logarithm(self):
        tester = app.test_client(self)
        response = tester.post('/calculadora', data=dict(number1='81', operation='logarithm'))
        self.assertEqual(response.status, '200 OK')
        self.assertTrue(b'1.9084850188786497' in response.data)


if __name__ == '__main__':
    main()
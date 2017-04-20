from unittest import TestCase, main
from prime import primes


class TestPrime(TestCase):
    def test_returns_empty_list_when_n_is_less_than_2(self):
        self.assertEqual([], primes(1))
        self.assertEqual([], primes(-1))

    def test_returns_list_with_two_when_n_is_two(self):
        self.assertEqual([2], primes(2))

    def test_requires_integer_as_argument(self):
        with self.assertRaises(Exception) as context:
            primes("23")
        self.assertEqual("Only integers expected as arguments", str(context.exception))

    def test_returns_prime_numbers_less_or_equal_to_n(self):
        self.assertLessEqual(max(primes(13)), 13)

    def test_returns_prime_numbers(self):
        self.assertListEqual([2, 3, 5, 7, 11, 13], primes(13))
        self.assertListEqual([2, 3, 5, 7, 11, 13, 17], primes(17))
        self.assertListEqual([2, 3, 5, 7, 11, 13, 17], primes(18))


if __name__ == '__main__':
    main()
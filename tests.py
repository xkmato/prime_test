from unittest import TestCase, main
from prime import primes


class TestPrime(TestCase):
    def returns_empty_list_when_n_is_less_than_2(self):
        self.assertEquals([], primes(1))
        self.assertEquals([], primes(-1))

    def returns_list_with_two_when_n_is_two(self):
        self.assertEquals([2], primes(2))

    def requires_integer_as_argument(self):
        with self.assertRaises(Exception) as context:
            primes("23")
        self.assertTrue("Only integers expected" in context.exception)

    def test_returns_prime_numbers(self):
        self.assertListEqual([2, 3, 5, 7, 11, 13], primes(13))
        self.assertListEqual([2, 3, 5, 7, 11, 17], primes(17))
        self.assertListEqual([2, 3, 5, 7, 11, 17], primes(18))


if __name__ == '__main__':
    main()
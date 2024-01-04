#define BOOST_TEST_MODULE mytests
#include <boost/test/included/unit_test.hpp>
#include "../testfuncs.cpp"

BOOST_AUTO_TEST_CASE(myTestCase)
{
  BOOST_TEST(fibonacci(10) == 55);
}

BOOST_AUTO_TEST_CASE(fibonacciAAA) {
	int result;

	result = fibonacci(10);

	BOOST_TEST(result == 55);
}
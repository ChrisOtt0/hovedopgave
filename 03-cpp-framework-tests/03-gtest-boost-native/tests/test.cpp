#include "pch.h"
#include "../testfuncs.cpp"

TEST(FactorialTests, HandleZeroInput) {
	EXPECT_EQ(factorial(0), 1);
}

TEST(FactorialTests, HandlePositiveInputs) {
	EXPECT_EQ(factorial(1), 1);
	EXPECT_EQ(factorial(2), 2);
	EXPECT_EQ(factorial(3), 6);
	EXPECT_EQ(factorial(10), 3'628'800);
}

TEST(FibonacciTests, AAAStructure) {
	int result;

	result = fibonacci(10);

	EXPECT_EQ(result, 55);
}
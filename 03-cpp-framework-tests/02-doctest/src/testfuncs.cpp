#include "doctest.h"


int factorial(int number) { 
    return number > 1 ? factorial(number - 1) * number : 1; 
}

int fibonacci(int n) {
    if (n == 0) return 0;
    else if (n == 1) return 1;
    else return fibonacci(n - 1) + fibonacci(n - 2);
}


TEST_CASE("testing the factorial function") {
    CHECK(factorial(0) == 1);
    CHECK(factorial(1) == 1);
    CHECK(factorial(2) == 2);
    CHECK(factorial(3) == 6);
    CHECK(factorial(10) == 3628800);
}

TEST_CASE("testing the fibonacci function") {
    CHECK(fibonacci(0) == 0);
    CHECK(fibonacci(1) == 1);
    CHECK(fibonacci(2) == 1);
    CHECK(fibonacci(3) == 2);
    CHECK(fibonacci(4) == 3);
    CHECK(fibonacci(5) == 5);
    CHECK(fibonacci(10) == 55);
}

TEST_CASE("testing fibonacci with AAA structure") {
    int result;

    result = fibonacci(10);

    CHECK(result == 55);
}
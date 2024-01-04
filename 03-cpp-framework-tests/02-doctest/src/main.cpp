#define DOCTEST_CONFIG_IMPLEMENT
#include "doctest.h"

#include <iostream>
#include "testfuncs.h"

using namespace std;


int main(int argc, char** argv) {
#ifdef TEST
    doctest::Context context;
    context.setOption("order-by", "name");
    return context.run();
#endif

    cout << fibonacci(10) << endl;
    return 0;
}
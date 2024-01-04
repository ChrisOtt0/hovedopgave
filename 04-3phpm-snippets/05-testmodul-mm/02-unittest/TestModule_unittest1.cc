/**
 * @file TestModule_unittest1.cc
 * @brief Unittests for the gtest Test Module
 *
 * Tests the add function with some positive and negative variables
 *
 */

#include "gtest/gtest.h"
#include "TestModule.h"

namespace {

    TEST(AddTest, PositiveNumbers) {
        EXPECT_EQ(5, add(2,3));
    }

    TEST(AddTest, NegativeNumbers) {
        EXPECT_EQ(-5, add(2,-7));
    }

}
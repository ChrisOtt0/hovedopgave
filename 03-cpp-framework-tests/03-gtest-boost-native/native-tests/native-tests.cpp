#include "pch.h"
#include "CppUnitTest.h"
#include "../testfuncs.cpp"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace nativetests
{
	TEST_CLASS(nativetests)
	{
	public:
		
		TEST_METHOD(TestMethod1)
		{
			int result;

			result = fibonacci(10);

			Assert::AreEqual(result, 55);
		}
	};
}

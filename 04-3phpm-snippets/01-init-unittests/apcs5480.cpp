#pragma once
#include "pch.h"
#include "fff.h"
#include "fakeit.hpp"
#include "../../src/PowerModuleCS5480/APCS5480.h"
#include "../../src/Eeprom/APEeprom.h."
#include "../../src/Serial/APUart.h."

DEFINE_FFF_GLOBALS;

APEeprom get_eeprom_mock() {
	fakeit::Mock<APEeprom> eeprom_mock;

	fakeit::When(Method(eeprom_mock, writeEeprom)).Return(true);
	fakeit::When(Method(eeprom_mock, readEeprom)).Return(true);

	return eeprom_mock.get();
}

// convertRegisterToInt Tests //
/*
	index = number_of_bytes
	expected result = 0
*/
TEST(APCS5480Tests, convertRegisterToIntTest1) {
	// Arrange
	uint32_t expected = 0;
	uint32_t result;

	const uint8_t DATA_LENGTH = 0;
	uint8_t bytes[3] = {};

	uint8_t serial = 1;
	APEeprom mock = get_eeprom_mock();
	APCS5480PowerModule pm = APCS5480PowerModule(serial, &mock, false);

	// Act
	result = pm.convertRegisterToInt(bytes, DATA_LENGTH);

	// Assert
	EXPECT_EQ(expected, result);
}

/*
	index > number
*/
TEST(APCS5480Tests, convertRegisterToIntTest2) {
	// Arrange
	
	// Act

	// Assert

}

// convertUInt32toBytes //
#pragma once

#include "MedicalAnalysis.h"

class BMI : public MedicalAnalysis{
private:
	double value;
public:
	BMI(std::string date, double value) : MedicalAnalysis(date), value(value){}

	bool isResultOK() override;
	std::string toString() override;
};
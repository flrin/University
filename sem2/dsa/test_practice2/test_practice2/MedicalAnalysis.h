#pragma once

#include <string>
#include <sstream>

class MedicalAnalysis {
protected:
	std::string date;
public:
	MedicalAnalysis(std::string date) : date(date) {}
	virtual bool isResultOK() = 0;
	virtual std::string toString() = 0;
	std::string getDate() { return date; }
};
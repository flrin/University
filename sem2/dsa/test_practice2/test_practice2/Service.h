#pragma once

#include "Person.h"

class Service {
private:
	Person person;
public:
	Service() = default;
	void add(std::string date, double value);
	void add(std::string date, int systolic, int diastolic);

	std::vector<std::shared_ptr<MedicalAnalysis>> getAll();

	bool isIll(int month);

	void save(std::string filename, std::string date1, std::string date2);
};
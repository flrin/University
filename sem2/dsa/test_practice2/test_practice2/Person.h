#pragma once

#include <iostream>
#include <fstream>
#include <string>
#include "MedicalAnalysis.h"
#include <vector>
#include "BMI.h"
#include "BP.h"

class Person {
private:
	std::string name;
	std::vector<std::shared_ptr<MedicalAnalysis>> analysises;
public:
	Person(std::string name) : name(name) {}
	Person() = default;

	void addAnalysis(std::shared_ptr<MedicalAnalysis> a);
	std::vector<std::shared_ptr<MedicalAnalysis>> getAllAnalyses();
	std::vector<std::shared_ptr<MedicalAnalysis>> getAnalysesByMonth(int month);
	bool isIll(int month);
	std::vector<std::shared_ptr<MedicalAnalysis>> getAnalysisBetweenDates(std::string date1, std::string date2);
	void writeToFile(std::string filename, std::string date1, std::string date2);
};
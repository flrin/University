#include "Service.h"

void Service::add(std::string date, double value)
{
	std::shared_ptr<MedicalAnalysis>bmi = std::make_shared<BMI>(date, value);
	person.addAnalysis(bmi);
}

void Service::add(std::string date, int systolic, int diastolic)
{
	std::shared_ptr<MedicalAnalysis>bp = std::make_shared<BP>(date, systolic, diastolic);
	person.addAnalysis(bp);
}

std::vector<std::shared_ptr<MedicalAnalysis>> Service::getAll()
{
	return person.getAllAnalyses();
}

bool Service::isIll(int month)
{
	return person.isIll(month);
}

void Service::save(std::string filename, std::string date1, std::string date2)
{
	person.writeToFile(filename, date1, date2);
}

#include "Person.h"

void Person::addAnalysis(std::shared_ptr<MedicalAnalysis> a)
{
	analysises.push_back(a);
}

std::vector<std::shared_ptr<MedicalAnalysis>> Person::getAllAnalyses()
{
	return analysises;
}

std::vector<std::shared_ptr<MedicalAnalysis>> Person::getAnalysesByMonth(int month)
{
	std::vector<std::shared_ptr<MedicalAnalysis>> month_analysis;
	for (const auto& analysis : analysises)
		if (stoi(analysis->getDate().substr(5, 2)) == month) {
			month_analysis.push_back(analysis);
		}
	return month_analysis;
}

bool Person::isIll(int month)
{
	for (const auto& analysis : getAnalysesByMonth(month)) {
		if (analysis->isResultOK()) {
			return false;
		}
	}

	return true;
}

std::vector<std::shared_ptr<MedicalAnalysis>> Person::getAnalysisBetweenDates(std::string date1, std::string date2)
{
	std::vector<std::shared_ptr<MedicalAnalysis>> between_analysises;

	for (const auto& analyses : analysises) {
		if (date1 < analyses->getDate() && date2 > analyses->getDate())
			between_analysises.push_back(analyses);
	}

	return between_analysises;
}

void Person::writeToFile(std::string filename, std::string date1, std::string date2)
{
	std::ofstream fout(filename);

	for (const auto& analysis : analysises) {
		fout << analysis->toString() << std::endl;
	}

	fout.close();
}

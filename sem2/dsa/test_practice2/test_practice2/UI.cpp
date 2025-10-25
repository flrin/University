#include "UI.h"

void UI::start()
{
	while (1) {
		std::cout << "1. Add\n";
		std::cout << "2. Show all\n";
		std::cout << "3. Is ill\n";
		std::cout << "4. Save\n";

		std::cout << ">>";
		std::string input;
		std::cin >> input;

		if (input == "1"){
			std::string type, date;
			std::cout << "type: ";
			std::cin >> type;
			std::cout << "date: ";
			std::cin >> date;
			if (type == "BMI") {
				double value;
				std::cout << "value: ";
				std::cin >> value;

				service.add(date, value);
			}
			else {
				int systolic, diastolic;
				std::cout << "systolic value: ";
				std::cin >> systolic;
				std::cout << "diastolic value: ";
				std::cin >> diastolic;

				service.add(date, systolic, diastolic);
			}
		}
		else if (input == "2") {
			for (const auto& i : service.getAll()) {
				std::cout << i->toString() << std::endl;
			}
		}
		else if (input == "3") {
			int month;
			std::cin >> month;
			std::cout << "is ill?: " << service.isIll(month) << std::endl;
		}
		else if (input == "4") {
			std::string filename, date1, date2;
			std::cout << "file name: ";
			std::cin >> filename;
			std::cout << "date 1: ";
			std::cin >> date1;
			std::cout << "date 2: ";
			std::cin >> date2;
			service.save(filename, date1, date2);
		}
	}
}

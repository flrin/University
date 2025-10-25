
#include <iostream>
#include "Matrix.h"
#include "ExtendedTest.h"
#include "ShortTest.h"

#include <tuple>

using namespace std;


int main() {
	testAll();
	testSetElemsOnLines();
	testAllExtended();
	cout << "Test End" << endl;
	system("pause");
}
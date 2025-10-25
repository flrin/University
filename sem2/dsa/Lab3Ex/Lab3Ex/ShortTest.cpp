#include <assert.h>
#include "Matrix.h"

using namespace std;

void testAll() { 
	Matrix m(4, 4);
	assert(m.nrLines() == 4);
	assert(m.nrColumns() == 4);	
	m.modify(1, 1, 5);
	assert(m.element(1, 1) == 5);
	TElem old = m.modify(1, 1, 6);
	assert(m.element(1, 2) == NULL_TELEM);
	assert(old == 5);
}

void testSetElemsOnLines() {
	Matrix m(4, 4);
	m.setElemsOnLine(1, 5);
	assert(m.element(1, 0) == 5);
	assert(m.element(1, 1) == 5);
	assert(m.element(1, 2) == 5);
	assert(m.element(1, 3) == 5);
	assert(m.element(0, 0) == NULL_TELEM);
	assert(m.element(2, 0) == NULL_TELEM);
	assert(m.element(3, 0) == NULL_TELEM);
}


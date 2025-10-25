#include "FixedCapBiMap.h"
#include "FixedCapBiMapIterator.h"
#include <exception>
using namespace std;


FixedCapBiMapIterator::FixedCapBiMapIterator(const FixedCapBiMap& d) : map(d)
{
	this->current_index = 0;
}


void FixedCapBiMapIterator::first() {
	this->current_index = 0;
}


void FixedCapBiMapIterator::next() {
	if (!this->valid())
		throw exception();
	this->current_index++;
}


TElem FixedCapBiMapIterator::getCurrent(){
	if (!this->valid())
		throw exception();
	return this->map.elements[this->current_index];
}


bool FixedCapBiMapIterator::valid() const {
	if (this->current_index >= this->map.mapsize)
		return false;
	return true;
}




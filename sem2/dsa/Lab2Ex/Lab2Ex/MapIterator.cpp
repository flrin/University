#include "Map.h"
#include "MapIterator.h"
#include <exception>
using namespace std;

//BC: O(1) WC: O(1) TC: O(1)
MapIterator::MapIterator(const Map& d) : map(d)
{
	current = 0;
}

//O(1)
void MapIterator::first() {
	current = 0;
}

//O(1)
void MapIterator::next() {
	if (!valid()) {
		throw exception();
	}
	current++;
}

//O(1)
TElem MapIterator::getCurrent(){
	if (!valid()) {
		throw exception();
	}
	return map.elements[current];
}

//O(1)
bool MapIterator::valid() const {
	return map.length > current;
}




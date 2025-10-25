#include "FixedCapBiMap.h"
#include "FixedCapBiMapIterator.h"
#include <exception>
#include <cstdio>

FixedCapBiMap::FixedCapBiMap(int capacity) {
	if (capacity <= 0) {
		throw std::exception();
	}
	this->cap = capacity;
	this->mapsize = 0;
	this->elements = new TElem[capacity];
}

FixedCapBiMap::~FixedCapBiMap() {
	delete[] this->elements;
}

bool FixedCapBiMap::add(TKey c, TValue v){
	
	if (this->isFull())
		throw std::exception();

	int apparitions = 0;
	for (int i = 0; i < this->mapsize; i++)
		if (this->elements[i].first == c)
			apparitions++;

	if (apparitions < 2) {
		TElem elem;
		elem.first = c;
		elem.second = v;
		this->elements[this->mapsize] = elem;
		this->mapsize++;
		return true;
	}

	return false;
}

ValuePair FixedCapBiMap::search(TKey c) const{
	
	TValue first = NULL_TVALUE;
	TValue second = NULL_TVALUE;

	for (int i = 0; i < this->mapsize; i++) {
		if (this->elements[i].first == c) {
			if (first == NULL_TVALUE)
				first = this->elements[i].second;
			else {
				second = this->elements[i].second;
				break;
			}
		}
	}

	return std::pair<TValue, TValue>(first, second);
}

bool FixedCapBiMap::remove(TKey c, TValue v){
	for (int i = 0; i < this->mapsize; i++)
		if (this->elements[i].first == c && this->elements[i].second == v) {
			this->mapsize--;
			for (int j = i; j < this->mapsize; j++)
				this->elements[j] = this->elements[j + 1];
			return true;
		}
	return false;
}


int FixedCapBiMap::size() const {
	return this->mapsize;
}

bool FixedCapBiMap::isEmpty() const{
	if (this->mapsize == 0)
		return true;
	return false;
}

bool FixedCapBiMap::isFull() const {
	if (this->mapsize == this->cap)
		return true;
	return false;
}

ValuePair FixedCapBiMap::removeKey(TKey k)
{
	ValuePair vp = search(k);
	if (vp.first != NULL_TVALUE) {
		remove(k, vp.first);
		if (vp.second != NULL_TVALUE)
			remove(k, vp.second);
	}
	return vp;
}

FixedCapBiMapIterator FixedCapBiMap::iterator() const {
	return FixedCapBiMapIterator(*this);
}




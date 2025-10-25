#include "Map.h"
#include "MapIterator.h"

//BC: Theta(1) WC: Theta(n) TC: O(n)
void Map::replace(TKey k, TValue oldValue, TValue newValue)
{
	for (int i = 0; i < length; i++) {
		if (elements[i].first == k && elements[i].second == oldValue) {
			elements[i].second = newValue;
			return;
		}
	}
}

//BC: O(1) WC: O(1) TC: O(1)
Map::Map() {
	elements = new TElem[1];
	capacity = 1;
	length = 0;
}

//BC: O(1) WC: O(1) TC: O(1)
Map::~Map() {
	delete elements;
}

//BC: O(N) WC: O(n) TC: O(n)
void Map::resize() {
	TElem* newElements = new TElem[capacity * 2];
	for (int i = 0; i < length; i++) {
		newElements[i] = elements[i];
	}
	delete elements;
	elements = newElements;
	capacity *= 2;
}

//BC: O(1) WC: O(n) TC: O(n)
TValue Map::add(TKey c, TValue v){
	for (int i = 0; i < length; i++) {
		if (elements[i].first == c) {
			TValue oldValue = elements[i].second;
			elements[i].second = v;
			return oldValue;
		}
	}
	if (length == capacity) {
		resize();
	}
	elements[length] = TElem(c, v);
	length++;
	return NULL_TVALUE;
}

//BC: O(1) WC: O(n) TC: O(n)
TValue Map::search(TKey c) const{
	for (int i = 0; i < length; i++) {
		if (elements[i].first == c) {
			return elements[i].second;
		}
	}
	return NULL_TVALUE;
}

//BC: O(n) WC: O(n) TC: O(n)
TValue Map::remove(TKey c){
	for (int i = 0; i < length; i++) {
		if (elements[i].first == c) {
			TValue oldValue = elements[i].second;
			for (int j = i; j < length - 1; j++) {
				elements[j] = elements[j + 1];
			}
			length--;
			return oldValue;
		}
	}
	return NULL_TVALUE;
}

//O(1)
int Map::size() const {
	return length;
}

//O(1)
bool Map::isEmpty() const{
	return length == 0;
}

//O(1)
MapIterator Map::iterator() const {
	return MapIterator(*this);
}




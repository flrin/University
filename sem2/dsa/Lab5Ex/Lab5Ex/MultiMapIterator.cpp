#include "MultiMapIterator.h"
#include "MultiMap.h"

#include <iostream>;

//Theta(1)
MultiMapIterator::MultiMapIterator(const MultiMap& c): col(c) {
	first();
}

//Theta(1)
TElem MultiMapIterator::getCurrent() const{
	if (!valid())
		throw exception("BLEH :P");

	return TElem(current->key, current->value);
}

//Theta(1)
bool MultiMapIterator::valid() const {
	return hash_key < col.m && current != nullptr;
}

//Best case: Theta(1), Worst Case: Theta(m), Total Case: O(m)
void MultiMapIterator::next() {
	if (!valid()) {
		throw exception("Exceeded list");
	}
	
	if (current->next != nullptr) {
		current = current->next;
	}
	else {
		++hash_key;
		while (hash_key < col.m && col.table[hash_key] == nullptr) { ++hash_key; }
		
		if (hash_key >= col.m) {
			current = nullptr;
		}
		current = col.table[hash_key];
	}
}

//Theta(1)
void MultiMapIterator::first() {
	hash_key = 0;
	while (hash_key < col.m && col.table[hash_key] == nullptr) { hash_key++; }
	current = col.table[hash_key];
}


#include "MultiMap.h"
#include "MultiMapIterator.h"
#include <exception>
#include <iostream>

using namespace std;

//Theta(1)
int hashFunc(int m, int k) {
	return abs(k) % m;
}

//Theta(m)
MultiMap::MultiMap() {
	m = 13;
	n = 0;
	table = new Node*[m];

	for (int i = 0; i < m; i++)
		table[i] = nullptr;

	hfunction = hashFunc;
}

//Theta(1)
void MultiMap::add(TKey c, TValue v) {
	int position = hfunction(m, c);

	Node* hash_key_first = table[position];
	Node* new_node = new Node(c, v, hash_key_first);
	table[position] = new_node;
	n++;
}

//Best Case: Theta(1), Worst Case: Theta(a), Total Case: O(a)
bool MultiMap::remove(TKey c, TValue v) {
	int position = hfunction(m, c);

	Node* current = table[position];
	Node* prev = nullptr;

	while (current != nullptr && !(current->key == c && current->value == v)) {
		prev = current;
		current = current->next;
	}

	if (current == nullptr) {
		return false;
	}

	n--;

	if (prev == nullptr) {
		table[position] = current->next;
		delete current;
		return true;
	}

	prev->next = current->next;
	delete current;
	return true;

}

//Theta(a)
vector<TValue> MultiMap::search(TKey c) const {
	vector<TValue> values;

	int position = hfunction(m, c);
	Node* current = table[position];

	while (current != nullptr) {
		if (current->key == c) {
			values.push_back(current->value);
		}
		current = current->next;
	}
	
	return values;
}

//Theta(1)
int MultiMap::size() const {
	return n;
}

//Theta(1)
bool MultiMap::isEmpty() const {
	return n == 0;
}

//Theta(1)
MultiMapIterator MultiMap::iterator() const {
	return MultiMapIterator(*this);
}

//Theta(n + m)
MultiMap::~MultiMap() {
	for (int i = 0; i < m; i++) {
		Node* current = table[i];

		while (current != nullptr) {
			Node* next = current->next;
			delete current;
			current = next;
		}
			
	}
	delete table;
}


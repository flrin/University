#include "ListIterator.h"
#include "SortedIteratedList.h"
#include <iostream>
using namespace std;
#include <exception>

//Theta (n)
void SortedIteratedList::filter(Condition cond)
{
	ListIterator it(*this);

	it.first();
	while (it.valid()) {
		int current = it.getCurrent();
		if (!cond(current))
			remove(it);
		else {
			it.next();
		}
	}
}

//Theta (1)
SortedIteratedList::SortedIteratedList(Relation r) {
	capacity = 1;
	elements = new Node[1];
	elements[0] = Node();
	tail = -1;
	head = -1;
	firstEmpty = 0;
	list_size = 0;
	relation = r;
}

//Best case: Theta(1), Worst case: Theta(n), Total case: O(n)
int SortedIteratedList::lastEmpty() {
	int current = firstEmpty;

	if (current == -1)
		return -1;

	while (elements[current].next != -1)
		current = elements[current].next;

	return current;
}

//Best case = Worst case = Total case: Theta(n)
void SortedIteratedList::resize() {
	Node* newElements = new Node[capacity * 2];
	for (int i = 0; i < capacity; i++) {
		newElements[i] = elements[i];
	}

	int last_empty = lastEmpty();
	if (last_empty == -1) {
		last_empty = capacity;
		firstEmpty = capacity;
	}
		

	for (int i = capacity; i < 2 * capacity; i++) {
		newElements[i] = Node();
		newElements[last_empty].next = i;
		last_empty = i;
	}

	newElements[last_empty].next = -1;

	delete[] elements;
	elements = newElements;
	capacity *= 2;
}

//Theta(1)
int SortedIteratedList::size() const {
	return list_size;
}

//Theta(1)
bool SortedIteratedList::isEmpty() const {
	return list_size == 0;
}

//Theta(1)
ListIterator SortedIteratedList::first() const {
	ListIterator it = ListIterator(*this);
	it.first();
	return it;
}

//Theta(1)
TComp SortedIteratedList::getElement(ListIterator poz) const {
	if (!poz.valid())
		throw exception("Invalid poz");
	
	return poz.getCurrent();
}

//Theta(1)
TComp SortedIteratedList::remove(ListIterator& poz) {
	if (!poz.valid())
		throw exception("Invalid pointer");

	int prev_poz = elements[poz.current_node].prev;
	int next_poz = elements[poz.current_node].next;
	int poz_i = poz.current_node;

	poz.next();

	if (prev_poz != -1)
		elements[prev_poz].next = next_poz;
	else
		head = next_poz;
	
	if (next_poz != -1)
		elements[next_poz].prev = prev_poz;
	else
		tail = prev_poz;

	int last = lastEmpty();

	if (last == -1) {
		firstEmpty = poz_i;
	}
	else
		elements[lastEmpty()].next = poz_i;

	TComp old_value = elements[poz_i].value;

	elements[poz_i].next = -1;
	elements[poz_i].value = NULL_TCOMP;
	elements[poz_i].prev = next_poz;

	list_size--;

	return old_value;

}

//Best case: Theta(1), Worst case: Theta(n), Total case: O(n)
ListIterator SortedIteratedList::search(TComp e) const{
	ListIterator it = ListIterator(*this);
	it.first();

	while (it.valid()) {

		if (it.getCurrent() == e) {
			return it;
		}

		it.next();
	}

	return it;
}

//Best case: Theta(1), Worst case: Theta(n), Total case: O(n)
void SortedIteratedList::add(TComp e) {
	if (list_size == capacity)
		resize();

	Node new_node = Node();
	new_node.value = e;

	int index_to_put = firstEmpty;
	firstEmpty = elements[firstEmpty].next;
	elements[index_to_put] = new_node;

	if (isEmpty()) {
		head = index_to_put;
		tail = index_to_put;
	}
	else {
		int current = head;
		if (relation(elements[index_to_put].value, elements[current].value)) {
			elements[index_to_put].prev = -1;
			elements[index_to_put].next = head;
			
			elements[head].prev = index_to_put;
			head = index_to_put;
			
			list_size++;

			return;
		}
		
		while (current != tail && relation(elements[current].value, elements[index_to_put].value)) {
			current = elements[current].next;
		}

		if (current == tail && relation(elements[current].value, elements[index_to_put].value)) {
			elements[index_to_put].prev = tail;
			elements[tail].next = index_to_put;
			tail = index_to_put;
		}
		else {
			int prev_neighbour = elements[current].prev;
			elements[prev_neighbour].next = index_to_put;
			elements[index_to_put].prev = prev_neighbour;
			elements[current].prev = index_to_put;
			elements[index_to_put].next = current;
		}
	}

	list_size++;
}

SortedIteratedList::~SortedIteratedList() {
	delete[] elements;
}

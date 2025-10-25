#include "ListIterator.h"
#include "SortedIteratedList.h"
#include <exception>

using namespace std;

ListIterator::ListIterator(const SortedIteratedList& list) : list(list), current_node(list.head){}

//Theta(1)
void ListIterator::first(){
	current_node = list.head;
}

//Theta(1)
void ListIterator::next(){
	if (!valid())
		throw exception("Exceeded list");

	current_node = list.elements[current_node].next;
}

//Theta(1)
bool ListIterator::valid() const{
	if (current_node == -1)
		return false;
	return true;
}


//Theta(1)
TComp ListIterator::getCurrent() const{
	return list.elements[current_node].value;
}



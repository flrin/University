#include "SortedBagIterator.h"
#include "SortedBag.h"
#include <exception>

using namespace std;

//Theta(1)
SortedBagIterator::SortedBagIterator(SortedBag& b) : bag(b) {
	current = nullptr;
	first();
}

//Theta(1)
TComp SortedBagIterator::getCurrent() {
	if (valid())
		return current->value;
	throw exception("Invalid iterator");
}

//Theta(1)
bool SortedBagIterator::valid() {
	if (current == nullptr)
		return false;
	return true;
}

//Best Case: Theta(1), Worst Case: Theta(n), Total Case: O(n)
void SortedBagIterator::next() {
	if (!valid())
		throw exception("Invalid iterator");

	if (current->right != nullptr) {
		current = current->right;
		while (current->left != nullptr) {
			current = current->left;
		}
	}
	else {
		Node* old_current = current;
		current = bag.root;
		Node* last_left_turn = nullptr;
		while (current != nullptr && current != old_current) {
			if (bag.relation(current->value, old_current->value)) {
				current = current->right;
			}
			else {
				last_left_turn = current;
				current = current->left;
			}
		}
		current = last_left_turn;
	}
}

//Best Case: Theta(1), Worst Case: Theta(n), Total Case: O(n)
void SortedBagIterator::first() {
	current = bag.root;
	if (current == nullptr)
		return;
	while (current->left != nullptr) {
		current = current->left;
	}
}

//Best Case: Theta(1), Worst Case: Theta(n), Total Case: O(n)
TElem SortedBagIterator::remove()
{
	TElem current_value = getCurrent();
	next();
	bag.remove(current_value);
	return current_value;
}


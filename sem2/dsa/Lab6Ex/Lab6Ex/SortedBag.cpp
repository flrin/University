#include "SortedBag.h"
#include "SortedBagIterator.h"

//Theta(1)
SortedBag::SortedBag(Relation r) {
	relation = r;
	root = nullptr;
	n = 0;
}

//Best Case: Theta(1), Worst Case: Theta(n), Total Case: O(n)
void SortedBag::add(TComp e) {
	Node* prev = nullptr;
	Node* current = root;
	Node* new_node = new Node(e, nullptr, nullptr);
	while (current != nullptr) {
		prev = current;
		if (relation(current->value, e)) {
			current = current->right;
		}
		else {
			current = current->left;
		}
	}
	n++;
	if (prev == nullptr) {
		root = new_node;
		return;
	}
	
	if (relation(prev->value, e)) {
		prev->right = new_node;
		return;
	}

	prev->left = new_node;
}

//Best Case: Theta(1), Worst Case: Theta(n), Total Case: O(n)
bool SortedBag::remove(TComp e) {
	Node* prev = nullptr;
	Node* current = root;
	while (current != nullptr && current->value != e) {
		prev = current;
		if (relation(current->value, e)) {
			current = current->right;
		}
		else {
			current = current->left;
		}
	}

	if (current == nullptr)
		return false;

	if (current->right != nullptr) {
		Node* new_base = current->right;
		while (new_base->left != nullptr)
			new_base = new_base->left;

		new_base->left = current->left;
	}
	else {
		current->right = current->left;
	}
	
	if (prev == nullptr) {
		root = current->right;
	}
	else {
		if (prev->left == current) {
			prev->left = current->right;
		}
		else {
			prev->right = current->right;
		}
	}
	
	delete current;
	n--;
	return true;
}

//Best Case: Theta(1), Worst Case: Theta(n), Total Case: O(n)
bool SortedBag::search(TComp elem) const {
	Node* current = root;
	while (current != nullptr && current->value != elem) {
		if (relation(current->value, elem)) {
			current = current->right;
		}
		else {
			current = current->left;
		}
	}
	if (current == nullptr) {
		return false;
	}
	return true;
}

//Best Case: Theta(1), Worst Case: Theta(n), Total Case: O(n)
int SortedBag::nrOccurrences(TComp elem) const {
	int nr = 0;

	Node* current = root;
	while (current != nullptr) {
		if (current->value == elem)
			nr++;

		if (relation(current->value, elem)) {
			current = current->right;
		}
		else {
			current = current->left;
		}
	}

	return nr;
}

//Theta(1)
int SortedBag::size() const {
	return n;
}

//Theta(1)
bool SortedBag::isEmpty() const {
	return n == 0;
}

//Theta(1)
SortedBagIterator SortedBag::iterator() {
	return SortedBagIterator(*this);
}

//Theta(n)
void SortedBag::deleteRecursive(Node* node) {
	if (node == nullptr) return;
	deleteRecursive(node->left);
	deleteRecursive(node->right);
	delete node;
}

//Theta(n)
SortedBag::~SortedBag() {
	deleteRecursive(root);
}

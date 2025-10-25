#include "Matrix.h"
#include <exception>

using namespace std;


Matrix::Matrix(int l, int c) {
	head = nullptr;
	tail = nullptr;
	lines = l;
	cols = c;
}


int Matrix::nrLines() const {
	return lines;
}


int Matrix::nrColumns() const {
	return cols;
}

//BC: Theta(1) WC: Theta(n) TC: O(n)
TElem Matrix::element(int i, int j) const {
	if (i < 0 || i >= lines || j < 0 || j >= cols)
		throw exception("Invalid position");

	Node* current = head;

	while (current != nullptr) {
		if (get<0>(current->value) == i && get<1>(current->value) == j)
			return get<2>(current->value);
		else if (get<0>(current->value) > i)
			return NULL_TELEM;
		else if (get<0>(current->value) == i && get<1>(current->value) > j)
			return NULL_TELEM;
		current = current->next;
	}

	return NULL_TELEM;
}

//BC: Theta(1) WC: Theta(n) TC: O(n)
TElem Matrix::modify(int i, int j, TElem e) {
	if (i < 0 || i >= lines || j < 0 || j >= cols)
		throw exception("Invalid position");

	Node* current = head;


	while (current != nullptr) {
		if (get<0>(current->value) == i && get<1>(current->value) == j){
			TElem old = get<2>(current->value);
			get<2>(current->value) = e;
			return old;
		}
		else if (get<0>(current->value) > i)
			break;
		else if (get<0>(current->value) == i && get<1>(current->value) > j)
			break;
		current = current->next;
	}

	std::tuple<int, int, TElem> new_node_value{ i, j, e };
	Node* new_node = new Node{new_node_value};

	new_node->next = current;

	if (current == nullptr) {
		new_node->prev = tail;

		if (head == nullptr) {
			head = new_node;
			tail = new_node;
			return NULL_TELEM;
		}

		tail->next = new_node;
		tail = new_node;
		return NULL_TELEM;
	}
		

	if (current != head) {
		new_node->prev = current->prev;
		current->prev->next = new_node;
		current->prev = new_node;
		return NULL_TELEM;
	}
	
	current->prev = new_node;
	head = new_node;

	return NULL_TELEM;
}

// BC: Theta(cols^2) WC: Theta(cols^2 + n * cols) TC: O(cols^2 + n * cols)
void Matrix::setElemsOnLine(int line, TElem elem)
{
	if (line < 0 || line >= lines)
		throw exception("Invalid position");

	for (int j = 0; j < cols; j++)
		modify(line, j, elem);
}



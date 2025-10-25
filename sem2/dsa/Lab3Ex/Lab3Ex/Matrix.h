#pragma once
#include <tuple>

//DO NOT CHANGE THIS PART
typedef int TElem;
#define NULL_TELEM 0


class Node {
	friend class Matrix;
private:
	std::tuple<int, int, TElem>value;
	Node* next;
	Node* prev;
public:
	Node(std::tuple<int, int, TElem>v) : value(v), next(nullptr), prev(nullptr) {}
};

class Matrix {

private:
	Node* head;
	Node* tail;
	int lines;
	int cols;

public:
	//constructor
	Matrix(int l, int c);

	//returns the number of lines
	int nrLines() const;

	//returns the number of columns
	int nrColumns() const;

	//returns the element from line i and column j (indexing starts from 0)
	//throws exception if (i,j) is not a valid position in the Matrix
	TElem element(int i, int j) const;

	//modifies the value from line i and column j
	//returns the previous value from the position
	//throws exception if (i,j) is not a valid position in the Matrix
	TElem modify(int i, int j, TElem e);



	void setElemsOnLine(int line, TElem elem);
};

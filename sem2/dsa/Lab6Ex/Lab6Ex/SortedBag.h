#pragma once
//DO NOT INCLUDE SORTEDBAGITERATOR

//DO NOT CHANGE THIS PART
typedef int TComp;
typedef TComp TElem;
typedef bool(*Relation)(TComp, TComp);
#define NULL_TCOMP -11111;

class SortedBagIterator;

class Node {
public:
	Node(TComp value, Node* left, Node* right) : value(value), left(left), right(right) {}
	TComp value;
	Node* left;
	Node* right;
};

class SortedBag {
	friend class SortedBagIterator;

private:
	Relation relation;
	Node* root;
	int n;

public:
	//constructor
	SortedBag(Relation r);

	//adds an element to the sorted bag
	void add(TComp e);

	//removes one occurence of an element from a sorted bag
	//returns true if an eleent was removed, false otherwise (if e was not part of the sorted bag)
	bool remove(TComp e);

	//checks if an element appearch is the sorted bag
	bool search(TComp e) const;

	//returns the number of occurrences for an element in the sorted bag
	int nrOccurrences(TComp e) const;

	//returns the number of elements from the sorted bag
	int size() const;

	//returns an iterator for this sorted bag
	SortedBagIterator iterator();

	//checks if the sorted bag is empty
	bool isEmpty() const;

	void deleteRecursive(Node* node);

	//destructor
	~SortedBag();
};
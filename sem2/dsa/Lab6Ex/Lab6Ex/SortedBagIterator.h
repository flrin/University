#pragma once
#include "SortedBag.h"

class SortedBag;

class SortedBagIterator
{
	friend class SortedBag;

private:
	SortedBag& bag;
	SortedBagIterator(SortedBag& b);

	Node* current;

public:
	TComp getCurrent();
	bool valid();
	void next();
	void first();
	TElem remove();
};


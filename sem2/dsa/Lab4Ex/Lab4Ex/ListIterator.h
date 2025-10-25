#pragma once
#include "SortedIteratedList.h"

//DO NOT CHANGE THIS PART
class ListIterator{
	friend class SortedIteratedList;
private:
	const SortedIteratedList& list;
	int current_node;

	ListIterator(const SortedIteratedList& list);

	
	
public:
	void first();
	void next();
	bool valid() const;
    TComp getCurrent() const;
};



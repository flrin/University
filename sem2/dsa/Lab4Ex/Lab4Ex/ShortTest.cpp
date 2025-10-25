#include <assert.h>

#include "SortedIteratedList.h"
#include "ListIterator.h"

#include <exception>
#include "ShortTest.h"

#include <iostream>

using namespace std;

bool relation1(TComp e1, TComp e2) {
	if (e1 <= e2) {
		return true;
	}
	else {
		return false;
	}
}

void testAll(){
	SortedIteratedList list = SortedIteratedList(relation1);
	assert(list.size() == 0);
	assert(list.isEmpty());
    list.add(1);
    assert(list.size() == 1);
    assert(!list.isEmpty());
    ListIterator it = list.search(1);
    assert(it.valid());
    assert(it.getCurrent() == 1);
    it.next();
    assert(!it.valid());
    it.first();
    assert(it.valid());
    ListIterator itFirst = list.first();
    assert(itFirst.valid());
    assert(itFirst.getCurrent() == 1);
    assert(list.remove(it) == 1);
    assert(list.size() == 0);
    assert(list.isEmpty());
}

void testFilter()
{
    SortedIteratedList list = SortedIteratedList(relation1);
    list.add(-1);
    list.add(0);
    list.add(5);
    list.add(9);
    list.add(-99);
    list.add(-6);
    assert(list.size() == 6);

    Condition cond = [](TComp a) {return a > 0;};
    list.filter(cond);
    assert(list.size() == 2);

    cout << "Test Filter Succes!" << endl;
}


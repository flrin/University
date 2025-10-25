#pragma once

#include "Person.h"
#include "Service.h"

class UI {
private:
	Service& service;
public:
	UI(Service& service) : service(service) {}
	void start();
};
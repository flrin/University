// test_practice2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

#include "UI.h"

int main()
{
    Service service;
    service.add("2025.05.05", 200);
    service.add("2026.12.12", 70, 80);

    service.save("a.txt", "1000.11.11", "9999.11.11");

    UI ui(service);

    ui.start();
}
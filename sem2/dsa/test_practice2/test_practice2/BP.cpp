#include "BP.h"

bool BP::isResultOK()
{
    if (60 <= diastolicValue && diastolicValue <= 79 && 90 <= systolicValue && systolicValue <= 119)
        return true;
    return false;
}

std::string BP::toString()
{
    std::stringstream ss;
    ss << "BP, " << date << ", systolic value: " << systolicValue << ", disastolic value: " << diastolicValue << ", is ok?: " << isResultOK();
    return ss.str();
}

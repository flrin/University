#include "BMI.h"

bool BMI::isResultOK()
{
    if (18.5 <= value && value <= 25)
        return true;
    return false;
}

std::string BMI::toString()
{
    std::stringstream ss;
    ss << "BMI, " << date << ", " << value << ", is ok?: " << isResultOK();
    return ss.str();
}

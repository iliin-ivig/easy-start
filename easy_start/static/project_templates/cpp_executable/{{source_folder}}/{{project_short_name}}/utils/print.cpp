#include "print.h"

#include <iostream>

namespace {{project_short_name}}::utils
{
    void print(std::string_view msg)
    {
        std::cout << msg << std::endl;
    }
}

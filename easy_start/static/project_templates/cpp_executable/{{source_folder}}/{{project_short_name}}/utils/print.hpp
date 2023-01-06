#pragma once

#include "print.h"

#include <iostream>

namespace {{project_short_name}}::utils
{
    void print(const auto& obj)
    {
        std::cout << obj << std::endl;
    }
}

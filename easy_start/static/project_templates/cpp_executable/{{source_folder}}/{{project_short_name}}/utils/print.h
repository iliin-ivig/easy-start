#pragma once

#include <string_view>

namespace {{project_short_name}}::utils
{
    // Naive implementation for demonstration purposes only.
    void print(std::string_view msg);
    void print(const auto& obj);
}

#include "print.hpp"

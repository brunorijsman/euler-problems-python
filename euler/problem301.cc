#include <iostream>

bool is_lost(unsigned long x, unsigned long y, unsigned long z)
{
    return (x ^ y ^ z) == 0;
}

int main()
{
    unsigned long limit = 2UL << 29;
    unsigned long lost = 0;
    for (unsigned i = 1; i <= limit; ++i) {
        if (is_lost(i, 2*i, 3*i)) {
            ++lost;
        }
    }
    std::cout << lost << std::endl;
    return 0;
}

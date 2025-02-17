#ifndef USEFULFUNCS_H
#define USEFULFUNCS_H

#include <iostream>
#include <vector>
#include <string>
#include <chrono>
#include <iomanip>
#include <sstream>
#include <algorithm>


std::string _replace (std::string main, std::string from, std::string to);
std::string _replace (std::string main, char from, char to);
std::string _replace (double main, char from, char to);

std::string _padLeft (const std::string& main, char fill, int totalLength);
std::string _padRight (const std::string& main, char fill, int totalLength);



std::string operator*(const std::string& str, int times);


bool _isPalindrome(const std::string& str);
bool _isPalindrome(int num);

// ########################

bool _isPalindrome(const std::string& str) {
    int len = str.length();

    if (len <= 1) {return true;}
    
    for (int x = 0 ; x < len / 2 ; x++) {
        if (str[x] != str[len - x - 1]){return false;}
    }
    return true;
}

bool _isPalindrome(int num) {
    std::ostringstream oss;
    oss << num;
    std::string str = oss.str();
    return _isPalindrome(str);
}






std::string operator*(const std::string& str, int times) {
    if (times <= 0) {return 0;}

    std::string res;
    res.reserve(str.size() * times);

    for (int i = 0 ; i < times ; i++) {
        res += str;
    }
    return res;
}






inline std::string _padLeft (const std::string& main, char fill, int totalLength) {
    /*int toApend = totalLength - main.length();
    std::string pad = "";
    for (int x = 0 ; x < toApend ; x++) {
        pad += fill;
    }
    return pad + main;*/ //     <-- this version is like two times slower
    if (main.length() >= totalLength){return main;}
    return std::string((totalLength - main.length()), fill) + main;
}

inline std::string _padRight (const std::string& main, char fill, int totalLength) {
    /*int toApend = totalLength - main.length();
    std::string pad = "";
    for (int x = 0 ; x < toApend ; x++) {
        pad += fill;
    }
    return main + pad;*/
    if (main.length() >= totalLength){return main;}
    return main + std::string((totalLength - main.length()), fill);
}









inline std::string _replace (std::string main, std::string from, std::string to) {
    if (from.empty()) {return main;}

    size_t start_pos = 0;
    while ((start_pos = main.find(from, start_pos)) != std::string::npos) {
        main.replace(start_pos, from.length(), to);
        start_pos += to.length();
    }
    return main;
}

inline std::string _replace (std::string main, char from, char to) {
    std::replace(main.begin(), main.end(), from, to);
    return main;
}

inline std::string _replace(double main, char from, char to)
{
    std::ostringstream oss;
    oss << main;
    std::string output = oss.str();
    std::replace(output.begin(), output.end(), from, to);
    return output;
}

#endif // USEFULFUNCS_H
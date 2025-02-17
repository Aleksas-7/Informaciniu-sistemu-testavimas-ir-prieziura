#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include "UsefulFuncs.h"

/*

g++ -std=c++17 unitests.cpp -o unitests
./unitests

*/

TEST_CASE("Padding strings", "[string]") {
    REQUIRE(_padLeft("Hello", 'F', 10) == "FFFFFHello");
    REQUIRE(_padLeft("HI", 'Q', 1) == "HI");
    REQUIRE(_padLeft("", 'Q', 5) == "QQQQQ");

    REQUIRE(_padRight("Hello", 'F', 10) == "HelloFFFFF");
    REQUIRE(_padRight("HI", 'Q', 1) == "HI");
    REQUIRE(_padRight("", 'Q', 5) == "QQQQQ");
    
}


TEST_CASE("String replacement", "[string]") {
    REQUIRE(_replace("test", 'e', 'Q') == "tQst");
    REQUIRE(_replace("test", "test", "newTest") == "newTest");
    REQUIRE(_replace("zeTESTzeGOOD", "ze", "oo") == "ooTESTooGOOD");
    REQUIRE(_replace((double)8.224, '2', 'a') == "8.aa4");
    REQUIRE(_replace((double)8.224, '.', ',') == "8,224");
}

TEST_CASE("Palindrome strings", "[string]") {
    REQUIRE(_isPalindrome("aabaa"));
    REQUIRE(_isPalindrome("aabbaa"));
    REQUIRE_FALSE(_isPalindrome("hi"));
    REQUIRE(_isPalindrome("a"));
    REQUIRE(_isPalindrome(""));
}

TEST_CASE("Palindrome int's", "[int]") {
    REQUIRE(_isPalindrome(12321));
    REQUIRE(_isPalindrome(123321));
    REQUIRE_FALSE(_isPalindrome(95));
    REQUIRE(_isPalindrome(1));
    REQUIRE_FALSE(_isPalindrome(-1));
}

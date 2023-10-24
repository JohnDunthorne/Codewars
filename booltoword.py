def bool_to_word(boolean):
    if boolean is True:
        return "Yes"
    else:
        return "No"


import codewars_test as test
from solution import bool_to_word


@test.describe("Fixed Tests")
def basic_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(bool_to_word(True), "Yes")
        test.assert_equals(bool_to_word(False), "No")

    ##

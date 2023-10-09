def paperwork(n, m):
    # Happy Coding! ^_^
    if n < 0:
        return 0
    if m < 0:
        return 0
    else:
        return n * m

    import codewars_test as test


from solution import paperwork


@test.describe("Fixed Tests")
def basic_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(paperwork(5, 5), 25, "Failed at Paperwork(5,5)")
        test.assert_equals(paperwork(1, 2), 2, "Failed at Paperwork(1,2)")
        test.assert_equals(paperwork(-5, 5), 0, "Failed at Paperwork(-5,5)")
        test.assert_equals(paperwork(5, -5), 0, "Failed at Paperwork(5,-5)")
        test.assert_equals(paperwork(-5, -5), 0, "Failed at Paperwork(-5,-5)")
        test.assert_equals(paperwork(5, 0), 0, "Failed at Paperwork(5,0)")

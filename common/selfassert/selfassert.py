class SelfAssert:
    # def __init__(self,actual,expect):
    #     self.actual = actual
    #     self.expect = expect
    #等于
    @staticmethod
    def eq(actual,expect):
        assert actual == expect

    #小于
    @staticmethod
    def lt(actual, expect):
        assert actual < expect
    #大于
    @staticmethod
    def gt(actual, expect):
        assert actual > expect
    #小于等于
    @staticmethod
    def lte(actual, expect):
        assert actual <= expect
    #大于等于
    @staticmethod
    def gte(actual, expect):
        assert actual >= expect

if __name__ == '__main__':
    SelfAssert.eq(None,2)

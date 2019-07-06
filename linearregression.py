import math

class LinearRegression(object):
    """
    Implements linear regression on two lists of numerics

    Simply set independent_data and dependent_data,
    call the calculate method,
    and retrieve a and b
    """

    def __init__(self):
        """
        Not much happening here - just create empty attributes
        """

        self.independent_data = None
        self.dependent_data = None
        self.a = None
        self.b = None

    def calculate(self):
        """
        After calling separate functions to calculate a few intermediate values
        calculate a and b (gradient and offset).
        """

        independent_mean = self.__arithmetic_mean(self.independent_data)
        dependent_mean = self.__arithmetic_mean(self.dependent_data)
        products_mean = self.__mean_of_products(self.independent_data, self.dependent_data)
        independent_variance = self.__variance(self.independent_data)

        self.a = (products_mean - (independent_mean * dependent_mean) ) / independent_variance
        self.b = dependent_mean - (self.a * independent_mean)

    def __arithmetic_mean(self, data):
        """
        The arithmetic mean is what most people refer to as the "average",
        or the total divided by the count
        """

        total = 0

        for d in data:
            total += d

        return total / len(data)

    def __mean_of_products(self, data1, data2):
        """
        This is a type of arithmetic mean, but of the products of corresponding values
        in bivariate data
        """

        total = 0

        for i in range(0, len(data1)):
            total += (data1[i] * data2[i])

        return total / len(data1)

    def __variance(self, data):
        """
        The variance is a measure of how much individual items of data typically vary from the
        mean of all the data.
        The items are squared to eliminate negatives.
        (The square root of the variance is the standard deviation.)
        """

        squares = []

        for d in data:
            squares.append(d**2)

        mean_of_squares = self.__arithmetic_mean(squares)
        mean_of_data = self.__arithmetic_mean(data)
        square_of_mean = mean_of_data**2
        variance = mean_of_squares - square_of_mean

        return variance

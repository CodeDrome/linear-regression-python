import data
import linearregression


def main():
    """
    Demonstrate the LinearRegression class with three sets of test data
    provided by the data module
    """

    print("----------------------")
    print("| code-in-python.com |")
    print("| Linear Regression  |")
    print("----------------------\n")

    independent = []
    dependent = []

    lr = linearregression.LinearRegression()

    for d in range(1, 4):

        if data.populatedata(independent, dependent, d) == True:

            lr.independent_data = independent
            lr.dependent_data = dependent

            lr.calculate()

            print("Dataset %d\n---------" % d)
            print("Independent data: " + (str(lr.independent_data)))
            print("Dependent data:   " + (str(lr.dependent_data)))
            print("y = %gx + %g" % (lr.a, lr.b))

            print("")

        else:
            print("Cannot populate Dataset %d" % d)


main()

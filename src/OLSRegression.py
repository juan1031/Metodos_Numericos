import numpy as np


class OLSRegression:
    def fit(self, X, y):
        # Add a column of ones for the intercept term
        X = np.column_stack((np.ones(len(X)), X))

        # Solve for coefficients using normal equations
        self.coefficients = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

        # Predict y values
        y_pred = X.dot(self.coefficients)

        # Calculate residuals
        residuals = y - y_pred

        # Calculate total sum of squares (TSS)
        TSS = np.sum((y - np.mean(y)) ** 2)

        # Calculate residual sum of squares (RSS)
        RSS = np.sum(residuals ** 2)

        # Calculate R-squared
        self.R_squared = 1 - (RSS / TSS)

        # Calculate error standard deviation
        self.error_std = np.sqrt(RSS / (len(X) - len(self.coefficients)))

    def get_coefficients(self):
        return self.coefficients

    def get_R_squared(self):
        return self.R_squared

    def get_error_std(self):
        return self.error_std


# Example usage
if __name__ == "__main__":
    # Sample data
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y = np.array([3, 4, 5, 6])

    # Fit the model
    model = OLSRegression()
    model.fit(X, y)

    # Get coefficients, R-squared, and error standard deviation
    coefficients = model.get_coefficients()
    R_squared = model.get_R_squared()
    error_std = model.get_error_std()

    print("Coefficients:", coefficients)
    print("R-squared:", R_squared)
    print("Error standard deviation:", error_std)

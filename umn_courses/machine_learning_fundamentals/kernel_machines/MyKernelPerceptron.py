import numpy as np

"""
Specify your sigma for RBF kernel in the order of questions (simulated data, digit-49, digit-79)
"""
# sigma_pool = [0.5, 0.5, 0.5]
sigma_pool = [1, 1, 1]
# sigma_pool = [1.5, 1.5, 1.5]
# sigma_pool = [2, 2, 2]
# sigma_pool = [3, 3, 3]
# sigma_pool = [10, 10, 10]


class KernelPerceptron:
    """
    Perceptron Algorithm with RBF Kernel
    """

    def __init__(self, train_x, train_y, sigma_idx):
        self.sigma = sigma_pool[sigma_idx]  # sigma value for RBF kernel
        self.train_x = (
            train_x  # kernel perceptron makes predictions based on training data
        )
        self.train_y = train_y
        self.alpha = np.zeros([len(train_x),]).astype(
            "float32"
        )  # parameters to be optimized

    def RBF_kernel(self, x):
        """
        x: (x_t - x_sample)
        """
        # Implement the RBF kernel
        euclidean_distance = np.sum(np.square(x), axis=-1)
        return np.exp(-1 * euclidean_distance / (2 * self.sigma ** 2))

    def fit(self, train_x, train_y):
        # set a maximum training iteration
        max_iter = 1000

        # training the model
        for iter in range(max_iter):
            error_count = 0  # use a counter to record number of misclassification

            # loop through all samples and update the parameter accordingly
            for i in range(len(train_x)):
                x_sample = train_x[i]
                summation = 0
                
                for j in range(len(train_x)):
                    x_t = self.train_x[j]
                    
                    summation += self.alpha[j] * train_y[j] * self.RBF_kernel(x_t - x_sample)
                    
                y = np.sign(summation)
                
                if y != train_y[i]:
                    self.alpha[i] += 1
                    error_count += 1

            # stop training if parameters do not change any more
            if error_count == 0:
                break

    def predict(self, test_x):
        # generate predictions for given data
        pred = np.ones([len(test_x)]).astype("float32")  # placeholder

        # loop through all samples and update the parameter accordingly
        for i in range(len(test_x)):
            summation = 0
            
            for j in range(len(self.train_y)):
                x_t = self.train_x[j]
                x_sample = test_x[i]
                
                summation += self.alpha[j] * self.train_y[j] * self.RBF_kernel(x_t - x_sample)
                
            pred[i] = np.sign(summation)

        return pred

    def param(
        self,
    ):
        return self.alpha

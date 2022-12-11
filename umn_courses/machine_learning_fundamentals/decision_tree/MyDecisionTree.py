import numpy as np


class Tree_node:
    """
    Data structure for nodes in the decision-tree
    """

    def __init__(
        self,
    ):
        self.is_leaf = False  # whether or not the current node is a leaf node
        self.feature = None  # index of the selected feature (for non-leaf node)
        self.label = None  # class label (for leaf node)
        self.left_child = None  # left child node
        self.right_child = None  # right child node


class Decision_tree:
    """
    Decision tree with binary features
    """

    def __init__(self, min_entropy):
        self.min_entropy = min_entropy
        self.root = None

    def fit(self, train_x, train_y):
        # construct the decision-tree with recursion
        self.root = self.generate_tree(train_x, train_y)

    def predict(self, test_x):
        # iterate through all samples
        prediction = np.zeros([len(test_x),]).astype(
            "int"
        )  # placeholder
        for i in range(len(test_x)):
            # traverse the decision-tree based on the features of the current sample
            prev_node = self.root
            loop = True
            
            while loop:
                if prev_node.label in range(0, 10):
                    prediction[i] = prev_node.label
                    loop = False
                else:
                    if test_x[i, prev_node.feature] == 1:
                        prev_node = prev_node.left_child
                    elif test_x[i, prev_node.feature] == 0:
                        prev_node = prev_node.right_child

        return prediction

    def generate_tree(self, data, label):
        # initialize the current tree node
        cur_node = Tree_node()

        # compute the node entropy
        node_entropy = self.compute_node_entropy(label)

        # determine if the current node is a leaf node
        if node_entropy < self.min_entropy:
            # determine the class label for leaf node
            cur_node.is_leaf = True
            
            unique_label = np.unique(label) # unique label array
            f_count = lambda l: len(label[np.where(label == l)]) # count function for each label
            label_count = list(map(f_count, unique_label)) # count of each label
            cur_node.label = unique_label[np.argmax(label_count)] # choose the label which has maximum count
            
            return cur_node

        # select the feature that will best split the current non-leaf node
        selected_feature = self.select_feature(data, label)
        cur_node.feature = selected_feature

        # split the data based on the selected feature and start the next level of recursion
        left_data = data[np.where(data[:, selected_feature] == 1)]
        left_label = label[np.where(data[:, selected_feature] == 1)]
        
        right_data = data[np.where(data[:, selected_feature] == 0)]
        right_label = label[np.where(data[:, selected_feature] == 0)]
        
        # although we get selected_feature, if the data is same after splitting, we have to make the current node
        # as a leaf node to avoid stuck in recursion
        if (len(left_data) == 0) or (len(right_data) == 0):
            cur_node.is_leaf = True
            
            unique_label = np.unique(label) # unique label array
            f_count = lambda l: len(label[np.where(label == l)]) # count function for each label
            label_count = list(map(f_count, unique_label)) # count of each label
            cur_node.label = unique_label[np.argmax(label_count)] # choose the label which has maximum count
            
            return cur_node
        else:
            cur_node.left_child = self.generate_tree(left_data, left_label)
            cur_node.right_child = self.generate_tree(right_data, right_label)

        return cur_node

    def select_feature(self, data, label):
        # iterate through all features and compute their corresponding entropy
        best_feat = 0
        min_entropy = -1 # added

        for i in range(len(data[0])):
            
            # compute the entropy of splitting based on the selected features
            cur_entropy = self.compute_split_entropy(
                label[np.where(data[:, i] == 1)], label[np.where(data[:, i] == 0)]
            )  # You need to replace the placeholders ('None') with valid inputs
            
            # select the feature with minimum entropy
            if min_entropy == -1:
                min_entropy = cur_entropy
            
            if cur_entropy <= min_entropy:
                min_entropy = cur_entropy
                best_feat = i

        return best_feat

    def compute_split_entropy(self, left_y, right_y):
        # compute the entropy of a potential split, left_y and right_y are labels for the two splits
        split_entropy = 0  # placeholder
        
        left_w = len(left_y) / (len(left_y) + len(right_y))
        right_w = len(right_y) / (len(left_y) + len(right_y))
            
        split_entropy = left_w * self.compute_node_entropy(left_y) + right_w * self.compute_node_entropy(right_y)

        return split_entropy

    def compute_node_entropy(self, label):
        # compute the entropy of a tree node (add 1e-15 inside the log2 when computing the entropy to prevent numerical issue)
        node_entropy = 0  # placeholder
        unique_label = np.unique(label)
        
        # if there is only one kind of label or there is no label, then return 0 node_entropy
        if len(unique_label) <= 1:
            return node_entropy
        
        for l in unique_label:
            prob = len(label[np.where(label == l)]) / len(label) # calculate probability of each class
            # log_prob = np.log2(prob + 1e-15) / np.log2(len(unique_label)) # logarithm with different base
            log_prob = np.log2(prob + 1e-15)
        
            node_entropy += -prob * log_prob

        return node_entropy

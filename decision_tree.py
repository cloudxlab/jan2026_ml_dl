import random


class Node:
    def __init__(
        self,
        feature=None,
        threshold=None,
        left=None,
        right=None,
        value=None
    ):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

    def is_leaf(self):
        return self.value is not None


class DecisionTreeRegressor:

    def __init__(
        self,
        max_depth,
        min_samples_split,
        max_features=None
    ):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.max_features = max_features
        self.root = None
    
    def variance(self, values):
        if len(values) == 0:
            return 0
        
        mean = sum(values) / len(values)
        total_squared_distance = 0

        for value in values:
            total_squared_distance += (value - mean) ** 2

        return total_squared_distance / len(values)

    def total_variance(self,left, right):
        total_size = len(left) + len(right)

        left_weight = len(left) / total_size
        right_weight = len(right) / total_size

        return left_weight * self.variance(left) + right_weight * self.variance(right)

    def find_best_split(self, X, y):
        parent_variance = self.variance(y)
        best_feature = None
        best_threshold = None
        best_gain = -float("inf")

        n_features = len(X[0])

        if self.max_features is None:
            features_to_consider = range(n_features)
        else:
            features_to_consider = random.sample(
                range(n_features),
                min(self.max_features, n_features)
            )

        for feature_idx in features_to_consider:

            thresholds = sorted(
                set(row[feature_idx] for row in X)
            )

            for threshold in thresholds:
                left_y = []
                right_y = []

                for row, target in zip(X, y):
                    if row[feature_idx] <= threshold:
                        left_y.append(target)
                    else:
                        right_y.append(target)

                if not left_y or not right_y:
                    continue

                child_variance = (self.total_variance(left_y,right_y))

                gain = (parent_variance - child_variance)

                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature_idx
                    best_threshold = threshold

        return (best_feature,best_threshold)
    
    def build_tree(self, X, y, depth=0):
        # Stop if too few samples
        if len(y) < self.min_samples_split:
            return Node(value=sum(y) / len(y))

        # Stop if maximum depth reached
        if depth >= self.max_depth:
            return Node(value=sum(y) / len(y))

        # Stop if node is perfectly pure
        if self.variance(y) == 0:
            return Node(value=y[0])

        # Find the best split
        feature, threshold = self.find_best_split(X, y)
        # No valid split found
        if feature is None:
            return Node(value=sum(y) / len(y))

        # Split the data
        left_X = []
        left_y = []
        right_X = []
        right_y = []

        for row, target in zip(X, y):
            if row[feature] <= threshold:
                left_X.append(row)
                left_y.append(target)
            else:
                right_X.append(row)
                right_y.append(target)

        # Recursively build children
        left_child = self.build_tree(
            left_X,
            left_y,
            depth + 1
        )

        right_child = self.build_tree(
            right_X,
            right_y,
            depth + 1
        )

        # Return internal node
        return Node(
            feature=feature,
            threshold=threshold,
            left=left_child,
            right=right_child
        )
    
    def fit(self, X, y):
        self.root = self.build_tree(X, y)
        
    def predict_one(self,row,node):
        if node.is_leaf():
            return node.value

        if row[node.feature] <= node.threshold:
            return self.predict_one(
                row,
                node.left
            )

        return self.predict_one(
            row,
            node.right
        )

    def predict(self, X):
        predictions = []

        for row in X:
            predictions.append(
                self.predict_one(
                    row,
                    self.root
                )
            )

        return predictions
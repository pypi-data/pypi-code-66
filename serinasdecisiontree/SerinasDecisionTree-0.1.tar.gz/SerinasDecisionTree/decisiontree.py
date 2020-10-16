from collections import Counter
import numpy as np

class DecisionTreeClassifier:

    '''Can handle numeric features and dataframes that are free of missing data.
    If missing values, please impute first.'''

    def __init__(self, min_samples=2, max_depth=5, tree=None, append=None):
        
        self.max_depth = max_depth
        self.min_samples = min_samples
        self.tree = None
        self.append = None
        
        
    def fit(self, train_df):
        
        # run method decision_tree and set it as the self.tree attribute
        self.tree = self.decision_tree(train_df, self.min_samples, self.max_depth)
        
        return self
    
    
    def predict(self, test_df):

        # if a tree has been fitted
        if self.tree:
            
            # store true labels for our test_df
            y_test_true = test_df.iloc[:, -1]
            
            while self.append not in ['Y', 'y', 'N', 'n']:
                
                # ask the user if they want the DTC's predictions appended
                self.append = input('Append predictions as new column in input dataframe? Y or N')
                
                # if they do 
                if self.append in ['Y', 'y']:
                    
                    continue
            
                # if they don't want their predictions appended
                elif self.append in ['N', 'n']:
                    
                    # create a copy of the test_df so results don't get appended
                    test_df = test_df.copy()
                    
                # if not a valid input  
                else:
                    
                    print("Not a valid input. Try again you silly goose.")
            
            # create a new column for our predictions
            test_df['predictions'] = test_df.apply(self.classify_observation, axis=1, args=(self.tree,))
            
            # return True or False where our predictions are equal to our labels
            test_df['correct_predictions'] = test_df['predictions'] == y_test_true

            # return how accurate the predictions are
            return ("Accuracy:", test_df['correct_predictions'].mean())
        
        # if a tree wasn't fitted
        else:
            print("NotFittedError: Please fit your decision tree first!")


    def print_tree(self):
        
        return self.tree


    def entropy(self, data):

        # labels for input data
        labels = data[:,-1]

        # get unique labels along with their counts
        _, label_counts = np.unique(labels, return_counts=True)

        # array of probabilities of each label
        probabilities = label_counts / label_counts.sum()
        
        # return entropy
        return sum(probabilities * -np.log2(probabilities))
    
    
    def information_gain(self, data, data_below_threshold, data_above_threshold):
        
        parent_entropy = self.entropy(data)
        
        entropy_below_threshold = self.entropy(data_below_threshold)
        
        entropy_above_threshold = self.entropy(data_above_threshold)
        
        weight_below_threshold = len(data_below_threshold) / len(data)
        
        weight_above_threshold = len(data_above_threshold) / len(data)
        
        children_entropy = (weight_below_threshold * entropy_below_threshold) + (weight_above_threshold * entropy_above_threshold)
    
        # return information gain
        return parent_entropy - children_entropy
    


    def purity(self, data):

        # last column of the df must be the labels!
        labels = data[:, -1]

        # if data has only one kind of label
        if len(np.unique(labels)) == 1:

            # it is pure
            return True

        # if data has a few different labels still
        else:

            # it isn't pure
            return False
        
    
    def make_classification(self, data):

        '''Once the max depth or min samples or purity is 1, 
        we classify the data with whatever the majority of the labels are'''

        # labels for input data
        labels = data[:,-1]

        # instantiate a Counter object on the labels
        counter = Counter(labels)

        # return the most common class/label
        return counter.most_common(1)[0][0]

    
    def split_data(self, data, split_feature, split_threshold):

        # array of only the split_feature
        feature_values = data[:,split_feature]

        # array where feature values do not exceed threshold, array where does exceed threshold
        return data[feature_values <= split_threshold], data[feature_values > split_threshold]


    def potential_splits(self, data):
        
        # dictionary of splits
        potential_splits = {}

        # store the number of features (not including labels/target)
        n_features = len(data[0])

        # for each feature in possible features
        for feature in range(n_features - 1):

            # for our dictionary, each feature should be a key
            potential_splits[feature] = []

            # we need to iterate through each feature's unique values
            unique_values_for_feature = np.unique(data[:, feature])

            for index in range(len(unique_values_for_feature)):
                
                if index != 0:

                    # we need to partition the data, we need the midpoint between the unique values
                    current = unique_values_for_feature[index]
                    prev = unique_values_for_feature[index - 1]
                    midpoint = (current + prev) / 2

                    # for our dictionary each value should be a midpoint between the 
                    # unique values for that feature
                    potential_splits[feature].append(midpoint)

        # return dictionary
        return potential_splits

    
    def find_best_split(self, data, potential_splits):

        best_info_gain = 0

        # for each dictionary key
        for key in potential_splits:
            
            # for each value for that key
            for value in potential_splits[key]:

                # split our data on that threshold (value)
                data_below_threshold, data_above_threshold = self.split_data(
                    data=data, 
                    split_feature=key,
                    split_threshold=value)
                
                # calculate information gain at this split
                info_gain_for_this_split = self.information_gain(data_below_threshold, data_above_threshold)

                # if info gain at this split is higher than the highest info gain found so far
                if info_gain_for_this_split > best_info_gain:

                    # the info gain at this split is now the highest 
                    best_info_gain = info_gain_for_this_split

                    # keep a record of this key, value pair
                    best_split_feature = key
                    best_split_threshold = value

        # return the best potential split
        return best_split_feature, best_split_threshold


    def decision_tree(self, train_df, min_samples, max_depth, counter=0):

        '''only one arg needed (df). fitting this training df will account for
        splitting data into X and y'''

        # if this is our first potential split
        if counter == 0:

            # set this global variable so we can use it each time we call decision_tree()
            global feature_names
            feature_names = train_df.columns

            # get our df values
            data = train_df.values

        # if we have recursively reached this point
        else:

            # our 'train_df' is actually already an array upon recursion
            data = train_df
            
        # base case: if our impurity for a subtree is 0 or we have reached our 
        # maximum depth or min samples
        if (self.purity(data)) or (len(data) < min_samples) or (counter == max_depth):
            
            # at this point we'll have to make a judgment call and classify it based on the majority
            return self.make_classification(data)

        # if we haven't reach one of our stopping points
        else:

            # increment counter
            counter += 1

            # get a dictionary of our potential splits
            potential_splits = self.potential_splits(data)
            
            # find the best split
            split_feature, split_threshold = self.find_best_split(data, potential_splits)

            # get the data below and above
            data_below_threshold, data_above_threshold = self.split_data(data, split_feature, split_threshold)

            # store feature name as string
            feature_name_as_string = feature_names[split_feature]

            # feature_name <= threshold value
            split_question = f"{feature_name_as_string} <= {split_threshold}"

            # create a dictionary for these split_questions 
            subtree = {split_question: []}

            # recursion on our true values
            answer_true = self.decision_tree(data_below_threshold, min_samples, max_depth, counter)

            # recursion on our false values
            answer_false = self.decision_tree(data_above_threshold, min_samples, max_depth, counter)

            # if both answers are the same class
            if answer_true == answer_false:

                # choose one to be the subtree
                subtree = answer_true
            
            # if answers result in different class
            else:

                # append to dictionary
                subtree[split_question].append(answer_true)
                subtree[split_question].append(answer_false)
            
            return subtree

        
    def classify_observation(self, observation, tree):

        # store the current question 
        split_question = list(tree.keys())[0]

        # grab the feature name and value 
        feature_name, _, value = split_question.split()

        # if the row at that feature column is less than the threshold
        if observation[feature_name] <= float(value):

            # answer yes, it's under the threshold
            answer = tree[split_question][0]

        # if the row at that feature column has exceeded the threshold
        else:

            # answer no, it has exceeded the threshold
            answer = tree[split_question][1]

        # if the answer is not a dictionary
        if not isinstance(answer, dict):

            # return answer as it is a class label
            return answer

        # if the answer is a dictionary
        else:

            # recursion with the 'answer' subtree as the tree argument
            return self.classify_observation(observation, answer)
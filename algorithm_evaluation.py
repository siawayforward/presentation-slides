#import modules needed
from data_slices import *
from recommender_metrics import *
from sklearn.metrics.pairwise import cosine_similarity

class RecommenderAlgorithm:

    def __init__(self, algorithm, name):
        if algorithm: self.algorithm = algorithm
        if name: self.algorithm_name = name

    def get_algorithm(self):
        return self.algorithm

    def get_algorithm_name(self):
        return self.algorithm_name

    def evaluate_algorithm(self):
        pass

    def get_algorithm_predictions(self):
        pass
    
    def get_algorithm_metrics(self):
        pass


    
        


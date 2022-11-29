"""Kmeans Module"""
import sys
import csv
import numpy as np


class KmeansClustering:
    """KmeansClustering"""

    def __init__(self, max_iter: int = 20, ncentroid: int = 5):
        """Constructor"""
        self.ncentroid = ncentroid  # number of centroids
        self.max_iter = max_iter  # number of max iter to update the centroids
        self.centroids = []  # values of the centroids

    # private functions
    def ___get_cluster_indexes(self, dataset):
        """returns a ndarray with the proper cluster index for each row"""
        # create a new matrix with the distance from each centroid
        dist_matrix = np.array([np.linalg.norm(centroid - data_point)
                                for data_point in dataset
                                for centroid in self.centroids])
        dist_matrix = dist_matrix.reshape(
            dataset.shape[0], self.centroids.shape[0])

        # get the shortest distance index on a new matrix
        return np.argmin(dist_matrix, axis=1).reshape(dataset.shape[0], 1)

    def __calculate_sse(self, dataset, clusters):
        """
        calculate the Sum of Squared errors from the centroïds stored on the
        object and the dataset and clusters in parameters.
        """
        ### Reste a faire le calcul du sse (voir formule)
        return 6

    # public functions
    def do_multiple_kmeans(self, dataset, iterations: int = 10):
        """
        perform K-means multiple time and return the best centroïd array
        according to the SSE value
        """
        # init a global sse array with all information from iterations
        sse = np.empty((0, int(self.ncentroid), 4), dtype=np.float32)
        for _ in range(iterations):
            # get a set of stable centroids
            self.fit(dataset)
            # get the cluster id for each dataset row
            clusters = self.predict(dataset)
            # calculate sse
            current_sse = self.__calculate_sse(dataset, clusters)
            # concatenate sse and centroids in a single array
            current_sse_centroid = np.hstack(
                     (np.full((self.centroids.shape[0], 1), current_sse),
                      self.centroids))
            current_sse_centroid = np.expand_dims(current_sse_centroid, axis=0)

            # add the current set to the global sse array
            sse = np.vstack((sse, current_sse_centroid))
    
        # remove the first uninitialized row
        sse = sse[1:, :, :]

        # pick the subset with the lowest sse and store the corresponding 
        # centroids in the class

    def fit(self, X):  # entraine sur les donnees
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from
        the dataset.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        None.
        Raises:
        -------
        This function should not raise any Exception.
        """
        # 1. pick n different random centroids from the dataset to initialize
        rng = np.random.default_rng()
        try:
            self.centroids = rng.choice(X, int(self.ncentroid), replace=False)
        except TypeError:
            return None

        # loop to find the best pos for current centroids
        for _ in range(int(self.max_iter)):
            # 2. associate each point with a centroid according to the distance
            cluster_indexes = self.___get_cluster_indexes(X)

            # - concatenate origin and current assignment tab
            assigned_set = np.concatenate((X, cluster_indexes), axis=1)

            # 3. compute the mean of the cluster and move the centroid
            new_centroids = np.array([np.mean(
                assigned_set[assigned_set[:, -1] == index], axis=0)
                for index, _ in enumerate(self.centroids)])
            new_centroids = new_centroids[:, :-1]

            # 4. loop to 2 until there is no change in the clusters
            centroid_diff = new_centroids - self.centroids
            self.centroids = new_centroids
            if np.mean(centroid_diff) == 0:
                break

        return None

    def predict(self, X):  # predit sur des nouvelles donnees
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
        This function should not raise any Exception.
        """
        return self.___get_cluster_indexes(X)


def main(**kwargs):
    """Main program"""

    # 1. parameters check
    if len([key for key, value in kwargs.items()
           if key in ['filepath', 'ncentroid', 'max_iter']]) != 3:
        print("Error: wrong parameter(s)")
        return None

    # 2. assigning parameters
    (_, filepath), (_, ncentroid), (_, max_iter) = kwargs.items()

    # 3. open and load data file
    rows = []
    try:
        with open(filepath, 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                rows.append(row)
    except (FileNotFoundError, PermissionError) as ex:
        print(ex)
        return None
    except StopIteration:
        print("Error while iterating throught the file")
        return None

    # 4. data to nd array
    data = np.array(rows, dtype=float)[:, 1:]

    # 5. create a Kmeans clustering object
    kmc = KmeansClustering(max_iter=max_iter, ncentroid=ncentroid)

    # 6. fit the Kmeans using the dataset
    kmc.do_multiple_kmeans(data)

    # 6bis. multiple Kmeans to select good centroids

    # 7. predict using the dataset to get the cluster indexes
    cluster_prediction = kmc.predict(data)

    # 8. label the clusters
    labels = ['Venus', 'Earth', 'Mars', 'Belt']


if __name__ == '__main__':

    try:
        # check for arguments
        if len(sys.argv) != 4:
            print('Usage: \n\tpython Kmeans.py filepath="../mypath/file.csv" '
                  'ncentroids=4 max_iter=30')
        else:
            main(**dict(arg.split('=') for arg in sys.argv[1:]))
    except (ValueError) as exc:
        print(exc)

"""Kmeans Module"""
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt


class KmeansClustering:
    """KmeansClustering"""

    def __init__(self, max_iter: int = 20, ncentroid: int = 5):
        """Constructor"""
        self.ncentroid = ncentroid  # number of centroids
        self.max_iter = max_iter  # number of max iter to update the centroids
        self.centroids = []  # values of the centroids

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
        # create an assigned set from the dataset
        cluster_indexes = self.___get_cluster_indexes(dataset)
        assigned_set = np.concatenate((dataset, cluster_indexes), axis=1)
        centroids = np.array(self.centroids)
        # calculate the sse part for each dataset entry
        sse_by_row = [[
            np.sum((ds[:-1] - centroids[i, :])**2)
            for ds in assigned_set[assigned_set[:, 3] == i]
        ]
            for i in range(int(self.ncentroid))
        ]
        # sum the sse by centroid
        sse_by_centroid = np.array([np.sum(sse_part)
                                   for sse_part in sse_by_row])
        # sum the sse on the entire set
        sse = np.sum(sse_by_centroid)
        return sse

    def do_multiple_kmeans(self, dataset, iterations: int = 30):
        """
        perform K-means multiple time and return the best centroïd array
        according to the SSE values
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

        # find the lowest sse
        lowest_sse = sse[:, :, 0].min()
        # filter the global matrix to keep only the best set of centroids
        self.centroids = sse[sse[:, :, 0] == lowest_sse][:4, 1:]

    def get_region(self):
        """
        according to the caracteristics of the centroids, associate a region
        with each centroid.
        Then add a "label" column to the matrix in parameter and return it.
        """
        belt, venus, earth, mars = 0, 0, 0, 0
        labels = [None] * 4

        # 1. Get max and min for useful dimension
        max_height = np.argmax(self.centroids[:, 0])
        min_height = np.argmin(self.centroids[:, 0])
        max_weight = np.argmax(self.centroids[:, 1])
        min_weight = np.argmin(self.centroids[:, 1])
        min_density = np.argmin(self.centroids[:, 2])

        # 2. Find regions
        belt = max_height if max_height == min_density == max_weight else max_weight
        earth = min_height
        venus = min_weight
        mars = 6 - belt - earth - venus

        # 3. Assign labels
        labels[belt] = 'Belt'
        labels[earth] = 'Earth'
        labels[venus] = 'Venus'
        labels[mars] = 'Mars'

        return labels

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
    dataset = np.array(rows, dtype=float)[:, 1:]

    # 5. create a Kmeans clustering object
    kmc = KmeansClustering(max_iter=max_iter, ncentroid=ncentroid)

    # 6. fit the Kmeans using the dataset
    kmc.do_multiple_kmeans(dataset)

    # 7. predict using the dataset to get the cluster indexes
    prediction = kmc.predict(dataset)

    # 8. associate region if ncentroids == 4
    labels = None
    if int(ncentroid) == 4:
        labels = kmc.get_region()

    # 8. display detailed information
    print(f'{"":-<4}{"":-<10}{"":-<10}{"":-<20}{"":-<20}{"":-<20}')
    print(f'{"id":<4}{"region":<10}{"indiv.":<10}{"height":<20}{"weight":<20}{"density":<20}')
    print(f'{"":-<4}{"":-<10}{"":-<10}{"":-<20}{"":-<20}{"":-<20}')

    [print(f'{index:<4}{labels[index]:<10}{np.count_nonzero(prediction == index):<10}{height:<20}{weight:<20}{density:<20}')
     for index, (height, weight, density) in enumerate(kmc.centroids)]
    
    print(f'{"":-<4}{"":-<10}{"":-<10}{"":-<20}{"":-<20}{"":-<20}')

    # 9. 2D plot the clusters

    # 10. 3D plot the clusters
    # fig = plt.figure()
    # ax = fig.add_subplot(projection='3d')

    # for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
    #     xs = randrange(n, 23, 32)
    #     ys = randrange(n, 0, 100)
    #     zs = randrange(n, zlow, zhigh)
    #     ax.scatter(xs, ys, zs, marker=m)
    # ax.set_xlabel('height')
    # ax.set_ylabel('weight')
    # ax.set_zlabel('bone density')
    # plt.show()

    # X. label the clusters
    # labels = ['Venus', 'Earth', 'Mars', 'Belt']


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

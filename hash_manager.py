from hash_algorithm import HashAlgorithm

class HashManager:

    def __init__(self, algorithm: HashAlgorithm = None):
        self.algorithm = algorithm

    def set_algorithm(self, algorithm: HashAlgorithm):
        self.algorithm = algorithm

    def generate_hash(self, text: str) -> str:

        if self.algorithm is None:
            raise ValueError("Algoritma hash belum dipilih")

        return self.algorithm.hash(text)
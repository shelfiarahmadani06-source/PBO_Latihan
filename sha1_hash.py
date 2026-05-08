import hashlib
from hash_algorithm import HashAlgorithm

class SHA1Hash(HashAlgorithm):

    def __init__(self):
        super().__init__("SHA1")

    def hash(self, text: str) -> str:
        return hashlib.sha1(text.encode()).hexdigest()
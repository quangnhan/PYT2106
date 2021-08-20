from builder import Builder
from castle import Castle


class CastleBuilder(Builder):
    def __init__(self):
        self._result = Castle()
    
    def build_pool(self, number):
        self._result.pool = number

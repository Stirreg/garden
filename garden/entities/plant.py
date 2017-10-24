"""Garden plant model module."""

class Plant():
    """Plant entity."""
    def __init__(self, binomial=None, names=None, cultivars=(), image=None):
        self.binomial = binomial
        self.names = names
        self.cultivars = cultivars
        self.image = image

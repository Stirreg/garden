"""Garden plant repository module."""
from garden.entities.plant import Plant


class PlantRepository():
    """Plant repository."""
    def __init__(self, mongo):
        self.mongo = mongo

    def save(self, plant):
        """Persist a plant object to the database."""
        self.mongo.db.flora.update_one(
            {'binomial': plant.binomial},
            {'$set': plant.__dict__},
            upsert=True
        )

    def get_one_by_binomial(self, binomial):
        """
        Retrieve a plant document from the database,
        build a plant object from the plant document and return the plant object.
        """
        document = self.mongo.db.flora.find_one({'binomial': binomial})
        # TODO: Investigate if setattr might be a better option here.
        plant = Plant(**self.prepare_document(document))
        return plant

    def get_all(self):
        """
        Get all plant documents from the database,
        build a plant object for each of the plant documents and return a list of plant objects.
        """
        documents = self.mongo.db.flora.find().sort('names', 1)
        # TODO: Investigate if setattr might be a better option here.
        plants = [Plant(**self.prepare_document(document)) for document in documents]
        return plants

    def delete_one_by_binomial(self, binomial):
        """Delete a plant document using the binomial."""
        self.mongo.db.flora.delete_one({'binomial': binomial})

    def prepare_document(self, document):
        """Remove the _id field from a plant document."""
        del document['_id']
        return document

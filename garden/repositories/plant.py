from garden.models.plant import Plant

class PlantRepository():
    def __init__(self, mongo):
        self.mongo = mongo

    def save(self, plant):
        self.mongo.db.flora.update_one(
            {'binomial': plant.binomial},
            {'$set': plant.__dict__},
            upsert=True
        )

    def get_one_by_binomial(self, binomial):
        document = self.mongo.db.flora.find_one({'binomial': binomial})
        # TODO: Investigate if setattr might be a better option here.
        plant = Plant(**self.prepare_document(document))
        return plant

    def get_all(self):
        documents = self.mongo.db.flora.find().sort('names', 1)
        # TODO: Investigate if setattr might be a better option here.
        plants = [Plant(**self.prepare_document(document)) for document in documents]
        return plants

    def delete_one_by_binomial(self, binomial):
        self.mongo.db.flora.delete_one({'binomial': binomial})

    def prepare_document(self, document):
        del document['_id']
        return document

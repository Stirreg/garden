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

    def get(self, binomial):
        data = self.mongo.db.flora.find_one({'binomial': binomial})
        del data['_id']
        # TODO: Figure out which of the following two lines is better.
        plant = Plant(**data)
        # plant.__dict__.update(data)
        return plant
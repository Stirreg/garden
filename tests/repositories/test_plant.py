import unittest
from unittest.mock import Mock
from garden.repositories.plant import PlantRepository
from garden.entities.plant import Plant


class PlantTests(unittest.TestCase):

    def setUp(self):
        self.mongo_mock = Mock()
        self.plant_mock = Plant(
            binomial='bla',
            names=['bla', 'bla'],
            cultivars=['bla', 'bla', 'bla'],
            image=None
        )
        self.document_mock = {
            "_id": 1,
            "binomial": "bla",
            "names": [
                "bla", "bla"
            ],
            "cultivars": [
                "bla", "bla"
            ],
            "image": None
        }

    def test_save(self):
        plant_repository = PlantRepository(self.mongo_mock)

        plant_repository.save(self.plant_mock)

        self.mongo_mock.db.flora.update_one.assert_called_once_with(
            {'binomial': self.plant_mock.binomial},
            {'$set': self.plant_mock.__dict__},
            upsert=True
        )

    def test_get_one_by_binomial(self):
        self.mongo_mock.db.flora.find_one.return_value = self.document_mock

        plant_repository = PlantRepository(self.mongo_mock)

        plant = plant_repository.get_one_by_binomial(self.plant_mock.binomial)

        self.mongo_mock.db.flora.find_one.assert_called_once_with({'binomial': self.plant_mock.binomial})
        self.assertIsInstance(plant, Plant)

    def test_get_all(self):
        cursor_mock = Mock()

        cursor_mock.sort.return_value = [
            self.document_mock
        ]

        self.mongo_mock.db.flora.find.return_value = cursor_mock

        plant_repository = PlantRepository(self.mongo_mock)

        plants = plant_repository.get_all()

        self.mongo_mock.db.flora.find.assert_called_once()
        cursor_mock.sort.assert_called_once_with('names', 1)
        self.assertIsInstance(plants[0], Plant)

    def test_delete_one_by_binomial(self):
        plant_repository = PlantRepository(self.mongo_mock)

        plant_repository.delete_one_by_binomial(self.plant_mock.binomial)

        self.mongo_mock.db.flora.delete_one.assert_called_once_with({'binomial': self.plant_mock.binomial})

    def test_prepare_document(self):
        plant_repository = PlantRepository(self.mongo_mock)

        document = plant_repository.prepare_document(self.document_mock)

        self.assertEqual(document, {
            "binomial": "bla",
            "names": [
                "bla", "bla"
            ],
            "cultivars": [
                "bla", "bla"
            ],
            "image": None
        })
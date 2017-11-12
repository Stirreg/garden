import unittest
from unittest.mock import Mock
from garden.services.plant import PlantService
from garden.entities.plant import Plant


class PlantTests(unittest.TestCase):

    def setUp(self):
        self.plant_repository_mock = Mock()
        self.plant_mock = Plant(
            binomial='bla',
            names=['bla', 'bla'],
            cultivars=['bla', 'bla', 'bla'],
            image=None
        )

    def test_save_plant(self):
        plant_service = PlantService(self.plant_repository_mock)

        plant = plant_service.save_plant(self.plant_mock)

        self.plant_repository_mock.save.assert_called_once_with(self.plant_mock)

    def test_get_one_by_binomial(self):
        self.plant_repository_mock.get_one_by_binomial.return_value = self.plant_mock

        plant_service = PlantService(self.plant_repository_mock)

        self.assertEqual(plant_service.get_one_by_binomial(self.plant_mock.binomial), self.plant_mock)
        self.plant_repository_mock.get_one_by_binomial.assert_called_once_with(self.plant_mock.binomial)

    def test_delete_one_by_binomial(self):
        plant_service = PlantService(self.plant_repository_mock)

        plant_service.delete_one_by_binomial(self.plant_mock.binomial)

        self.plant_repository_mock.delete_one_by_binomial.assert_called_once_with(self.plant_mock.binomial)

    def test_get_all(self):
        plants_mock = [
            self.plant_mock
        ]

        self.plant_repository_mock.get_all.return_value = plants_mock

        plant_service = PlantService(self.plant_repository_mock)

        self.assertEqual(plant_service.get_all(), plants_mock)
        self.plant_repository_mock.get_all.assert_called_once()

    def test_create_plant_from_form(self):
        plant_form_mock = Mock()
        plant_form_mock.binomial.data = 'bla'
        plant_form_mock.names.data = 'bla, bla'
        plant_form_mock.cultivars.data = 'bla, bla, bla'
        plant_form_mock.image.data = None

        plant_service = PlantService(self.plant_repository_mock)

        plant = plant_service.create_plant_from_form(plant_form_mock)

        self.assertIsInstance(plant, Plant)
        self.assertEqual(plant.binomial, 'bla')
        self.assertEqual(plant.names, ['bla', 'bla'])
        self.assertEqual(plant.cultivars, ['bla', 'bla', 'bla'])
        self.assertEqual(plant.image, None)


"""Garden plant service module."""
from garden.entities.plant import Plant
from bson import Binary


class PlantService():
    """Plant service."""
    def __init__(self, plant_repository):
        self.plant_repository = plant_repository

    def save_from_form(self, form):
        """Save a plant using the plant form object and return the created plant object."""
        plant = Plant(
            binomial=form.binomial.data,
            names=form.names.data.split(', ') if form.names.data else (),
            cultivars=form.cultivars.data.split(', ') if form.cultivars.data else (),
            image=Binary(form.image.data.read()) if form.image.data else None
        )

        self.plant_repository.save(plant)

        return plant

    def get_one_by_binomial(self, binomial):
        """Return a plant object from a binomial."""
        return self.plant_repository.get_one_by_binomial(binomial)

    def delete_one_by_binomial(self, binomial):
        """Delete a plant object."""
        self.plant_repository.delete_one_by_binomial(binomial)

    def get_all(self):
        """Return a list of all plant objects."""
        return self.plant_repository.get_all()

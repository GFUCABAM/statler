from json import JSONEncoder

from statler_api.models import StatlerModel


class StatlerEncoder(JSONEncoder):
    """A JSONEncoder which can handle StatlerModels with an appropriately impelemented getApiFields() method."""

    def default(self, o):
        """Encode an object: either a StatlerModel instance or an object which is serializable by default."""

        # Specially handle StatlerModels
        if isinstance(o, StatlerModel):
            return o.getApiFields()

        # Otherwise, call the parent implementation.
        else:
            return JSONEncoder.default(self, o)

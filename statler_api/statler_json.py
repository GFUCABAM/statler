from json import JSONEncoder, dumps

from statler_api.models import StatlerModel


def encodeDefault(o):
    """Encode an object: either a StatlerModel instance or an object which is serializable by default."""

    # Specially handle StatlerModels
    if isinstance(o, StatlerModel):
        return o.getApiFields()

    # Otherwise, call the parent implementation.
    else:
        return JSONEncoder.default(o)


def serializeModel(model):
    """Serializes a StatlerModel to JSON."""

    return dumps(model, default=encodeDefault)

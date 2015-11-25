from django.db import models


class StatlerModel:
    """ A base class for all Statler models, extending the Django Model base class with Statler specific functions."""

    def getApiFields(self):
        """ Converts the object to a serializable format
<<<<<<< HEAD
=======

>>>>>>> refs/remotes/origin/dev
        All fields on the returned object must be:
        1. serializable by the builtin JSONDecoder (dictionaries, lists, primitives)
        OR
        2. an instance of StatlerModel
<<<<<<< HEAD
=======

>>>>>>> refs/remotes/origin/dev
        :return: An object (probably a dictionary) includingserializable by the builtin json package
        """

        return {
            "value": self.__str__(),
            "message": "getApi is not implemented on type " + type(self)
        }
<<<<<<< HEAD
=======


>>>>>>> refs/remotes/origin/dev

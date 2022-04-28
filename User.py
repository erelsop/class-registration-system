class User:

    # User class with 2 protected instance variables for: user's ID and user's PIN

    def __init__(self, id, pin):

        # Constructor that takes a user ID and PIN as arguments
        # The instance variables are initialized as (id = id argument) and (pin = pin argument)

        self._id = id
        self._pin = pin

    def get_id(self):

        # This function return the current user's ID

        return self._id

    def get_pin(self):

        # This function returns the current user's PIN

        return self._pin

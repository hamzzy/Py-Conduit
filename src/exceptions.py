class ConduitSDKError(Exception):
    """
    Python Paystack Error
    """
    pass


class MissingAuthKeyError(ConduitSDKError):
    """
    We can't find the authentication key
    """
    pass
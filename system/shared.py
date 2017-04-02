import os
import errno

class LastErrorHolder:
    """
    Support holding of last error
    """
    def __init__(self):
        self.errorText  = ""
        self.__hasError = False

    def clearError(self):
        """
        Clears last error
        :return: None
        """
        self.errorText  = ""
        self.__hasError = False

    def setError(self, errorText):
        """
        Sets new error
        :param errorText: new error text
        :return: False
        """
        self.errorText   = errorText
        self.__hasError  = True

        return False

    @property
    def hasError(self):
        """
        Holds error flag.
        :return: True when have error, otherwise False
        """
        return self.__hasError

def mkdir_p_ex(path):
    try:
        if os.path.exists(path) and os.path.isdir(path):
            return (True, None)

        os.makedirs(path)
        return (True, None)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            return (True, None)
        else:
            return (False, str(exc))
    except Exception as e:
        return (False, str(e))

def mkdir_p(path):
    (ok, stub) = mkdir_p_ex(path)
    return ok
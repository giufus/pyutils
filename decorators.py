from functools import wraps
from time import time


def allows_only(valid_keys):
    """

    :param valid_keys: query params we will not remove
    :return: decorated decorator
    """

    @wraps(valid_keys)
    def allows_only_decorator(fn):
        """
        :param fn: function to decorate
        :return:  decorated function
        """

        @wraps(fn)
        def wrap_func(*args, **kwargs):
            """

            :param args: list of args
            :param kwargs: dict of args
            :return: yes, please
            """
            # this decorator works with event object from aws lambda function
            # event is a dict and is passed to the function as 1st argument
            # event has dict attribute called `queryStringParameters`
            # we will filter `queryStringParameters` in place
            query_params: dict = args[0]['queryStringParameters']
            unwanted = set(query_params) - set(valid_keys)
            for unwanted_key in unwanted:
                del query_params[unwanted_key]
            return fn(*args, **kwargs)

        return wrap_func

    return allows_only_decorator


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f"func '{f.__name__}' response time is {te - ts} seconds")
        return result

    return wrap

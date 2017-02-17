from functools import wraps

def log_shape(func):
    @wraps(func)
    def deco(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info("In %s [%s]", func.__name__, result.shape)
        return result
    return deco

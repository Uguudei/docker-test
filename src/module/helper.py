import logging
import time
import functools


def hello_world():
    """This function is used for testing project structure"""
    print('Hello World!')


def elapsed_time(total_seconds):
    """prints total elapsed time
    Args:
        total_seconds (float): total elapsed seconds
    Returns:
        total_elapsed_time (str): string of hours minutes seconds
    """
    days = int(total_seconds // 86400)
    hours = int(total_seconds // 3600 - total_seconds // 86400 * 24)
    minutes = int(total_seconds // 60 - total_seconds // 3600 * 60)
    seconds = int(total_seconds - total_seconds // 60 * 60)
    ms = int((total_seconds - total_seconds // 60 * 60) % 1 * 1000)
    elapsed_days = '{} d '.format(days) if days >= 1 else ''
    elapsed_hours = '{} hr '.format(hours) if hours >= 1 else ''
    elapsed_minutes = '{} min '.format(minutes) if minutes >= 1 else ''
    elapsed_seconds = '{} sec '.format(seconds) if seconds >= 1 else ''
    elapsed_ms = '{} ms'.format(ms) if minutes == 0 else ''
    return elapsed_days + elapsed_hours + elapsed_minutes + elapsed_seconds + elapsed_ms


def timeit(method):
    """method timer decorator"""
    def timed(*args, **kw):
        start_time = time.time()
        result = method(*args, **kw)
        end_time = time.time()
        elapsed_duration = elapsed_time(time.time() - start_time)
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((end_time - start_time) * 1000)
        else:
            print('{!r:<20} time spent: {}'.format(method.__name__, elapsed_duration))
        return result
    return timed


def logging_timer(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(f.__name__)
        logger.info(f'{f.__name__} initiated')
        start_time = time.time()
        method_result = f(*args, **kwargs)
        elapsed_duration = elapsed_time(time.time() - start_time)
        logger.info(f'{f.__name__} ended - time spent: {elapsed_duration}')
        return method_result

    return wrapper

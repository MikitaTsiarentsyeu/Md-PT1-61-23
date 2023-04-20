import logging
from datetime import datetime

num_input = input('Enter your number:\n')


def init_logger(name: str):
    """
    Logger Creation Function
    """
    global logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    strfmt = '[%(asctime)s | %(name)s | %(levelname)s] > %(message)s'
    datefmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(fmt=strfmt, datefmt=datefmt)

    fh = logging.FileHandler('my_log_file.log', mode='w')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)

    sh = logging.StreamHandler()
    sh.setLevel(logging.ERROR)
    sh.setFormatter(formatter)

    logger.addHandler(sh)
    logger.addHandler(fh)

    logger.info('logger was initialized...\n')


def timeit(func):
    """
    A decorator function that combines multiple functions to extend functionality.
    """
    def wrapper(count):
        logger.info(f'Enter function - {func.__name__}')
        logger.debug(f'Arguments {type(count)} = {count}')
        result = func(count)
        logger.info('Program completed')
        logger.info(f'Program running time - {datetime.now() - start}\n')
        print(
            f'The full progress of the work {func.__name__} is described in the file - my_log_file.log\n')
        return result
    return wrapper


@timeit
def create_list_comp(count_elem: int) -> list:
    """
    The function creates a list of even elements and then writes it to a file.
    """
    with open('create_list_comp.txt', 'w') as f:
        res = [x for x in range(count_elem+1) if x % 2 == 0]
        for i in res:
            f.write(f'{i} ')
    logger.debug(f'Result written to file: {f.name}')
    return res


@timeit
def create_list_for(count_elem: int) -> list:
    """
    The function creates a list of odd elements and then writes it to a file.
    """
    with open('create_list_for.txt', 'w') as f:
        l = []
        for i in range(count_elem+1):
            if i % 2 != 0:
                l.append(i)
                f.write(f'{str(i)} ')
    logger.debug(f'Result written to file: {f.name}')
    return l


try:
    start = datetime.now()
    init_logger('logger')
    create_list_comp(int(num_input))
    create_list_for(int(num_input))
except ValueError as vl:
    logger.exception(f'exception - {vl}.\n')
except:
    logger.exception(f'Error')

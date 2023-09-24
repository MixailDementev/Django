from django.http import HttpResponse
from random import randint
import logging


logger = logging.getLogger(__name__)

def head_tails(request):
    result = 'HEADS' if randint(0, 1) else 'TAILS'
    logger.info(result)
    return HttpResponse(result)

def cube(request):
    edge = randint(1, 6)
    logger.info(f'Edge: {str(edge)}')
    return HttpResponse(f'Edge: {str(edge)}')

def rand_number(request):
    number = randint(1, 100)
    logger.info(f'Number: {str(number)}')
    return HttpResponse(f'Number: {str(number)}')

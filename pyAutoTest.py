# === IMPORTS ==================================================================

import enum
import math
import os
import pyvisa
import string
import typing


# === GLOBAL CONSTANTS =========================================================

_VERSION_MAJOR : int = 0
_VERSION_MINOR : int = 0
_VERSION_UPDATE : int = 1

_VERSION : str = '{0}.{1}.{2}'.format(_VERSION_MAJOR, _VERSION_MINOR, _VERSION_UPDATE)
_FILE_NAME : str = os.path.basename(__file__)


# === FUNCTIONS ================================================================

def _process():
    print('>> {0}()'.format(_process.__name__))
    _processPyVISA()
    print('<< {0}'.format(_process.__name__))
    
def _processPyVISA():
    print('>> {0}()'.format(_processPyVISA.__name__))
    rm = pyvisa.ResourceManager()
    resources = rm.list_resources()
    print('\tresources = {0}'.format(resources))
    for resource in resources:
        instrument = rm.open_resource(resource)
        response = instrument.query('*IDN?')
        print(response)
    print('<< {0}'.format(_processPyVISA.__name__))
    

# === MAIN =====================================================================

if __name__ == '__main__':
    print('{0} version {1}'.format(_FILE_NAME, _VERSION))
    _process()
else:
    print('ERROR: {0} needs to be the calling python module!'.format(_FILE_NAME))

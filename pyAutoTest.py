# === IMPORTS ==================================================================

import datetime
import enum
import math
import os
import pyvisa
import string
import time
import typing


# === GLOBAL CONSTANTS =========================================================

_VERSION_MAJOR : int = 0
_VERSION_MINOR : int = 0
_VERSION_UPDATE : int = 1

_VERSION : str = '{0}.{1}.{2}'.format(_VERSION_MAJOR, _VERSION_MINOR, _VERSION_UPDATE)
_FILE_NAME : str = os.path.basename(__file__)


# === FUNCTIONS ================================================================

def _process():
    print('>> {0}'.format(_process.__name__))
    _processPyVISA()
    print('<< {0}'.format(_process.__name__))
    
def _processPyVISA():
    print('>> {0}'.format(_processPyVISA.__name__))
    rm = pyvisa.ResourceManager()
    resources = rm.list_resources()
    print('\tresources = {0}'.format(resources))
    for resource in resources:
        instrument = rm.open_resource(resource)
        _processInstrument(instrument)
    print('<< {0}'.format(_processPyVISA.__name__))
    
def _processInstrument(instrument : pyvisa.resources.MessageBasedResource):
    print('>> {0}'.format(_processInstrument.__name__))
    idn : str = instrument.query('*IDN?').strip()
    idList : typing.List[str] = idn.split(',')
    print(idn)
    for id in idList:
        if id == 'DG822':
            _processDG822(instrument)
    print('<< {0}'.format(_processInstrument.__name__))
    
def _processDG822(instrument : pyvisa.resources.MessageBasedResource):
    print('>> {0}'.format(_processDG822.__name__))
    instrument.write(':SOUR1:APPL:USER 100,1,2,3')
    instrument.write(':OUTP1 ON')
    output1State = instrument.query(':OUTP1?').strip()
    output2State = instrument.query(':OUTP2?').strip()
    now = datetime.datetime.now()
    print("{0} output[1] = {1}  output[2] = {2}".format(now.strftime('%H:%M:%S'), output1State, output2State))
    time.sleep(5)
    instrument.write(':OUTP1 OFF')
    output1State = instrument.query(':OUTP1?').strip()
    output2State = instrument.query(':OUTP2?').strip()
    now = datetime.datetime.now()
    print("{0} output[1] = {1}  output[2] = {2}".format(now.strftime('%H:%M:%S'), output1State, output2State))
    print('<< {0}'.format(_processDG822.__name__))
    

# === MAIN =====================================================================

if __name__ == '__main__':
    print('{0} version {1}'.format(_FILE_NAME, _VERSION))
    _process()
else:
    print('ERROR: {0} needs to be the calling python module!'.format(_FILE_NAME))

# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_cas')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_cas')
    _cas = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_cas', [dirname(__file__)])
        except ImportError:
            import _cas
            return _cas
        try:
            _mod = imp.load_module('_cas', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _cas = swig_import_helper()
    del swig_import_helper
else:
    import _cas
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

try:
    import weakref
    weakref_proxy = weakref.proxy
except __builtin__.Exception:
    weakref_proxy = lambda x: x


EPICS_VERSION = _cas.EPICS_VERSION
EPICS_REVISION = _cas.EPICS_REVISION
EPICS_MODIFICATION = _cas.EPICS_MODIFICATION
EPICS_PATCH_LEVEL = _cas.EPICS_PATCH_LEVEL
EPICS_DEV_SNAPSHOT = _cas.EPICS_DEV_SNAPSHOT
EPICS_SITE_VERSION = _cas.EPICS_SITE_VERSION
EPICS_VERSION_STRING = _cas.EPICS_VERSION_STRING
epicsReleaseVersion = _cas.epicsReleaseVersion
EPICS_UPDATE_LEVEL = _cas.EPICS_UPDATE_LEVEL
EPICS_CVS_SNAPSHOT = _cas.EPICS_CVS_SNAPSHOT
MAX_ENUM_STRING_SIZE = _cas.MAX_ENUM_STRING_SIZE
MAX_ENUM_STATES = _cas.MAX_ENUM_STATES
M_cas = _cas.M_cas
M_casApp = _cas.M_casApp
S_cas_success = _cas.S_cas_success
S_cas_internal = _cas.S_cas_internal
S_cas_noMemory = _cas.S_cas_noMemory
S_cas_bindFail = _cas.S_cas_bindFail
S_cas_hugeRequest = _cas.S_cas_hugeRequest
S_cas_sendBlocked = _cas.S_cas_sendBlocked
S_cas_badElementCount = _cas.S_cas_badElementCount
S_cas_noConvert = _cas.S_cas_noConvert
S_cas_badWriteType = _cas.S_cas_badWriteType
S_cas_noContext = _cas.S_cas_noContext
S_cas_disconnect = _cas.S_cas_disconnect
S_cas_recvBlocked = _cas.S_cas_recvBlocked
S_cas_badType = _cas.S_cas_badType
S_cas_timerDoesNotExist = _cas.S_cas_timerDoesNotExist
S_cas_badEventType = _cas.S_cas_badEventType
S_cas_badResourceId = _cas.S_cas_badResourceId
S_cas_chanCreateFailed = _cas.S_cas_chanCreateFailed
S_cas_noRead = _cas.S_cas_noRead
S_cas_noWrite = _cas.S_cas_noWrite
S_cas_noEventsSelected = _cas.S_cas_noEventsSelected
S_cas_noFD = _cas.S_cas_noFD
S_cas_badProtocol = _cas.S_cas_badProtocol
S_cas_redundantPost = _cas.S_cas_redundantPost
S_cas_badPVName = _cas.S_cas_badPVName
S_cas_badParameter = _cas.S_cas_badParameter
S_cas_validRequest = _cas.S_cas_validRequest
S_cas_tooManyEvents = _cas.S_cas_tooManyEvents
S_cas_noInterface = _cas.S_cas_noInterface
S_cas_badBounds = _cas.S_cas_badBounds
S_cas_pvAlreadyAttached = _cas.S_cas_pvAlreadyAttached
S_cas_badRequest = _cas.S_cas_badRequest
S_cas_invalidAsynchIO = _cas.S_cas_invalidAsynchIO
S_cas_posponeWhenNonePending = _cas.S_cas_posponeWhenNonePending
S_casApp_success = _cas.S_casApp_success
S_casApp_noMemory = _cas.S_casApp_noMemory
S_casApp_pvNotFound = _cas.S_casApp_pvNotFound
S_casApp_badPVId = _cas.S_casApp_badPVId
S_casApp_noSupport = _cas.S_casApp_noSupport
S_casApp_asyncCompletion = _cas.S_casApp_asyncCompletion
S_casApp_badDimension = _cas.S_casApp_badDimension
S_casApp_canceledAsyncIO = _cas.S_casApp_canceledAsyncIO
S_casApp_outOfBounds = _cas.S_casApp_outOfBounds
S_casApp_undefined = _cas.S_casApp_undefined
S_casApp_postponeAsyncIO = _cas.S_casApp_postponeAsyncIO
aitEnumInvalid = _cas.aitEnumInvalid
aitEnumInt8 = _cas.aitEnumInt8
aitEnumUint8 = _cas.aitEnumUint8
aitEnumInt16 = _cas.aitEnumInt16
aitEnumUint16 = _cas.aitEnumUint16
aitEnumEnum16 = _cas.aitEnumEnum16
aitEnumInt32 = _cas.aitEnumInt32
aitEnumUint32 = _cas.aitEnumUint32
aitEnumFloat32 = _cas.aitEnumFloat32
aitEnumFloat64 = _cas.aitEnumFloat64
aitEnumFixedString = _cas.aitEnumFixedString
aitEnumString = _cas.aitEnumString
aitEnumContainer = _cas.aitEnumContainer
class epicsTimeStamp(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, epicsTimeStamp, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, epicsTimeStamp, name)
    __repr__ = _swig_repr
    __swig_setmethods__["secPastEpoch"] = _cas.epicsTimeStamp_secPastEpoch_set
    __swig_getmethods__["secPastEpoch"] = _cas.epicsTimeStamp_secPastEpoch_get
    if _newclass:
        secPastEpoch = _swig_property(_cas.epicsTimeStamp_secPastEpoch_get, _cas.epicsTimeStamp_secPastEpoch_set)
    __swig_setmethods__["nsec"] = _cas.epicsTimeStamp_nsec_set
    __swig_getmethods__["nsec"] = _cas.epicsTimeStamp_nsec_get
    if _newclass:
        nsec = _swig_property(_cas.epicsTimeStamp_nsec_get, _cas.epicsTimeStamp_nsec_set)

    def __init__(self):
        this = _cas.new_epicsTimeStamp()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _cas.delete_epicsTimeStamp
    __del__ = lambda self: None

    def __str__(self):
        return '%d,%d' % (self.secPastEpoch, self.nsec)

epicsTimeStamp_swigregister = _cas.epicsTimeStamp_swigregister
epicsTimeStamp_swigregister(epicsTimeStamp)


import warnings
import sys
if sys.version_info[0] > 2:
    str2char = lambda x: bytes(str(x),'utf8')
    numerics = (bool, int, float)
    import collections.abc
    is_sequence = lambda x: isinstance(x, collections.abc.Sequence)
else: 
    str2char = str
    numerics = (bool, int, float, long)
    import operator
    is_sequence = operator.isSequenceType

class gdd(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, gdd, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, gdd, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _cas.new_gdd(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def setApplType(self, t):
        return _cas.gdd_setApplType(self, t)

    def applicationType(self):
        return _cas.gdd_applicationType(self)

    def primitiveType(self):
        return _cas.gdd_primitiveType(self)

    def setPrimType(self, t):
        return _cas.gdd_setPrimType(self, t)

    def dimension(self):
        return _cas.gdd_dimension(self)

    def setDimension(self, d, arg3=None):
        return _cas.gdd_setDimension(self, d, arg3)

    def setBound(self, dim_to_set, first, count):
        return _cas.gdd_setBound(self, dim_to_set, first, count)

    def getBound(self, dim_to_get):
        return _cas.gdd_getBound(self, dim_to_get)

    def getDataSizeElements(self):
        return _cas.gdd_getDataSizeElements(self)

    def getTimeStamp(self, *args):
        return _cas.gdd_getTimeStamp(self, *args)

    def setTimeStamp(self, *args):
        return _cas.gdd_setTimeStamp(self, *args)

    def setStatus(self, *args):
        return _cas.gdd_setStatus(self, *args)

    def getStatus(self, *args):
        return _cas.gdd_getStatus(self, *args)

    def setStat(self, arg2):
        return _cas.gdd_setStat(self, arg2)

    def setSevr(self, arg2):
        return _cas.gdd_setSevr(self, arg2)

    def getStat(self):
        return _cas.gdd_getStat(self)

    def getSevr(self):
        return _cas.gdd_getSevr(self)

    def setStatSevr(self, stat, sevr):
        return _cas.gdd_setStatSevr(self, stat, sevr)

    def getStatSevr(self):
        return _cas.gdd_getStatSevr(self)

    def isScalar(self):
        return _cas.gdd_isScalar(self)

    def isContainer(self):
        return _cas.gdd_isContainer(self)

    def isAtomic(self):
        return _cas.gdd_isAtomic(self)

    def clear(self):
        return _cas.gdd_clear(self)

    def dump(self):
        return _cas.gdd_dump(self)

    def reference(self):
        return _cas.gdd_reference(self)

    def unreference(self):
        return _cas.gdd_unreference(self)

    def getConvertNumeric(self):
        return _cas.gdd_getConvertNumeric(self)

    def getConvertString(self):
        return _cas.gdd_getConvertString(self)

    def putConvertNumeric(self, d):
        return _cas.gdd_putConvertNumeric(self, d)

    def putConvertString(self, d):
        return _cas.gdd_putConvertString(self, d)

    def putNumeric(self, d):
        return _cas.gdd_putNumeric(self, d)

    def putString(self, d):
        return _cas.gdd_putString(self, d)

    def putDD(self, dd):
        return _cas.gdd_putDD(self, dd)

    def putCharArray(self, dput):
        return _cas.gdd_putCharArray(self, dput)

    def putNumericArray(self, dput):
        return _cas.gdd_putNumericArray(self, dput)

    def putFStringArray(self, dput):
        return _cas.gdd_putFStringArray(self, dput)

    def putStringArray(self, dput):
        return _cas.gdd_putStringArray(self, dput)

    def putCharDataBuffer(self, dput):
        return _cas.gdd_putCharDataBuffer(self, dput)

    def putShortDataBuffer(self, dput):
        return _cas.gdd_putShortDataBuffer(self, dput)

    def putIntDataBuffer(self, dput):
        return _cas.gdd_putIntDataBuffer(self, dput)

    def putFloatDataBuffer(self, dput):
        return _cas.gdd_putFloatDataBuffer(self, dput)

    def putDoubleDataBuffer(self, dput):
        return _cas.gdd_putDoubleDataBuffer(self, dput)

    def getCharArray(self, dget):
        return _cas.gdd_getCharArray(self, dget)

    def getNumericArray(self, dget):
        return _cas.gdd_getNumericArray(self, dget)

    def getStringArray(self, dget):
        return _cas.gdd_getStringArray(self, dget)

    def __getitem__(self, index):
        return _cas.gdd___getitem__(self, index)
    if _newclass:
        createDD = staticmethod(_cas.gdd_createDD)
    else:
        createDD = _cas.gdd_createDD

    def put(self, value):
        primitiveType = self.primitiveType()
        if type(value) == gdd:
            if value.isAtomic():
                ndims = value.dimension()
                self.setDimension(ndims)
                for dim in range(ndims):
                    status, index, size = value.getBound(dim)
                    self.setBound(dim, index, size)
            self.putDD(value)
        elif isinstance(value, numerics):
            if self.isAtomic():
                self.setBound(0, 0, 1);
                self.putNumericArray([value])
            else:
                self.putConvertNumeric(value)
        elif type(value) == str:
            if self.isScalar():
                self.putConvertString(value)
            else:
    # if atomic then string is converted to char array
                valueChar = [ord(v) for v in value]
    # null terminate
                valueChar.append(0)
                self.setDimension(1)
                self.setBound(0, 0, len(valueChar))
                self.putCharArray(valueChar)
        elif hasattr(value, 'shape'): # numpy data type
            if len(value.shape) == 0: # scalar
                self.putConvertNumeric(value.astype(float))
            else:
                self.setDimension(1)
                self.setBound(0,0,value.size)
                if self.primitiveType() == aitEnumFixedString:
                    self.putFStringArray([str2char(v) for v in value])
                elif self.primitiveType() == aitEnumString:
                    self.putStringArray([str2char(v) for v in value])
                else:
                    if value.dtype in ['i1', 'u1']:
                        self.putCharDataBuffer(value.data)
                    elif value.dtype in ['i2', 'u2']:
                        self.putShortDataBuffer(value.data)
                    elif value.dtype in ['i4', 'u4']:
                        self.putIntDataBuffer(value.data)
                    elif value.dtype == 'f4':
                        self.putFloatDataBuffer(value.data)
                    elif value.dtype == 'f8':
                        self.putDoubleDataBuffer(value.data)
                    else:
                        warnings.warn("gdd does not support data type %s. Conversion is involved." % value.dtype)
                        self.putNumericArray(value) 
        elif is_sequence(value):
            if self.primitiveType() == aitEnumInvalid:
                if isinstance(value[0], numerics):
                    self.setPrimType(aitEnumFloat64)
                else:
                    self.setPrimType(aitEnumString)
            self.setDimension(1)
            self.setBound(0,0,len(value))
            if self.primitiveType() == aitEnumFixedString:
                self.putFStringArray([str2char(v) for v in value])
            elif self.primitiveType() == aitEnumString:
                self.putStringArray([str2char(v) for v in value])
            else:
                self.putNumericArray(value)

    def get(self):
        primitiveType = self.primitiveType()
        if self.isScalar():
            if primitiveType in [aitEnumString, aitEnumFixedString]:
                return self.getConvertString()
            else:
                valueFloat = self.getConvertNumeric()
                if primitiveType in [aitEnumFloat32, aitEnumFloat64]:
                    return valueFloat
                else:
                    valueInt = int(valueFloat)
                    if primitiveType in [aitEnumUint8, aitEnumInt8]:
                        valueChar = valueInt & 0xFF
                        if valueChar == 0:
                            return ''
                        else:
                            return chr(valueChar)
                    else:
                        return valueInt
        else:
            if primitiveType in [aitEnumString, aitEnumFixedString]:
                return self.getStringArray(self.getDataSizeElements())
            elif primitiveType in [aitEnumUint8, aitEnumInt8]:
                valueChar = self.getCharArray(self.getDataSizeElements())
                return ''.join([chr(x) for x in valueChar]).rstrip('\x00')
            else:
                valueFloat =  self.getNumericArray(self.getDataSizeElements())
                if primitiveType in [aitEnumFloat32, aitEnumFloat64]:
                    return valueFloat
                else:
                    return [int(x) for x in valueFloat]


    __swig_destroy__ = _cas.delete_gdd
    __del__ = lambda self: None
gdd_swigregister = _cas.gdd_swigregister
gdd_swigregister(gdd)

def gdd_createDD(app):
    return _cas.gdd_createDD(app)
gdd_createDD = _cas.gdd_createDD

DBE_VALUE = _cas.DBE_VALUE
DBE_ARCHIVE = _cas.DBE_ARCHIVE
DBE_LOG = _cas.DBE_LOG
DBE_ALARM = _cas.DBE_ALARM
DBE_PROPERTY = _cas.DBE_PROPERTY
class caNetAddr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, caNetAddr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, caNetAddr, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _cas.new_caNetAddr()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def stringConvert(self, pString):
        return _cas.caNetAddr_stringConvert(self, pString)
    __swig_destroy__ = _cas.delete_caNetAddr
    __del__ = lambda self: None
caNetAddr_swigregister = _cas.caNetAddr_swigregister
caNetAddr_swigregister(caNetAddr)

pverExistsHere = _cas.pverExistsHere
pverDoesNotExistHere = _cas.pverDoesNotExistHere
pverAsyncCompletion = _cas.pverAsyncCompletion
class caServer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, caServer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, caServer, name)
    __repr__ = _swig_repr

    def __init__(self):
        if self.__class__ == caServer:
            _self = None
        else:
            _self = self
        this = _cas.new_caServer(_self, )
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _cas.delete_caServer
    __del__ = lambda self: None

    def pvExistTest(self, ctx, clientAddress, pPVAliasName):
        return _cas.caServer_pvExistTest(self, ctx, clientAddress, pPVAliasName)

    def pvAttach(self, ctx, pPVAliasName):
        return _cas.caServer_pvAttach(self, ctx, pPVAliasName)

    def registerEvent(self, pName):
        return _cas.caServer_registerEvent(self, pName)

    def valueEventMask(self):
        return _cas.caServer_valueEventMask(self)

    def logEventMask(self):
        return _cas.caServer_logEventMask(self)

    def alarmEventMask(self):
        return _cas.caServer_alarmEventMask(self)

    def setDebugLevel(self, level):
        return _cas.caServer_setDebugLevel(self, level)

    def getDebugLevel(self):
        return _cas.caServer_getDebugLevel(self)

    def show(self, level):
        return _cas.caServer_show(self, level)

    def subscriptionEventsPosted(self):
        return _cas.caServer_subscriptionEventsPosted(self)

    def subscriptionEventsProcessed(self):
        return _cas.caServer_subscriptionEventsProcessed(self)

    def createTimer(self):
        return _cas.caServer_createTimer(self)

    def generateBeaconAnomaly(self):
        return _cas.caServer_generateBeaconAnomaly(self)
    def __disown__(self):
        self.this.disown()
        _cas.disown_caServer(self)
        return weakref_proxy(self)
caServer_swigregister = _cas.caServer_swigregister
caServer_swigregister(caServer)

class casPV(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, casPV, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, casPV, name)
    __repr__ = _swig_repr

    def __init__(self):
        if self.__class__ == casPV:
            _self = None
        else:
            _self = self
        this = _cas.new_casPV(_self, )
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _cas.delete_casPV
    __del__ = lambda self: None

    def show(self, level):
        return _cas.casPV_show(self, level)

    def interestRegister(self):
        return _cas.casPV_interestRegister(self)

    def interestDelete(self):
        return _cas.casPV_interestDelete(self)

    def beginTransaction(self):
        return _cas.casPV_beginTransaction(self)

    def endTransaction(self):
        return _cas.casPV_endTransaction(self)

    def read(self, ctx, prototype):
        return _cas.casPV_read(self, ctx, prototype)

    def write(self, ctx, value):
        return _cas.casPV_write(self, ctx, value)

    def writeNotify(self, ctx, value):
        return _cas.casPV_writeNotify(self, ctx, value)

    def bestExternalType(self):
        return _cas.casPV_bestExternalType(self)

    def maxDimension(self):
        return _cas.casPV_maxDimension(self)

    def maxBound(self, dimension):
        return _cas.casPV_maxBound(self, dimension)

    def destroy(self):
        return _cas.casPV_destroy(self)

    def getName(self):
        return _cas.casPV_getName(self)

    def getCAS(self):
        return _cas.casPV_getCAS(self)
    def __disown__(self):
        self.this.disown()
        _cas.disown_casPV(self)
        return weakref_proxy(self)
casPV_swigregister = _cas.casPV_swigregister
casPV_swigregister(casPV)
EPICS_HAS_WRITENOTIFY = _cas.EPICS_HAS_WRITENOTIFY

class PV(casPV):
    __swig_setmethods__ = {}
    for _s in [casPV]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, PV, name, value)
    __swig_getmethods__ = {}
    for _s in [casPV]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, PV, name)
    __repr__ = _swig_repr

    def __init__(self):
        if self.__class__ == PV:
            _self = None
        else:
            _self = self
        this = _cas.new_PV(_self, )
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _cas.delete_PV
    __del__ = lambda self: None

    def read(self, ctx, protoIn):
        return _cas.PV_read(self, ctx, protoIn)

    def postEvent(self, mask, value):
        return _cas.PV_postEvent(self, mask, value)

    def getValue(self, value):
        return _cas.PV_getValue(self, value)

    def getPrecision(self, prec):
        return _cas.PV_getPrecision(self, prec)

    def getHighLimit(self, hilim):
        return _cas.PV_getHighLimit(self, hilim)

    def getLowLimit(self, lolim):
        return _cas.PV_getLowLimit(self, lolim)

    def getHighAlarmLimit(self, hilim):
        return _cas.PV_getHighAlarmLimit(self, hilim)

    def getLowAlarmLimit(self, lolim):
        return _cas.PV_getLowAlarmLimit(self, lolim)

    def getHighWarnLimit(self, hilim):
        return _cas.PV_getHighWarnLimit(self, hilim)

    def getLowWarnLimit(self, lolim):
        return _cas.PV_getLowWarnLimit(self, lolim)

    def getUnits(self, units):
        return _cas.PV_getUnits(self, units)

    def getEnums(self, enums):
        return _cas.PV_getEnums(self, enums)

    def setAccessSecurityGroup(self, arg2):
        return _cas.PV_setAccessSecurityGroup(self, arg2)

    def startAsyncWrite(self, ctx):
        return _cas.PV_startAsyncWrite(self, ctx)

    def endAsyncWrite(self, status):
        return _cas.PV_endAsyncWrite(self, status)

    def hasAsyncWrite(self):
        return _cas.PV_hasAsyncWrite(self)

    def destroy(self):
        return _cas.PV_destroy(self)
    def __disown__(self):
        self.this.disown()
        _cas.disown_PV(self)
        return weakref_proxy(self)
PV_swigregister = _cas.PV_swigregister
PV_swigregister(PV)

class casChannel(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, casChannel, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, casChannel, name)
    __repr__ = _swig_repr

    def __init__(self, ctx):
        if self.__class__ == casChannel:
            _self = None
        else:
            _self = self
        this = _cas.new_casChannel(_self, ctx)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _cas.delete_casChannel
    __del__ = lambda self: None

    def setOwner(self, pUserName, pHostName):
        return _cas.casChannel_setOwner(self, pUserName, pHostName)

    def readAccess(self):
        return _cas.casChannel_readAccess(self)

    def writeAccess(self):
        return _cas.casChannel_writeAccess(self)

    def confirmationRequested(self):
        return _cas.casChannel_confirmationRequested(self)

    def beginTransaction(self):
        return _cas.casChannel_beginTransaction(self)

    def endTransaction(self):
        return _cas.casChannel_endTransaction(self)

    def read(self, ctx, prototype):
        return _cas.casChannel_read(self, ctx, prototype)

    def write(self, ctx, value):
        return _cas.casChannel_write(self, ctx, value)

    def writeNotify(self, ctx, value):
        return _cas.casChannel_writeNotify(self, ctx, value)

    def show(self, level):
        return _cas.casChannel_show(self, level)

    def destroy(self):
        return _cas.casChannel_destroy(self)
    def __disown__(self):
        self.this.disown()
        _cas.disown_casChannel(self)
        return weakref_proxy(self)
casChannel_swigregister = _cas.casChannel_swigregister
casChannel_swigregister(casChannel)


def asCaStart():
    return _cas.asCaStart()
asCaStart = _cas.asCaStart

def asCaStop():
    return _cas.asCaStop()
asCaStop = _cas.asCaStop

def asInitFile(filename, substitutions):
    return _cas.asInitFile(filename, substitutions)
asInitFile = _cas.asInitFile

def process(delay):
    return _cas.process(delay)
process = _cas.process

_casPV = casPV
casPV = PV

# This file is compatible with both classic and new-style classes.



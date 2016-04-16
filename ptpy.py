'''This module implements Picture Transfer Protocol'''
from construct import (  # noqa
    LengthValueAdapter, Field, Container, ConstAdapter, ULInt8, Struct, Enum,
    LFloat32, UBInt16, UBInt32, Array, Flag, CString, Sequence, Embedded,
    BitStruct, BitField, Padding, FieldError, NoneOf, Byte
)


# Exceptions
class PTPError(Exception):
    pass

# Apparently nobody uses the SessionID field.
SessionID = NoneOf(UBInt32('SessionID'), [0])
TransactionID = UBInt32('TransactionID')
Parameter = BitField('Parameter', 32)
OperationCode = Enum(UBInt16('OperationCode'),
                     Undefined=0x1000,
                     GetDeviceInfo=0x1001,
                     OpenSession=0x1002,
                     CloseSession=0x1003,
                     GetStorageIDs=0x1004,
                     GetStorageInfo=0x1005,
                     GetNumObjects=0x1006,
                     GetObjectHandles=0x1007,
                     GetObjectInfo=0x1008,
                     GetObject=0x1009,
                     GetThumb=0x100A,
                     DeleteObject=0x100B,
                     SendObjectInfo=0x100C,
                     SendObject=0x100D,
                     InitiateCapture=0x100E,
                     FormatStore=0x100F,
                     ResetDevice=0x1010,
                     SelfTest=0x1011,
                     SetObjectProtection=0x1012,
                     PowerDown=0x1013,
                     GetDevicePropDesc=0x1014,
                     GetDevicePropValue=0x1015,
                     SetDevicePropValue=0x1016,
                     ResetDevicePropValue=0x1017,
                     TerminateOpenCapture=0x1018,
                     MoveObject=0x1019,
                     CopyObject=0x101A,
                     GetPartialObject=0x101B,
                     InitiateOpenCapture=0x101C,
                     StartEnumHandles=0x101D,
                     EnumHandles=0x101E,
                     StopEnumHandles=0x101F,
                     GetVendorExtensionMapss=0x1020,
                     GetVendorDeviceInfo=0x1021,
                     GetResizedImageObject=0x1022,
                     GetFilesystemManifest=0x1023,
                     GetStreamInfo=0x1024,
                     GetStream=0x1025,
                     )
ResponseCode = Enum(UBInt16('ResponseCode'),
                    Undefined=0x2000,
                    OK=0x2001,
                    GeneralError=0x2002,
                    SessionNotOpen=0x2003,
                    InvalidTransactionID=0x2004,
                    OperationNotSupported=0x2005,
                    ParameterNotSupported=0x2006,
                    IncompleteTransfer=0x2007,
                    InvalidStorageId=0x2008,
                    InvalidObjectHandle=0x2009,
                    DevicePropNotSupported=0x200A,
                    InvalidObjectFormatCode=0x200B,
                    StoreFull=0x200C,
                    ObjectWriteProtected=0x200D,
                    StoreReadOnly=0x200E,
                    AccessDenied=0x200F,
                    NoThumbnailPresent=0x2010,
                    SelfTestFailed=0x2011,
                    PartialDeletion=0x2012,
                    StoreNotAvailable=0x2013,
                    SpecificationByFormatUnsupported=0x2014,
                    NoValidObjectInfo=0x2015,
                    InvalidCodeFormat=0x2016,
                    UnknownVendorCode=0x2017,
                    CaptureAlreadyTerminated=0x2018,
                    DeviceBusy=0x2019,
                    InvalidParentObject=0x201A,
                    InvalidDevicePropFormat=0x201B,
                    InvalidDevicePropValue=0x201C,
                    InvalidParameter=0x201D,
                    SessionAlreadyOpened=0x201E,
                    TransactionCanceled=0x201F,
                    SpecificationOfDestinationUnsupported=0x2020,
                    InvalidEnumHandle=0x2021,
                    NoStreamEnabled=0x2022,
                    InvalidDataset=0x2023,
                    )
EventCode = Enum(UBInt16('EventCode'),
                 Undefined=0x4000,
                 CancelTransaction=0x4001,
                 ObjectAdded=0x4002,
                 ObjectRemoved=0x4003,
                 StoreAdded=0x4004,
                 StoreRemoved=0x4005,
                 DevicePropChanged=0x4006,
                 ObjectInfoChanged=0x4007,
                 DeviceInfoChanged=0x4008,
                 RequestObjectTransfer=0x4009,
                 StoreFull=0x400A,
                 DeviceReset=0x400B,
                 StorageInfoChanged=0x400C,
                 CaptureComplete=0x400D,
                 UnreportedStatus=0x400E,
                 )
Event = Struct('Event',
               EventCode,
               SessionID,
               TransactionID,
               Array(3, Parameter),
               )
Response = Struct('Response',
                  ResponseCode,
                  SessionID,
                  TransactionID,
                  Array(5, Parameter),
                  )
Operation = Struct('Operation',
                   OperationCode,
                   SessionID,
                   TransactionID,
                   Array(5, Parameter),
                   )

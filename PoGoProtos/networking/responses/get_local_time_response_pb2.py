# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/get_local_time_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/get_local_time_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n=pogoprotos/networking/responses/get_local_time_response.proto\x12\x1fpogoprotos.networking.responses\"\xb7\x03\n\x14GetLocalTimeResponse\x12L\n\x06status\x18\x01 \x01(\x0e\x32<.pogoprotos.networking.responses.GetLocalTimeResponse.Status\x12T\n\x0blocal_times\x18\x02 \x03(\x0b\x32?.pogoprotos.networking.responses.GetLocalTimeResponse.LocalTime\x1a\xc5\x01\n\tLocalTime\x12\x14\n\x0ctimestamp_ms\x18\x01 \x01(\x03\x12\x0c\n\x04year\x18\x02 \x01(\x05\x12\r\n\x05month\x18\x03 \x01(\x05\x12\x14\n\x0c\x64\x61y_of_month\x18\x04 \x01(\x05\x12\x13\n\x0b\x64\x61y_of_week\x18\x05 \x01(\x05\x12\r\n\x05hours\x18\x06 \x01(\x05\x12\x0f\n\x07minutes\x18\x07 \x01(\x05\x12\x0f\n\x07seconds\x18\x08 \x01(\x05\x12\x14\n\x0cmilliseconds\x18\t \x01(\x05\x12\x13\n\x0btimezone_id\x18\n \x01(\t\"3\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x62\x06proto3')
)



_GETLOCALTIMERESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.responses.GetLocalTimeResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_UNKNOWN', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=487,
  serialized_end=538,
)
_sym_db.RegisterEnumDescriptor(_GETLOCALTIMERESPONSE_STATUS)


_GETLOCALTIMERESPONSE_LOCALTIME = _descriptor.Descriptor(
  name='LocalTime',
  full_name='pogoprotos.networking.responses.GetLocalTimeResponse.LocalTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp_ms', full_name='pogoprotos.networking.responses.GetLocalTimeResponse.LocalTime.timestamp_ms', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='year', full_name='pogoprotos.networking.responses.GetLocalTimeResponse.LocalTime.year', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month', full_name='pogoprotos.networking.responses.GetLocalTimeResponse.LocalTime.month', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day_of_month', full_name='pogoprotos.networking.responses.GetLocalTimeResponse.LocalTime.day_of_month', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day_of_week', full_name='pogoprotos.networking.responses.GetLocalTimeResponse.LocalTime.day_of_week', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hours', full_name='pogoprotos.networking.responses.GetLocalTimeResponse.LocalTime.hours', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minutes', full_name='pogoprotos.networking.responses.GetLocalTimeResponse.LocalTime.minutes', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seconds', full_name='pogoprotos.networking.responses.GetLocalTimeResponse.LocalTime.seconds', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='milliseconds', full_name='pogoprotos.networking.responses.GetLocalTimeResponse.LocalTime.milliseconds', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timezone_id', full_name='pogoprotos.networking.responses.GetLocalTimeResponse.LocalTime.timezone_id', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=288,
  serialized_end=485,
)

_GETLOCALTIMERESPONSE = _descriptor.Descriptor(
  name='GetLocalTimeResponse',
  full_name='pogoprotos.networking.responses.GetLocalTimeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.GetLocalTimeResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_times', full_name='pogoprotos.networking.responses.GetLocalTimeResponse.local_times', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETLOCALTIMERESPONSE_LOCALTIME, ],
  enum_types=[
    _GETLOCALTIMERESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=538,
)

_GETLOCALTIMERESPONSE_LOCALTIME.containing_type = _GETLOCALTIMERESPONSE
_GETLOCALTIMERESPONSE.fields_by_name['status'].enum_type = _GETLOCALTIMERESPONSE_STATUS
_GETLOCALTIMERESPONSE.fields_by_name['local_times'].message_type = _GETLOCALTIMERESPONSE_LOCALTIME
_GETLOCALTIMERESPONSE_STATUS.containing_type = _GETLOCALTIMERESPONSE
DESCRIPTOR.message_types_by_name['GetLocalTimeResponse'] = _GETLOCALTIMERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetLocalTimeResponse = _reflection.GeneratedProtocolMessageType('GetLocalTimeResponse', (_message.Message,), dict(

  LocalTime = _reflection.GeneratedProtocolMessageType('LocalTime', (_message.Message,), dict(
    DESCRIPTOR = _GETLOCALTIMERESPONSE_LOCALTIME,
    __module__ = 'pogoprotos.networking.responses.get_local_time_response_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetLocalTimeResponse.LocalTime)
    ))
  ,
  DESCRIPTOR = _GETLOCALTIMERESPONSE,
  __module__ = 'pogoprotos.networking.responses.get_local_time_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetLocalTimeResponse)
  ))
_sym_db.RegisterMessage(GetLocalTimeResponse)
_sym_db.RegisterMessage(GetLocalTimeResponse.LocalTime)


# @@protoc_insertion_point(module_scope)

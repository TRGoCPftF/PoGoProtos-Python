# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/platform_request.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.networking.platform import platform_request_type_pb2 as pogoprotos_dot_networking_dot_platform_dot_platform__request__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/platform/platform_request.proto',
  package='pogoprotos.networking.platform',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n5pogoprotos/networking/platform/platform_request.proto\x12\x1epogoprotos.networking.platform\x1a:pogoprotos/networking/platform/platform_request_type.proto\"~\n\x0fPlatformRequest\x12R\n\x15platform_request_type\x18\x01 \x01(\x0e\x32\x33.pogoprotos.networking.platform.PlatformRequestType\x12\x17\n\x0frequest_message\x18\x02 \x01(\x0c\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_networking_dot_platform_dot_platform__request__type__pb2.DESCRIPTOR,])




_PLATFORMREQUEST = _descriptor.Descriptor(
  name='PlatformRequest',
  full_name='pogoprotos.networking.platform.PlatformRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='platform_request_type', full_name='pogoprotos.networking.platform.PlatformRequest.platform_request_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_message', full_name='pogoprotos.networking.platform.PlatformRequest.request_message', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=149,
  serialized_end=275,
)

_PLATFORMREQUEST.fields_by_name['platform_request_type'].enum_type = pogoprotos_dot_networking_dot_platform_dot_platform__request__type__pb2._PLATFORMREQUESTTYPE
DESCRIPTOR.message_types_by_name['PlatformRequest'] = _PLATFORMREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlatformRequest = _reflection.GeneratedProtocolMessageType('PlatformRequest', (_message.Message,), dict(
  DESCRIPTOR = _PLATFORMREQUEST,
  __module__ = 'pogoprotos.networking.platform.platform_request_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.PlatformRequest)
  ))
_sym_db.RegisterMessage(PlatformRequest)


# @@protoc_insertion_point(module_scope)
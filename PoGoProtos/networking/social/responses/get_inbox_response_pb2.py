# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/social/responses/get_inbox_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.inbox import client_inbox_pb2 as pogoprotos_dot_data_dot_inbox_dot_client__inbox__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/social/responses/get_inbox_response.proto',
  package='pogoprotos.networking.social.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n?pogoprotos/networking/social/responses/get_inbox_response.proto\x12&pogoprotos.networking.social.responses\x1a(pogoprotos/data/inbox/client_inbox.proto\"\xc5\x01\n\x10GetInboxResponse\x12O\n\x06result\x18\x01 \x01(\x0e\x32?.pogoprotos.networking.social.responses.GetInboxResponse.Result\x12\x31\n\x05inbox\x18\x02 \x01(\x0b\x32\".pogoprotos.data.inbox.ClientInbox\"-\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07\x46\x41ILURE\x10\x02\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_inbox_dot_client__inbox__pb2.DESCRIPTOR,])



_GETINBOXRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.social.responses.GetInboxResponse.Result',
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
      name='FAILURE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=302,
  serialized_end=347,
)
_sym_db.RegisterEnumDescriptor(_GETINBOXRESPONSE_RESULT)


_GETINBOXRESPONSE = _descriptor.Descriptor(
  name='GetInboxResponse',
  full_name='pogoprotos.networking.social.responses.GetInboxResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.social.responses.GetInboxResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inbox', full_name='pogoprotos.networking.social.responses.GetInboxResponse.inbox', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETINBOXRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=347,
)

_GETINBOXRESPONSE.fields_by_name['result'].enum_type = _GETINBOXRESPONSE_RESULT
_GETINBOXRESPONSE.fields_by_name['inbox'].message_type = pogoprotos_dot_data_dot_inbox_dot_client__inbox__pb2._CLIENTINBOX
_GETINBOXRESPONSE_RESULT.containing_type = _GETINBOXRESPONSE
DESCRIPTOR.message_types_by_name['GetInboxResponse'] = _GETINBOXRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetInboxResponse = _reflection.GeneratedProtocolMessageType('GetInboxResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETINBOXRESPONSE,
  __module__ = 'pogoprotos.networking.social.responses.get_inbox_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.social.responses.GetInboxResponse)
  ))
_sym_db.RegisterMessage(GetInboxResponse)


# @@protoc_insertion_point(module_scope)

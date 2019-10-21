# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/social/responses/is_my_friend_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/social/responses/is_my_friend_response.proto',
  package='pogoprotos.networking.social.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nBpogoprotos/networking/social/responses/is_my_friend_response.proto\x12&pogoprotos.networking.social.responses\"\xd3\x01\n\x12IsMyFriendResponse\x12Q\n\x06result\x18\x01 \x01(\x0e\x32\x41.pogoprotos.networking.social.responses.IsMyFriendResponse.Result\x12\x11\n\tis_friend\x18\x02 \x01(\x08\"W\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x12\"\n\x1e\x45RROR_PLAYER_NOT_FOUND_DELETED\x10\x03\x62\x06proto3')
)



_ISMYFRIENDRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.social.responses.IsMyFriendResponse.Result',
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
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_NOT_FOUND_DELETED', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=235,
  serialized_end=322,
)
_sym_db.RegisterEnumDescriptor(_ISMYFRIENDRESPONSE_RESULT)


_ISMYFRIENDRESPONSE = _descriptor.Descriptor(
  name='IsMyFriendResponse',
  full_name='pogoprotos.networking.social.responses.IsMyFriendResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.social.responses.IsMyFriendResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_friend', full_name='pogoprotos.networking.social.responses.IsMyFriendResponse.is_friend', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ISMYFRIENDRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=322,
)

_ISMYFRIENDRESPONSE.fields_by_name['result'].enum_type = _ISMYFRIENDRESPONSE_RESULT
_ISMYFRIENDRESPONSE_RESULT.containing_type = _ISMYFRIENDRESPONSE
DESCRIPTOR.message_types_by_name['IsMyFriendResponse'] = _ISMYFRIENDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IsMyFriendResponse = _reflection.GeneratedProtocolMessageType('IsMyFriendResponse', (_message.Message,), dict(
  DESCRIPTOR = _ISMYFRIENDRESPONSE,
  __module__ = 'pogoprotos.networking.social.responses.is_my_friend_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.social.responses.IsMyFriendResponse)
  ))
_sym_db.RegisterMessage(IsMyFriendResponse)


# @@protoc_insertion_point(module_scope)

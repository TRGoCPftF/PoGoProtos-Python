# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/reassign_player_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/reassign_player_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n>pogoprotos/networking/responses/reassign_player_response.proto\x12\x1fpogoprotos.networking.responses\"\xa7\x01\n\x16ReassignPlayerResponse\x12N\n\x06result\x18\x01 \x01(\x0e\x32>.pogoprotos.networking.responses.ReassignPlayerResponse.Result\x12\x1b\n\x13reassigned_instance\x18\x02 \x01(\x05\" \n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x62\x06proto3')
)



_REASSIGNPLAYERRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.ReassignPlayerResponse.Result',
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
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=235,
  serialized_end=267,
)
_sym_db.RegisterEnumDescriptor(_REASSIGNPLAYERRESPONSE_RESULT)


_REASSIGNPLAYERRESPONSE = _descriptor.Descriptor(
  name='ReassignPlayerResponse',
  full_name='pogoprotos.networking.responses.ReassignPlayerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.ReassignPlayerResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reassigned_instance', full_name='pogoprotos.networking.responses.ReassignPlayerResponse.reassigned_instance', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REASSIGNPLAYERRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=267,
)

_REASSIGNPLAYERRESPONSE.fields_by_name['result'].enum_type = _REASSIGNPLAYERRESPONSE_RESULT
_REASSIGNPLAYERRESPONSE_RESULT.containing_type = _REASSIGNPLAYERRESPONSE
DESCRIPTOR.message_types_by_name['ReassignPlayerResponse'] = _REASSIGNPLAYERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReassignPlayerResponse = _reflection.GeneratedProtocolMessageType('ReassignPlayerResponse', (_message.Message,), dict(
  DESCRIPTOR = _REASSIGNPLAYERRESPONSE,
  __module__ = 'pogoprotos.networking.responses.reassign_player_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.ReassignPlayerResponse)
  ))
_sym_db.RegisterMessage(ReassignPlayerResponse)


# @@protoc_insertion_point(module_scope)

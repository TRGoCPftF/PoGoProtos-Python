# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/invasion_complete_dialogue_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.map.fort import invasion_status_pb2 as pogoprotos_dot_map_dot_fort_dot_invasion__status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/invasion_complete_dialogue_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nIpogoprotos/networking/responses/invasion_complete_dialogue_response.proto\x12\x1fpogoprotos.networking.responses\x1a)pogoprotos/map/fort/invasion_status.proto\"^\n InvasionCompleteDialogueResponse\x12:\n\x06status\x18\x01 \x01(\x0e\x32*.pogoprotos.map.fort.InvasionStatus.Statusb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_map_dot_fort_dot_invasion__status__pb2.DESCRIPTOR,])




_INVASIONCOMPLETEDIALOGUERESPONSE = _descriptor.Descriptor(
  name='InvasionCompleteDialogueResponse',
  full_name='pogoprotos.networking.responses.InvasionCompleteDialogueResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.InvasionCompleteDialogueResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=153,
  serialized_end=247,
)

_INVASIONCOMPLETEDIALOGUERESPONSE.fields_by_name['status'].enum_type = pogoprotos_dot_map_dot_fort_dot_invasion__status__pb2._INVASIONSTATUS_STATUS
DESCRIPTOR.message_types_by_name['InvasionCompleteDialogueResponse'] = _INVASIONCOMPLETEDIALOGUERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InvasionCompleteDialogueResponse = _reflection.GeneratedProtocolMessageType('InvasionCompleteDialogueResponse', (_message.Message,), dict(
  DESCRIPTOR = _INVASIONCOMPLETEDIALOGUERESPONSE,
  __module__ = 'pogoprotos.networking.responses.invasion_complete_dialogue_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.InvasionCompleteDialogueResponse)
  ))
_sym_db.RegisterMessage(InvasionCompleteDialogueResponse)


# @@protoc_insertion_point(module_scope)

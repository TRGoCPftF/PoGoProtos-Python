# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/complete_snapshot_session_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/complete_snapshot_session_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nHpogoprotos/networking/responses/complete_snapshot_session_response.proto\x12\x1fpogoprotos.networking.responses\"\xd0\x01\n\x1f\x43ompleteSnapshotSessionResponse\x12W\n\x06status\x18\x01 \x01(\x0e\x32G.pogoprotos.networking.responses.CompleteSnapshotSessionResponse.Status\"T\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1f\n\x1b\x45RROR_PHOTO_POKEMON_INVALID\x10\x02\x12\x11\n\rERROR_UNKNOWN\x10\x03\x62\x06proto3')
)



_COMPLETESNAPSHOTSESSIONRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.responses.CompleteSnapshotSessionResponse.Status',
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
      name='ERROR_PHOTO_POKEMON_INVALID', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_UNKNOWN', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=234,
  serialized_end=318,
)
_sym_db.RegisterEnumDescriptor(_COMPLETESNAPSHOTSESSIONRESPONSE_STATUS)


_COMPLETESNAPSHOTSESSIONRESPONSE = _descriptor.Descriptor(
  name='CompleteSnapshotSessionResponse',
  full_name='pogoprotos.networking.responses.CompleteSnapshotSessionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.CompleteSnapshotSessionResponse.status', index=0,
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
    _COMPLETESNAPSHOTSESSIONRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=318,
)

_COMPLETESNAPSHOTSESSIONRESPONSE.fields_by_name['status'].enum_type = _COMPLETESNAPSHOTSESSIONRESPONSE_STATUS
_COMPLETESNAPSHOTSESSIONRESPONSE_STATUS.containing_type = _COMPLETESNAPSHOTSESSIONRESPONSE
DESCRIPTOR.message_types_by_name['CompleteSnapshotSessionResponse'] = _COMPLETESNAPSHOTSESSIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CompleteSnapshotSessionResponse = _reflection.GeneratedProtocolMessageType('CompleteSnapshotSessionResponse', (_message.Message,), dict(
  DESCRIPTOR = _COMPLETESNAPSHOTSESSIONRESPONSE,
  __module__ = 'pogoprotos.networking.responses.complete_snapshot_session_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.CompleteSnapshotSessionResponse)
  ))
_sym_db.RegisterMessage(CompleteSnapshotSessionResponse)


# @@protoc_insertion_point(module_scope)

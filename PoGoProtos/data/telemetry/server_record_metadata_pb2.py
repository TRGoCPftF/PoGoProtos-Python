# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/server_record_metadata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/server_record_metadata.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n6pogoprotos/data/telemetry/server_record_metadata.proto\x12\x19pogoprotos.data.telemetry\"\x84\x01\n\x14ServerRecordMetadata\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x16\n\x0etelemetry_name\x18\x02 \x01(\t\x12\x12\n\nsession_id\x18\x03 \x01(\t\x12\x12\n\nrequest_id\x18\x04 \x01(\t\x12\x1b\n\x13server_timestamp_ms\x18\x05 \x01(\x03\x62\x06proto3')
)




_SERVERRECORDMETADATA = _descriptor.Descriptor(
  name='ServerRecordMetadata',
  full_name='pogoprotos.data.telemetry.ServerRecordMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='pogoprotos.data.telemetry.ServerRecordMetadata.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='telemetry_name', full_name='pogoprotos.data.telemetry.ServerRecordMetadata.telemetry_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='pogoprotos.data.telemetry.ServerRecordMetadata.session_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='pogoprotos.data.telemetry.ServerRecordMetadata.request_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='server_timestamp_ms', full_name='pogoprotos.data.telemetry.ServerRecordMetadata.server_timestamp_ms', index=4,
      number=5, type=3, cpp_type=2, label=1,
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
  serialized_start=86,
  serialized_end=218,
)

DESCRIPTOR.message_types_by_name['ServerRecordMetadata'] = _SERVERRECORDMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServerRecordMetadata = _reflection.GeneratedProtocolMessageType('ServerRecordMetadata', (_message.Message,), dict(
  DESCRIPTOR = _SERVERRECORDMETADATA,
  __module__ = 'pogoprotos.data.telemetry.server_record_metadata_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.ServerRecordMetadata)
  ))
_sym_db.RegisterMessage(ServerRecordMetadata)


# @@protoc_insertion_point(module_scope)

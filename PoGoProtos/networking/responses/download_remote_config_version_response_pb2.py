# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/download_remote_config_version_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/download_remote_config_version_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nMpogoprotos/networking/responses/download_remote_config_version_response.proto\x12\x1fpogoprotos.networking.responses\"\x83\x02\n#DownloadRemoteConfigVersionResponse\x12[\n\x06result\x18\x01 \x01(\x0e\x32K.pogoprotos.networking.responses.DownloadRemoteConfigVersionResponse.Result\x12#\n\x1bitem_templates_timestamp_ms\x18\x02 \x01(\x04\x12!\n\x19\x61sset_digest_timestamp_ms\x18\x03 \x01(\x04\x12\x15\n\rexperiment_id\x18\x04 \x03(\r\" \n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x62\x06proto3')
)



_DOWNLOADREMOTECONFIGVERSIONRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.DownloadRemoteConfigVersionResponse.Result',
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
  serialized_start=342,
  serialized_end=374,
)
_sym_db.RegisterEnumDescriptor(_DOWNLOADREMOTECONFIGVERSIONRESPONSE_RESULT)


_DOWNLOADREMOTECONFIGVERSIONRESPONSE = _descriptor.Descriptor(
  name='DownloadRemoteConfigVersionResponse',
  full_name='pogoprotos.networking.responses.DownloadRemoteConfigVersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.DownloadRemoteConfigVersionResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_templates_timestamp_ms', full_name='pogoprotos.networking.responses.DownloadRemoteConfigVersionResponse.item_templates_timestamp_ms', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asset_digest_timestamp_ms', full_name='pogoprotos.networking.responses.DownloadRemoteConfigVersionResponse.asset_digest_timestamp_ms', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='experiment_id', full_name='pogoprotos.networking.responses.DownloadRemoteConfigVersionResponse.experiment_id', index=3,
      number=4, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DOWNLOADREMOTECONFIGVERSIONRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=374,
)

_DOWNLOADREMOTECONFIGVERSIONRESPONSE.fields_by_name['result'].enum_type = _DOWNLOADREMOTECONFIGVERSIONRESPONSE_RESULT
_DOWNLOADREMOTECONFIGVERSIONRESPONSE_RESULT.containing_type = _DOWNLOADREMOTECONFIGVERSIONRESPONSE
DESCRIPTOR.message_types_by_name['DownloadRemoteConfigVersionResponse'] = _DOWNLOADREMOTECONFIGVERSIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DownloadRemoteConfigVersionResponse = _reflection.GeneratedProtocolMessageType('DownloadRemoteConfigVersionResponse', (_message.Message,), dict(
  DESCRIPTOR = _DOWNLOADREMOTECONFIGVERSIONRESPONSE,
  __module__ = 'pogoprotos.networking.responses.download_remote_config_version_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.DownloadRemoteConfigVersionResponse)
  ))
_sym_db.RegisterMessage(DownloadRemoteConfigVersionResponse)


# @@protoc_insertion_point(module_scope)

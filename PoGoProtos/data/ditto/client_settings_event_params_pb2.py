# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/ditto/client_settings_event_params.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/ditto/client_settings_event_params.proto',
  package='pogoprotos.data.ditto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n8pogoprotos/data/ditto/client_settings_event_params.proto\x12\x15pogoprotos.data.ditto\"-\n\x19\x43lientSettingsEventParams\x12\x10\n\x08payloads\x18\x01 \x01(\x0c\x62\x06proto3')
)




_CLIENTSETTINGSEVENTPARAMS = _descriptor.Descriptor(
  name='ClientSettingsEventParams',
  full_name='pogoprotos.data.ditto.ClientSettingsEventParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payloads', full_name='pogoprotos.data.ditto.ClientSettingsEventParams.payloads', index=0,
      number=1, type=12, cpp_type=9, label=1,
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
  serialized_start=83,
  serialized_end=128,
)

DESCRIPTOR.message_types_by_name['ClientSettingsEventParams'] = _CLIENTSETTINGSEVENTPARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientSettingsEventParams = _reflection.GeneratedProtocolMessageType('ClientSettingsEventParams', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTSETTINGSEVENTPARAMS,
  __module__ = 'pogoprotos.data.ditto.client_settings_event_params_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.ditto.ClientSettingsEventParams)
  ))
_sym_db.RegisterMessage(ClientSettingsEventParams)


# @@protoc_insertion_point(module_scope)

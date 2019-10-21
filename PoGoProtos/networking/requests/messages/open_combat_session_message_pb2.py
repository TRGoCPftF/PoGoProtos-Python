# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/open_combat_session_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/open_combat_session_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nIpogoprotos/networking/requests/messages/open_combat_session_message.proto\x12\'pogoprotos.networking.requests.messages\"n\n\x18OpenCombatSessionMessage\x12\x11\n\tcombat_id\x18\x01 \x01(\t\x12\x1c\n\x14\x61ttacking_pokemon_id\x18\x02 \x03(\x06\x12!\n\x19\x63ombat_league_template_id\x18\x03 \x01(\tb\x06proto3')
)




_OPENCOMBATSESSIONMESSAGE = _descriptor.Descriptor(
  name='OpenCombatSessionMessage',
  full_name='pogoprotos.networking.requests.messages.OpenCombatSessionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='combat_id', full_name='pogoprotos.networking.requests.messages.OpenCombatSessionMessage.combat_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attacking_pokemon_id', full_name='pogoprotos.networking.requests.messages.OpenCombatSessionMessage.attacking_pokemon_id', index=1,
      number=2, type=6, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='combat_league_template_id', full_name='pogoprotos.networking.requests.messages.OpenCombatSessionMessage.combat_league_template_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=118,
  serialized_end=228,
)

DESCRIPTOR.message_types_by_name['OpenCombatSessionMessage'] = _OPENCOMBATSESSIONMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OpenCombatSessionMessage = _reflection.GeneratedProtocolMessageType('OpenCombatSessionMessage', (_message.Message,), dict(
  DESCRIPTOR = _OPENCOMBATSESSIONMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.open_combat_session_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.OpenCombatSessionMessage)
  ))
_sym_db.RegisterMessage(OpenCombatSessionMessage)


# @@protoc_insertion_point(module_scope)

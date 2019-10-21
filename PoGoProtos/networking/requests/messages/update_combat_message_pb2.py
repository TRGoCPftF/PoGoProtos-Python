# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/update_combat_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.combat import combat_action_pb2 as pogoprotos_dot_data_dot_combat_dot_combat__action__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/update_combat_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nCpogoprotos/networking/requests/messages/update_combat_message.proto\x12\'pogoprotos.networking.requests.messages\x1a*pogoprotos/data/combat/combat_action.proto\"^\n\x13UpdateCombatMessage\x12\x11\n\tcombat_id\x18\x01 \x01(\t\x12\x34\n\x06\x61\x63tion\x18\x02 \x01(\x0b\x32$.pogoprotos.data.combat.CombatActionb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_combat_dot_combat__action__pb2.DESCRIPTOR,])




_UPDATECOMBATMESSAGE = _descriptor.Descriptor(
  name='UpdateCombatMessage',
  full_name='pogoprotos.networking.requests.messages.UpdateCombatMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='combat_id', full_name='pogoprotos.networking.requests.messages.UpdateCombatMessage.combat_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='pogoprotos.networking.requests.messages.UpdateCombatMessage.action', index=1,
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
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=156,
  serialized_end=250,
)

_UPDATECOMBATMESSAGE.fields_by_name['action'].message_type = pogoprotos_dot_data_dot_combat_dot_combat__action__pb2._COMBATACTION
DESCRIPTOR.message_types_by_name['UpdateCombatMessage'] = _UPDATECOMBATMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateCombatMessage = _reflection.GeneratedProtocolMessageType('UpdateCombatMessage', (_message.Message,), dict(
  DESCRIPTOR = _UPDATECOMBATMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.update_combat_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.UpdateCombatMessage)
  ))
_sym_db.RegisterMessage(UpdateCombatMessage)


# @@protoc_insertion_point(module_scope)

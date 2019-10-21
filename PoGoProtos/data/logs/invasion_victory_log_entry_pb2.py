# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/logs/invasion_victory_log_entry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory import loot_pb2 as pogoprotos_dot_inventory_dot_loot__pb2
from pogoprotos.data import enum_wrapper_pb2 as pogoprotos_dot_data_dot_enum__wrapper__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/logs/invasion_victory_log_entry.proto',
  package='pogoprotos.data.logs',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n5pogoprotos/data/logs/invasion_victory_log_entry.proto\x12\x14pogoprotos.data.logs\x1a\x1fpogoprotos/inventory/loot.proto\x1a\"pogoprotos/data/enum_wrapper.proto\"\x8c\x01\n\x17InvasionVictoryLogEntry\x12+\n\x07rewards\x18\x01 \x01(\x0b\x32\x1a.pogoprotos.inventory.Loot\x12\x44\n\x0cinvasion_npc\x18\x02 \x01(\x0e\x32..pogoprotos.data.EnumWrapper.InvasionCharacterb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_loot__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_enum__wrapper__pb2.DESCRIPTOR,])




_INVASIONVICTORYLOGENTRY = _descriptor.Descriptor(
  name='InvasionVictoryLogEntry',
  full_name='pogoprotos.data.logs.InvasionVictoryLogEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rewards', full_name='pogoprotos.data.logs.InvasionVictoryLogEntry.rewards', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='invasion_npc', full_name='pogoprotos.data.logs.InvasionVictoryLogEntry.invasion_npc', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=149,
  serialized_end=289,
)

_INVASIONVICTORYLOGENTRY.fields_by_name['rewards'].message_type = pogoprotos_dot_inventory_dot_loot__pb2._LOOT
_INVASIONVICTORYLOGENTRY.fields_by_name['invasion_npc'].enum_type = pogoprotos_dot_data_dot_enum__wrapper__pb2._ENUMWRAPPER_INVASIONCHARACTER
DESCRIPTOR.message_types_by_name['InvasionVictoryLogEntry'] = _INVASIONVICTORYLOGENTRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InvasionVictoryLogEntry = _reflection.GeneratedProtocolMessageType('InvasionVictoryLogEntry', (_message.Message,), dict(
  DESCRIPTOR = _INVASIONVICTORYLOGENTRY,
  __module__ = 'pogoprotos.data.logs.invasion_victory_log_entry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.logs.InvasionVictoryLogEntry)
  ))
_sym_db.RegisterMessage(InvasionVictoryLogEntry)


# @@protoc_insertion_point(module_scope)

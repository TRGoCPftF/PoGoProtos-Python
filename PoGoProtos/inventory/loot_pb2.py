# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/inventory/loot.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory import loot_item_pb2 as pogoprotos_dot_inventory_dot_loot__item__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/inventory/loot.proto',
  package='pogoprotos.inventory',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1fpogoprotos/inventory/loot.proto\x12\x14pogoprotos.inventory\x1a$pogoprotos/inventory/loot_item.proto\"9\n\x04Loot\x12\x31\n\tloot_item\x18\x01 \x03(\x0b\x32\x1e.pogoprotos.inventory.LootItemb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_loot__item__pb2.DESCRIPTOR,])




_LOOT = _descriptor.Descriptor(
  name='Loot',
  full_name='pogoprotos.inventory.Loot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='loot_item', full_name='pogoprotos.inventory.Loot.loot_item', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=95,
  serialized_end=152,
)

_LOOT.fields_by_name['loot_item'].message_type = pogoprotos_dot_inventory_dot_loot__item__pb2._LOOTITEM
DESCRIPTOR.message_types_by_name['Loot'] = _LOOT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Loot = _reflection.GeneratedProtocolMessageType('Loot', (_message.Message,), dict(
  DESCRIPTOR = _LOOT,
  __module__ = 'pogoprotos.inventory.loot_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.inventory.Loot)
  ))
_sym_db.RegisterMessage(Loot)


# @@protoc_insertion_point(module_scope)

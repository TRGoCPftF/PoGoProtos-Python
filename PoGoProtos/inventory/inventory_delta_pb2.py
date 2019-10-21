# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/inventory/inventory_delta.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory import inventory_item_pb2 as pogoprotos_dot_inventory_dot_inventory__item__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/inventory/inventory_delta.proto',
  package='pogoprotos.inventory',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n*pogoprotos/inventory/inventory_delta.proto\x12\x14pogoprotos.inventory\x1a)pogoprotos/inventory/inventory_item.proto\"\x87\x01\n\x0eInventoryDelta\x12\x1d\n\x15original_timestamp_ms\x18\x01 \x01(\x03\x12\x18\n\x10new_timestamp_ms\x18\x02 \x01(\x03\x12<\n\x0finventory_items\x18\x03 \x03(\x0b\x32#.pogoprotos.inventory.InventoryItemb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_inventory__item__pb2.DESCRIPTOR,])




_INVENTORYDELTA = _descriptor.Descriptor(
  name='InventoryDelta',
  full_name='pogoprotos.inventory.InventoryDelta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='original_timestamp_ms', full_name='pogoprotos.inventory.InventoryDelta.original_timestamp_ms', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_timestamp_ms', full_name='pogoprotos.inventory.InventoryDelta.new_timestamp_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inventory_items', full_name='pogoprotos.inventory.InventoryDelta.inventory_items', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=112,
  serialized_end=247,
)

_INVENTORYDELTA.fields_by_name['inventory_items'].message_type = pogoprotos_dot_inventory_dot_inventory__item__pb2._INVENTORYITEM
DESCRIPTOR.message_types_by_name['InventoryDelta'] = _INVENTORYDELTA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InventoryDelta = _reflection.GeneratedProtocolMessageType('InventoryDelta', (_message.Message,), dict(
  DESCRIPTOR = _INVENTORYDELTA,
  __module__ = 'pogoprotos.inventory.inventory_delta_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.inventory.InventoryDelta)
  ))
_sym_db.RegisterMessage(InventoryDelta)


# @@protoc_insertion_point(module_scope)

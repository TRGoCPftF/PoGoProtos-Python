# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/raid/exclusive_raid_cancellation.proto

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
  name='pogoprotos/data/raid/exclusive_raid_cancellation.proto',
  package='pogoprotos.data.raid',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n6pogoprotos/data/raid/exclusive_raid_cancellation.proto\x12\x14pogoprotos.data.raid\x1a$pogoprotos/inventory/loot_item.proto\"\xd3\x01\n\x19\x45xclusiveRaidCancellation\x12\x0f\n\x07\x66ort_id\x18\x01 \x01(\t\x12\x15\n\rstart_time_ms\x18\x02 \x01(\x03\x12\x13\n\x0b\x65nd_time_ms\x18\x03 \x01(\x03\x12\x11\n\timage_url\x18\x04 \x01(\t\x12\x10\n\x08latitude\x18\x05 \x01(\x01\x12\x11\n\tlongitude\x18\x06 \x01(\x01\x12\x10\n\x08gym_name\x18\x07 \x01(\t\x12/\n\x07rewards\x18\x08 \x03(\x0b\x32\x1e.pogoprotos.inventory.LootItemb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_loot__item__pb2.DESCRIPTOR,])




_EXCLUSIVERAIDCANCELLATION = _descriptor.Descriptor(
  name='ExclusiveRaidCancellation',
  full_name='pogoprotos.data.raid.ExclusiveRaidCancellation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fort_id', full_name='pogoprotos.data.raid.ExclusiveRaidCancellation.fort_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time_ms', full_name='pogoprotos.data.raid.ExclusiveRaidCancellation.start_time_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time_ms', full_name='pogoprotos.data.raid.ExclusiveRaidCancellation.end_time_ms', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_url', full_name='pogoprotos.data.raid.ExclusiveRaidCancellation.image_url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='pogoprotos.data.raid.ExclusiveRaidCancellation.latitude', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='pogoprotos.data.raid.ExclusiveRaidCancellation.longitude', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gym_name', full_name='pogoprotos.data.raid.ExclusiveRaidCancellation.gym_name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rewards', full_name='pogoprotos.data.raid.ExclusiveRaidCancellation.rewards', index=7,
      number=8, type=11, cpp_type=10, label=3,
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
  serialized_start=119,
  serialized_end=330,
)

_EXCLUSIVERAIDCANCELLATION.fields_by_name['rewards'].message_type = pogoprotos_dot_inventory_dot_loot__item__pb2._LOOTITEM
DESCRIPTOR.message_types_by_name['ExclusiveRaidCancellation'] = _EXCLUSIVERAIDCANCELLATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExclusiveRaidCancellation = _reflection.GeneratedProtocolMessageType('ExclusiveRaidCancellation', (_message.Message,), dict(
  DESCRIPTOR = _EXCLUSIVERAIDCANCELLATION,
  __module__ = 'pogoprotos.data.raid.exclusive_raid_cancellation_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.raid.ExclusiveRaidCancellation)
  ))
_sym_db.RegisterMessage(ExclusiveRaidCancellation)


# @@protoc_insertion_point(module_scope)

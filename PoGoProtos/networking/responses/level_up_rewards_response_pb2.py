# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/level_up_rewards_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory.item import item_id_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__id__pb2
from pogoprotos.inventory.item import item_award_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__award__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/level_up_rewards_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n?pogoprotos/networking/responses/level_up_rewards_response.proto\x12\x1fpogoprotos.networking.responses\x1a\'pogoprotos/inventory/item/item_id.proto\x1a*pogoprotos/inventory/item/item_award.proto\"\xb4\x02\n\x16LevelUpRewardsResponse\x12N\n\x06result\x18\x01 \x01(\x0e\x32>.pogoprotos.networking.responses.LevelUpRewardsResponse.Result\x12;\n\ritems_awarded\x18\x02 \x03(\x0b\x32$.pogoprotos.inventory.item.ItemAward\x12\x39\n\x0eitems_unlocked\x18\x04 \x03(\x0e\x32!.pogoprotos.inventory.item.ItemId\x12\x1b\n\x13\x61vatar_template_ids\x18\x05 \x03(\t\"5\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x13\n\x0f\x41WARDED_ALREADY\x10\x02\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_item_dot_item__id__pb2.DESCRIPTOR,pogoprotos_dot_inventory_dot_item_dot_item__award__pb2.DESCRIPTOR,])



_LEVELUPREWARDSRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.LevelUpRewardsResponse.Result',
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
      name='AWARDED_ALREADY', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=441,
  serialized_end=494,
)
_sym_db.RegisterEnumDescriptor(_LEVELUPREWARDSRESPONSE_RESULT)


_LEVELUPREWARDSRESPONSE = _descriptor.Descriptor(
  name='LevelUpRewardsResponse',
  full_name='pogoprotos.networking.responses.LevelUpRewardsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.LevelUpRewardsResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items_awarded', full_name='pogoprotos.networking.responses.LevelUpRewardsResponse.items_awarded', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items_unlocked', full_name='pogoprotos.networking.responses.LevelUpRewardsResponse.items_unlocked', index=2,
      number=4, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatar_template_ids', full_name='pogoprotos.networking.responses.LevelUpRewardsResponse.avatar_template_ids', index=3,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LEVELUPREWARDSRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=186,
  serialized_end=494,
)

_LEVELUPREWARDSRESPONSE.fields_by_name['result'].enum_type = _LEVELUPREWARDSRESPONSE_RESULT
_LEVELUPREWARDSRESPONSE.fields_by_name['items_awarded'].message_type = pogoprotos_dot_inventory_dot_item_dot_item__award__pb2._ITEMAWARD
_LEVELUPREWARDSRESPONSE.fields_by_name['items_unlocked'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__id__pb2._ITEMID
_LEVELUPREWARDSRESPONSE_RESULT.containing_type = _LEVELUPREWARDSRESPONSE
DESCRIPTOR.message_types_by_name['LevelUpRewardsResponse'] = _LEVELUPREWARDSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LevelUpRewardsResponse = _reflection.GeneratedProtocolMessageType('LevelUpRewardsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LEVELUPREWARDSRESPONSE,
  __module__ = 'pogoprotos.networking.responses.level_up_rewards_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.LevelUpRewardsResponse)
  ))
_sym_db.RegisterMessage(LevelUpRewardsResponse)


# @@protoc_insertion_point(module_scope)

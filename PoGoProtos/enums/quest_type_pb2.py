# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/quest_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/quest_type.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!pogoprotos/enums/quest_type.proto\x12\x10pogoprotos.enums*\xe3\x06\n\tQuestType\x12\x16\n\x12QUEST_UNKNOWN_TYPE\x10\x00\x12 \n\x1cQUEST_FIRST_CATCH_OF_THE_DAY\x10\x01\x12#\n\x1fQUEST_FIRST_POKESTOP_OF_THE_DAY\x10\x02\x12\x14\n\x10QUEST_MULTI_PART\x10\x03\x12\x17\n\x13QUEST_CATCH_POKEMON\x10\x04\x12\x17\n\x13QUEST_SPIN_POKESTOP\x10\x05\x12\x13\n\x0fQUEST_HATCH_EGG\x10\x06\x12\x1d\n\x19QUEST_COMPLETE_GYM_BATTLE\x10\x07\x12\x1e\n\x1aQUEST_COMPLETE_RAID_BATTLE\x10\x08\x12\x18\n\x14QUEST_COMPLETE_QUEST\x10\t\x12\x1a\n\x16QUEST_TRANSFER_POKEMON\x10\n\x12\x1a\n\x16QUEST_FAVORITE_POKEMON\x10\x0b\x12\x16\n\x12QUEST_AUTOCOMPLETE\x10\x0c\x12 \n\x1cQUEST_USE_BERRY_IN_ENCOUNTER\x10\r\x12\x19\n\x15QUEST_UPGRADE_POKEMON\x10\x0e\x12\x18\n\x14QUEST_EVOLVE_POKEMON\x10\x0f\x12\x14\n\x10QUEST_LAND_THROW\x10\x10\x12\x19\n\x15QUEST_GET_BUDDY_CANDY\x10\x11\x12\x14\n\x10QUEST_BADGE_RANK\x10\x12\x12\x16\n\x12QUEST_PLAYER_LEVEL\x10\x13\x12\x13\n\x0fQUEST_JOIN_RAID\x10\x14\x12\x19\n\x15QUEST_COMPLETE_BATTLE\x10\x15\x12\x14\n\x10QUEST_ADD_FRIEND\x10\x16\x12\x17\n\x13QUEST_TRADE_POKEMON\x10\x17\x12\x13\n\x0fQUEST_SEND_GIFT\x10\x18\x12\x1d\n\x19QUEST_EVOLVE_INTO_POKEMON\x10\x19\x12\x19\n\x15QUEST_COMPLETE_COMBAT\x10\x1b\x12\x17\n\x13QUEST_TAKE_SNAPSHOT\x10\x1c\x12\x1c\n\x18QUEST_BATTLE_TEAM_ROCKET\x10\x1d\x12\x18\n\x14QUEST_PURIFY_POKEMON\x10\x1e\x12\x1a\n\x16QUEST_FIND_TEAM_ROCKET\x10\x1f\x12 \n\x1cQUEST_FIRST_GRUNT_OF_THE_DAY\x10 b\x06proto3')
)

_QUESTTYPE = _descriptor.EnumDescriptor(
  name='QuestType',
  full_name='pogoprotos.enums.QuestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='QUEST_UNKNOWN_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_FIRST_CATCH_OF_THE_DAY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_FIRST_POKESTOP_OF_THE_DAY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_MULTI_PART', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_CATCH_POKEMON', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_SPIN_POKESTOP', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_HATCH_EGG', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_COMPLETE_GYM_BATTLE', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_COMPLETE_RAID_BATTLE', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_COMPLETE_QUEST', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_TRANSFER_POKEMON', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_FAVORITE_POKEMON', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_AUTOCOMPLETE', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_USE_BERRY_IN_ENCOUNTER', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_UPGRADE_POKEMON', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_EVOLVE_POKEMON', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_LAND_THROW', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_GET_BUDDY_CANDY', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_BADGE_RANK', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_PLAYER_LEVEL', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_JOIN_RAID', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_COMPLETE_BATTLE', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_ADD_FRIEND', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_TRADE_POKEMON', index=23, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_SEND_GIFT', index=24, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_EVOLVE_INTO_POKEMON', index=25, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_COMPLETE_COMBAT', index=26, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_TAKE_SNAPSHOT', index=27, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_BATTLE_TEAM_ROCKET', index=28, number=29,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_PURIFY_POKEMON', index=29, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_FIND_TEAM_ROCKET', index=30, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_FIRST_GRUNT_OF_THE_DAY', index=31, number=32,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=56,
  serialized_end=923,
)
_sym_db.RegisterEnumDescriptor(_QUESTTYPE)

QuestType = enum_type_wrapper.EnumTypeWrapper(_QUESTTYPE)
QUEST_UNKNOWN_TYPE = 0
QUEST_FIRST_CATCH_OF_THE_DAY = 1
QUEST_FIRST_POKESTOP_OF_THE_DAY = 2
QUEST_MULTI_PART = 3
QUEST_CATCH_POKEMON = 4
QUEST_SPIN_POKESTOP = 5
QUEST_HATCH_EGG = 6
QUEST_COMPLETE_GYM_BATTLE = 7
QUEST_COMPLETE_RAID_BATTLE = 8
QUEST_COMPLETE_QUEST = 9
QUEST_TRANSFER_POKEMON = 10
QUEST_FAVORITE_POKEMON = 11
QUEST_AUTOCOMPLETE = 12
QUEST_USE_BERRY_IN_ENCOUNTER = 13
QUEST_UPGRADE_POKEMON = 14
QUEST_EVOLVE_POKEMON = 15
QUEST_LAND_THROW = 16
QUEST_GET_BUDDY_CANDY = 17
QUEST_BADGE_RANK = 18
QUEST_PLAYER_LEVEL = 19
QUEST_JOIN_RAID = 20
QUEST_COMPLETE_BATTLE = 21
QUEST_ADD_FRIEND = 22
QUEST_TRADE_POKEMON = 23
QUEST_SEND_GIFT = 24
QUEST_EVOLVE_INTO_POKEMON = 25
QUEST_COMPLETE_COMBAT = 27
QUEST_TAKE_SNAPSHOT = 28
QUEST_BATTLE_TEAM_ROCKET = 29
QUEST_PURIFY_POKEMON = 30
QUEST_FIND_TEAM_ROCKET = 31
QUEST_FIRST_GRUNT_OF_THE_DAY = 32


DESCRIPTOR.enum_types_by_name['QuestType'] = _QUESTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)

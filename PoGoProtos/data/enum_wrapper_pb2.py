# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/enum_wrapper.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/enum_wrapper.proto',
  package='pogoprotos.data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\"pogoprotos/data/enum_wrapper.proto\x12\x0fpogoprotos.data\"\xcf\x0f\n\x0b\x45numWrapper\"i\n\x11\x43haracterCategory\x12\t\n\x05UNSET\x10\x00\x12\x0f\n\x0bTEAM_LEADER\x10\x01\x12\t\n\x05GRUNT\x10\x02\x12\x08\n\x04\x41RLO\x10\x03\x12\t\n\x05\x43LIFF\x10\x04\x12\n\n\x06SIERRA\x10\x05\x12\x0c\n\x08GIOVANNI\x10\x06\"\xf2\x0c\n\x11InvasionCharacter\x12\x13\n\x0f\x43HARACTER_UNSET\x10\x00\x12\x15\n\x11\x43HARACTER_BLANCHE\x10\x01\x12\x15\n\x11\x43HARACTER_CANDELA\x10\x02\x12\x13\n\x0f\x43HARACTER_SPARK\x10\x03\x12\x18\n\x14\x43HARACTER_GRUNT_MALE\x10\x04\x12\x1a\n\x16\x43HARACTER_GRUNT_FEMALE\x10\x05\x12\x1e\n\x1a\x43HARACTER_BUG_GRUNT_FEMALE\x10\x06\x12\x1c\n\x18\x43HARACTER_BUG_GRUNT_MALE\x10\x07\x12#\n\x1f\x43HARACTER_DARKNESS_GRUNT_FEMALE\x10\x08\x12!\n\x1d\x43HARACTER_DARKNESS_GRUNT_MALE\x10\t\x12\x1f\n\x1b\x43HARACTER_DARK_GRUNT_FEMALE\x10\n\x12\x1d\n\x19\x43HARACTER_DARK_GRUNT_MALE\x10\x0b\x12!\n\x1d\x43HARACTER_DRAGON_GRUNT_FEMALE\x10\x0c\x12\x1f\n\x1b\x43HARACTER_DRAGON_GRUNT_MALE\x10\r\x12 \n\x1c\x43HARACTER_FAIRY_GRUNT_FEMALE\x10\x0e\x12\x1e\n\x1a\x43HARACTER_FAIRY_GRUNT_MALE\x10\x0f\x12#\n\x1f\x43HARACTER_FIGHTING_GRUNT_FEMALE\x10\x10\x12!\n\x1d\x43HARACTER_FIGHTING_GRUNT_MALE\x10\x11\x12\x1f\n\x1b\x43HARACTER_FIRE_GRUNT_FEMALE\x10\x12\x12\x1d\n\x19\x43HARACTER_FIRE_GRUNT_MALE\x10\x13\x12!\n\x1d\x43HARACTER_FLYING_GRUNT_FEMALE\x10\x14\x12\x1f\n\x1b\x43HARACTER_FLYING_GRUNT_MALE\x10\x15\x12 \n\x1c\x43HARACTER_GRASS_GRUNT_FEMALE\x10\x16\x12\x1e\n\x1a\x43HARACTER_GRASS_GRUNT_MALE\x10\x17\x12!\n\x1d\x43HARACTER_GROUND_GRUNT_FEMALE\x10\x18\x12\x1f\n\x1b\x43HARACTER_GROUND_GRUNT_MALE\x10\x19\x12\x1e\n\x1a\x43HARACTER_ICE_GRUNT_FEMALE\x10\x1a\x12\x1c\n\x18\x43HARACTER_ICE_GRUNT_MALE\x10\x1b\x12 \n\x1c\x43HARACTER_METAL_GRUNT_FEMALE\x10\x1c\x12\x1e\n\x1a\x43HARACTER_METAL_GRUNT_MALE\x10\x1d\x12!\n\x1d\x43HARACTER_NORMAL_GRUNT_FEMALE\x10\x1e\x12\x1f\n\x1b\x43HARACTER_NORMAL_GRUNT_MALE\x10\x1f\x12!\n\x1d\x43HARACTER_POISON_GRUNT_FEMALE\x10 \x12\x1f\n\x1b\x43HARACTER_POISON_GRUNT_MALE\x10!\x12\"\n\x1e\x43HARACTER_PSYCHIC_GRUNT_FEMALE\x10\"\x12 \n\x1c\x43HARACTER_PSYCHIC_GRUNT_MALE\x10#\x12\x1f\n\x1b\x43HARACTER_ROCK_GRUNT_FEMALE\x10$\x12\x1d\n\x19\x43HARACTER_ROCK_GRUNT_MALE\x10%\x12 \n\x1c\x43HARACTER_WATER_GRUNT_FEMALE\x10&\x12\x1e\n\x1a\x43HARACTER_WATER_GRUNT_MALE\x10\'\x12 \n\x1c\x43HARACTER_PLAYER_TEAM_LEADER\x10(\x12\x1d\n\x19\x43HARACTER_EXECUTIVE_CLIFF\x10)\x12\x1c\n\x18\x43HARACTER_EXECUTIVE_ARLO\x10*\x12\x1e\n\x1a\x43HARACTER_EXECUTIVE_SIERRA\x10+\x12\x16\n\x12\x43HARACTER_GIOVANNI\x10,\x12\x1e\n\x1a\x43HARACTER_DECOY_GRUNT_MALE\x10-\x12 \n\x1c\x43HARACTER_DECOY_GRUNT_FEMALE\x10.\x12 \n\x1c\x43HARACTER_GHOST_GRUNT_FEMALE\x10/\x12\x1e\n\x1a\x43HARACTER_GHOST_GRUNT_MALE\x10\x30\x12#\n\x1f\x43HARACTER_ELECTRIC_GRUNT_FEMALE\x10\x31\x12!\n\x1d\x43HARACTER_ELECTRIC_GRUNT_MALE\x10\x32\"\x7f\n\x1bInvasionCharacterExpression\x12\x14\n\x10\x45XPRESSION_UNSET\x10\x00\x12\x11\n\rPLACEHOLDER_1\x10\x01\x12\x11\n\rPLACEHOLDER_2\x10\x02\x12\x11\n\rPLACEHOLDER_3\x10\x03\x12\x11\n\rPLACEHOLDER_4\x10\x04\"_\n\rPokestopStyle\x12\x13\n\x0fPOKESTOP_NORMAL\x10\x00\x12\x1c\n\x18POKESTOP_ROCKET_INVASION\x10\x01\x12\x1b\n\x17POKESTOP_ROCKET_VICTORY\x10\x02\x62\x06proto3')
)



_ENUMWRAPPER_CHARACTERCATEGORY = _descriptor.EnumDescriptor(
  name='CharacterCategory',
  full_name='pogoprotos.data.EnumWrapper.CharacterCategory',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEAM_LEADER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRUNT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARLO', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLIFF', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIERRA', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GIOVANNI', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=71,
  serialized_end=176,
)
_sym_db.RegisterEnumDescriptor(_ENUMWRAPPER_CHARACTERCATEGORY)

_ENUMWRAPPER_INVASIONCHARACTER = _descriptor.EnumDescriptor(
  name='InvasionCharacter',
  full_name='pogoprotos.data.EnumWrapper.InvasionCharacter',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_BLANCHE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_CANDELA', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_SPARK', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_GRUNT_MALE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_GRUNT_FEMALE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_BUG_GRUNT_FEMALE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_BUG_GRUNT_MALE', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_DARKNESS_GRUNT_FEMALE', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_DARKNESS_GRUNT_MALE', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_DARK_GRUNT_FEMALE', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_DARK_GRUNT_MALE', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_DRAGON_GRUNT_FEMALE', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_DRAGON_GRUNT_MALE', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_FAIRY_GRUNT_FEMALE', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_FAIRY_GRUNT_MALE', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_FIGHTING_GRUNT_FEMALE', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_FIGHTING_GRUNT_MALE', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_FIRE_GRUNT_FEMALE', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_FIRE_GRUNT_MALE', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_FLYING_GRUNT_FEMALE', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_FLYING_GRUNT_MALE', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_GRASS_GRUNT_FEMALE', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_GRASS_GRUNT_MALE', index=23, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_GROUND_GRUNT_FEMALE', index=24, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_GROUND_GRUNT_MALE', index=25, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_ICE_GRUNT_FEMALE', index=26, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_ICE_GRUNT_MALE', index=27, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_METAL_GRUNT_FEMALE', index=28, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_METAL_GRUNT_MALE', index=29, number=29,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_NORMAL_GRUNT_FEMALE', index=30, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_NORMAL_GRUNT_MALE', index=31, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_POISON_GRUNT_FEMALE', index=32, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_POISON_GRUNT_MALE', index=33, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_PSYCHIC_GRUNT_FEMALE', index=34, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_PSYCHIC_GRUNT_MALE', index=35, number=35,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_ROCK_GRUNT_FEMALE', index=36, number=36,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_ROCK_GRUNT_MALE', index=37, number=37,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_WATER_GRUNT_FEMALE', index=38, number=38,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_WATER_GRUNT_MALE', index=39, number=39,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_PLAYER_TEAM_LEADER', index=40, number=40,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_EXECUTIVE_CLIFF', index=41, number=41,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_EXECUTIVE_ARLO', index=42, number=42,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_EXECUTIVE_SIERRA', index=43, number=43,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_GIOVANNI', index=44, number=44,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_DECOY_GRUNT_MALE', index=45, number=45,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_DECOY_GRUNT_FEMALE', index=46, number=46,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_GHOST_GRUNT_FEMALE', index=47, number=47,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_GHOST_GRUNT_MALE', index=48, number=48,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_ELECTRIC_GRUNT_FEMALE', index=49, number=49,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER_ELECTRIC_GRUNT_MALE', index=50, number=50,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=179,
  serialized_end=1829,
)
_sym_db.RegisterEnumDescriptor(_ENUMWRAPPER_INVASIONCHARACTER)

_ENUMWRAPPER_INVASIONCHARACTEREXPRESSION = _descriptor.EnumDescriptor(
  name='InvasionCharacterExpression',
  full_name='pogoprotos.data.EnumWrapper.InvasionCharacterExpression',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EXPRESSION_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLACEHOLDER_1', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLACEHOLDER_2', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLACEHOLDER_3', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLACEHOLDER_4', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1831,
  serialized_end=1958,
)
_sym_db.RegisterEnumDescriptor(_ENUMWRAPPER_INVASIONCHARACTEREXPRESSION)

_ENUMWRAPPER_POKESTOPSTYLE = _descriptor.EnumDescriptor(
  name='PokestopStyle',
  full_name='pogoprotos.data.EnumWrapper.PokestopStyle',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='POKESTOP_NORMAL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKESTOP_ROCKET_INVASION', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKESTOP_ROCKET_VICTORY', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1960,
  serialized_end=2055,
)
_sym_db.RegisterEnumDescriptor(_ENUMWRAPPER_POKESTOPSTYLE)


_ENUMWRAPPER = _descriptor.Descriptor(
  name='EnumWrapper',
  full_name='pogoprotos.data.EnumWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ENUMWRAPPER_CHARACTERCATEGORY,
    _ENUMWRAPPER_INVASIONCHARACTER,
    _ENUMWRAPPER_INVASIONCHARACTEREXPRESSION,
    _ENUMWRAPPER_POKESTOPSTYLE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=2055,
)

_ENUMWRAPPER_CHARACTERCATEGORY.containing_type = _ENUMWRAPPER
_ENUMWRAPPER_INVASIONCHARACTER.containing_type = _ENUMWRAPPER
_ENUMWRAPPER_INVASIONCHARACTEREXPRESSION.containing_type = _ENUMWRAPPER
_ENUMWRAPPER_POKESTOPSTYLE.containing_type = _ENUMWRAPPER
DESCRIPTOR.message_types_by_name['EnumWrapper'] = _ENUMWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EnumWrapper = _reflection.GeneratedProtocolMessageType('EnumWrapper', (_message.Message,), dict(
  DESCRIPTOR = _ENUMWRAPPER,
  __module__ = 'pogoprotos.data.enum_wrapper_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.EnumWrapper)
  ))
_sym_db.RegisterMessage(EnumWrapper)


# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/inventory/item/item_id.proto

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
  name='pogoprotos/inventory/item/item_id.proto',
  package='pogoprotos.inventory.item',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\'pogoprotos/inventory/item/item_id.proto\x12\x19pogoprotos.inventory.item*\x92\x0b\n\x06ItemId\x12\x10\n\x0cITEM_UNKNOWN\x10\x00\x12\x12\n\x0eITEM_POKE_BALL\x10\x01\x12\x13\n\x0fITEM_GREAT_BALL\x10\x02\x12\x13\n\x0fITEM_ULTRA_BALL\x10\x03\x12\x14\n\x10ITEM_MASTER_BALL\x10\x04\x12\x15\n\x11ITEM_PREMIER_BALL\x10\x05\x12\x0f\n\x0bITEM_POTION\x10\x65\x12\x15\n\x11ITEM_SUPER_POTION\x10\x66\x12\x15\n\x11ITEM_HYPER_POTION\x10g\x12\x13\n\x0fITEM_MAX_POTION\x10h\x12\x10\n\x0bITEM_REVIVE\x10\xc9\x01\x12\x14\n\x0fITEM_MAX_REVIVE\x10\xca\x01\x12\x13\n\x0eITEM_LUCKY_EGG\x10\xad\x02\x12\x1a\n\x15ITEM_INCENSE_ORDINARY\x10\x91\x03\x12\x17\n\x12ITEM_INCENSE_SPICY\x10\x92\x03\x12\x16\n\x11ITEM_INCENSE_COOL\x10\x93\x03\x12\x18\n\x13ITEM_INCENSE_FLORAL\x10\x94\x03\x12\x1c\n\x17ITEM_INCENSE_BELUGA_BOX\x10\x95\x03\x12\x13\n\x0eITEM_TROY_DISK\x10\xf5\x03\x12\x1b\n\x16ITEM_TROY_DISK_GLACIAL\x10\xf6\x03\x12\x19\n\x14ITEM_TROY_DISK_MOSSY\x10\xf7\x03\x12\x1c\n\x17ITEM_TROY_DISK_MAGNETIC\x10\xf8\x03\x12\x12\n\rITEM_X_ATTACK\x10\xda\x04\x12\x13\n\x0eITEM_X_DEFENSE\x10\xdb\x04\x12\x13\n\x0eITEM_X_MIRACLE\x10\xdc\x04\x12\x14\n\x0fITEM_RAZZ_BERRY\x10\xbd\x05\x12\x14\n\x0fITEM_BLUK_BERRY\x10\xbe\x05\x12\x15\n\x10ITEM_NANAB_BERRY\x10\xbf\x05\x12\x15\n\x10ITEM_WEPAR_BERRY\x10\xc0\x05\x12\x15\n\x10ITEM_PINAP_BERRY\x10\xc1\x05\x12\x1b\n\x16ITEM_GOLDEN_RAZZ_BERRY\x10\xc2\x05\x12\x1c\n\x17ITEM_GOLDEN_NANAB_BERRY\x10\xc3\x05\x12\x1c\n\x17ITEM_GOLDEN_PINAP_BERRY\x10\xc4\x05\x12\x18\n\x13ITEM_SPECIAL_CAMERA\x10\xa1\x06\x12#\n\x1eITEM_INCUBATOR_BASIC_UNLIMITED\x10\x85\x07\x12\x19\n\x14ITEM_INCUBATOR_BASIC\x10\x86\x07\x12\x19\n\x14ITEM_INCUBATOR_SUPER\x10\x87\x07\x12!\n\x1cITEM_POKEMON_STORAGE_UPGRADE\x10\xe9\x07\x12\x1e\n\x19ITEM_ITEM_STORAGE_UPGRADE\x10\xea\x07\x12\x13\n\x0eITEM_SUN_STONE\x10\xcd\x08\x12\x14\n\x0fITEM_KINGS_ROCK\x10\xce\x08\x12\x14\n\x0fITEM_METAL_COAT\x10\xcf\x08\x12\x16\n\x11ITEM_DRAGON_SCALE\x10\xd0\x08\x12\x12\n\rITEM_UP_GRADE\x10\xd1\x08\x12\x1e\n\x19ITEM_GEN4_EVOLUTION_STONE\x10\xd2\x08\x12\x1e\n\x19ITEM_GEN5_EVOLUTION_STONE\x10\xd3\x08\x12!\n\x1cITEM_MOVE_REROLL_FAST_ATTACK\x10\xb1\t\x12$\n\x1fITEM_MOVE_REROLL_SPECIAL_ATTACK\x10\xb2\t\x12\x14\n\x0fITEM_RARE_CANDY\x10\x95\n\x12\x1a\n\x15ITEM_FREE_RAID_TICKET\x10\xf9\n\x12\x1a\n\x15ITEM_PAID_RAID_TICKET\x10\xfa\n\x12\x1f\n\x1aITEM_LEGENDARY_RAID_TICKET\x10\xfb\n\x12\x14\n\x0fITEM_STAR_PIECE\x10\xfc\n\x12\x19\n\x14ITEM_FRIEND_GIFT_BOX\x10\xfd\n\x12\x15\n\x10ITEM_TEAM_CHANGE\x10\xfe\n\x12\x1d\n\x18ITEM_GLOBAL_EVENT_TICKET\x10\xc0\x0c\x62\x06proto3')
)

_ITEMID = _descriptor.EnumDescriptor(
  name='ItemId',
  full_name='pogoprotos.inventory.item.ItemId',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ITEM_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_POKE_BALL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_GREAT_BALL', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_ULTRA_BALL', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_MASTER_BALL', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_PREMIER_BALL', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_POTION', index=6, number=101,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_SUPER_POTION', index=7, number=102,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_HYPER_POTION', index=8, number=103,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_MAX_POTION', index=9, number=104,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_REVIVE', index=10, number=201,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_MAX_REVIVE', index=11, number=202,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_LUCKY_EGG', index=12, number=301,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_INCENSE_ORDINARY', index=13, number=401,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_INCENSE_SPICY', index=14, number=402,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_INCENSE_COOL', index=15, number=403,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_INCENSE_FLORAL', index=16, number=404,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_INCENSE_BELUGA_BOX', index=17, number=405,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TROY_DISK', index=18, number=501,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TROY_DISK_GLACIAL', index=19, number=502,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TROY_DISK_MOSSY', index=20, number=503,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TROY_DISK_MAGNETIC', index=21, number=504,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_X_ATTACK', index=22, number=602,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_X_DEFENSE', index=23, number=603,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_X_MIRACLE', index=24, number=604,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_RAZZ_BERRY', index=25, number=701,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_BLUK_BERRY', index=26, number=702,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_NANAB_BERRY', index=27, number=703,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_WEPAR_BERRY', index=28, number=704,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_PINAP_BERRY', index=29, number=705,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_GOLDEN_RAZZ_BERRY', index=30, number=706,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_GOLDEN_NANAB_BERRY', index=31, number=707,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_GOLDEN_PINAP_BERRY', index=32, number=708,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_SPECIAL_CAMERA', index=33, number=801,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_INCUBATOR_BASIC_UNLIMITED', index=34, number=901,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_INCUBATOR_BASIC', index=35, number=902,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_INCUBATOR_SUPER', index=36, number=903,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_POKEMON_STORAGE_UPGRADE', index=37, number=1001,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_ITEM_STORAGE_UPGRADE', index=38, number=1002,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_SUN_STONE', index=39, number=1101,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_KINGS_ROCK', index=40, number=1102,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_METAL_COAT', index=41, number=1103,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_DRAGON_SCALE', index=42, number=1104,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_UP_GRADE', index=43, number=1105,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_GEN4_EVOLUTION_STONE', index=44, number=1106,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_GEN5_EVOLUTION_STONE', index=45, number=1107,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_MOVE_REROLL_FAST_ATTACK', index=46, number=1201,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_MOVE_REROLL_SPECIAL_ATTACK', index=47, number=1202,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_RARE_CANDY', index=48, number=1301,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_FREE_RAID_TICKET', index=49, number=1401,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_PAID_RAID_TICKET', index=50, number=1402,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_LEGENDARY_RAID_TICKET', index=51, number=1403,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_STAR_PIECE', index=52, number=1404,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_FRIEND_GIFT_BOX', index=53, number=1405,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TEAM_CHANGE', index=54, number=1406,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_GLOBAL_EVENT_TICKET', index=55, number=1600,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=71,
  serialized_end=1497,
)
_sym_db.RegisterEnumDescriptor(_ITEMID)

ItemId = enum_type_wrapper.EnumTypeWrapper(_ITEMID)
ITEM_UNKNOWN = 0
ITEM_POKE_BALL = 1
ITEM_GREAT_BALL = 2
ITEM_ULTRA_BALL = 3
ITEM_MASTER_BALL = 4
ITEM_PREMIER_BALL = 5
ITEM_POTION = 101
ITEM_SUPER_POTION = 102
ITEM_HYPER_POTION = 103
ITEM_MAX_POTION = 104
ITEM_REVIVE = 201
ITEM_MAX_REVIVE = 202
ITEM_LUCKY_EGG = 301
ITEM_INCENSE_ORDINARY = 401
ITEM_INCENSE_SPICY = 402
ITEM_INCENSE_COOL = 403
ITEM_INCENSE_FLORAL = 404
ITEM_INCENSE_BELUGA_BOX = 405
ITEM_TROY_DISK = 501
ITEM_TROY_DISK_GLACIAL = 502
ITEM_TROY_DISK_MOSSY = 503
ITEM_TROY_DISK_MAGNETIC = 504
ITEM_X_ATTACK = 602
ITEM_X_DEFENSE = 603
ITEM_X_MIRACLE = 604
ITEM_RAZZ_BERRY = 701
ITEM_BLUK_BERRY = 702
ITEM_NANAB_BERRY = 703
ITEM_WEPAR_BERRY = 704
ITEM_PINAP_BERRY = 705
ITEM_GOLDEN_RAZZ_BERRY = 706
ITEM_GOLDEN_NANAB_BERRY = 707
ITEM_GOLDEN_PINAP_BERRY = 708
ITEM_SPECIAL_CAMERA = 801
ITEM_INCUBATOR_BASIC_UNLIMITED = 901
ITEM_INCUBATOR_BASIC = 902
ITEM_INCUBATOR_SUPER = 903
ITEM_POKEMON_STORAGE_UPGRADE = 1001
ITEM_ITEM_STORAGE_UPGRADE = 1002
ITEM_SUN_STONE = 1101
ITEM_KINGS_ROCK = 1102
ITEM_METAL_COAT = 1103
ITEM_DRAGON_SCALE = 1104
ITEM_UP_GRADE = 1105
ITEM_GEN4_EVOLUTION_STONE = 1106
ITEM_GEN5_EVOLUTION_STONE = 1107
ITEM_MOVE_REROLL_FAST_ATTACK = 1201
ITEM_MOVE_REROLL_SPECIAL_ATTACK = 1202
ITEM_RARE_CANDY = 1301
ITEM_FREE_RAID_TICKET = 1401
ITEM_PAID_RAID_TICKET = 1402
ITEM_LEGENDARY_RAID_TICKET = 1403
ITEM_STAR_PIECE = 1404
ITEM_FRIEND_GIFT_BOX = 1405
ITEM_TEAM_CHANGE = 1406
ITEM_GLOBAL_EVENT_TICKET = 1600


DESCRIPTOR.enum_types_by_name['ItemId'] = _ITEMID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)

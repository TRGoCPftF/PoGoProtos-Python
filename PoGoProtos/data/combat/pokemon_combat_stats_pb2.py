# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/combat/pokemon_combat_stats.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/combat/pokemon_combat_stats.proto',
  package='pogoprotos.data.combat',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n1pogoprotos/data/combat/pokemon_combat_stats.proto\x12\x16pogoprotos.data.combat\"8\n\x12PokemonCombatStats\x12\x0f\n\x07num_won\x18\x01 \x01(\x05\x12\x11\n\tnum_total\x18\x02 \x01(\x05\x62\x06proto3')
)




_POKEMONCOMBATSTATS = _descriptor.Descriptor(
  name='PokemonCombatStats',
  full_name='pogoprotos.data.combat.PokemonCombatStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_won', full_name='pogoprotos.data.combat.PokemonCombatStats.num_won', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_total', full_name='pogoprotos.data.combat.PokemonCombatStats.num_total', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=77,
  serialized_end=133,
)

DESCRIPTOR.message_types_by_name['PokemonCombatStats'] = _POKEMONCOMBATSTATS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PokemonCombatStats = _reflection.GeneratedProtocolMessageType('PokemonCombatStats', (_message.Message,), dict(
  DESCRIPTOR = _POKEMONCOMBATSTATS,
  __module__ = 'pogoprotos.data.combat.pokemon_combat_stats_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.combat.PokemonCombatStats)
  ))
_sym_db.RegisterMessage(PokemonCombatStats)


# @@protoc_insertion_point(module_scope)

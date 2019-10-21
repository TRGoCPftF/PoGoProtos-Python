# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/combat_minigame_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import pokemon_type_pb2 as pogoprotos_dot_enums_dot_pokemon__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/combat_minigame_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n9pogoprotos/data/telemetry/combat_minigame_telemetry.proto\x12\x19pogoprotos.data.telemetry\x1a#pogoprotos/enums/pokemon_type.proto\"\xe9\x01\n\x17\x43ombatMinigameTelemetry\x12Z\n\x0b\x63ombat_type\x18\x01 \x01(\x0e\x32\x45.pogoprotos.data.telemetry.CombatMinigameTelemetry.MinigameCombatType\x12\x30\n\tmove_type\x18\x02 \x01(\x0e\x32\x1d.pogoprotos.enums.PokemonType\x12\r\n\x05score\x18\x03 \x01(\x02\"1\n\x12MinigameCombatType\x12\t\n\x05UNSET\x10\x00\x12\x07\n\x03PVP\x10\x01\x12\x07\n\x03PVE\x10\x02\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_pokemon__type__pb2.DESCRIPTOR,])



_COMBATMINIGAMETELEMETRY_MINIGAMECOMBATTYPE = _descriptor.EnumDescriptor(
  name='MinigameCombatType',
  full_name='pogoprotos.data.telemetry.CombatMinigameTelemetry.MinigameCombatType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PVP', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PVE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=310,
  serialized_end=359,
)
_sym_db.RegisterEnumDescriptor(_COMBATMINIGAMETELEMETRY_MINIGAMECOMBATTYPE)


_COMBATMINIGAMETELEMETRY = _descriptor.Descriptor(
  name='CombatMinigameTelemetry',
  full_name='pogoprotos.data.telemetry.CombatMinigameTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='combat_type', full_name='pogoprotos.data.telemetry.CombatMinigameTelemetry.combat_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='move_type', full_name='pogoprotos.data.telemetry.CombatMinigameTelemetry.move_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='pogoprotos.data.telemetry.CombatMinigameTelemetry.score', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMBATMINIGAMETELEMETRY_MINIGAMECOMBATTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=359,
)

_COMBATMINIGAMETELEMETRY.fields_by_name['combat_type'].enum_type = _COMBATMINIGAMETELEMETRY_MINIGAMECOMBATTYPE
_COMBATMINIGAMETELEMETRY.fields_by_name['move_type'].enum_type = pogoprotos_dot_enums_dot_pokemon__type__pb2._POKEMONTYPE
_COMBATMINIGAMETELEMETRY_MINIGAMECOMBATTYPE.containing_type = _COMBATMINIGAMETELEMETRY
DESCRIPTOR.message_types_by_name['CombatMinigameTelemetry'] = _COMBATMINIGAMETELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CombatMinigameTelemetry = _reflection.GeneratedProtocolMessageType('CombatMinigameTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _COMBATMINIGAMETELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.combat_minigame_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.CombatMinigameTelemetry)
  ))
_sym_db.RegisterMessage(CombatMinigameTelemetry)


# @@protoc_insertion_point(module_scope)

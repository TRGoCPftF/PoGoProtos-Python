# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/raid/raid_encounter.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data import pokemon_data_pb2 as pogoprotos_dot_data_dot_pokemon__data__pb2
from pogoprotos.data.capture import capture_probability_pb2 as pogoprotos_dot_data_dot_capture_dot_capture__probability__pb2
from pogoprotos.enums import raid_level_pb2 as pogoprotos_dot_enums_dot_raid__level__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/raid/raid_encounter.proto',
  package='pogoprotos.data.raid',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n)pogoprotos/data/raid/raid_encounter.proto\x12\x14pogoprotos.data.raid\x1a\"pogoprotos/data/pokemon_data.proto\x1a\x31pogoprotos/data/capture/capture_probability.proto\x1a!pogoprotos/enums/raid_level.proto\"\x93\x02\n\rRaidEncounter\x12-\n\x07pokemon\x18\x01 \x01(\x0b\x32\x1c.pogoprotos.data.PokemonData\x12\x14\n\x0c\x65ncounter_id\x18\x02 \x01(\x03\x12\x15\n\rspawnpoint_id\x18\x03 \x01(\t\x12J\n\x15\x63\x61pture_probabilities\x18\x04 \x01(\x0b\x32+.pogoprotos.data.capture.CaptureProbability\x12\x18\n\x10throws_remaining\x18\x05 \x01(\x05\x12/\n\nraid_level\x18\x06 \x01(\x0e\x32\x1b.pogoprotos.enums.RaidLevel\x12\x0f\n\x07\x66ort_id\x18\x07 \x01(\tb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_pokemon__data__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_capture_dot_capture__probability__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_raid__level__pb2.DESCRIPTOR,])




_RAIDENCOUNTER = _descriptor.Descriptor(
  name='RaidEncounter',
  full_name='pogoprotos.data.raid.RaidEncounter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon', full_name='pogoprotos.data.raid.RaidEncounter.pokemon', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encounter_id', full_name='pogoprotos.data.raid.RaidEncounter.encounter_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spawnpoint_id', full_name='pogoprotos.data.raid.RaidEncounter.spawnpoint_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capture_probabilities', full_name='pogoprotos.data.raid.RaidEncounter.capture_probabilities', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='throws_remaining', full_name='pogoprotos.data.raid.RaidEncounter.throws_remaining', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raid_level', full_name='pogoprotos.data.raid.RaidEncounter.raid_level', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fort_id', full_name='pogoprotos.data.raid.RaidEncounter.fort_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=190,
  serialized_end=465,
)

_RAIDENCOUNTER.fields_by_name['pokemon'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
_RAIDENCOUNTER.fields_by_name['capture_probabilities'].message_type = pogoprotos_dot_data_dot_capture_dot_capture__probability__pb2._CAPTUREPROBABILITY
_RAIDENCOUNTER.fields_by_name['raid_level'].enum_type = pogoprotos_dot_enums_dot_raid__level__pb2._RAIDLEVEL
DESCRIPTOR.message_types_by_name['RaidEncounter'] = _RAIDENCOUNTER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RaidEncounter = _reflection.GeneratedProtocolMessageType('RaidEncounter', (_message.Message,), dict(
  DESCRIPTOR = _RAIDENCOUNTER,
  __module__ = 'pogoprotos.data.raid.raid_encounter_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.raid.RaidEncounter)
  ))
_sym_db.RegisterMessage(RaidEncounter)


# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/pokemon/encounter_attributes.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import pokemon_movement_type_pb2 as pogoprotos_dot_enums_dot_pokemon__movement__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/pokemon/encounter_attributes.proto',
  package='pogoprotos.settings.master.pokemon',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n=pogoprotos/settings/master/pokemon/encounter_attributes.proto\x12\"pogoprotos.settings.master.pokemon\x1a,pogoprotos/enums/pokemon_movement_type.proto\"\xc3\x04\n\x13\x45ncounterAttributes\x12\x19\n\x11\x62\x61se_capture_rate\x18\x01 \x01(\x02\x12\x16\n\x0e\x62\x61se_flee_rate\x18\x02 \x01(\x02\x12\x1a\n\x12\x63ollision_radius_m\x18\x03 \x01(\x02\x12\x1a\n\x12\x63ollision_height_m\x18\x04 \x01(\x02\x12\x1f\n\x17\x63ollision_head_radius_m\x18\x05 \x01(\x02\x12<\n\rmovement_type\x18\x06 \x01(\x0e\x32%.pogoprotos.enums.PokemonMovementType\x12\x18\n\x10movement_timer_s\x18\x07 \x01(\x02\x12\x13\n\x0bjump_time_s\x18\x08 \x01(\x02\x12\x16\n\x0e\x61ttack_timer_s\x18\t \x01(\x02\x12\"\n\x1a\x62onus_candy_capture_reward\x18\n \x01(\x05\x12%\n\x1d\x62onus_stardust_capture_reward\x18\x0b \x01(\x05\x12\x1a\n\x12\x61ttack_probability\x18\x0c \x01(\x02\x12\x19\n\x11\x64odge_probability\x18\r \x01(\x02\x12\x18\n\x10\x64odge_duration_s\x18\x0e \x01(\x02\x12\x16\n\x0e\x64odge_distance\x18\x0f \x01(\x02\x12\x17\n\x0f\x63\x61mera_distance\x18\x10 \x01(\x02\x12&\n\x1emin_pokemon_action_frequency_s\x18\x11 \x01(\x02\x12&\n\x1emax_pokemon_action_frequency_s\x18\x12 \x01(\x02\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_pokemon__movement__type__pb2.DESCRIPTOR,])




_ENCOUNTERATTRIBUTES = _descriptor.Descriptor(
  name='EncounterAttributes',
  full_name='pogoprotos.settings.master.pokemon.EncounterAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_capture_rate', full_name='pogoprotos.settings.master.pokemon.EncounterAttributes.base_capture_rate', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base_flee_rate', full_name='pogoprotos.settings.master.pokemon.EncounterAttributes.base_flee_rate', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collision_radius_m', full_name='pogoprotos.settings.master.pokemon.EncounterAttributes.collision_radius_m', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collision_height_m', full_name='pogoprotos.settings.master.pokemon.EncounterAttributes.collision_height_m', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collision_head_radius_m', full_name='pogoprotos.settings.master.pokemon.EncounterAttributes.collision_head_radius_m', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='movement_type', full_name='pogoprotos.settings.master.pokemon.EncounterAttributes.movement_type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='movement_timer_s', full_name='pogoprotos.settings.master.pokemon.EncounterAttributes.movement_timer_s', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='jump_time_s', full_name='pogoprotos.settings.master.pokemon.EncounterAttributes.jump_time_s', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attack_timer_s', full_name='pogoprotos.settings.master.pokemon.EncounterAttributes.attack_timer_s', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bonus_candy_capture_reward', full_name='pogoprotos.settings.master.pokemon.EncounterAttributes.bonus_candy_capture_reward', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bonus_stardust_capture_reward', full_name='pogoprotos.settings.master.pokemon.EncounterAttributes.bonus_stardust_capture_reward', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attack_probability', full_name='pogoprotos.settings.master.pokemon.EncounterAttributes.attack_probability', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dodge_probability', full_name='pogoprotos.settings.master.pokemon.EncounterAttributes.dodge_probability', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dodge_duration_s', full_name='pogoprotos.settings.master.pokemon.EncounterAttributes.dodge_duration_s', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dodge_distance', full_name='pogoprotos.settings.master.pokemon.EncounterAttributes.dodge_distance', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='camera_distance', full_name='pogoprotos.settings.master.pokemon.EncounterAttributes.camera_distance', index=15,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_pokemon_action_frequency_s', full_name='pogoprotos.settings.master.pokemon.EncounterAttributes.min_pokemon_action_frequency_s', index=16,
      number=17, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_pokemon_action_frequency_s', full_name='pogoprotos.settings.master.pokemon.EncounterAttributes.max_pokemon_action_frequency_s', index=17,
      number=18, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=148,
  serialized_end=727,
)

_ENCOUNTERATTRIBUTES.fields_by_name['movement_type'].enum_type = pogoprotos_dot_enums_dot_pokemon__movement__type__pb2._POKEMONMOVEMENTTYPE
DESCRIPTOR.message_types_by_name['EncounterAttributes'] = _ENCOUNTERATTRIBUTES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EncounterAttributes = _reflection.GeneratedProtocolMessageType('EncounterAttributes', (_message.Message,), dict(
  DESCRIPTOR = _ENCOUNTERATTRIBUTES,
  __module__ = 'pogoprotos.settings.master.pokemon.encounter_attributes_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.pokemon.EncounterAttributes)
  ))
_sym_db.RegisterMessage(EncounterAttributes)


# @@protoc_insertion_point(module_scope)

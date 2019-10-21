# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/gym_feed_pokemon_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.badge import awarded_gym_badge_pb2 as pogoprotos_dot_data_dot_badge_dot_awarded__gym__badge__pb2
from pogoprotos.enums import pokemon_family_id_pb2 as pogoprotos_dot_enums_dot_pokemon__family__id__pb2
from pogoprotos.data.gym import gym_status_and_defenders_pb2 as pogoprotos_dot_data_dot_gym_dot_gym__status__and__defenders__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/gym_feed_pokemon_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n?pogoprotos/networking/responses/gym_feed_pokemon_response.proto\x12\x1fpogoprotos.networking.responses\x1a-pogoprotos/data/badge/awarded_gym_badge.proto\x1a(pogoprotos/enums/pokemon_family_id.proto\x1a\x32pogoprotos/data/gym/gym_status_and_defenders.proto\"\xd4\x05\n\x16GymFeedPokemonResponse\x12N\n\x06result\x18\x01 \x01(\x0e\x32>.pogoprotos.networking.responses.GymFeedPokemonResponse.Result\x12L\n\x18gym_status_and_defenders\x18\x02 \x01(\x0b\x32*.pogoprotos.data.gym.GymStatusAndDefenders\x12\x41\n\x11\x61warded_gym_badge\x18\x03 \x01(\x0b\x32&.pogoprotos.data.badge.AwardedGymBadge\x12\x18\n\x10stardust_awarded\x18\x04 \x01(\x05\x12\x12\n\nxp_awarded\x18\x05 \x01(\x05\x12\x19\n\x11num_candy_awarded\x18\x06 \x01(\x05\x12:\n\x0f\x66\x61mily_candy_id\x18\x07 \x01(\x0e\x32!.pogoprotos.enums.PokemonFamilyId\x12\x19\n\x11\x63ooldown_complete\x18\x08 \x01(\x03\"\xb8\x02\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x14\n\x10\x45RROR_CANNOT_USE\x10\x02\x12\x16\n\x12\x45RROR_NOT_IN_RANGE\x10\x03\x12\x1b\n\x17\x45RROR_POKEMON_NOT_THERE\x10\x04\x12\x16\n\x12\x45RROR_POKEMON_FULL\x10\x05\x12\x19\n\x15\x45RROR_NO_BERRIES_LEFT\x10\x06\x12\x14\n\x10\x45RROR_WRONG_TEAM\x10\x07\x12\x15\n\x11\x45RROR_WRONG_COUNT\x10\x08\x12\x12\n\x0e\x45RROR_TOO_FAST\x10\t\x12\x16\n\x12\x45RROR_TOO_FREQUENT\x10\n\x12\x12\n\x0e\x45RROR_GYM_BUSY\x10\x0b\x12\x15\n\x11\x45RROR_RAID_ACTIVE\x10\x0c\x12\x14\n\x10\x45RROR_GYM_CLOSED\x10\rb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_badge_dot_awarded__gym__badge__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__family__id__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_gym_dot_gym__status__and__defenders__pb2.DESCRIPTOR,])



_GYMFEEDPOKEMONRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.GymFeedPokemonResponse.Result',
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
      name='ERROR_CANNOT_USE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NOT_IN_RANGE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_NOT_THERE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_FULL', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NO_BERRIES_LEFT', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_WRONG_TEAM', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_WRONG_COUNT', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_TOO_FAST', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_TOO_FREQUENT', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_GYM_BUSY', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_RAID_ACTIVE', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_GYM_CLOSED', index=13, number=13,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=654,
  serialized_end=966,
)
_sym_db.RegisterEnumDescriptor(_GYMFEEDPOKEMONRESPONSE_RESULT)


_GYMFEEDPOKEMONRESPONSE = _descriptor.Descriptor(
  name='GymFeedPokemonResponse',
  full_name='pogoprotos.networking.responses.GymFeedPokemonResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.GymFeedPokemonResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gym_status_and_defenders', full_name='pogoprotos.networking.responses.GymFeedPokemonResponse.gym_status_and_defenders', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='awarded_gym_badge', full_name='pogoprotos.networking.responses.GymFeedPokemonResponse.awarded_gym_badge', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stardust_awarded', full_name='pogoprotos.networking.responses.GymFeedPokemonResponse.stardust_awarded', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xp_awarded', full_name='pogoprotos.networking.responses.GymFeedPokemonResponse.xp_awarded', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_candy_awarded', full_name='pogoprotos.networking.responses.GymFeedPokemonResponse.num_candy_awarded', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='family_candy_id', full_name='pogoprotos.networking.responses.GymFeedPokemonResponse.family_candy_id', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cooldown_complete', full_name='pogoprotos.networking.responses.GymFeedPokemonResponse.cooldown_complete', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GYMFEEDPOKEMONRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=242,
  serialized_end=966,
)

_GYMFEEDPOKEMONRESPONSE.fields_by_name['result'].enum_type = _GYMFEEDPOKEMONRESPONSE_RESULT
_GYMFEEDPOKEMONRESPONSE.fields_by_name['gym_status_and_defenders'].message_type = pogoprotos_dot_data_dot_gym_dot_gym__status__and__defenders__pb2._GYMSTATUSANDDEFENDERS
_GYMFEEDPOKEMONRESPONSE.fields_by_name['awarded_gym_badge'].message_type = pogoprotos_dot_data_dot_badge_dot_awarded__gym__badge__pb2._AWARDEDGYMBADGE
_GYMFEEDPOKEMONRESPONSE.fields_by_name['family_candy_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__family__id__pb2._POKEMONFAMILYID
_GYMFEEDPOKEMONRESPONSE_RESULT.containing_type = _GYMFEEDPOKEMONRESPONSE
DESCRIPTOR.message_types_by_name['GymFeedPokemonResponse'] = _GYMFEEDPOKEMONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GymFeedPokemonResponse = _reflection.GeneratedProtocolMessageType('GymFeedPokemonResponse', (_message.Message,), dict(
  DESCRIPTOR = _GYMFEEDPOKEMONRESPONSE,
  __module__ = 'pogoprotos.networking.responses.gym_feed_pokemon_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GymFeedPokemonResponse)
  ))
_sym_db.RegisterMessage(GymFeedPokemonResponse)


# @@protoc_insertion_point(module_scope)

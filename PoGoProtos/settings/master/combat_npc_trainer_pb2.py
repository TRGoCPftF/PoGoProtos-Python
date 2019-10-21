# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/combat_npc_trainer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.player import player_avatar_pb2 as pogoprotos_dot_data_dot_player_dot_player__avatar__pb2
from pogoprotos.data import pokemon_display_pb2 as pogoprotos_dot_data_dot_pokemon__display__pb2
from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/combat_npc_trainer.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n3pogoprotos/settings/master/combat_npc_trainer.proto\x12\x1apogoprotos.settings.master\x1a*pogoprotos/data/player/player_avatar.proto\x1a%pogoprotos/data/pokemon_display.proto\x1a!pogoprotos/enums/pokemon_id.proto\"\x85\x04\n\x10\x43ombatNpcTrainer\x12\x14\n\x0ctrainer_name\x18\x01 \x01(\t\x12!\n\x19\x63ombat_league_template_id\x18\x02 \x01(\t\x12\x1d\n\x15\x63ombat_personality_id\x18\x03 \x01(\t\x12\x19\n\x11win_loot_table_id\x18\x04 \x01(\t\x12\x1a\n\x12lose_loot_table_id\x18\x05 \x01(\t\x12\x34\n\x06\x61vatar\x18\x07 \x01(\x0b\x32$.pogoprotos.data.player.PlayerAvatar\x12R\n\x11\x61vailable_pokemon\x18\x08 \x03(\x0b\x32\x37.pogoprotos.settings.master.CombatNpcTrainer.NpcPokemon\x12\x15\n\rtrainer_title\x18\t \x01(\t\x12\x15\n\rtrainer_quote\x18\n \x01(\t\x12\x10\n\x08icon_url\x18\x0b \x01(\t\x12\x1d\n\x15\x62\x61\x63kdrop_image_bundle\x18\x0c \x01(\t\x1ay\n\nNpcPokemon\x12\x31\n\x0cpokemon_type\x18\x01 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\x38\n\x0fpokemon_display\x18\x02 \x01(\x0b\x32\x1f.pogoprotos.data.PokemonDisplayb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_player_dot_player__avatar__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_pokemon__display__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,])




_COMBATNPCTRAINER_NPCPOKEMON = _descriptor.Descriptor(
  name='NpcPokemon',
  full_name='pogoprotos.settings.master.CombatNpcTrainer.NpcPokemon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_type', full_name='pogoprotos.settings.master.CombatNpcTrainer.NpcPokemon.pokemon_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokemon_display', full_name='pogoprotos.settings.master.CombatNpcTrainer.NpcPokemon.pokemon_display', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=598,
  serialized_end=719,
)

_COMBATNPCTRAINER = _descriptor.Descriptor(
  name='CombatNpcTrainer',
  full_name='pogoprotos.settings.master.CombatNpcTrainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trainer_name', full_name='pogoprotos.settings.master.CombatNpcTrainer.trainer_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='combat_league_template_id', full_name='pogoprotos.settings.master.CombatNpcTrainer.combat_league_template_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='combat_personality_id', full_name='pogoprotos.settings.master.CombatNpcTrainer.combat_personality_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='win_loot_table_id', full_name='pogoprotos.settings.master.CombatNpcTrainer.win_loot_table_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lose_loot_table_id', full_name='pogoprotos.settings.master.CombatNpcTrainer.lose_loot_table_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatar', full_name='pogoprotos.settings.master.CombatNpcTrainer.avatar', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='available_pokemon', full_name='pogoprotos.settings.master.CombatNpcTrainer.available_pokemon', index=6,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trainer_title', full_name='pogoprotos.settings.master.CombatNpcTrainer.trainer_title', index=7,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trainer_quote', full_name='pogoprotos.settings.master.CombatNpcTrainer.trainer_quote', index=8,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon_url', full_name='pogoprotos.settings.master.CombatNpcTrainer.icon_url', index=9,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='backdrop_image_bundle', full_name='pogoprotos.settings.master.CombatNpcTrainer.backdrop_image_bundle', index=10,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COMBATNPCTRAINER_NPCPOKEMON, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=202,
  serialized_end=719,
)

_COMBATNPCTRAINER_NPCPOKEMON.fields_by_name['pokemon_type'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_COMBATNPCTRAINER_NPCPOKEMON.fields_by_name['pokemon_display'].message_type = pogoprotos_dot_data_dot_pokemon__display__pb2._POKEMONDISPLAY
_COMBATNPCTRAINER_NPCPOKEMON.containing_type = _COMBATNPCTRAINER
_COMBATNPCTRAINER.fields_by_name['avatar'].message_type = pogoprotos_dot_data_dot_player_dot_player__avatar__pb2._PLAYERAVATAR
_COMBATNPCTRAINER.fields_by_name['available_pokemon'].message_type = _COMBATNPCTRAINER_NPCPOKEMON
DESCRIPTOR.message_types_by_name['CombatNpcTrainer'] = _COMBATNPCTRAINER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CombatNpcTrainer = _reflection.GeneratedProtocolMessageType('CombatNpcTrainer', (_message.Message,), dict(

  NpcPokemon = _reflection.GeneratedProtocolMessageType('NpcPokemon', (_message.Message,), dict(
    DESCRIPTOR = _COMBATNPCTRAINER_NPCPOKEMON,
    __module__ = 'pogoprotos.settings.master.combat_npc_trainer_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.CombatNpcTrainer.NpcPokemon)
    ))
  ,
  DESCRIPTOR = _COMBATNPCTRAINER,
  __module__ = 'pogoprotos.settings.master.combat_npc_trainer_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.CombatNpcTrainer)
  ))
_sym_db.RegisterMessage(CombatNpcTrainer)
_sym_db.RegisterMessage(CombatNpcTrainer.NpcPokemon)


# @@protoc_insertion_point(module_scope)

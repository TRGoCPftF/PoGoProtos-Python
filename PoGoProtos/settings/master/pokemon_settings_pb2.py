# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/pokemon_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import buddy_size_pb2 as pogoprotos_dot_enums_dot_buddy__size__pb2
from pogoprotos.enums import form_pb2 as pogoprotos_dot_enums_dot_form__pb2
from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2
from pogoprotos.enums import pokemon_rarity_pb2 as pogoprotos_dot_enums_dot_pokemon__rarity__pb2
from pogoprotos.enums import pokemon_type_pb2 as pogoprotos_dot_enums_dot_pokemon__type__pb2
from pogoprotos.enums import pokemon_move_pb2 as pogoprotos_dot_enums_dot_pokemon__move__pb2
from pogoprotos.enums import pokemon_family_id_pb2 as pogoprotos_dot_enums_dot_pokemon__family__id__pb2
from pogoprotos.settings.master.pokemon import stats_attributes_pb2 as pogoprotos_dot_settings_dot_master_dot_pokemon_dot_stats__attributes__pb2
from pogoprotos.settings.master.pokemon import camera_attributes_pb2 as pogoprotos_dot_settings_dot_master_dot_pokemon_dot_camera__attributes__pb2
from pogoprotos.settings.master.pokemon import encounter_attributes_pb2 as pogoprotos_dot_settings_dot_master_dot_pokemon_dot_encounter__attributes__pb2
from pogoprotos.settings.master.pokemon import evolution_branch_pb2 as pogoprotos_dot_settings_dot_master_dot_pokemon_dot_evolution__branch__pb2
from pogoprotos.settings.master.pokemon import animation_override_pb2 as pogoprotos_dot_settings_dot_master_dot_pokemon_dot_animation__override__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/pokemon_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n1pogoprotos/settings/master/pokemon_settings.proto\x12\x1apogoprotos.settings.master\x1a!pogoprotos/enums/buddy_size.proto\x1a\x1bpogoprotos/enums/form.proto\x1a!pogoprotos/enums/pokemon_id.proto\x1a%pogoprotos/enums/pokemon_rarity.proto\x1a#pogoprotos/enums/pokemon_type.proto\x1a#pogoprotos/enums/pokemon_move.proto\x1a(pogoprotos/enums/pokemon_family_id.proto\x1a\x39pogoprotos/settings/master/pokemon/stats_attributes.proto\x1a:pogoprotos/settings/master/pokemon/camera_attributes.proto\x1a=pogoprotos/settings/master/pokemon/encounter_attributes.proto\x1a\x39pogoprotos/settings/master/pokemon/evolution_branch.proto\x1a;pogoprotos/settings/master/pokemon/animation_override.proto\"\x97\x12\n\x0fPokemonSettings\x12/\n\npokemon_id\x18\x01 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\x13\n\x0bmodel_scale\x18\x03 \x01(\x02\x12+\n\x04type\x18\x04 \x01(\x0e\x32\x1d.pogoprotos.enums.PokemonType\x12-\n\x06type_2\x18\x05 \x01(\x0e\x32\x1d.pogoprotos.enums.PokemonType\x12\x44\n\x06\x63\x61mera\x18\x06 \x01(\x0b\x32\x34.pogoprotos.settings.master.pokemon.CameraAttributes\x12J\n\tencounter\x18\x07 \x01(\x0b\x32\x37.pogoprotos.settings.master.pokemon.EncounterAttributes\x12\x42\n\x05stats\x18\x08 \x01(\x0b\x32\x33.pogoprotos.settings.master.pokemon.StatsAttributes\x12\x32\n\x0bquick_moves\x18\t \x03(\x0e\x32\x1d.pogoprotos.enums.PokemonMove\x12\x36\n\x0f\x63inematic_moves\x18\n \x03(\x0e\x32\x1d.pogoprotos.enums.PokemonMove\x12\x16\n\x0e\x61nimation_time\x18\x0b \x03(\x02\x12\x32\n\revolution_ids\x18\x0c \x03(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\x16\n\x0e\x65volution_pips\x18\r \x01(\x05\x12/\n\x06rarity\x18\x0e \x01(\x0e\x32\x1f.pogoprotos.enums.PokemonRarity\x12\x18\n\x10pokedex_height_m\x18\x0f \x01(\x02\x12\x19\n\x11pokedex_weight_kg\x18\x10 \x01(\x02\x12\x36\n\x11parent_pokemon_id\x18\x11 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\x16\n\x0eheight_std_dev\x18\x12 \x01(\x02\x12\x16\n\x0eweight_std_dev\x18\x13 \x01(\x02\x12\x1c\n\x14km_distance_to_hatch\x18\x14 \x01(\x02\x12\x34\n\tfamily_id\x18\x15 \x01(\x0e\x32!.pogoprotos.enums.PokemonFamilyId\x12\x17\n\x0f\x63\x61ndy_to_evolve\x18\x16 \x01(\x05\x12\x19\n\x11km_buddy_distance\x18\x17 \x01(\x02\x12/\n\nbuddy_size\x18\x18 \x01(\x0e\x32\x1b.pogoprotos.enums.BuddySize\x12\x14\n\x0cmodel_height\x18\x19 \x01(\x02\x12M\n\x10\x65volution_branch\x18\x1a \x03(\x0b\x32\x33.pogoprotos.settings.master.pokemon.EvolutionBranch\x12\x16\n\x0emodel_scale_v2\x18\x1b \x01(\x02\x12$\n\x04\x66orm\x18\x1c \x01(\x0e\x32\x16.pogoprotos.enums.Form\x12\x37\n\x10\x65vent_quick_move\x18\x1d \x01(\x0e\x32\x1d.pogoprotos.enums.PokemonMove\x12;\n\x14\x65vent_cinematic_move\x18\x1e \x01(\x0e\x32\x1d.pogoprotos.enums.PokemonMove\x12\x19\n\x11\x62uddy_offset_male\x18\x1f \x03(\x02\x12\x1b\n\x13\x62uddy_offset_female\x18  \x03(\x02\x12\x13\n\x0b\x62uddy_scale\x18! \x01(\x02\x12\x1d\n\x15\x62uddy_portrait_offset\x18\" \x03(\x02\x12+\n\x0bparent_form\x18# \x01(\x0e\x32\x16.pogoprotos.enums.Form\x12Z\n\nthird_move\x18$ \x01(\x0b\x32\x46.pogoprotos.settings.master.PokemonSettings.PokemonThirdMoveAttributes\x12\x17\n\x0fis_transferable\x18% \x01(\x08\x12\x15\n\ris_deployable\x18& \x01(\x08\x12$\n\x1c\x63ombat_shoulder_camera_angle\x18\' \x03(\x02\x12\x13\n\x0bis_tradable\x18( \x01(\x08\x12#\n\x1b\x63ombat_default_camera_angle\x18) \x03(\x02\x12*\n\"combat_opponent_focus_camera_angle\x18* \x03(\x02\x12(\n combat_player_focus_camera_angle\x18+ \x03(\x02\x12-\n%combat_player_pokemon_position_offset\x18, \x03(\x02\x12\\\n\x1dphotobomb_animation_overrides\x18- \x03(\x0b\x32\x35.pogoprotos.settings.master.pokemon.AnimationOverride\x12L\n\x06shadow\x18. \x01(\x0b\x32<.pogoprotos.settings.master.PokemonSettings.ShadowAttributes\x12\x1a\n\x12\x62uddy_group_number\x18/ \x01(\x05\x12!\n\x19\x61\x64\x64itional_cp_boost_level\x18\x30 \x01(\x05\x1aQ\n\x1aPokemonThirdMoveAttributes\x12\x1a\n\x12stardust_to_unlock\x18\x01 \x01(\x05\x12\x17\n\x0f\x63\x61ndy_to_unlock\x18\x02 \x01(\x05\x1a\xd3\x01\n\x10ShadowAttributes\x12$\n\x1cpurification_stardust_needed\x18\x01 \x01(\r\x12!\n\x19purification_candy_needed\x18\x02 \x01(\r\x12;\n\x14purified_charge_move\x18\x03 \x01(\x0e\x32\x1d.pogoprotos.enums.PokemonMove\x12\x39\n\x12shadow_charge_move\x18\x04 \x01(\x0e\x32\x1d.pogoprotos.enums.PokemonMoveb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_buddy__size__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_form__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__rarity__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__type__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__move__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__family__id__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_pokemon_dot_stats__attributes__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_pokemon_dot_camera__attributes__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_pokemon_dot_encounter__attributes__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_pokemon_dot_evolution__branch__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_pokemon_dot_animation__override__pb2.DESCRIPTOR,])




_POKEMONSETTINGS_POKEMONTHIRDMOVEATTRIBUTES = _descriptor.Descriptor(
  name='PokemonThirdMoveAttributes',
  full_name='pogoprotos.settings.master.PokemonSettings.PokemonThirdMoveAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stardust_to_unlock', full_name='pogoprotos.settings.master.PokemonSettings.PokemonThirdMoveAttributes.stardust_to_unlock', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='candy_to_unlock', full_name='pogoprotos.settings.master.PokemonSettings.PokemonThirdMoveAttributes.candy_to_unlock', index=1,
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
  serialized_start=2670,
  serialized_end=2751,
)

_POKEMONSETTINGS_SHADOWATTRIBUTES = _descriptor.Descriptor(
  name='ShadowAttributes',
  full_name='pogoprotos.settings.master.PokemonSettings.ShadowAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='purification_stardust_needed', full_name='pogoprotos.settings.master.PokemonSettings.ShadowAttributes.purification_stardust_needed', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='purification_candy_needed', full_name='pogoprotos.settings.master.PokemonSettings.ShadowAttributes.purification_candy_needed', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='purified_charge_move', full_name='pogoprotos.settings.master.PokemonSettings.ShadowAttributes.purified_charge_move', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shadow_charge_move', full_name='pogoprotos.settings.master.PokemonSettings.ShadowAttributes.shadow_charge_move', index=3,
      number=4, type=14, cpp_type=8, label=1,
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
  serialized_start=2754,
  serialized_end=2965,
)

_POKEMONSETTINGS = _descriptor.Descriptor(
  name='PokemonSettings',
  full_name='pogoprotos.settings.master.PokemonSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.settings.master.PokemonSettings.pokemon_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_scale', full_name='pogoprotos.settings.master.PokemonSettings.model_scale', index=1,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='pogoprotos.settings.master.PokemonSettings.type', index=2,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type_2', full_name='pogoprotos.settings.master.PokemonSettings.type_2', index=3,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='camera', full_name='pogoprotos.settings.master.PokemonSettings.camera', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encounter', full_name='pogoprotos.settings.master.PokemonSettings.encounter', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stats', full_name='pogoprotos.settings.master.PokemonSettings.stats', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quick_moves', full_name='pogoprotos.settings.master.PokemonSettings.quick_moves', index=7,
      number=9, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cinematic_moves', full_name='pogoprotos.settings.master.PokemonSettings.cinematic_moves', index=8,
      number=10, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='animation_time', full_name='pogoprotos.settings.master.PokemonSettings.animation_time', index=9,
      number=11, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='evolution_ids', full_name='pogoprotos.settings.master.PokemonSettings.evolution_ids', index=10,
      number=12, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='evolution_pips', full_name='pogoprotos.settings.master.PokemonSettings.evolution_pips', index=11,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rarity', full_name='pogoprotos.settings.master.PokemonSettings.rarity', index=12,
      number=14, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokedex_height_m', full_name='pogoprotos.settings.master.PokemonSettings.pokedex_height_m', index=13,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokedex_weight_kg', full_name='pogoprotos.settings.master.PokemonSettings.pokedex_weight_kg', index=14,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent_pokemon_id', full_name='pogoprotos.settings.master.PokemonSettings.parent_pokemon_id', index=15,
      number=17, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height_std_dev', full_name='pogoprotos.settings.master.PokemonSettings.height_std_dev', index=16,
      number=18, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight_std_dev', full_name='pogoprotos.settings.master.PokemonSettings.weight_std_dev', index=17,
      number=19, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='km_distance_to_hatch', full_name='pogoprotos.settings.master.PokemonSettings.km_distance_to_hatch', index=18,
      number=20, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='family_id', full_name='pogoprotos.settings.master.PokemonSettings.family_id', index=19,
      number=21, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='candy_to_evolve', full_name='pogoprotos.settings.master.PokemonSettings.candy_to_evolve', index=20,
      number=22, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='km_buddy_distance', full_name='pogoprotos.settings.master.PokemonSettings.km_buddy_distance', index=21,
      number=23, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buddy_size', full_name='pogoprotos.settings.master.PokemonSettings.buddy_size', index=22,
      number=24, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_height', full_name='pogoprotos.settings.master.PokemonSettings.model_height', index=23,
      number=25, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='evolution_branch', full_name='pogoprotos.settings.master.PokemonSettings.evolution_branch', index=24,
      number=26, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_scale_v2', full_name='pogoprotos.settings.master.PokemonSettings.model_scale_v2', index=25,
      number=27, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='form', full_name='pogoprotos.settings.master.PokemonSettings.form', index=26,
      number=28, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_quick_move', full_name='pogoprotos.settings.master.PokemonSettings.event_quick_move', index=27,
      number=29, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_cinematic_move', full_name='pogoprotos.settings.master.PokemonSettings.event_cinematic_move', index=28,
      number=30, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buddy_offset_male', full_name='pogoprotos.settings.master.PokemonSettings.buddy_offset_male', index=29,
      number=31, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buddy_offset_female', full_name='pogoprotos.settings.master.PokemonSettings.buddy_offset_female', index=30,
      number=32, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buddy_scale', full_name='pogoprotos.settings.master.PokemonSettings.buddy_scale', index=31,
      number=33, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buddy_portrait_offset', full_name='pogoprotos.settings.master.PokemonSettings.buddy_portrait_offset', index=32,
      number=34, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent_form', full_name='pogoprotos.settings.master.PokemonSettings.parent_form', index=33,
      number=35, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='third_move', full_name='pogoprotos.settings.master.PokemonSettings.third_move', index=34,
      number=36, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_transferable', full_name='pogoprotos.settings.master.PokemonSettings.is_transferable', index=35,
      number=37, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_deployable', full_name='pogoprotos.settings.master.PokemonSettings.is_deployable', index=36,
      number=38, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='combat_shoulder_camera_angle', full_name='pogoprotos.settings.master.PokemonSettings.combat_shoulder_camera_angle', index=37,
      number=39, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_tradable', full_name='pogoprotos.settings.master.PokemonSettings.is_tradable', index=38,
      number=40, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='combat_default_camera_angle', full_name='pogoprotos.settings.master.PokemonSettings.combat_default_camera_angle', index=39,
      number=41, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='combat_opponent_focus_camera_angle', full_name='pogoprotos.settings.master.PokemonSettings.combat_opponent_focus_camera_angle', index=40,
      number=42, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='combat_player_focus_camera_angle', full_name='pogoprotos.settings.master.PokemonSettings.combat_player_focus_camera_angle', index=41,
      number=43, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='combat_player_pokemon_position_offset', full_name='pogoprotos.settings.master.PokemonSettings.combat_player_pokemon_position_offset', index=42,
      number=44, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='photobomb_animation_overrides', full_name='pogoprotos.settings.master.PokemonSettings.photobomb_animation_overrides', index=43,
      number=45, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shadow', full_name='pogoprotos.settings.master.PokemonSettings.shadow', index=44,
      number=46, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buddy_group_number', full_name='pogoprotos.settings.master.PokemonSettings.buddy_group_number', index=45,
      number=47, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='additional_cp_boost_level', full_name='pogoprotos.settings.master.PokemonSettings.additional_cp_boost_level', index=46,
      number=48, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_POKEMONSETTINGS_POKEMONTHIRDMOVEATTRIBUTES, _POKEMONSETTINGS_SHADOWATTRIBUTES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=638,
  serialized_end=2965,
)

_POKEMONSETTINGS_POKEMONTHIRDMOVEATTRIBUTES.containing_type = _POKEMONSETTINGS
_POKEMONSETTINGS_SHADOWATTRIBUTES.fields_by_name['purified_charge_move'].enum_type = pogoprotos_dot_enums_dot_pokemon__move__pb2._POKEMONMOVE
_POKEMONSETTINGS_SHADOWATTRIBUTES.fields_by_name['shadow_charge_move'].enum_type = pogoprotos_dot_enums_dot_pokemon__move__pb2._POKEMONMOVE
_POKEMONSETTINGS_SHADOWATTRIBUTES.containing_type = _POKEMONSETTINGS
_POKEMONSETTINGS.fields_by_name['pokemon_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_POKEMONSETTINGS.fields_by_name['type'].enum_type = pogoprotos_dot_enums_dot_pokemon__type__pb2._POKEMONTYPE
_POKEMONSETTINGS.fields_by_name['type_2'].enum_type = pogoprotos_dot_enums_dot_pokemon__type__pb2._POKEMONTYPE
_POKEMONSETTINGS.fields_by_name['camera'].message_type = pogoprotos_dot_settings_dot_master_dot_pokemon_dot_camera__attributes__pb2._CAMERAATTRIBUTES
_POKEMONSETTINGS.fields_by_name['encounter'].message_type = pogoprotos_dot_settings_dot_master_dot_pokemon_dot_encounter__attributes__pb2._ENCOUNTERATTRIBUTES
_POKEMONSETTINGS.fields_by_name['stats'].message_type = pogoprotos_dot_settings_dot_master_dot_pokemon_dot_stats__attributes__pb2._STATSATTRIBUTES
_POKEMONSETTINGS.fields_by_name['quick_moves'].enum_type = pogoprotos_dot_enums_dot_pokemon__move__pb2._POKEMONMOVE
_POKEMONSETTINGS.fields_by_name['cinematic_moves'].enum_type = pogoprotos_dot_enums_dot_pokemon__move__pb2._POKEMONMOVE
_POKEMONSETTINGS.fields_by_name['evolution_ids'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_POKEMONSETTINGS.fields_by_name['rarity'].enum_type = pogoprotos_dot_enums_dot_pokemon__rarity__pb2._POKEMONRARITY
_POKEMONSETTINGS.fields_by_name['parent_pokemon_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_POKEMONSETTINGS.fields_by_name['family_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__family__id__pb2._POKEMONFAMILYID
_POKEMONSETTINGS.fields_by_name['buddy_size'].enum_type = pogoprotos_dot_enums_dot_buddy__size__pb2._BUDDYSIZE
_POKEMONSETTINGS.fields_by_name['evolution_branch'].message_type = pogoprotos_dot_settings_dot_master_dot_pokemon_dot_evolution__branch__pb2._EVOLUTIONBRANCH
_POKEMONSETTINGS.fields_by_name['form'].enum_type = pogoprotos_dot_enums_dot_form__pb2._FORM
_POKEMONSETTINGS.fields_by_name['event_quick_move'].enum_type = pogoprotos_dot_enums_dot_pokemon__move__pb2._POKEMONMOVE
_POKEMONSETTINGS.fields_by_name['event_cinematic_move'].enum_type = pogoprotos_dot_enums_dot_pokemon__move__pb2._POKEMONMOVE
_POKEMONSETTINGS.fields_by_name['parent_form'].enum_type = pogoprotos_dot_enums_dot_form__pb2._FORM
_POKEMONSETTINGS.fields_by_name['third_move'].message_type = _POKEMONSETTINGS_POKEMONTHIRDMOVEATTRIBUTES
_POKEMONSETTINGS.fields_by_name['photobomb_animation_overrides'].message_type = pogoprotos_dot_settings_dot_master_dot_pokemon_dot_animation__override__pb2._ANIMATIONOVERRIDE
_POKEMONSETTINGS.fields_by_name['shadow'].message_type = _POKEMONSETTINGS_SHADOWATTRIBUTES
DESCRIPTOR.message_types_by_name['PokemonSettings'] = _POKEMONSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PokemonSettings = _reflection.GeneratedProtocolMessageType('PokemonSettings', (_message.Message,), dict(

  PokemonThirdMoveAttributes = _reflection.GeneratedProtocolMessageType('PokemonThirdMoveAttributes', (_message.Message,), dict(
    DESCRIPTOR = _POKEMONSETTINGS_POKEMONTHIRDMOVEATTRIBUTES,
    __module__ = 'pogoprotos.settings.master.pokemon_settings_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.PokemonSettings.PokemonThirdMoveAttributes)
    ))
  ,

  ShadowAttributes = _reflection.GeneratedProtocolMessageType('ShadowAttributes', (_message.Message,), dict(
    DESCRIPTOR = _POKEMONSETTINGS_SHADOWATTRIBUTES,
    __module__ = 'pogoprotos.settings.master.pokemon_settings_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.PokemonSettings.ShadowAttributes)
    ))
  ,
  DESCRIPTOR = _POKEMONSETTINGS,
  __module__ = 'pogoprotos.settings.master.pokemon_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.PokemonSettings)
  ))
_sym_db.RegisterMessage(PokemonSettings)
_sym_db.RegisterMessage(PokemonSettings.PokemonThirdMoveAttributes)
_sym_db.RegisterMessage(PokemonSettings.ShadowAttributes)


# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/combat_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/combat_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n0pogoprotos/settings/master/combat_settings.proto\x12\x1apogoprotos.settings.master\"\xb1\x0c\n\x0e\x43ombatSettings\x12\x1e\n\x16round_duration_seconds\x18\x01 \x01(\x02\x12\x1d\n\x15turn_duration_seconds\x18\x02 \x01(\x02\x12!\n\x19minigame_duration_seconds\x18\x03 \x01(\x02\x12)\n!same_type_attack_bonus_multiplier\x18\x04 \x01(\x02\x12$\n\x1c\x66\x61st_attack_bonus_multiplier\x18\x05 \x01(\x02\x12&\n\x1e\x63harge_attack_bonus_multiplier\x18\x06 \x01(\x02\x12 \n\x18\x64\x65\x66\x65nse_bonus_multiplier\x18\x07 \x01(\x02\x12&\n\x1eminigame_bonus_base_multiplier\x18\x08 \x01(\x02\x12*\n\"minigame_bonus_variable_multiplier\x18\t \x01(\x02\x12\x12\n\nmax_energy\x18\n \x01(\x05\x12$\n\x1c\x64\x65\x66\x65nder_minigame_multiplier\x18\x0b \x01(\x02\x12\'\n\x1f\x63hange_pokemon_duration_seconds\x18\x0c \x01(\x02\x12.\n&minigame_submit_score_duration_seconds\x18\r \x01(\x02\x12\x31\n)quick_swap_combat_start_available_seconds\x18\x0e \x01(\x02\x12,\n$quick_swap_cooldown_duration_seconds\x18\x0f \x01(\x02\x12|\n\"offensive_input_challenge_settings\x18\x10 \x01(\x0b\x32P.pogoprotos.settings.master.CombatSettings.CombatOffensiveInputChallengeSettings\x12|\n\"defensive_input_challenge_settings\x18\x11 \x01(\x0b\x32P.pogoprotos.settings.master.CombatSettings.CombatDefensiveInputChallengeSettings\x12\x19\n\x11\x63harge_score_base\x18\x12 \x01(\x02\x12\x19\n\x11\x63harge_score_nice\x18\x13 \x01(\x02\x12\x1a\n\x12\x63harge_score_great\x18\x14 \x01(\x02\x12\x1e\n\x16\x63harge_score_excellent\x18\x15 \x01(\x02\x12%\n\x1dswap_animation_duration_turns\x18\x16 \x01(\x05\x12-\n%super_effective_flyout_duration_turns\x18\x17 \x01(\x05\x12\x30\n(not_very_effective_flyout_duration_turns\x18\x18 \x01(\x05\x12%\n\x1d\x62locked_flyout_duration_turns\x18\x19 \x01(\x05\x12.\n&normal_effective_flyout_duration_turns\x18\x1a \x01(\x05\x12&\n\x1e\x66\x61int_animation_duration_turns\x18\x1b \x01(\x05\x12\x1c\n\x14npc_swap_delay_turns\x18\x1c \x01(\x05\x12&\n\x1enpc_charged_attack_delay_turns\x18\x1d \x01(\x05\x1a\xcf\x01\n%CombatOffensiveInputChallengeSettings\x12\x15\n\rscore_per_tap\x18\x01 \x01(\x02\x12\x1e\n\x16score_decay_per_second\x18\x02 \x01(\x02\x12\x11\n\tmax_score\x18\x03 \x01(\x02\x12.\n&high_score_additional_decay_per_second\x18\x04 \x01(\x02\x12,\n$max_time_additional_decay_per_second\x18\x05 \x01(\x02\x1aM\n%CombatDefensiveInputChallengeSettings\x12$\n\x1c\x66ull_rotations_for_max_score\x18\x01 \x01(\x02\x62\x06proto3')
)




_COMBATSETTINGS_COMBATOFFENSIVEINPUTCHALLENGESETTINGS = _descriptor.Descriptor(
  name='CombatOffensiveInputChallengeSettings',
  full_name='pogoprotos.settings.master.CombatSettings.CombatOffensiveInputChallengeSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='score_per_tap', full_name='pogoprotos.settings.master.CombatSettings.CombatOffensiveInputChallengeSettings.score_per_tap', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score_decay_per_second', full_name='pogoprotos.settings.master.CombatSettings.CombatOffensiveInputChallengeSettings.score_decay_per_second', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_score', full_name='pogoprotos.settings.master.CombatSettings.CombatOffensiveInputChallengeSettings.max_score', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='high_score_additional_decay_per_second', full_name='pogoprotos.settings.master.CombatSettings.CombatOffensiveInputChallengeSettings.high_score_additional_decay_per_second', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_time_additional_decay_per_second', full_name='pogoprotos.settings.master.CombatSettings.CombatOffensiveInputChallengeSettings.max_time_additional_decay_per_second', index=4,
      number=5, type=2, cpp_type=6, label=1,
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
  serialized_start=1380,
  serialized_end=1587,
)

_COMBATSETTINGS_COMBATDEFENSIVEINPUTCHALLENGESETTINGS = _descriptor.Descriptor(
  name='CombatDefensiveInputChallengeSettings',
  full_name='pogoprotos.settings.master.CombatSettings.CombatDefensiveInputChallengeSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='full_rotations_for_max_score', full_name='pogoprotos.settings.master.CombatSettings.CombatDefensiveInputChallengeSettings.full_rotations_for_max_score', index=0,
      number=1, type=2, cpp_type=6, label=1,
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
  serialized_start=1589,
  serialized_end=1666,
)

_COMBATSETTINGS = _descriptor.Descriptor(
  name='CombatSettings',
  full_name='pogoprotos.settings.master.CombatSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='round_duration_seconds', full_name='pogoprotos.settings.master.CombatSettings.round_duration_seconds', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='turn_duration_seconds', full_name='pogoprotos.settings.master.CombatSettings.turn_duration_seconds', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minigame_duration_seconds', full_name='pogoprotos.settings.master.CombatSettings.minigame_duration_seconds', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='same_type_attack_bonus_multiplier', full_name='pogoprotos.settings.master.CombatSettings.same_type_attack_bonus_multiplier', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fast_attack_bonus_multiplier', full_name='pogoprotos.settings.master.CombatSettings.fast_attack_bonus_multiplier', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='charge_attack_bonus_multiplier', full_name='pogoprotos.settings.master.CombatSettings.charge_attack_bonus_multiplier', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defense_bonus_multiplier', full_name='pogoprotos.settings.master.CombatSettings.defense_bonus_multiplier', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minigame_bonus_base_multiplier', full_name='pogoprotos.settings.master.CombatSettings.minigame_bonus_base_multiplier', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minigame_bonus_variable_multiplier', full_name='pogoprotos.settings.master.CombatSettings.minigame_bonus_variable_multiplier', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_energy', full_name='pogoprotos.settings.master.CombatSettings.max_energy', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defender_minigame_multiplier', full_name='pogoprotos.settings.master.CombatSettings.defender_minigame_multiplier', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='change_pokemon_duration_seconds', full_name='pogoprotos.settings.master.CombatSettings.change_pokemon_duration_seconds', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minigame_submit_score_duration_seconds', full_name='pogoprotos.settings.master.CombatSettings.minigame_submit_score_duration_seconds', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quick_swap_combat_start_available_seconds', full_name='pogoprotos.settings.master.CombatSettings.quick_swap_combat_start_available_seconds', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quick_swap_cooldown_duration_seconds', full_name='pogoprotos.settings.master.CombatSettings.quick_swap_cooldown_duration_seconds', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offensive_input_challenge_settings', full_name='pogoprotos.settings.master.CombatSettings.offensive_input_challenge_settings', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defensive_input_challenge_settings', full_name='pogoprotos.settings.master.CombatSettings.defensive_input_challenge_settings', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='charge_score_base', full_name='pogoprotos.settings.master.CombatSettings.charge_score_base', index=17,
      number=18, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='charge_score_nice', full_name='pogoprotos.settings.master.CombatSettings.charge_score_nice', index=18,
      number=19, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='charge_score_great', full_name='pogoprotos.settings.master.CombatSettings.charge_score_great', index=19,
      number=20, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='charge_score_excellent', full_name='pogoprotos.settings.master.CombatSettings.charge_score_excellent', index=20,
      number=21, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='swap_animation_duration_turns', full_name='pogoprotos.settings.master.CombatSettings.swap_animation_duration_turns', index=21,
      number=22, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='super_effective_flyout_duration_turns', full_name='pogoprotos.settings.master.CombatSettings.super_effective_flyout_duration_turns', index=22,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='not_very_effective_flyout_duration_turns', full_name='pogoprotos.settings.master.CombatSettings.not_very_effective_flyout_duration_turns', index=23,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blocked_flyout_duration_turns', full_name='pogoprotos.settings.master.CombatSettings.blocked_flyout_duration_turns', index=24,
      number=25, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='normal_effective_flyout_duration_turns', full_name='pogoprotos.settings.master.CombatSettings.normal_effective_flyout_duration_turns', index=25,
      number=26, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='faint_animation_duration_turns', full_name='pogoprotos.settings.master.CombatSettings.faint_animation_duration_turns', index=26,
      number=27, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='npc_swap_delay_turns', full_name='pogoprotos.settings.master.CombatSettings.npc_swap_delay_turns', index=27,
      number=28, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='npc_charged_attack_delay_turns', full_name='pogoprotos.settings.master.CombatSettings.npc_charged_attack_delay_turns', index=28,
      number=29, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COMBATSETTINGS_COMBATOFFENSIVEINPUTCHALLENGESETTINGS, _COMBATSETTINGS_COMBATDEFENSIVEINPUTCHALLENGESETTINGS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=1666,
)

_COMBATSETTINGS_COMBATOFFENSIVEINPUTCHALLENGESETTINGS.containing_type = _COMBATSETTINGS
_COMBATSETTINGS_COMBATDEFENSIVEINPUTCHALLENGESETTINGS.containing_type = _COMBATSETTINGS
_COMBATSETTINGS.fields_by_name['offensive_input_challenge_settings'].message_type = _COMBATSETTINGS_COMBATOFFENSIVEINPUTCHALLENGESETTINGS
_COMBATSETTINGS.fields_by_name['defensive_input_challenge_settings'].message_type = _COMBATSETTINGS_COMBATDEFENSIVEINPUTCHALLENGESETTINGS
DESCRIPTOR.message_types_by_name['CombatSettings'] = _COMBATSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CombatSettings = _reflection.GeneratedProtocolMessageType('CombatSettings', (_message.Message,), dict(

  CombatOffensiveInputChallengeSettings = _reflection.GeneratedProtocolMessageType('CombatOffensiveInputChallengeSettings', (_message.Message,), dict(
    DESCRIPTOR = _COMBATSETTINGS_COMBATOFFENSIVEINPUTCHALLENGESETTINGS,
    __module__ = 'pogoprotos.settings.master.combat_settings_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.CombatSettings.CombatOffensiveInputChallengeSettings)
    ))
  ,

  CombatDefensiveInputChallengeSettings = _reflection.GeneratedProtocolMessageType('CombatDefensiveInputChallengeSettings', (_message.Message,), dict(
    DESCRIPTOR = _COMBATSETTINGS_COMBATDEFENSIVEINPUTCHALLENGESETTINGS,
    __module__ = 'pogoprotos.settings.master.combat_settings_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.CombatSettings.CombatDefensiveInputChallengeSettings)
    ))
  ,
  DESCRIPTOR = _COMBATSETTINGS,
  __module__ = 'pogoprotos.settings.master.combat_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.CombatSettings)
  ))
_sym_db.RegisterMessage(CombatSettings)
_sym_db.RegisterMessage(CombatSettings.CombatOffensiveInputChallengeSettings)
_sym_db.RegisterMessage(CombatSettings.CombatDefensiveInputChallengeSettings)


# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/logs/action_log_entry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.logs import catch_pokemon_log_entry_pb2 as pogoprotos_dot_data_dot_logs_dot_catch__pokemon__log__entry__pb2
from pogoprotos.data.logs import fort_search_log_entry_pb2 as pogoprotos_dot_data_dot_logs_dot_fort__search__log__entry__pb2
from pogoprotos.data.logs import buddy_pokemon_log_entry_pb2 as pogoprotos_dot_data_dot_logs_dot_buddy__pokemon__log__entry__pb2
from pogoprotos.data.logs import raid_rewards_log_entry_pb2 as pogoprotos_dot_data_dot_logs_dot_raid__rewards__log__entry__pb2
from pogoprotos.data.logs import passcode_rewards_log_entry_pb2 as pogoprotos_dot_data_dot_logs_dot_passcode__rewards__log__entry__pb2
from pogoprotos.data.logs import complete_quest_log_entry_pb2 as pogoprotos_dot_data_dot_logs_dot_complete__quest__log__entry__pb2
from pogoprotos.data.logs import complete_quest_stamp_card_log_entry_pb2 as pogoprotos_dot_data_dot_logs_dot_complete__quest__stamp__card__log__entry__pb2
from pogoprotos.data.logs import complete_quest_pokemon_encounter_log_entry_pb2 as pogoprotos_dot_data_dot_logs_dot_complete__quest__pokemon__encounter__log__entry__pb2
from pogoprotos.data.logs import open_gift_log_entry_pb2 as pogoprotos_dot_data_dot_logs_dot_open__gift__log__entry__pb2
from pogoprotos.data.logs import send_gift_log_entry_pb2 as pogoprotos_dot_data_dot_logs_dot_send__gift__log__entry__pb2
from pogoprotos.data.logs import trading_log_entry_pb2 as pogoprotos_dot_data_dot_logs_dot_trading__log__entry__pb2
from pogoprotos.data.logs import share_ex_raid_pass_log_entry_pb2 as pogoprotos_dot_data_dot_logs_dot_share__ex__raid__pass__log__entry__pb2
from pogoprotos.data.logs import decline_ex_raid_pass_log_entry_pb2 as pogoprotos_dot_data_dot_logs_dot_decline__ex__raid__pass__log__entry__pb2
from pogoprotos.data.logs import fitness_rewards_log_entry_pb2 as pogoprotos_dot_data_dot_logs_dot_fitness__rewards__log__entry__pb2
from pogoprotos.data.logs import beluga_daily_transfer_log_entry_pb2 as pogoprotos_dot_data_dot_logs_dot_beluga__daily__transfer__log__entry__pb2
from pogoprotos.data.logs import combat_log_entry_pb2 as pogoprotos_dot_data_dot_logs_dot_combat__log__entry__pb2
from pogoprotos.data.logs import purify_pokemon_log_entry_pb2 as pogoprotos_dot_data_dot_logs_dot_purify__pokemon__log__entry__pb2
from pogoprotos.data.logs import invasion_victory_log_entry_pb2 as pogoprotos_dot_data_dot_logs_dot_invasion__victory__log__entry__pb2
from pogoprotos.data.logs import vs_seeker_set_log_entry_pb2 as pogoprotos_dot_data_dot_logs_dot_vs__seeker__set__log__entry__pb2
from pogoprotos.data.logs import vs_seeker_complete_season_log_entry_pb2 as pogoprotos_dot_data_dot_logs_dot_vs__seeker__complete__season__log__entry__pb2
from pogoprotos.data.logs import vs_seeker_win_rewards_log_entry_pb2 as pogoprotos_dot_data_dot_logs_dot_vs__seeker__win__rewards__log__entry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/logs/action_log_entry.proto',
  package='pogoprotos.data.logs',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n+pogoprotos/data/logs/action_log_entry.proto\x12\x14pogoprotos.data.logs\x1a\x32pogoprotos/data/logs/catch_pokemon_log_entry.proto\x1a\x30pogoprotos/data/logs/fort_search_log_entry.proto\x1a\x32pogoprotos/data/logs/buddy_pokemon_log_entry.proto\x1a\x31pogoprotos/data/logs/raid_rewards_log_entry.proto\x1a\x35pogoprotos/data/logs/passcode_rewards_log_entry.proto\x1a\x33pogoprotos/data/logs/complete_quest_log_entry.proto\x1a>pogoprotos/data/logs/complete_quest_stamp_card_log_entry.proto\x1a\x45pogoprotos/data/logs/complete_quest_pokemon_encounter_log_entry.proto\x1a.pogoprotos/data/logs/open_gift_log_entry.proto\x1a.pogoprotos/data/logs/send_gift_log_entry.proto\x1a,pogoprotos/data/logs/trading_log_entry.proto\x1a\x37pogoprotos/data/logs/share_ex_raid_pass_log_entry.proto\x1a\x39pogoprotos/data/logs/decline_ex_raid_pass_log_entry.proto\x1a\x34pogoprotos/data/logs/fitness_rewards_log_entry.proto\x1a:pogoprotos/data/logs/beluga_daily_transfer_log_entry.proto\x1a+pogoprotos/data/logs/combat_log_entry.proto\x1a\x33pogoprotos/data/logs/purify_pokemon_log_entry.proto\x1a\x35pogoprotos/data/logs/invasion_victory_log_entry.proto\x1a\x32pogoprotos/data/logs/vs_seeker_set_log_entry.proto\x1a>pogoprotos/data/logs/vs_seeker_complete_season_log_entry.proto\x1a:pogoprotos/data/logs/vs_seeker_win_rewards_log_entry.proto\"\xc8\x0c\n\x0e\x41\x63tionLogEntry\x12\x14\n\x0ctimestamp_ms\x18\x01 \x01(\x03\x12\r\n\x05sfida\x18\x02 \x01(\x08\x12\x43\n\rcatch_pokemon\x18\x03 \x01(\x0b\x32*.pogoprotos.data.logs.CatchPokemonLogEntryH\x00\x12?\n\x0b\x66ort_search\x18\x04 \x01(\x0b\x32(.pogoprotos.data.logs.FortSearchLogEntryH\x00\x12\x43\n\rbuddy_pokemon\x18\x05 \x01(\x0b\x32*.pogoprotos.data.logs.BuddyPokemonLogEntryH\x00\x12\x41\n\x0craid_rewards\x18\x06 \x01(\x0b\x32).pogoprotos.data.logs.RaidRewardsLogEntryH\x00\x12I\n\x10passcode_rewards\x18\x07 \x01(\x0b\x32-.pogoprotos.data.logs.PasscodeRewardsLogEntryH\x00\x12\x45\n\x0e\x63omplete_quest\x18\x08 \x01(\x0b\x32+.pogoprotos.data.logs.CompleteQuestLogEntryH\x00\x12Y\n\x19\x63omplete_quest_stamp_card\x18\t \x01(\x0b\x32\x34.pogoprotos.data.logs.CompleteQuestStampCardLogEntryH\x00\x12g\n complete_quest_pokemon_encounter\x18\n \x01(\x0b\x32;.pogoprotos.data.logs.CompleteQuestPokemonEncounterLogEntryH\x00\x12L\n\x0f\x62\x65luga_transfer\x18\x0b \x01(\x0b\x32\x31.pogoprotos.data.logs.BelugaDailyTransferLogEntryH\x00\x12;\n\topen_gift\x18\x0c \x01(\x0b\x32&.pogoprotos.data.logs.OpenGiftLogEntryH\x00\x12;\n\tsend_gift\x18\r \x01(\x0b\x32&.pogoprotos.data.logs.SendGiftLogEntryH\x00\x12\x38\n\x07trading\x18\x0e \x01(\x0b\x32%.pogoprotos.data.logs.TradingLogEntryH\x00\x12K\n\x12share_ex_raid_pass\x18\x0f \x01(\x0b\x32-.pogoprotos.data.logs.ShareExRaidPassLogEntryH\x00\x12O\n\x14\x64\x65\x63line_ex_raid_pass\x18\x10 \x01(\x0b\x32/.pogoprotos.data.logs.DeclineExRaidPassLogEntryH\x00\x12G\n\x0f\x66itness_rewards\x18\x11 \x01(\x0b\x32,.pogoprotos.data.logs.FitnessRewardsLogEntryH\x00\x12\x36\n\x06\x63ombat\x18\x12 \x01(\x0b\x32$.pogoprotos.data.logs.CombatLogEntryH\x00\x12\x45\n\x0epurify_pokemon\x18\x13 \x01(\x0b\x32+.pogoprotos.data.logs.PurifyPokemonLogEntryH\x00\x12I\n\x10invasion_victory\x18\x14 \x01(\x0b\x32-.pogoprotos.data.logs.InvasionVictoryLogEntryH\x00\x12\x42\n\rvs_seeker_set\x18\x15 \x01(\x0b\x32).pogoprotos.data.logs.VsSeekerSetLogEntryH\x00\x12Y\n\x19vs_seeker_complete_season\x18\x16 \x01(\x0b\x32\x34.pogoprotos.data.logs.VsSeekerCompleteSeasonLogEntryH\x00\x12Q\n\x15vs_seeker_win_rewards\x18\x17 \x01(\x0b\x32\x30.pogoprotos.data.logs.VsSeekerWinRewardsLogEntryH\x00\x42\x08\n\x06\x41\x63tionb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_logs_dot_catch__pokemon__log__entry__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_logs_dot_fort__search__log__entry__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_logs_dot_buddy__pokemon__log__entry__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_logs_dot_raid__rewards__log__entry__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_logs_dot_passcode__rewards__log__entry__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_logs_dot_complete__quest__log__entry__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_logs_dot_complete__quest__stamp__card__log__entry__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_logs_dot_complete__quest__pokemon__encounter__log__entry__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_logs_dot_open__gift__log__entry__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_logs_dot_send__gift__log__entry__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_logs_dot_trading__log__entry__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_logs_dot_share__ex__raid__pass__log__entry__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_logs_dot_decline__ex__raid__pass__log__entry__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_logs_dot_fitness__rewards__log__entry__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_logs_dot_beluga__daily__transfer__log__entry__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_logs_dot_combat__log__entry__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_logs_dot_purify__pokemon__log__entry__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_logs_dot_invasion__victory__log__entry__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_logs_dot_vs__seeker__set__log__entry__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_logs_dot_vs__seeker__complete__season__log__entry__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_logs_dot_vs__seeker__win__rewards__log__entry__pb2.DESCRIPTOR,])




_ACTIONLOGENTRY = _descriptor.Descriptor(
  name='ActionLogEntry',
  full_name='pogoprotos.data.logs.ActionLogEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp_ms', full_name='pogoprotos.data.logs.ActionLogEntry.timestamp_ms', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sfida', full_name='pogoprotos.data.logs.ActionLogEntry.sfida', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='catch_pokemon', full_name='pogoprotos.data.logs.ActionLogEntry.catch_pokemon', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fort_search', full_name='pogoprotos.data.logs.ActionLogEntry.fort_search', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buddy_pokemon', full_name='pogoprotos.data.logs.ActionLogEntry.buddy_pokemon', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raid_rewards', full_name='pogoprotos.data.logs.ActionLogEntry.raid_rewards', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='passcode_rewards', full_name='pogoprotos.data.logs.ActionLogEntry.passcode_rewards', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='complete_quest', full_name='pogoprotos.data.logs.ActionLogEntry.complete_quest', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='complete_quest_stamp_card', full_name='pogoprotos.data.logs.ActionLogEntry.complete_quest_stamp_card', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='complete_quest_pokemon_encounter', full_name='pogoprotos.data.logs.ActionLogEntry.complete_quest_pokemon_encounter', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='beluga_transfer', full_name='pogoprotos.data.logs.ActionLogEntry.beluga_transfer', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='open_gift', full_name='pogoprotos.data.logs.ActionLogEntry.open_gift', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='send_gift', full_name='pogoprotos.data.logs.ActionLogEntry.send_gift', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trading', full_name='pogoprotos.data.logs.ActionLogEntry.trading', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='share_ex_raid_pass', full_name='pogoprotos.data.logs.ActionLogEntry.share_ex_raid_pass', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='decline_ex_raid_pass', full_name='pogoprotos.data.logs.ActionLogEntry.decline_ex_raid_pass', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fitness_rewards', full_name='pogoprotos.data.logs.ActionLogEntry.fitness_rewards', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='combat', full_name='pogoprotos.data.logs.ActionLogEntry.combat', index=17,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='purify_pokemon', full_name='pogoprotos.data.logs.ActionLogEntry.purify_pokemon', index=18,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='invasion_victory', full_name='pogoprotos.data.logs.ActionLogEntry.invasion_victory', index=19,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vs_seeker_set', full_name='pogoprotos.data.logs.ActionLogEntry.vs_seeker_set', index=20,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vs_seeker_complete_season', full_name='pogoprotos.data.logs.ActionLogEntry.vs_seeker_complete_season', index=21,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vs_seeker_win_rewards', full_name='pogoprotos.data.logs.ActionLogEntry.vs_seeker_win_rewards', index=22,
      number=23, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='Action', full_name='pogoprotos.data.logs.ActionLogEntry.Action',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1219,
  serialized_end=2827,
)

_ACTIONLOGENTRY.fields_by_name['catch_pokemon'].message_type = pogoprotos_dot_data_dot_logs_dot_catch__pokemon__log__entry__pb2._CATCHPOKEMONLOGENTRY
_ACTIONLOGENTRY.fields_by_name['fort_search'].message_type = pogoprotos_dot_data_dot_logs_dot_fort__search__log__entry__pb2._FORTSEARCHLOGENTRY
_ACTIONLOGENTRY.fields_by_name['buddy_pokemon'].message_type = pogoprotos_dot_data_dot_logs_dot_buddy__pokemon__log__entry__pb2._BUDDYPOKEMONLOGENTRY
_ACTIONLOGENTRY.fields_by_name['raid_rewards'].message_type = pogoprotos_dot_data_dot_logs_dot_raid__rewards__log__entry__pb2._RAIDREWARDSLOGENTRY
_ACTIONLOGENTRY.fields_by_name['passcode_rewards'].message_type = pogoprotos_dot_data_dot_logs_dot_passcode__rewards__log__entry__pb2._PASSCODEREWARDSLOGENTRY
_ACTIONLOGENTRY.fields_by_name['complete_quest'].message_type = pogoprotos_dot_data_dot_logs_dot_complete__quest__log__entry__pb2._COMPLETEQUESTLOGENTRY
_ACTIONLOGENTRY.fields_by_name['complete_quest_stamp_card'].message_type = pogoprotos_dot_data_dot_logs_dot_complete__quest__stamp__card__log__entry__pb2._COMPLETEQUESTSTAMPCARDLOGENTRY
_ACTIONLOGENTRY.fields_by_name['complete_quest_pokemon_encounter'].message_type = pogoprotos_dot_data_dot_logs_dot_complete__quest__pokemon__encounter__log__entry__pb2._COMPLETEQUESTPOKEMONENCOUNTERLOGENTRY
_ACTIONLOGENTRY.fields_by_name['beluga_transfer'].message_type = pogoprotos_dot_data_dot_logs_dot_beluga__daily__transfer__log__entry__pb2._BELUGADAILYTRANSFERLOGENTRY
_ACTIONLOGENTRY.fields_by_name['open_gift'].message_type = pogoprotos_dot_data_dot_logs_dot_open__gift__log__entry__pb2._OPENGIFTLOGENTRY
_ACTIONLOGENTRY.fields_by_name['send_gift'].message_type = pogoprotos_dot_data_dot_logs_dot_send__gift__log__entry__pb2._SENDGIFTLOGENTRY
_ACTIONLOGENTRY.fields_by_name['trading'].message_type = pogoprotos_dot_data_dot_logs_dot_trading__log__entry__pb2._TRADINGLOGENTRY
_ACTIONLOGENTRY.fields_by_name['share_ex_raid_pass'].message_type = pogoprotos_dot_data_dot_logs_dot_share__ex__raid__pass__log__entry__pb2._SHAREEXRAIDPASSLOGENTRY
_ACTIONLOGENTRY.fields_by_name['decline_ex_raid_pass'].message_type = pogoprotos_dot_data_dot_logs_dot_decline__ex__raid__pass__log__entry__pb2._DECLINEEXRAIDPASSLOGENTRY
_ACTIONLOGENTRY.fields_by_name['fitness_rewards'].message_type = pogoprotos_dot_data_dot_logs_dot_fitness__rewards__log__entry__pb2._FITNESSREWARDSLOGENTRY
_ACTIONLOGENTRY.fields_by_name['combat'].message_type = pogoprotos_dot_data_dot_logs_dot_combat__log__entry__pb2._COMBATLOGENTRY
_ACTIONLOGENTRY.fields_by_name['purify_pokemon'].message_type = pogoprotos_dot_data_dot_logs_dot_purify__pokemon__log__entry__pb2._PURIFYPOKEMONLOGENTRY
_ACTIONLOGENTRY.fields_by_name['invasion_victory'].message_type = pogoprotos_dot_data_dot_logs_dot_invasion__victory__log__entry__pb2._INVASIONVICTORYLOGENTRY
_ACTIONLOGENTRY.fields_by_name['vs_seeker_set'].message_type = pogoprotos_dot_data_dot_logs_dot_vs__seeker__set__log__entry__pb2._VSSEEKERSETLOGENTRY
_ACTIONLOGENTRY.fields_by_name['vs_seeker_complete_season'].message_type = pogoprotos_dot_data_dot_logs_dot_vs__seeker__complete__season__log__entry__pb2._VSSEEKERCOMPLETESEASONLOGENTRY
_ACTIONLOGENTRY.fields_by_name['vs_seeker_win_rewards'].message_type = pogoprotos_dot_data_dot_logs_dot_vs__seeker__win__rewards__log__entry__pb2._VSSEEKERWINREWARDSLOGENTRY
_ACTIONLOGENTRY.oneofs_by_name['Action'].fields.append(
  _ACTIONLOGENTRY.fields_by_name['catch_pokemon'])
_ACTIONLOGENTRY.fields_by_name['catch_pokemon'].containing_oneof = _ACTIONLOGENTRY.oneofs_by_name['Action']
_ACTIONLOGENTRY.oneofs_by_name['Action'].fields.append(
  _ACTIONLOGENTRY.fields_by_name['fort_search'])
_ACTIONLOGENTRY.fields_by_name['fort_search'].containing_oneof = _ACTIONLOGENTRY.oneofs_by_name['Action']
_ACTIONLOGENTRY.oneofs_by_name['Action'].fields.append(
  _ACTIONLOGENTRY.fields_by_name['buddy_pokemon'])
_ACTIONLOGENTRY.fields_by_name['buddy_pokemon'].containing_oneof = _ACTIONLOGENTRY.oneofs_by_name['Action']
_ACTIONLOGENTRY.oneofs_by_name['Action'].fields.append(
  _ACTIONLOGENTRY.fields_by_name['raid_rewards'])
_ACTIONLOGENTRY.fields_by_name['raid_rewards'].containing_oneof = _ACTIONLOGENTRY.oneofs_by_name['Action']
_ACTIONLOGENTRY.oneofs_by_name['Action'].fields.append(
  _ACTIONLOGENTRY.fields_by_name['passcode_rewards'])
_ACTIONLOGENTRY.fields_by_name['passcode_rewards'].containing_oneof = _ACTIONLOGENTRY.oneofs_by_name['Action']
_ACTIONLOGENTRY.oneofs_by_name['Action'].fields.append(
  _ACTIONLOGENTRY.fields_by_name['complete_quest'])
_ACTIONLOGENTRY.fields_by_name['complete_quest'].containing_oneof = _ACTIONLOGENTRY.oneofs_by_name['Action']
_ACTIONLOGENTRY.oneofs_by_name['Action'].fields.append(
  _ACTIONLOGENTRY.fields_by_name['complete_quest_stamp_card'])
_ACTIONLOGENTRY.fields_by_name['complete_quest_stamp_card'].containing_oneof = _ACTIONLOGENTRY.oneofs_by_name['Action']
_ACTIONLOGENTRY.oneofs_by_name['Action'].fields.append(
  _ACTIONLOGENTRY.fields_by_name['complete_quest_pokemon_encounter'])
_ACTIONLOGENTRY.fields_by_name['complete_quest_pokemon_encounter'].containing_oneof = _ACTIONLOGENTRY.oneofs_by_name['Action']
_ACTIONLOGENTRY.oneofs_by_name['Action'].fields.append(
  _ACTIONLOGENTRY.fields_by_name['beluga_transfer'])
_ACTIONLOGENTRY.fields_by_name['beluga_transfer'].containing_oneof = _ACTIONLOGENTRY.oneofs_by_name['Action']
_ACTIONLOGENTRY.oneofs_by_name['Action'].fields.append(
  _ACTIONLOGENTRY.fields_by_name['open_gift'])
_ACTIONLOGENTRY.fields_by_name['open_gift'].containing_oneof = _ACTIONLOGENTRY.oneofs_by_name['Action']
_ACTIONLOGENTRY.oneofs_by_name['Action'].fields.append(
  _ACTIONLOGENTRY.fields_by_name['send_gift'])
_ACTIONLOGENTRY.fields_by_name['send_gift'].containing_oneof = _ACTIONLOGENTRY.oneofs_by_name['Action']
_ACTIONLOGENTRY.oneofs_by_name['Action'].fields.append(
  _ACTIONLOGENTRY.fields_by_name['trading'])
_ACTIONLOGENTRY.fields_by_name['trading'].containing_oneof = _ACTIONLOGENTRY.oneofs_by_name['Action']
_ACTIONLOGENTRY.oneofs_by_name['Action'].fields.append(
  _ACTIONLOGENTRY.fields_by_name['share_ex_raid_pass'])
_ACTIONLOGENTRY.fields_by_name['share_ex_raid_pass'].containing_oneof = _ACTIONLOGENTRY.oneofs_by_name['Action']
_ACTIONLOGENTRY.oneofs_by_name['Action'].fields.append(
  _ACTIONLOGENTRY.fields_by_name['decline_ex_raid_pass'])
_ACTIONLOGENTRY.fields_by_name['decline_ex_raid_pass'].containing_oneof = _ACTIONLOGENTRY.oneofs_by_name['Action']
_ACTIONLOGENTRY.oneofs_by_name['Action'].fields.append(
  _ACTIONLOGENTRY.fields_by_name['fitness_rewards'])
_ACTIONLOGENTRY.fields_by_name['fitness_rewards'].containing_oneof = _ACTIONLOGENTRY.oneofs_by_name['Action']
_ACTIONLOGENTRY.oneofs_by_name['Action'].fields.append(
  _ACTIONLOGENTRY.fields_by_name['combat'])
_ACTIONLOGENTRY.fields_by_name['combat'].containing_oneof = _ACTIONLOGENTRY.oneofs_by_name['Action']
_ACTIONLOGENTRY.oneofs_by_name['Action'].fields.append(
  _ACTIONLOGENTRY.fields_by_name['purify_pokemon'])
_ACTIONLOGENTRY.fields_by_name['purify_pokemon'].containing_oneof = _ACTIONLOGENTRY.oneofs_by_name['Action']
_ACTIONLOGENTRY.oneofs_by_name['Action'].fields.append(
  _ACTIONLOGENTRY.fields_by_name['invasion_victory'])
_ACTIONLOGENTRY.fields_by_name['invasion_victory'].containing_oneof = _ACTIONLOGENTRY.oneofs_by_name['Action']
_ACTIONLOGENTRY.oneofs_by_name['Action'].fields.append(
  _ACTIONLOGENTRY.fields_by_name['vs_seeker_set'])
_ACTIONLOGENTRY.fields_by_name['vs_seeker_set'].containing_oneof = _ACTIONLOGENTRY.oneofs_by_name['Action']
_ACTIONLOGENTRY.oneofs_by_name['Action'].fields.append(
  _ACTIONLOGENTRY.fields_by_name['vs_seeker_complete_season'])
_ACTIONLOGENTRY.fields_by_name['vs_seeker_complete_season'].containing_oneof = _ACTIONLOGENTRY.oneofs_by_name['Action']
_ACTIONLOGENTRY.oneofs_by_name['Action'].fields.append(
  _ACTIONLOGENTRY.fields_by_name['vs_seeker_win_rewards'])
_ACTIONLOGENTRY.fields_by_name['vs_seeker_win_rewards'].containing_oneof = _ACTIONLOGENTRY.oneofs_by_name['Action']
DESCRIPTOR.message_types_by_name['ActionLogEntry'] = _ACTIONLOGENTRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ActionLogEntry = _reflection.GeneratedProtocolMessageType('ActionLogEntry', (_message.Message,), dict(
  DESCRIPTOR = _ACTIONLOGENTRY,
  __module__ = 'pogoprotos.data.logs.action_log_entry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.logs.ActionLogEntry)
  ))
_sym_db.RegisterMessage(ActionLogEntry)


# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/quests/client_quest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.quests import quest_pb2 as pogoprotos_dot_data_dot_quests_dot_quest__pb2
from pogoprotos.data.quests import quest_dialog_pb2 as pogoprotos_dot_data_dot_quests_dot_quest__dialog__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/quests/client_quest.proto',
  package='pogoprotos.data.quests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n)pogoprotos/data/quests/client_quest.proto\x12\x16pogoprotos.data.quests\x1a\"pogoprotos/data/quests/quest.proto\x1a)pogoprotos/data/quests/quest_dialog.proto\"\xe5\x03\n\x0b\x43lientQuest\x12,\n\x05quest\x18\x01 \x01(\x0b\x32\x1d.pogoprotos.data.quests.Quest\x12G\n\rquest_display\x18\x02 \x01(\x0b\x32\x30.pogoprotos.data.quests.ClientQuest.QuestDisplay\x1a\xde\x02\n\x0cQuestDisplay\x12\x10\n\x08quest_id\x18\x01 \x01(\t\x12\x33\n\x06\x64ialog\x18\x02 \x03(\x0b\x32#.pogoprotos.data.quests.QuestDialog\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\r\n\x05title\x18\x04 \x01(\t\x12\x0c\n\x04slot\x18\x05 \x01(\x05\x12\x44\n\nsubdisplay\x18\x06 \x03(\x0b\x32\x30.pogoprotos.data.quests.ClientQuest.QuestDisplay\x12\x1a\n\x12story_ending_quest\x18\x07 \x01(\x08\x12 \n\x18story_ending_description\x18\x08 \x01(\t\x12\x11\n\ttag_color\x18\t \x01(\t\x12\x12\n\ntag_string\x18\n \x01(\t\x12\x16\n\x0esponsor_string\x18\x0b \x01(\t\x12\x12\n\npartner_id\x18\x0c \x01(\tb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_quests_dot_quest__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_quests_dot_quest__dialog__pb2.DESCRIPTOR,])




_CLIENTQUEST_QUESTDISPLAY = _descriptor.Descriptor(
  name='QuestDisplay',
  full_name='pogoprotos.data.quests.ClientQuest.QuestDisplay',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quest_id', full_name='pogoprotos.data.quests.ClientQuest.QuestDisplay.quest_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dialog', full_name='pogoprotos.data.quests.ClientQuest.QuestDisplay.dialog', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='pogoprotos.data.quests.ClientQuest.QuestDisplay.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='pogoprotos.data.quests.ClientQuest.QuestDisplay.title', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slot', full_name='pogoprotos.data.quests.ClientQuest.QuestDisplay.slot', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subdisplay', full_name='pogoprotos.data.quests.ClientQuest.QuestDisplay.subdisplay', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='story_ending_quest', full_name='pogoprotos.data.quests.ClientQuest.QuestDisplay.story_ending_quest', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='story_ending_description', full_name='pogoprotos.data.quests.ClientQuest.QuestDisplay.story_ending_description', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag_color', full_name='pogoprotos.data.quests.ClientQuest.QuestDisplay.tag_color', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag_string', full_name='pogoprotos.data.quests.ClientQuest.QuestDisplay.tag_string', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sponsor_string', full_name='pogoprotos.data.quests.ClientQuest.QuestDisplay.sponsor_string', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partner_id', full_name='pogoprotos.data.quests.ClientQuest.QuestDisplay.partner_id', index=11,
      number=12, type=9, cpp_type=9, label=1,
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
  serialized_start=284,
  serialized_end=634,
)

_CLIENTQUEST = _descriptor.Descriptor(
  name='ClientQuest',
  full_name='pogoprotos.data.quests.ClientQuest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quest', full_name='pogoprotos.data.quests.ClientQuest.quest', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quest_display', full_name='pogoprotos.data.quests.ClientQuest.quest_display', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CLIENTQUEST_QUESTDISPLAY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=634,
)

_CLIENTQUEST_QUESTDISPLAY.fields_by_name['dialog'].message_type = pogoprotos_dot_data_dot_quests_dot_quest__dialog__pb2._QUESTDIALOG
_CLIENTQUEST_QUESTDISPLAY.fields_by_name['subdisplay'].message_type = _CLIENTQUEST_QUESTDISPLAY
_CLIENTQUEST_QUESTDISPLAY.containing_type = _CLIENTQUEST
_CLIENTQUEST.fields_by_name['quest'].message_type = pogoprotos_dot_data_dot_quests_dot_quest__pb2._QUEST
_CLIENTQUEST.fields_by_name['quest_display'].message_type = _CLIENTQUEST_QUESTDISPLAY
DESCRIPTOR.message_types_by_name['ClientQuest'] = _CLIENTQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientQuest = _reflection.GeneratedProtocolMessageType('ClientQuest', (_message.Message,), dict(

  QuestDisplay = _reflection.GeneratedProtocolMessageType('QuestDisplay', (_message.Message,), dict(
    DESCRIPTOR = _CLIENTQUEST_QUESTDISPLAY,
    __module__ = 'pogoprotos.data.quests.client_quest_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.ClientQuest.QuestDisplay)
    ))
  ,
  DESCRIPTOR = _CLIENTQUEST,
  __module__ = 'pogoprotos.data.quests.client_quest_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.ClientQuest)
  ))
_sym_db.RegisterMessage(ClientQuest)
_sym_db.RegisterMessage(ClientQuest.QuestDisplay)


# @@protoc_insertion_point(module_scope)

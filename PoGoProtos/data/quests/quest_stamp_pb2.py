# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/quests/quest_stamp.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/quests/quest_stamp.proto',
  package='pogoprotos.data.quests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n(pogoprotos/data/quests/quest_stamp.proto\x12\x16pogoprotos.data.quests\"\x9b\x01\n\nQuestStamp\x12;\n\x07\x63ontext\x18\x01 \x01(\x0e\x32*.pogoprotos.data.quests.QuestStamp.Context\x12\x14\n\x0ctimestamp_ms\x18\x02 \x01(\x04\":\n\x07\x43ontext\x12\t\n\x05UNSET\x10\x00\x12\x0f\n\x0bSTORY_QUEST\x10\x01\x12\x13\n\x0f\x43HALLENGE_QUEST\x10\x02\x62\x06proto3')
)



_QUESTSTAMP_CONTEXT = _descriptor.EnumDescriptor(
  name='Context',
  full_name='pogoprotos.data.quests.QuestStamp.Context',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORY_QUEST', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE_QUEST', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=166,
  serialized_end=224,
)
_sym_db.RegisterEnumDescriptor(_QUESTSTAMP_CONTEXT)


_QUESTSTAMP = _descriptor.Descriptor(
  name='QuestStamp',
  full_name='pogoprotos.data.quests.QuestStamp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='context', full_name='pogoprotos.data.quests.QuestStamp.context', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_ms', full_name='pogoprotos.data.quests.QuestStamp.timestamp_ms', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _QUESTSTAMP_CONTEXT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=224,
)

_QUESTSTAMP.fields_by_name['context'].enum_type = _QUESTSTAMP_CONTEXT
_QUESTSTAMP_CONTEXT.containing_type = _QUESTSTAMP
DESCRIPTOR.message_types_by_name['QuestStamp'] = _QUESTSTAMP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QuestStamp = _reflection.GeneratedProtocolMessageType('QuestStamp', (_message.Message,), dict(
  DESCRIPTOR = _QUESTSTAMP,
  __module__ = 'pogoprotos.data.quests.quest_stamp_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.QuestStamp)
  ))
_sym_db.RegisterMessage(QuestStamp)


# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/friends/outgoing_friend_invite_display.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.friends import outgoing_friend_invite_pb2 as pogoprotos_dot_data_dot_friends_dot_outgoing__friend__invite__pb2
from pogoprotos.data.player import player_summary_pb2 as pogoprotos_dot_data_dot_player_dot_player__summary__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/friends/outgoing_friend_invite_display.proto',
  package='pogoprotos.data.friends',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n<pogoprotos/data/friends/outgoing_friend_invite_display.proto\x12\x17pogoprotos.data.friends\x1a\x34pogoprotos/data/friends/outgoing_friend_invite.proto\x1a+pogoprotos/data/player/player_summary.proto\"\x93\x01\n\x1bOutgoingFriendInviteDisplay\x12=\n\x06invite\x18\x01 \x01(\x0b\x32-.pogoprotos.data.friends.OutgoingFriendInvite\x12\x35\n\x06player\x18\x02 \x01(\x0b\x32%.pogoprotos.data.player.PlayerSummaryb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_friends_dot_outgoing__friend__invite__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_player_dot_player__summary__pb2.DESCRIPTOR,])




_OUTGOINGFRIENDINVITEDISPLAY = _descriptor.Descriptor(
  name='OutgoingFriendInviteDisplay',
  full_name='pogoprotos.data.friends.OutgoingFriendInviteDisplay',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='invite', full_name='pogoprotos.data.friends.OutgoingFriendInviteDisplay.invite', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player', full_name='pogoprotos.data.friends.OutgoingFriendInviteDisplay.player', index=1,
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
  serialized_start=189,
  serialized_end=336,
)

_OUTGOINGFRIENDINVITEDISPLAY.fields_by_name['invite'].message_type = pogoprotos_dot_data_dot_friends_dot_outgoing__friend__invite__pb2._OUTGOINGFRIENDINVITE
_OUTGOINGFRIENDINVITEDISPLAY.fields_by_name['player'].message_type = pogoprotos_dot_data_dot_player_dot_player__summary__pb2._PLAYERSUMMARY
DESCRIPTOR.message_types_by_name['OutgoingFriendInviteDisplay'] = _OUTGOINGFRIENDINVITEDISPLAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OutgoingFriendInviteDisplay = _reflection.GeneratedProtocolMessageType('OutgoingFriendInviteDisplay', (_message.Message,), dict(
  DESCRIPTOR = _OUTGOINGFRIENDINVITEDISPLAY,
  __module__ = 'pogoprotos.data.friends.outgoing_friend_invite_display_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.friends.OutgoingFriendInviteDisplay)
  ))
_sym_db.RegisterMessage(OutgoingFriendInviteDisplay)


# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/social/messages/send_friend_invite_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/social/messages/send_friend_invite_message.proto',
  package='pogoprotos.networking.social.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nFpogoprotos/networking/social/messages/send_friend_invite_message.proto\x12%pogoprotos.networking.social.messages\"A\n\x17SendFriendInviteMessage\x12\x11\n\tplayer_id\x18\x01 \x01(\t\x12\x13\n\x0b\x66riend_code\x18\x02 \x01(\tb\x06proto3')
)




_SENDFRIENDINVITEMESSAGE = _descriptor.Descriptor(
  name='SendFriendInviteMessage',
  full_name='pogoprotos.networking.social.messages.SendFriendInviteMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_id', full_name='pogoprotos.networking.social.messages.SendFriendInviteMessage.player_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='friend_code', full_name='pogoprotos.networking.social.messages.SendFriendInviteMessage.friend_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=113,
  serialized_end=178,
)

DESCRIPTOR.message_types_by_name['SendFriendInviteMessage'] = _SENDFRIENDINVITEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendFriendInviteMessage = _reflection.GeneratedProtocolMessageType('SendFriendInviteMessage', (_message.Message,), dict(
  DESCRIPTOR = _SENDFRIENDINVITEMESSAGE,
  __module__ = 'pogoprotos.networking.social.messages.send_friend_invite_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.social.messages.SendFriendInviteMessage)
  ))
_sym_db.RegisterMessage(SendFriendInviteMessage)


# @@protoc_insertion_point(module_scope)

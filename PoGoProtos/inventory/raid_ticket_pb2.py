# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/inventory/raid_ticket.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory.item import item_id_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__id__pb2
from pogoprotos.inventory import exclusive_ticket_info_pb2 as pogoprotos_dot_inventory_dot_exclusive__ticket__info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/inventory/raid_ticket.proto',
  package='pogoprotos.inventory',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n&pogoprotos/inventory/raid_ticket.proto\x12\x14pogoprotos.inventory\x1a\'pogoprotos/inventory/item/item_id.proto\x1a\x30pogoprotos/inventory/exclusive_ticket_info.proto\"\x93\x01\n\nRaidTicket\x12\x11\n\tticket_id\x18\x01 \x01(\t\x12/\n\x04item\x18\x02 \x01(\x0e\x32!.pogoprotos.inventory.item.ItemId\x12\x41\n\x0e\x65xclusive_info\x18\x04 \x01(\x0b\x32).pogoprotos.inventory.ExclusiveTicketInfob\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_item_dot_item__id__pb2.DESCRIPTOR,pogoprotos_dot_inventory_dot_exclusive__ticket__info__pb2.DESCRIPTOR,])




_RAIDTICKET = _descriptor.Descriptor(
  name='RaidTicket',
  full_name='pogoprotos.inventory.RaidTicket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ticket_id', full_name='pogoprotos.inventory.RaidTicket.ticket_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item', full_name='pogoprotos.inventory.RaidTicket.item', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exclusive_info', full_name='pogoprotos.inventory.RaidTicket.exclusive_info', index=2,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=156,
  serialized_end=303,
)

_RAIDTICKET.fields_by_name['item'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__id__pb2._ITEMID
_RAIDTICKET.fields_by_name['exclusive_info'].message_type = pogoprotos_dot_inventory_dot_exclusive__ticket__info__pb2._EXCLUSIVETICKETINFO
DESCRIPTOR.message_types_by_name['RaidTicket'] = _RAIDTICKET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RaidTicket = _reflection.GeneratedProtocolMessageType('RaidTicket', (_message.Message,), dict(
  DESCRIPTOR = _RAIDTICKET,
  __module__ = 'pogoprotos.inventory.raid_ticket_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.inventory.RaidTicket)
  ))
_sym_db.RegisterMessage(RaidTicket)


# @@protoc_insertion_point(module_scope)

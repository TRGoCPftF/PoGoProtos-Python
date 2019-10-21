# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/titan/messages/submit_new_route_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/titan/messages/submit_new_route_message.proto',
  package='pogoprotos.networking.titan.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nCpogoprotos/networking/titan/messages/submit_new_route_message.proto\x12$pogoprotos.networking.titan.messages\"\xfd\x02\n\x15SubmitNewRouteMessage\x12\x1b\n\x13route_submission_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12R\n\x04pois\x18\x04 \x03(\x0b\x32\x44.pogoprotos.networking.titan.messages.SubmitNewRouteMessage.RoutePoi\x12`\n\x0bvisit_order\x18\x05 \x01(\x0e\x32K.pogoprotos.networking.titan.messages.SubmitNewRouteMessage.RouteVisitOrder\x1a\x1a\n\x08RoutePoi\x12\x0e\n\x06poi_id\x18\x01 \x01(\t\"Q\n\x0fRouteVisitOrder\x12!\n\x1dROUTE_VISIT_ORDER_UNSPECIFIED\x10\x00\x12\x0c\n\x08IN_ORDER\x10\x01\x12\r\n\tUNORDERED\x10\x02\x62\x06proto3')
)



_SUBMITNEWROUTEMESSAGE_ROUTEVISITORDER = _descriptor.EnumDescriptor(
  name='RouteVisitOrder',
  full_name='pogoprotos.networking.titan.messages.SubmitNewRouteMessage.RouteVisitOrder',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ROUTE_VISIT_ORDER_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IN_ORDER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNORDERED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=410,
  serialized_end=491,
)
_sym_db.RegisterEnumDescriptor(_SUBMITNEWROUTEMESSAGE_ROUTEVISITORDER)


_SUBMITNEWROUTEMESSAGE_ROUTEPOI = _descriptor.Descriptor(
  name='RoutePoi',
  full_name='pogoprotos.networking.titan.messages.SubmitNewRouteMessage.RoutePoi',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='poi_id', full_name='pogoprotos.networking.titan.messages.SubmitNewRouteMessage.RoutePoi.poi_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=382,
  serialized_end=408,
)

_SUBMITNEWROUTEMESSAGE = _descriptor.Descriptor(
  name='SubmitNewRouteMessage',
  full_name='pogoprotos.networking.titan.messages.SubmitNewRouteMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='route_submission_id', full_name='pogoprotos.networking.titan.messages.SubmitNewRouteMessage.route_submission_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='pogoprotos.networking.titan.messages.SubmitNewRouteMessage.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='pogoprotos.networking.titan.messages.SubmitNewRouteMessage.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pois', full_name='pogoprotos.networking.titan.messages.SubmitNewRouteMessage.pois', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visit_order', full_name='pogoprotos.networking.titan.messages.SubmitNewRouteMessage.visit_order', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SUBMITNEWROUTEMESSAGE_ROUTEPOI, ],
  enum_types=[
    _SUBMITNEWROUTEMESSAGE_ROUTEVISITORDER,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=491,
)

_SUBMITNEWROUTEMESSAGE_ROUTEPOI.containing_type = _SUBMITNEWROUTEMESSAGE
_SUBMITNEWROUTEMESSAGE.fields_by_name['pois'].message_type = _SUBMITNEWROUTEMESSAGE_ROUTEPOI
_SUBMITNEWROUTEMESSAGE.fields_by_name['visit_order'].enum_type = _SUBMITNEWROUTEMESSAGE_ROUTEVISITORDER
_SUBMITNEWROUTEMESSAGE_ROUTEVISITORDER.containing_type = _SUBMITNEWROUTEMESSAGE
DESCRIPTOR.message_types_by_name['SubmitNewRouteMessage'] = _SUBMITNEWROUTEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubmitNewRouteMessage = _reflection.GeneratedProtocolMessageType('SubmitNewRouteMessage', (_message.Message,), dict(

  RoutePoi = _reflection.GeneratedProtocolMessageType('RoutePoi', (_message.Message,), dict(
    DESCRIPTOR = _SUBMITNEWROUTEMESSAGE_ROUTEPOI,
    __module__ = 'pogoprotos.networking.titan.messages.submit_new_route_message_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.titan.messages.SubmitNewRouteMessage.RoutePoi)
    ))
  ,
  DESCRIPTOR = _SUBMITNEWROUTEMESSAGE,
  __module__ = 'pogoprotos.networking.titan.messages.submit_new_route_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.titan.messages.SubmitNewRouteMessage)
  ))
_sym_db.RegisterMessage(SubmitNewRouteMessage)
_sym_db.RegisterMessage(SubmitNewRouteMessage.RoutePoi)


# @@protoc_insertion_point(module_scope)

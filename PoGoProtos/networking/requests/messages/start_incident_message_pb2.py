# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/start_incident_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data import incident_lookup_pb2 as pogoprotos_dot_data_dot_incident__lookup__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/start_incident_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nDpogoprotos/networking/requests/messages/start_incident_message.proto\x12\'pogoprotos.networking.requests.messages\x1a%pogoprotos/data/incident_lookup.proto\"P\n\x14StartIncidentMessage\x12\x38\n\x0fincident_lookup\x18\x01 \x01(\x0b\x32\x1f.pogoprotos.data.IncidentLookupb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_incident__lookup__pb2.DESCRIPTOR,])




_STARTINCIDENTMESSAGE = _descriptor.Descriptor(
  name='StartIncidentMessage',
  full_name='pogoprotos.networking.requests.messages.StartIncidentMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='incident_lookup', full_name='pogoprotos.networking.requests.messages.StartIncidentMessage.incident_lookup', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=152,
  serialized_end=232,
)

_STARTINCIDENTMESSAGE.fields_by_name['incident_lookup'].message_type = pogoprotos_dot_data_dot_incident__lookup__pb2._INCIDENTLOOKUP
DESCRIPTOR.message_types_by_name['StartIncidentMessage'] = _STARTINCIDENTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StartIncidentMessage = _reflection.GeneratedProtocolMessageType('StartIncidentMessage', (_message.Message,), dict(
  DESCRIPTOR = _STARTINCIDENTMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.start_incident_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.StartIncidentMessage)
  ))
_sym_db.RegisterMessage(StartIncidentMessage)


# @@protoc_insertion_point(module_scope)

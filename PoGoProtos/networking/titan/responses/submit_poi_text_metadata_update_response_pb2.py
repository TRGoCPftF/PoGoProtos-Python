# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/titan/responses/submit_poi_text_metadata_update_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/titan/responses/submit_poi_text_metadata_update_response.proto',
  package='pogoprotos.networking.titan.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nTpogoprotos/networking/titan/responses/submit_poi_text_metadata_update_response.proto\x12%pogoprotos.networking.titan.responses\"\x9e\x02\n#SubmitPoiTextMetadataUpdateResponse\x12\x61\n\x06status\x18\x01 \x01(\x0e\x32Q.pogoprotos.networking.titan.responses.SubmitPoiTextMetadataUpdateResponse.Status\"\x93\x01\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x12\n\x0eINTERNAL_ERROR\x10\x02\x12\x1f\n\x1bTOO_MANY_RECENT_SUBMISSIONS\x10\x03\x12\t\n\x05MINOR\x10\x04\x12\x11\n\rNOT_AVAILABLE\x10\x05\x12\x11\n\rINVALID_INPUT\x10\x06\x62\x06proto3')
)



_SUBMITPOITEXTMETADATAUPDATERESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.titan.responses.SubmitPoiTextMetadataUpdateResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_MANY_RECENT_SUBMISSIONS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MINOR', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_AVAILABLE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_INPUT', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=267,
  serialized_end=414,
)
_sym_db.RegisterEnumDescriptor(_SUBMITPOITEXTMETADATAUPDATERESPONSE_STATUS)


_SUBMITPOITEXTMETADATAUPDATERESPONSE = _descriptor.Descriptor(
  name='SubmitPoiTextMetadataUpdateResponse',
  full_name='pogoprotos.networking.titan.responses.SubmitPoiTextMetadataUpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.titan.responses.SubmitPoiTextMetadataUpdateResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SUBMITPOITEXTMETADATAUPDATERESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=414,
)

_SUBMITPOITEXTMETADATAUPDATERESPONSE.fields_by_name['status'].enum_type = _SUBMITPOITEXTMETADATAUPDATERESPONSE_STATUS
_SUBMITPOITEXTMETADATAUPDATERESPONSE_STATUS.containing_type = _SUBMITPOITEXTMETADATAUPDATERESPONSE
DESCRIPTOR.message_types_by_name['SubmitPoiTextMetadataUpdateResponse'] = _SUBMITPOITEXTMETADATAUPDATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubmitPoiTextMetadataUpdateResponse = _reflection.GeneratedProtocolMessageType('SubmitPoiTextMetadataUpdateResponse', (_message.Message,), dict(
  DESCRIPTOR = _SUBMITPOITEXTMETADATAUPDATERESPONSE,
  __module__ = 'pogoprotos.networking.titan.responses.submit_poi_text_metadata_update_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.titan.responses.SubmitPoiTextMetadataUpdateResponse)
  ))
_sym_db.RegisterMessage(SubmitPoiTextMetadataUpdateResponse)


# @@protoc_insertion_point(module_scope)

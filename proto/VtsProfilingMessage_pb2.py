# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: VtsProfilingMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ComponentSpecificationMessage_pb2 as ComponentSpecificationMessage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='VtsProfilingMessage.proto',
  package='android.vts',
  syntax='proto2',
  serialized_pb=_b('\n\x19VtsProfilingMessage.proto\x12\x0b\x61ndroid.vts\x1a#ComponentSpecificationMessage.proto\"\xcf\x01\n\x12VtsProfilingRecord\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x34\n\x05\x65vent\x18\x02 \x01(\x0e\x32%.android.vts.InstrumentationEventType\x12\x0f\n\x07package\x18\x03 \x01(\x0c\x12\x0f\n\x07version\x18\x04 \x01(\x02\x12\x11\n\tinterface\x18\x05 \x01(\x0c\x12;\n\x08\x66unc_msg\x18\x06 \x01(\x0b\x32).android.vts.FunctionSpecificationMessage\"G\n\x13VtsProfilingMessage\x12\x30\n\x07records\x18\x01 \x03(\x0b\x32\x1f.android.vts.VtsProfilingRecord*\x81\x02\n\x18InstrumentationEventType\x12\x14\n\x10SERVER_API_ENTRY\x10\x00\x12\x13\n\x0fSERVER_API_EXIT\x10\x01\x12\x14\n\x10\x43LIENT_API_ENTRY\x10\x02\x12\x13\n\x0f\x43LIENT_API_EXIT\x10\x03\x12\x17\n\x13SYNC_CALLBACK_ENTRY\x10\x04\x12\x16\n\x12SYNC_CALLBACK_EXIT\x10\x05\x12\x18\n\x14\x41SYNC_CALLBACK_ENTRY\x10\x06\x12\x17\n\x13\x41SYNC_CALLBACK_EXIT\x10\x07\x12\x15\n\x11PASSTHROUGH_ENTRY\x10\x08\x12\x14\n\x10PASSTHROUGH_EXIT\x10\tB1\n\x15\x63om.android.vts.protoB\x18VtsProfilingMessageClass')
  ,
  dependencies=[ComponentSpecificationMessage__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_INSTRUMENTATIONEVENTTYPE = _descriptor.EnumDescriptor(
  name='InstrumentationEventType',
  full_name='android.vts.InstrumentationEventType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SERVER_API_ENTRY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVER_API_EXIT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLIENT_API_ENTRY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLIENT_API_EXIT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYNC_CALLBACK_ENTRY', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYNC_CALLBACK_EXIT', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ASYNC_CALLBACK_ENTRY', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ASYNC_CALLBACK_EXIT', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PASSTHROUGH_ENTRY', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PASSTHROUGH_EXIT', index=9, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=363,
  serialized_end=620,
)
_sym_db.RegisterEnumDescriptor(_INSTRUMENTATIONEVENTTYPE)

InstrumentationEventType = enum_type_wrapper.EnumTypeWrapper(_INSTRUMENTATIONEVENTTYPE)
SERVER_API_ENTRY = 0
SERVER_API_EXIT = 1
CLIENT_API_ENTRY = 2
CLIENT_API_EXIT = 3
SYNC_CALLBACK_ENTRY = 4
SYNC_CALLBACK_EXIT = 5
ASYNC_CALLBACK_ENTRY = 6
ASYNC_CALLBACK_EXIT = 7
PASSTHROUGH_ENTRY = 8
PASSTHROUGH_EXIT = 9



_VTSPROFILINGRECORD = _descriptor.Descriptor(
  name='VtsProfilingRecord',
  full_name='android.vts.VtsProfilingRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='android.vts.VtsProfilingRecord.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event', full_name='android.vts.VtsProfilingRecord.event', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='package', full_name='android.vts.VtsProfilingRecord.package', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='android.vts.VtsProfilingRecord.version', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='interface', full_name='android.vts.VtsProfilingRecord.interface', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='func_msg', full_name='android.vts.VtsProfilingRecord.func_msg', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version_major', full_name='android.vts.VtsProfilingRecord.version_major', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version_minor', full_name='android.vts.VtsProfilingRecord.version_minor', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=287,
)


_VTSPROFILINGMESSAGE = _descriptor.Descriptor(
  name='VtsProfilingMessage',
  full_name='android.vts.VtsProfilingMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='records', full_name='android.vts.VtsProfilingMessage.records', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=289,
  serialized_end=360,
)

_VTSPROFILINGRECORD.fields_by_name['event'].enum_type = _INSTRUMENTATIONEVENTTYPE
_VTSPROFILINGRECORD.fields_by_name['func_msg'].message_type = ComponentSpecificationMessage__pb2._FUNCTIONSPECIFICATIONMESSAGE
_VTSPROFILINGMESSAGE.fields_by_name['records'].message_type = _VTSPROFILINGRECORD
DESCRIPTOR.message_types_by_name['VtsProfilingRecord'] = _VTSPROFILINGRECORD
DESCRIPTOR.message_types_by_name['VtsProfilingMessage'] = _VTSPROFILINGMESSAGE
DESCRIPTOR.enum_types_by_name['InstrumentationEventType'] = _INSTRUMENTATIONEVENTTYPE

VtsProfilingRecord = _reflection.GeneratedProtocolMessageType('VtsProfilingRecord', (_message.Message,), dict(
  DESCRIPTOR = _VTSPROFILINGRECORD,
  __module__ = 'VtsProfilingMessage_pb2'
  # @@protoc_insertion_point(class_scope:android.vts.VtsProfilingRecord)
  ))
_sym_db.RegisterMessage(VtsProfilingRecord)

VtsProfilingMessage = _reflection.GeneratedProtocolMessageType('VtsProfilingMessage', (_message.Message,), dict(
  DESCRIPTOR = _VTSPROFILINGMESSAGE,
  __module__ = 'VtsProfilingMessage_pb2'
  # @@protoc_insertion_point(class_scope:android.vts.VtsProfilingMessage)
  ))
_sym_db.RegisterMessage(VtsProfilingMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\025com.android.vts.protoB\030VtsProfilingMessageClass'))
# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_TO_AppCustomData_t.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='_py_TO_AppCustomData_t.proto',
  package='',
  serialized_pb=_b('\n\x1c_py_TO_AppCustomData_t.proto\"\xa0\x01\n\x13TO_TlmChannels_t_pb\x12\x14\n\x0cListenerTask\x18\x01 \x02(\r\x12\x0e\n\x06Socket\x18\x02 \x02(\r\x12\x13\n\x0b\x43hildTaskID\x18\x03 \x02(\r\x12\x11\n\tTaskFlags\x18\x04 \x02(\r\x12\x10\n\x08Priority\x18\x05 \x02(\r\x12\x0c\n\x04Mode\x18\x06 \x02(\r\x12\n\n\x02IP\x18\x07 \x02(\t\x12\x0f\n\x07\x44stPort\x18\x08 \x02(\r\">\n\x15TO_AppCustomData_t_pb\x12%\n\x07\x43hannel\x18\x01 \x03(\x0b\x32\x14.TO_TlmChannels_t_pb')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TO_TLMCHANNELS_T_PB = _descriptor.Descriptor(
  name='TO_TlmChannels_t_pb',
  full_name='TO_TlmChannels_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ListenerTask', full_name='TO_TlmChannels_t_pb.ListenerTask', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Socket', full_name='TO_TlmChannels_t_pb.Socket', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ChildTaskID', full_name='TO_TlmChannels_t_pb.ChildTaskID', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TaskFlags', full_name='TO_TlmChannels_t_pb.TaskFlags', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Priority', full_name='TO_TlmChannels_t_pb.Priority', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Mode', full_name='TO_TlmChannels_t_pb.Mode', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='IP', full_name='TO_TlmChannels_t_pb.IP', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DstPort', full_name='TO_TlmChannels_t_pb.DstPort', index=7,
      number=8, type=13, cpp_type=3, label=2,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=193,
)


_TO_APPCUSTOMDATA_T_PB = _descriptor.Descriptor(
  name='TO_AppCustomData_t_pb',
  full_name='TO_AppCustomData_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Channel', full_name='TO_AppCustomData_t_pb.Channel', index=0,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=195,
  serialized_end=257,
)

_TO_APPCUSTOMDATA_T_PB.fields_by_name['Channel'].message_type = _TO_TLMCHANNELS_T_PB
DESCRIPTOR.message_types_by_name['TO_TlmChannels_t_pb'] = _TO_TLMCHANNELS_T_PB
DESCRIPTOR.message_types_by_name['TO_AppCustomData_t_pb'] = _TO_APPCUSTOMDATA_T_PB

TO_TlmChannels_t_pb = _reflection.GeneratedProtocolMessageType('TO_TlmChannels_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _TO_TLMCHANNELS_T_PB,
  __module__ = '_py_TO_AppCustomData_t_pb2'
  # @@protoc_insertion_point(class_scope:TO_TlmChannels_t_pb)
  ))
_sym_db.RegisterMessage(TO_TlmChannels_t_pb)

TO_AppCustomData_t_pb = _reflection.GeneratedProtocolMessageType('TO_AppCustomData_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _TO_APPCUSTOMDATA_T_PB,
  __module__ = '_py_TO_AppCustomData_t_pb2'
  # @@protoc_insertion_point(class_scope:TO_AppCustomData_t_pb)
  ))
_sym_db.RegisterMessage(TO_AppCustomData_t_pb)


# @@protoc_insertion_point(module_scope)
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_SC_OperData_t.proto

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
  name='_py_SC_OperData_t.proto',
  package='',
  serialized_pb=_b('\n\x17_py_SC_OperData_t.proto\"\xab\x05\n\rSC_HkTlm_t_pb\x12\x17\n\x0fRtsActiveErrCtr\x18\x01 \x02(\r\x12\x15\n\rLastRtsErrSeq\x18\x02 \x02(\r\x12\x16\n\x0eSwitchPendFlag\x18\x03 \x02(\r\x12\x14\n\x0c\x41ppendCmdArg\x18\x04 \x02(\r\x12\x19\n\x11RtsDisabledStatus\x18\x05 \x03(\r\x12\x11\n\tRtsNumber\x18\x06 \x02(\r\x12\x10\n\x08\x41tpState\x18\x07 \x02(\r\x12\x15\n\rLastAtsErrSeq\x18\x08 \x02(\r\x12\x0e\n\x06\x43mdCtr\x18\t \x02(\r\x12\x14\n\x0cRtsCmdErrCtr\x18\n \x02(\r\x12 \n\x18\x43ontinueAtsOnFailureFlag\x18\x0b \x02(\r\x12\x11\n\tAtsNumber\x18\x0c \x02(\r\x12\x13\n\x0bNextAtsTime\x18\r \x02(\r\x12\x15\n\rLastRtsErrCmd\x18\x0e \x02(\r\x12\x14\n\x0cRtsActiveCtr\x18\x0f \x02(\r\x12\x11\n\tRtsCmdCtr\x18\x10 \x02(\r\x12\x14\n\x0cNumRtsActive\x18\x11 \x02(\r\x12\x14\n\x0c\x41tpFreeBytes\x18\x12 \x03(\r\x12\x13\n\x0bNextRtsTime\x18\x13 \x02(\r\x12\x10\n\x08Padding8\x18\x14 \x02(\r\x12\x17\n\x0f\x41ppendLoadCount\x18\x15 \x02(\r\x12\x15\n\rLastAtsErrCmd\x18\x16 \x02(\r\x12\x17\n\x0f\x41ppendByteCount\x18\x17 \x02(\r\x12\x11\n\tTlmHeader\x18\x18 \x03(\r\x12\x18\n\x10\x41ppendEntryCount\x18\x19 \x02(\r\x12\x11\n\tCmdErrCtr\x18\x1a \x02(\r\x12\x14\n\x0c\x41tsCmdErrCtr\x18\x1b \x02(\r\x12\x14\n\x0c\x41tpCmdNumber\x18\x1c \x02(\r\x12\x11\n\tAtsCmdCtr\x18\x1d \x02(\r\x12\x1a\n\x12RtsExecutingStatus\x18\x1e \x03(\r\"\xba\x04\n\x10SC_OperData_t_pb\x12\x17\n\x0fRtsCtrlBlckAddr\x18\x01 \x02(\r\x12\x0f\n\x07\x43mdPipe\x18\x02 \x02(\t\x12\x15\n\rAtsInfoHandle\x18\x03 \x02(\x05\x12\x16\n\x0e\x41tsInfoTblAddr\x18\x04 \x02(\r\x12\x19\n\x11\x41ppendInfoTblAddr\x18\x05 \x02(\r\x12\x14\n\x0c\x41tsTblHandle\x18\x06 \x03(\x05\x12\x14\n\x0cRtsTblHandle\x18\x07 \x03(\x03\x12\x17\n\x0f\x41tsCtrlBlckAddr\x18\x08 \x02(\r\x12\x18\n\x10\x41ppendInfoHandle\x18\t \x02(\x05\x12\x16\n\x0eRtsInfoTblAddr\x18\n \x02(\r\x12\x1b\n\x13\x41tsCmdStatusTblAddr\x18\x0b \x03(\r\x12\x15\n\rAppendTblAddr\x18\x0c \x02(\r\x12 \n\x08HkPacket\x18\r \x02(\x0b\x32\x0e.SC_HkTlm_t_pb\x12\x0e\n\x06MsgPtr\x18\x0e \x02(\r\x12\x17\n\x0f\x41tsDupTestArray\x18\x0f \x03(\x05\x12\x12\n\nNumCmdsSec\x18\x10 \x02(\r\x12\x15\n\rRtsInfoHandle\x18\x11 \x02(\x05\x12\x12\n\nRtsTblAddr\x18\x12 \x03(\r\x12\x17\n\x0f\x41ppendTblHandle\x18\x13 \x02(\x05\x12\x12\n\nAtsTblAddr\x18\x14 \x03(\r\x12\x19\n\x11RtsCtrlBlckHandle\x18\x15 \x02(\x05\x12\x1a\n\x12\x41tsCmdStatusHandle\x18\x16 \x03(\x05\x12\x19\n\x11\x41tsCtrlBlckHandle\x18\x17 \x02(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SC_HKTLM_T_PB = _descriptor.Descriptor(
  name='SC_HkTlm_t_pb',
  full_name='SC_HkTlm_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='RtsActiveErrCtr', full_name='SC_HkTlm_t_pb.RtsActiveErrCtr', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LastRtsErrSeq', full_name='SC_HkTlm_t_pb.LastRtsErrSeq', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SwitchPendFlag', full_name='SC_HkTlm_t_pb.SwitchPendFlag', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AppendCmdArg', full_name='SC_HkTlm_t_pb.AppendCmdArg', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RtsDisabledStatus', full_name='SC_HkTlm_t_pb.RtsDisabledStatus', index=4,
      number=5, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RtsNumber', full_name='SC_HkTlm_t_pb.RtsNumber', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AtpState', full_name='SC_HkTlm_t_pb.AtpState', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LastAtsErrSeq', full_name='SC_HkTlm_t_pb.LastAtsErrSeq', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CmdCtr', full_name='SC_HkTlm_t_pb.CmdCtr', index=8,
      number=9, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RtsCmdErrCtr', full_name='SC_HkTlm_t_pb.RtsCmdErrCtr', index=9,
      number=10, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ContinueAtsOnFailureFlag', full_name='SC_HkTlm_t_pb.ContinueAtsOnFailureFlag', index=10,
      number=11, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AtsNumber', full_name='SC_HkTlm_t_pb.AtsNumber', index=11,
      number=12, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='NextAtsTime', full_name='SC_HkTlm_t_pb.NextAtsTime', index=12,
      number=13, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LastRtsErrCmd', full_name='SC_HkTlm_t_pb.LastRtsErrCmd', index=13,
      number=14, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RtsActiveCtr', full_name='SC_HkTlm_t_pb.RtsActiveCtr', index=14,
      number=15, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RtsCmdCtr', full_name='SC_HkTlm_t_pb.RtsCmdCtr', index=15,
      number=16, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='NumRtsActive', full_name='SC_HkTlm_t_pb.NumRtsActive', index=16,
      number=17, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AtpFreeBytes', full_name='SC_HkTlm_t_pb.AtpFreeBytes', index=17,
      number=18, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='NextRtsTime', full_name='SC_HkTlm_t_pb.NextRtsTime', index=18,
      number=19, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Padding8', full_name='SC_HkTlm_t_pb.Padding8', index=19,
      number=20, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AppendLoadCount', full_name='SC_HkTlm_t_pb.AppendLoadCount', index=20,
      number=21, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LastAtsErrCmd', full_name='SC_HkTlm_t_pb.LastAtsErrCmd', index=21,
      number=22, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AppendByteCount', full_name='SC_HkTlm_t_pb.AppendByteCount', index=22,
      number=23, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TlmHeader', full_name='SC_HkTlm_t_pb.TlmHeader', index=23,
      number=24, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AppendEntryCount', full_name='SC_HkTlm_t_pb.AppendEntryCount', index=24,
      number=25, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CmdErrCtr', full_name='SC_HkTlm_t_pb.CmdErrCtr', index=25,
      number=26, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AtsCmdErrCtr', full_name='SC_HkTlm_t_pb.AtsCmdErrCtr', index=26,
      number=27, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AtpCmdNumber', full_name='SC_HkTlm_t_pb.AtpCmdNumber', index=27,
      number=28, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AtsCmdCtr', full_name='SC_HkTlm_t_pb.AtsCmdCtr', index=28,
      number=29, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RtsExecutingStatus', full_name='SC_HkTlm_t_pb.RtsExecutingStatus', index=29,
      number=30, type=13, cpp_type=3, label=3,
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
  serialized_start=28,
  serialized_end=711,
)


_SC_OPERDATA_T_PB = _descriptor.Descriptor(
  name='SC_OperData_t_pb',
  full_name='SC_OperData_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='RtsCtrlBlckAddr', full_name='SC_OperData_t_pb.RtsCtrlBlckAddr', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CmdPipe', full_name='SC_OperData_t_pb.CmdPipe', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AtsInfoHandle', full_name='SC_OperData_t_pb.AtsInfoHandle', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AtsInfoTblAddr', full_name='SC_OperData_t_pb.AtsInfoTblAddr', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AppendInfoTblAddr', full_name='SC_OperData_t_pb.AppendInfoTblAddr', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AtsTblHandle', full_name='SC_OperData_t_pb.AtsTblHandle', index=5,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RtsTblHandle', full_name='SC_OperData_t_pb.RtsTblHandle', index=6,
      number=7, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AtsCtrlBlckAddr', full_name='SC_OperData_t_pb.AtsCtrlBlckAddr', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AppendInfoHandle', full_name='SC_OperData_t_pb.AppendInfoHandle', index=8,
      number=9, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RtsInfoTblAddr', full_name='SC_OperData_t_pb.RtsInfoTblAddr', index=9,
      number=10, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AtsCmdStatusTblAddr', full_name='SC_OperData_t_pb.AtsCmdStatusTblAddr', index=10,
      number=11, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AppendTblAddr', full_name='SC_OperData_t_pb.AppendTblAddr', index=11,
      number=12, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='HkPacket', full_name='SC_OperData_t_pb.HkPacket', index=12,
      number=13, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MsgPtr', full_name='SC_OperData_t_pb.MsgPtr', index=13,
      number=14, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AtsDupTestArray', full_name='SC_OperData_t_pb.AtsDupTestArray', index=14,
      number=15, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='NumCmdsSec', full_name='SC_OperData_t_pb.NumCmdsSec', index=15,
      number=16, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RtsInfoHandle', full_name='SC_OperData_t_pb.RtsInfoHandle', index=16,
      number=17, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RtsTblAddr', full_name='SC_OperData_t_pb.RtsTblAddr', index=17,
      number=18, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AppendTblHandle', full_name='SC_OperData_t_pb.AppendTblHandle', index=18,
      number=19, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AtsTblAddr', full_name='SC_OperData_t_pb.AtsTblAddr', index=19,
      number=20, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RtsCtrlBlckHandle', full_name='SC_OperData_t_pb.RtsCtrlBlckHandle', index=20,
      number=21, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AtsCmdStatusHandle', full_name='SC_OperData_t_pb.AtsCmdStatusHandle', index=21,
      number=22, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AtsCtrlBlckHandle', full_name='SC_OperData_t_pb.AtsCtrlBlckHandle', index=22,
      number=23, type=5, cpp_type=1, label=2,
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
  serialized_start=714,
  serialized_end=1284,
)

_SC_OPERDATA_T_PB.fields_by_name['HkPacket'].message_type = _SC_HKTLM_T_PB
DESCRIPTOR.message_types_by_name['SC_HkTlm_t_pb'] = _SC_HKTLM_T_PB
DESCRIPTOR.message_types_by_name['SC_OperData_t_pb'] = _SC_OPERDATA_T_PB

SC_HkTlm_t_pb = _reflection.GeneratedProtocolMessageType('SC_HkTlm_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _SC_HKTLM_T_PB,
  __module__ = '_py_SC_OperData_t_pb2'
  # @@protoc_insertion_point(class_scope:SC_HkTlm_t_pb)
  ))
_sym_db.RegisterMessage(SC_HkTlm_t_pb)

SC_OperData_t_pb = _reflection.GeneratedProtocolMessageType('SC_OperData_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _SC_OPERDATA_T_PB,
  __module__ = '_py_SC_OperData_t_pb2'
  # @@protoc_insertion_point(class_scope:SC_OperData_t_pb)
  ))
_sym_db.RegisterMessage(SC_OperData_t_pb)


# @@protoc_insertion_point(module_scope)
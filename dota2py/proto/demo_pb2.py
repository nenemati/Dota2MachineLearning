# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import google.protobuf.descriptor_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='demo.proto',
  package='',
  serialized_pb='\n\ndemo.proto\x1a google/protobuf/descriptor.proto\"\xfc\x01\n\x0f\x43\x44\x65moFileHeader\x12\x17\n\x0f\x64\x65mo_file_stamp\x18\x01 \x02(\t\x12\x18\n\x10network_protocol\x18\x02 \x01(\x05\x12\x13\n\x0bserver_name\x18\x03 \x01(\t\x12\x13\n\x0b\x63lient_name\x18\x04 \x01(\t\x12\x10\n\x08map_name\x18\x05 \x01(\t\x12\x16\n\x0egame_directory\x18\x06 \x01(\t\x12\x1b\n\x13\x66ullpackets_version\x18\x07 \x01(\x05\x12!\n\x19\x61llow_clientside_entities\x18\x08 \x01(\x08\x12\"\n\x1a\x61llow_clientside_particles\x18\t \x01(\x08\"\xde\x03\n\tCGameInfo\x12&\n\x04\x64ota\x18\x04 \x01(\x0b\x32\x18.CGameInfo.CDotaGameInfo\x1a\xa8\x03\n\rCDotaGameInfo\x12\x10\n\x08match_id\x18\x01 \x01(\r\x12\x11\n\tgame_mode\x18\x02 \x01(\x05\x12\x13\n\x0bgame_winner\x18\x03 \x01(\x05\x12\x39\n\x0bplayer_info\x18\x04 \x03(\x0b\x32$.CGameInfo.CDotaGameInfo.CPlayerInfo\x12\x10\n\x08leagueid\x18\x05 \x01(\r\x12=\n\npicks_bans\x18\x06 \x03(\x0b\x32).CGameInfo.CDotaGameInfo.CHeroSelectEvent\x12\x17\n\x0fradiant_team_id\x18\x07 \x01(\r\x12\x14\n\x0c\x64ire_team_id\x18\x08 \x01(\r\x1a^\n\x0b\x43PlayerInfo\x12\x11\n\thero_name\x18\x01 \x01(\t\x12\x13\n\x0bplayer_name\x18\x02 \x01(\t\x12\x16\n\x0eis_fake_client\x18\x03 \x01(\x08\x12\x0f\n\x07steamid\x18\x04 \x01(\x04\x1a\x42\n\x10\x43HeroSelectEvent\x12\x0f\n\x07is_pick\x18\x01 \x01(\x08\x12\x0c\n\x04team\x18\x02 \x01(\r\x12\x0f\n\x07hero_id\x18\x03 \x01(\r\"v\n\rCDemoFileInfo\x12\x15\n\rplayback_time\x18\x01 \x01(\x02\x12\x16\n\x0eplayback_ticks\x18\x02 \x01(\x05\x12\x17\n\x0fplayback_frames\x18\x03 \x01(\x05\x12\x1d\n\tgame_info\x18\x04 \x01(\x0b\x32\n.CGameInfo\"J\n\x0b\x43\x44\x65moPacket\x12\x13\n\x0bsequence_in\x18\x01 \x01(\x05\x12\x18\n\x10sequence_out_ack\x18\x02 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"Y\n\x0f\x43\x44\x65moFullPacket\x12(\n\x0cstring_table\x18\x01 \x01(\x0b\x32\x12.CDemoStringTables\x12\x1c\n\x06packet\x18\x02 \x01(\x0b\x32\x0c.CDemoPacket\"\x0f\n\rCDemoSyncTick\"$\n\x0f\x43\x44\x65moConsoleCmd\x12\x11\n\tcmdstring\x18\x01 \x01(\t\"\x1f\n\x0f\x43\x44\x65moSendTables\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\x81\x01\n\x0e\x43\x44\x65moClassInfo\x12(\n\x07\x63lasses\x18\x01 \x03(\x0b\x32\x17.CDemoClassInfo.class_t\x1a\x45\n\x07\x63lass_t\x12\x10\n\x08\x63lass_id\x18\x01 \x01(\x05\x12\x14\n\x0cnetwork_name\x18\x02 \x01(\t\x12\x12\n\ntable_name\x18\x03 \x01(\t\"7\n\x0f\x43\x44\x65moCustomData\x12\x16\n\x0e\x63\x61llback_index\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"+\n\x18\x43\x44\x65moCustomDataCallbacks\x12\x0f\n\x07save_id\x18\x01 \x03(\t\"\xfb\x01\n\x11\x43\x44\x65moStringTables\x12*\n\x06tables\x18\x01 \x03(\x0b\x32\x1a.CDemoStringTables.table_t\x1a$\n\x07items_t\x12\x0b\n\x03str\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x1a\x93\x01\n\x07table_t\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12)\n\x05items\x18\x02 \x03(\x0b\x32\x1a.CDemoStringTables.items_t\x12\x34\n\x10items_clientside\x18\x03 \x03(\x0b\x32\x1a.CDemoStringTables.items_t\x12\x13\n\x0btable_flags\x18\x04 \x01(\x05\"\x0b\n\tCDemoStop\"0\n\x0c\x43\x44\x65moUserCmd\x12\x12\n\ncmd_number\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c*\xdd\x02\n\rEDemoCommands\x12\x16\n\tDEM_Error\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x0c\n\x08\x44\x45M_Stop\x10\x00\x12\x12\n\x0e\x44\x45M_FileHeader\x10\x01\x12\x10\n\x0c\x44\x45M_FileInfo\x10\x02\x12\x10\n\x0c\x44\x45M_SyncTick\x10\x03\x12\x12\n\x0e\x44\x45M_SendTables\x10\x04\x12\x11\n\rDEM_ClassInfo\x10\x05\x12\x14\n\x10\x44\x45M_StringTables\x10\x06\x12\x0e\n\nDEM_Packet\x10\x07\x12\x14\n\x10\x44\x45M_SignonPacket\x10\x08\x12\x12\n\x0e\x44\x45M_ConsoleCmd\x10\t\x12\x12\n\x0e\x44\x45M_CustomData\x10\n\x12\x1b\n\x17\x44\x45M_CustomDataCallbacks\x10\x0b\x12\x0f\n\x0b\x44\x45M_UserCmd\x10\x0c\x12\x12\n\x0e\x44\x45M_FullPacket\x10\r\x12\x0b\n\x07\x44\x45M_Max\x10\x0e\x12\x14\n\x10\x44\x45M_IsCompressed\x10p')

_EDEMOCOMMANDS = descriptor.EnumDescriptor(
  name='EDemoCommands',
  full_name='EDemoCommands',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='DEM_Error', index=0, number=-1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DEM_Stop', index=1, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DEM_FileHeader', index=2, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DEM_FileInfo', index=3, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DEM_SyncTick', index=4, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DEM_SendTables', index=5, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DEM_ClassInfo', index=6, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DEM_StringTables', index=7, number=6,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DEM_Packet', index=8, number=7,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DEM_SignonPacket', index=9, number=8,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DEM_ConsoleCmd', index=10, number=9,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DEM_CustomData', index=11, number=10,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DEM_CustomDataCallbacks', index=12, number=11,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DEM_UserCmd', index=13, number=12,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DEM_FullPacket', index=14, number=13,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DEM_Max', index=15, number=14,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DEM_IsCompressed', index=16, number=112,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1711,
  serialized_end=2060,
)


DEM_Error = -1
DEM_Stop = 0
DEM_FileHeader = 1
DEM_FileInfo = 2
DEM_SyncTick = 3
DEM_SendTables = 4
DEM_ClassInfo = 5
DEM_StringTables = 6
DEM_Packet = 7
DEM_SignonPacket = 8
DEM_ConsoleCmd = 9
DEM_CustomData = 10
DEM_CustomDataCallbacks = 11
DEM_UserCmd = 12
DEM_FullPacket = 13
DEM_Max = 14
DEM_IsCompressed = 112



_CDEMOFILEHEADER = descriptor.Descriptor(
  name='CDemoFileHeader',
  full_name='CDemoFileHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='demo_file_stamp', full_name='CDemoFileHeader.demo_file_stamp', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='network_protocol', full_name='CDemoFileHeader.network_protocol', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='server_name', full_name='CDemoFileHeader.server_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='client_name', full_name='CDemoFileHeader.client_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='map_name', full_name='CDemoFileHeader.map_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='game_directory', full_name='CDemoFileHeader.game_directory', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='fullpackets_version', full_name='CDemoFileHeader.fullpackets_version', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='allow_clientside_entities', full_name='CDemoFileHeader.allow_clientside_entities', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='allow_clientside_particles', full_name='CDemoFileHeader.allow_clientside_particles', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=49,
  serialized_end=301,
)


_CGAMEINFO_CDOTAGAMEINFO_CPLAYERINFO = descriptor.Descriptor(
  name='CPlayerInfo',
  full_name='CGameInfo.CDotaGameInfo.CPlayerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='hero_name', full_name='CGameInfo.CDotaGameInfo.CPlayerInfo.hero_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='player_name', full_name='CGameInfo.CDotaGameInfo.CPlayerInfo.player_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_fake_client', full_name='CGameInfo.CDotaGameInfo.CPlayerInfo.is_fake_client', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='steamid', full_name='CGameInfo.CDotaGameInfo.CPlayerInfo.steamid', index=3,
      number=4, type=4, cpp_type=4, label=1,
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
  serialized_start=620,
  serialized_end=714,
)

_CGAMEINFO_CDOTAGAMEINFO_CHEROSELECTEVENT = descriptor.Descriptor(
  name='CHeroSelectEvent',
  full_name='CGameInfo.CDotaGameInfo.CHeroSelectEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='is_pick', full_name='CGameInfo.CDotaGameInfo.CHeroSelectEvent.is_pick', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='team', full_name='CGameInfo.CDotaGameInfo.CHeroSelectEvent.team', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hero_id', full_name='CGameInfo.CDotaGameInfo.CHeroSelectEvent.hero_id', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=716,
  serialized_end=782,
)

_CGAMEINFO_CDOTAGAMEINFO = descriptor.Descriptor(
  name='CDotaGameInfo',
  full_name='CGameInfo.CDotaGameInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='match_id', full_name='CGameInfo.CDotaGameInfo.match_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='game_mode', full_name='CGameInfo.CDotaGameInfo.game_mode', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='game_winner', full_name='CGameInfo.CDotaGameInfo.game_winner', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='player_info', full_name='CGameInfo.CDotaGameInfo.player_info', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='leagueid', full_name='CGameInfo.CDotaGameInfo.leagueid', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='picks_bans', full_name='CGameInfo.CDotaGameInfo.picks_bans', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='radiant_team_id', full_name='CGameInfo.CDotaGameInfo.radiant_team_id', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dire_team_id', full_name='CGameInfo.CDotaGameInfo.dire_team_id', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CGAMEINFO_CDOTAGAMEINFO_CPLAYERINFO, _CGAMEINFO_CDOTAGAMEINFO_CHEROSELECTEVENT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=358,
  serialized_end=782,
)

_CGAMEINFO = descriptor.Descriptor(
  name='CGameInfo',
  full_name='CGameInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='dota', full_name='CGameInfo.dota', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CGAMEINFO_CDOTAGAMEINFO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=304,
  serialized_end=782,
)


_CDEMOFILEINFO = descriptor.Descriptor(
  name='CDemoFileInfo',
  full_name='CDemoFileInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='playback_time', full_name='CDemoFileInfo.playback_time', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='playback_ticks', full_name='CDemoFileInfo.playback_ticks', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='playback_frames', full_name='CDemoFileInfo.playback_frames', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='game_info', full_name='CDemoFileInfo.game_info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=784,
  serialized_end=902,
)


_CDEMOPACKET = descriptor.Descriptor(
  name='CDemoPacket',
  full_name='CDemoPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sequence_in', full_name='CDemoPacket.sequence_in', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sequence_out_ack', full_name='CDemoPacket.sequence_out_ack', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='CDemoPacket.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  serialized_start=904,
  serialized_end=978,
)


_CDEMOFULLPACKET = descriptor.Descriptor(
  name='CDemoFullPacket',
  full_name='CDemoFullPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='string_table', full_name='CDemoFullPacket.string_table', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='packet', full_name='CDemoFullPacket.packet', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=980,
  serialized_end=1069,
)


_CDEMOSYNCTICK = descriptor.Descriptor(
  name='CDemoSyncTick',
  full_name='CDemoSyncTick',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1071,
  serialized_end=1086,
)


_CDEMOCONSOLECMD = descriptor.Descriptor(
  name='CDemoConsoleCmd',
  full_name='CDemoConsoleCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='cmdstring', full_name='CDemoConsoleCmd.cmdstring', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=1088,
  serialized_end=1124,
)


_CDEMOSENDTABLES = descriptor.Descriptor(
  name='CDemoSendTables',
  full_name='CDemoSendTables',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='data', full_name='CDemoSendTables.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  serialized_start=1126,
  serialized_end=1157,
)


_CDEMOCLASSINFO_CLASS_T = descriptor.Descriptor(
  name='class_t',
  full_name='CDemoClassInfo.class_t',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='class_id', full_name='CDemoClassInfo.class_t.class_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='network_name', full_name='CDemoClassInfo.class_t.network_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='table_name', full_name='CDemoClassInfo.class_t.table_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=1220,
  serialized_end=1289,
)

_CDEMOCLASSINFO = descriptor.Descriptor(
  name='CDemoClassInfo',
  full_name='CDemoClassInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='classes', full_name='CDemoClassInfo.classes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CDEMOCLASSINFO_CLASS_T, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1160,
  serialized_end=1289,
)


_CDEMOCUSTOMDATA = descriptor.Descriptor(
  name='CDemoCustomData',
  full_name='CDemoCustomData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='callback_index', full_name='CDemoCustomData.callback_index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='CDemoCustomData.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  serialized_start=1291,
  serialized_end=1346,
)


_CDEMOCUSTOMDATACALLBACKS = descriptor.Descriptor(
  name='CDemoCustomDataCallbacks',
  full_name='CDemoCustomDataCallbacks',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='save_id', full_name='CDemoCustomDataCallbacks.save_id', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=1348,
  serialized_end=1391,
)


_CDEMOSTRINGTABLES_ITEMS_T = descriptor.Descriptor(
  name='items_t',
  full_name='CDemoStringTables.items_t',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='str', full_name='CDemoStringTables.items_t.str', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='CDemoStringTables.items_t.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  serialized_start=1459,
  serialized_end=1495,
)

_CDEMOSTRINGTABLES_TABLE_T = descriptor.Descriptor(
  name='table_t',
  full_name='CDemoStringTables.table_t',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='table_name', full_name='CDemoStringTables.table_t.table_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='items', full_name='CDemoStringTables.table_t.items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='items_clientside', full_name='CDemoStringTables.table_t.items_clientside', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='table_flags', full_name='CDemoStringTables.table_t.table_flags', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=1498,
  serialized_end=1645,
)

_CDEMOSTRINGTABLES = descriptor.Descriptor(
  name='CDemoStringTables',
  full_name='CDemoStringTables',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='tables', full_name='CDemoStringTables.tables', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CDEMOSTRINGTABLES_ITEMS_T, _CDEMOSTRINGTABLES_TABLE_T, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1394,
  serialized_end=1645,
)


_CDEMOSTOP = descriptor.Descriptor(
  name='CDemoStop',
  full_name='CDemoStop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1647,
  serialized_end=1658,
)


_CDEMOUSERCMD = descriptor.Descriptor(
  name='CDemoUserCmd',
  full_name='CDemoUserCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='cmd_number', full_name='CDemoUserCmd.cmd_number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='CDemoUserCmd.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  serialized_start=1660,
  serialized_end=1708,
)

_CGAMEINFO_CDOTAGAMEINFO_CPLAYERINFO.containing_type = _CGAMEINFO_CDOTAGAMEINFO;
_CGAMEINFO_CDOTAGAMEINFO_CHEROSELECTEVENT.containing_type = _CGAMEINFO_CDOTAGAMEINFO;
_CGAMEINFO_CDOTAGAMEINFO.fields_by_name['player_info'].message_type = _CGAMEINFO_CDOTAGAMEINFO_CPLAYERINFO
_CGAMEINFO_CDOTAGAMEINFO.fields_by_name['picks_bans'].message_type = _CGAMEINFO_CDOTAGAMEINFO_CHEROSELECTEVENT
_CGAMEINFO_CDOTAGAMEINFO.containing_type = _CGAMEINFO;
_CGAMEINFO.fields_by_name['dota'].message_type = _CGAMEINFO_CDOTAGAMEINFO
_CDEMOFILEINFO.fields_by_name['game_info'].message_type = _CGAMEINFO
_CDEMOFULLPACKET.fields_by_name['string_table'].message_type = _CDEMOSTRINGTABLES
_CDEMOFULLPACKET.fields_by_name['packet'].message_type = _CDEMOPACKET
_CDEMOCLASSINFO_CLASS_T.containing_type = _CDEMOCLASSINFO;
_CDEMOCLASSINFO.fields_by_name['classes'].message_type = _CDEMOCLASSINFO_CLASS_T
_CDEMOSTRINGTABLES_ITEMS_T.containing_type = _CDEMOSTRINGTABLES;
_CDEMOSTRINGTABLES_TABLE_T.fields_by_name['items'].message_type = _CDEMOSTRINGTABLES_ITEMS_T
_CDEMOSTRINGTABLES_TABLE_T.fields_by_name['items_clientside'].message_type = _CDEMOSTRINGTABLES_ITEMS_T
_CDEMOSTRINGTABLES_TABLE_T.containing_type = _CDEMOSTRINGTABLES;
_CDEMOSTRINGTABLES.fields_by_name['tables'].message_type = _CDEMOSTRINGTABLES_TABLE_T
DESCRIPTOR.message_types_by_name['CDemoFileHeader'] = _CDEMOFILEHEADER
DESCRIPTOR.message_types_by_name['CGameInfo'] = _CGAMEINFO
DESCRIPTOR.message_types_by_name['CDemoFileInfo'] = _CDEMOFILEINFO
DESCRIPTOR.message_types_by_name['CDemoPacket'] = _CDEMOPACKET
DESCRIPTOR.message_types_by_name['CDemoFullPacket'] = _CDEMOFULLPACKET
DESCRIPTOR.message_types_by_name['CDemoSyncTick'] = _CDEMOSYNCTICK
DESCRIPTOR.message_types_by_name['CDemoConsoleCmd'] = _CDEMOCONSOLECMD
DESCRIPTOR.message_types_by_name['CDemoSendTables'] = _CDEMOSENDTABLES
DESCRIPTOR.message_types_by_name['CDemoClassInfo'] = _CDEMOCLASSINFO
DESCRIPTOR.message_types_by_name['CDemoCustomData'] = _CDEMOCUSTOMDATA
DESCRIPTOR.message_types_by_name['CDemoCustomDataCallbacks'] = _CDEMOCUSTOMDATACALLBACKS
DESCRIPTOR.message_types_by_name['CDemoStringTables'] = _CDEMOSTRINGTABLES
DESCRIPTOR.message_types_by_name['CDemoStop'] = _CDEMOSTOP
DESCRIPTOR.message_types_by_name['CDemoUserCmd'] = _CDEMOUSERCMD

class CDemoFileHeader(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CDEMOFILEHEADER
  
  # @@protoc_insertion_point(class_scope:CDemoFileHeader)

class CGameInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class CDotaGameInfo(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    
    class CPlayerInfo(message.Message):
      __metaclass__ = reflection.GeneratedProtocolMessageType
      DESCRIPTOR = _CGAMEINFO_CDOTAGAMEINFO_CPLAYERINFO
      
      # @@protoc_insertion_point(class_scope:CGameInfo.CDotaGameInfo.CPlayerInfo)
    
    class CHeroSelectEvent(message.Message):
      __metaclass__ = reflection.GeneratedProtocolMessageType
      DESCRIPTOR = _CGAMEINFO_CDOTAGAMEINFO_CHEROSELECTEVENT
      
      # @@protoc_insertion_point(class_scope:CGameInfo.CDotaGameInfo.CHeroSelectEvent)
    DESCRIPTOR = _CGAMEINFO_CDOTAGAMEINFO
    
    # @@protoc_insertion_point(class_scope:CGameInfo.CDotaGameInfo)
  DESCRIPTOR = _CGAMEINFO
  
  # @@protoc_insertion_point(class_scope:CGameInfo)

class CDemoFileInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CDEMOFILEINFO
  
  # @@protoc_insertion_point(class_scope:CDemoFileInfo)

class CDemoPacket(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CDEMOPACKET
  
  # @@protoc_insertion_point(class_scope:CDemoPacket)

class CDemoFullPacket(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CDEMOFULLPACKET
  
  # @@protoc_insertion_point(class_scope:CDemoFullPacket)

class CDemoSyncTick(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CDEMOSYNCTICK
  
  # @@protoc_insertion_point(class_scope:CDemoSyncTick)

class CDemoConsoleCmd(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CDEMOCONSOLECMD
  
  # @@protoc_insertion_point(class_scope:CDemoConsoleCmd)

class CDemoSendTables(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CDEMOSENDTABLES
  
  # @@protoc_insertion_point(class_scope:CDemoSendTables)

class CDemoClassInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class class_t(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _CDEMOCLASSINFO_CLASS_T
    
    # @@protoc_insertion_point(class_scope:CDemoClassInfo.class_t)
  DESCRIPTOR = _CDEMOCLASSINFO
  
  # @@protoc_insertion_point(class_scope:CDemoClassInfo)

class CDemoCustomData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CDEMOCUSTOMDATA
  
  # @@protoc_insertion_point(class_scope:CDemoCustomData)

class CDemoCustomDataCallbacks(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CDEMOCUSTOMDATACALLBACKS
  
  # @@protoc_insertion_point(class_scope:CDemoCustomDataCallbacks)

class CDemoStringTables(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class items_t(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _CDEMOSTRINGTABLES_ITEMS_T
    
    # @@protoc_insertion_point(class_scope:CDemoStringTables.items_t)
  
  class table_t(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _CDEMOSTRINGTABLES_TABLE_T
    
    # @@protoc_insertion_point(class_scope:CDemoStringTables.table_t)
  DESCRIPTOR = _CDEMOSTRINGTABLES
  
  # @@protoc_insertion_point(class_scope:CDemoStringTables)

class CDemoStop(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CDEMOSTOP
  
  # @@protoc_insertion_point(class_scope:CDemoStop)

class CDemoUserCmd(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CDEMOUSERCMD
  
  # @@protoc_insertion_point(class_scope:CDemoUserCmd)

# @@protoc_insertion_point(module_scope)

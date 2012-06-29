"""autogenerated by genmsg_py from SphereTraxData.msg. Do not edit."""
import roslib.message
import struct


class SphereTraxData(roslib.message.Message):
  _md5sum = "eac4f8449375cb87b179b846d39dae32"
  _type = "spheretrax_ros/SphereTraxData"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float64 timestamp
uint64 framenumber
float64 omega_x
float64 omega_y
float64 omega_z
float64 head_rate
float64 forw_rate
float64 side_rate


"""
  __slots__ = ['timestamp','framenumber','omega_x','omega_y','omega_z','head_rate','forw_rate','side_rate']
  _slot_types = ['float64','uint64','float64','float64','float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       timestamp,framenumber,omega_x,omega_y,omega_z,head_rate,forw_rate,side_rate
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(SphereTraxData, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.timestamp is None:
        self.timestamp = 0.
      if self.framenumber is None:
        self.framenumber = 0
      if self.omega_x is None:
        self.omega_x = 0.
      if self.omega_y is None:
        self.omega_y = 0.
      if self.omega_z is None:
        self.omega_z = 0.
      if self.head_rate is None:
        self.head_rate = 0.
      if self.forw_rate is None:
        self.forw_rate = 0.
      if self.side_rate is None:
        self.side_rate = 0.
    else:
      self.timestamp = 0.
      self.framenumber = 0
      self.omega_x = 0.
      self.omega_y = 0.
      self.omega_z = 0.
      self.head_rate = 0.
      self.forw_rate = 0.
      self.side_rate = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      _x = self
      buff.write(_struct_dQ6d.pack(_x.timestamp, _x.framenumber, _x.omega_x, _x.omega_y, _x.omega_z, _x.head_rate, _x.forw_rate, _x.side_rate))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      end = 0
      _x = self
      start = end
      end += 64
      (_x.timestamp, _x.framenumber, _x.omega_x, _x.omega_y, _x.omega_z, _x.head_rate, _x.forw_rate, _x.side_rate,) = _struct_dQ6d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      _x = self
      buff.write(_struct_dQ6d.pack(_x.timestamp, _x.framenumber, _x.omega_x, _x.omega_y, _x.omega_z, _x.head_rate, _x.forw_rate, _x.side_rate))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 64
      (_x.timestamp, _x.framenumber, _x.omega_x, _x.omega_y, _x.omega_z, _x.head_rate, _x.forw_rate, _x.side_rate,) = _struct_dQ6d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_dQ6d = struct.Struct("<dQ6d")
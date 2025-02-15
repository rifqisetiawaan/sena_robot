// Generated by gencpp from file sena_message/motor.msg
// DO NOT EDIT!


#ifndef SENA_MESSAGE_MESSAGE_MOTOR_H
#define SENA_MESSAGE_MESSAGE_MOTOR_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace sena_message
{
template <class ContainerAllocator>
struct motor_
{
  typedef motor_<ContainerAllocator> Type;

  motor_()
    : motor1(0.0)
    , motor2(0.0)
    , motor3(0.0)  {
    }
  motor_(const ContainerAllocator& _alloc)
    : motor1(0.0)
    , motor2(0.0)
    , motor3(0.0)  {
  (void)_alloc;
    }



   typedef float _motor1_type;
  _motor1_type motor1;

   typedef float _motor2_type;
  _motor2_type motor2;

   typedef float _motor3_type;
  _motor3_type motor3;





  typedef boost::shared_ptr< ::sena_message::motor_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::sena_message::motor_<ContainerAllocator> const> ConstPtr;

}; // struct motor_

typedef ::sena_message::motor_<std::allocator<void> > motor;

typedef boost::shared_ptr< ::sena_message::motor > motorPtr;
typedef boost::shared_ptr< ::sena_message::motor const> motorConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::sena_message::motor_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::sena_message::motor_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::sena_message::motor_<ContainerAllocator1> & lhs, const ::sena_message::motor_<ContainerAllocator2> & rhs)
{
  return lhs.motor1 == rhs.motor1 &&
    lhs.motor2 == rhs.motor2 &&
    lhs.motor3 == rhs.motor3;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::sena_message::motor_<ContainerAllocator1> & lhs, const ::sena_message::motor_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace sena_message

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::sena_message::motor_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sena_message::motor_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sena_message::motor_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sena_message::motor_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sena_message::motor_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sena_message::motor_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::sena_message::motor_<ContainerAllocator> >
{
  static const char* value()
  {
    return "65986bed022cdc1fac2edc1016acb2c6";
  }

  static const char* value(const ::sena_message::motor_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x65986bed022cdc1fULL;
  static const uint64_t static_value2 = 0xac2edc1016acb2c6ULL;
};

template<class ContainerAllocator>
struct DataType< ::sena_message::motor_<ContainerAllocator> >
{
  static const char* value()
  {
    return "sena_message/motor";
  }

  static const char* value(const ::sena_message::motor_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::sena_message::motor_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 motor1\n"
"float32 motor2\n"
"float32 motor3\n"
;
  }

  static const char* value(const ::sena_message::motor_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::sena_message::motor_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.motor1);
      stream.next(m.motor2);
      stream.next(m.motor3);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct motor_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::sena_message::motor_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::sena_message::motor_<ContainerAllocator>& v)
  {
    s << indent << "motor1: ";
    Printer<float>::stream(s, indent + "  ", v.motor1);
    s << indent << "motor2: ";
    Printer<float>::stream(s, indent + "  ", v.motor2);
    s << indent << "motor3: ";
    Printer<float>::stream(s, indent + "  ", v.motor3);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SENA_MESSAGE_MESSAGE_MOTOR_H

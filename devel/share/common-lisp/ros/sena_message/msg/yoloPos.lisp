; Auto-generated. Do not edit!


(cl:in-package sena_message-msg)


;//! \htmlinclude yoloPos.msg.html

(cl:defclass <yoloPos> (roslisp-msg-protocol:ros-message)
  ((x_bola
    :reader x_bola
    :initarg :x_bola
    :type cl:float
    :initform 0.0)
   (y_bola
    :reader y_bola
    :initarg :y_bola
    :type cl:float
    :initform 0.0)
   (x_kotak
    :reader x_kotak
    :initarg :x_kotak
    :type cl:float
    :initform 0.0)
   (y_kotak
    :reader y_kotak
    :initarg :y_kotak
    :type cl:float
    :initform 0.0))
)

(cl:defclass yoloPos (<yoloPos>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <yoloPos>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'yoloPos)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sena_message-msg:<yoloPos> is deprecated: use sena_message-msg:yoloPos instead.")))

(cl:ensure-generic-function 'x_bola-val :lambda-list '(m))
(cl:defmethod x_bola-val ((m <yoloPos>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sena_message-msg:x_bola-val is deprecated.  Use sena_message-msg:x_bola instead.")
  (x_bola m))

(cl:ensure-generic-function 'y_bola-val :lambda-list '(m))
(cl:defmethod y_bola-val ((m <yoloPos>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sena_message-msg:y_bola-val is deprecated.  Use sena_message-msg:y_bola instead.")
  (y_bola m))

(cl:ensure-generic-function 'x_kotak-val :lambda-list '(m))
(cl:defmethod x_kotak-val ((m <yoloPos>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sena_message-msg:x_kotak-val is deprecated.  Use sena_message-msg:x_kotak instead.")
  (x_kotak m))

(cl:ensure-generic-function 'y_kotak-val :lambda-list '(m))
(cl:defmethod y_kotak-val ((m <yoloPos>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sena_message-msg:y_kotak-val is deprecated.  Use sena_message-msg:y_kotak instead.")
  (y_kotak m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <yoloPos>) ostream)
  "Serializes a message object of type '<yoloPos>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'x_bola))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'y_bola))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'x_kotak))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'y_kotak))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <yoloPos>) istream)
  "Deserializes a message object of type '<yoloPos>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x_bola) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y_bola) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x_kotak) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y_kotak) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<yoloPos>)))
  "Returns string type for a message object of type '<yoloPos>"
  "sena_message/yoloPos")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'yoloPos)))
  "Returns string type for a message object of type 'yoloPos"
  "sena_message/yoloPos")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<yoloPos>)))
  "Returns md5sum for a message object of type '<yoloPos>"
  "01818e6dac8eb5be630fe9157773ca48")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'yoloPos)))
  "Returns md5sum for a message object of type 'yoloPos"
  "01818e6dac8eb5be630fe9157773ca48")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<yoloPos>)))
  "Returns full string definition for message of type '<yoloPos>"
  (cl:format cl:nil "float64 x_bola~%float64 y_bola~%float64 x_kotak~%float64 y_kotak~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'yoloPos)))
  "Returns full string definition for message of type 'yoloPos"
  (cl:format cl:nil "float64 x_bola~%float64 y_bola~%float64 x_kotak~%float64 y_kotak~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <yoloPos>))
  (cl:+ 0
     8
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <yoloPos>))
  "Converts a ROS message object to a list"
  (cl:list 'yoloPos
    (cl:cons ':x_bola (x_bola msg))
    (cl:cons ':y_bola (y_bola msg))
    (cl:cons ':x_kotak (x_kotak msg))
    (cl:cons ':y_kotak (y_kotak msg))
))

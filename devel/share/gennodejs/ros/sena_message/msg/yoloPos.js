// Auto-generated. Do not edit!

// (in-package sena_message.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class yoloPos {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.x_bola = null;
      this.y_bola = null;
      this.x_kotak = null;
      this.y_kotak = null;
    }
    else {
      if (initObj.hasOwnProperty('x_bola')) {
        this.x_bola = initObj.x_bola
      }
      else {
        this.x_bola = 0.0;
      }
      if (initObj.hasOwnProperty('y_bola')) {
        this.y_bola = initObj.y_bola
      }
      else {
        this.y_bola = 0.0;
      }
      if (initObj.hasOwnProperty('x_kotak')) {
        this.x_kotak = initObj.x_kotak
      }
      else {
        this.x_kotak = 0.0;
      }
      if (initObj.hasOwnProperty('y_kotak')) {
        this.y_kotak = initObj.y_kotak
      }
      else {
        this.y_kotak = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type yoloPos
    // Serialize message field [x_bola]
    bufferOffset = _serializer.float64(obj.x_bola, buffer, bufferOffset);
    // Serialize message field [y_bola]
    bufferOffset = _serializer.float64(obj.y_bola, buffer, bufferOffset);
    // Serialize message field [x_kotak]
    bufferOffset = _serializer.float64(obj.x_kotak, buffer, bufferOffset);
    // Serialize message field [y_kotak]
    bufferOffset = _serializer.float64(obj.y_kotak, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type yoloPos
    let len;
    let data = new yoloPos(null);
    // Deserialize message field [x_bola]
    data.x_bola = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [y_bola]
    data.y_bola = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [x_kotak]
    data.x_kotak = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [y_kotak]
    data.y_kotak = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 32;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sena_message/yoloPos';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '01818e6dac8eb5be630fe9157773ca48';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 x_bola
    float64 y_bola
    float64 x_kotak
    float64 y_kotak
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new yoloPos(null);
    if (msg.x_bola !== undefined) {
      resolved.x_bola = msg.x_bola;
    }
    else {
      resolved.x_bola = 0.0
    }

    if (msg.y_bola !== undefined) {
      resolved.y_bola = msg.y_bola;
    }
    else {
      resolved.y_bola = 0.0
    }

    if (msg.x_kotak !== undefined) {
      resolved.x_kotak = msg.x_kotak;
    }
    else {
      resolved.x_kotak = 0.0
    }

    if (msg.y_kotak !== undefined) {
      resolved.y_kotak = msg.y_kotak;
    }
    else {
      resolved.y_kotak = 0.0
    }

    return resolved;
    }
};

module.exports = yoloPos;

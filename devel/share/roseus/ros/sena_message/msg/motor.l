;; Auto-generated. Do not edit!


(when (boundp 'sena_message::motor)
  (if (not (find-package "SENA_MESSAGE"))
    (make-package "SENA_MESSAGE"))
  (shadow 'motor (find-package "SENA_MESSAGE")))
(unless (find-package "SENA_MESSAGE::MOTOR")
  (make-package "SENA_MESSAGE::MOTOR"))

(in-package "ROS")
;;//! \htmlinclude motor.msg.html


(defclass sena_message::motor
  :super ros::object
  :slots (_motor1 _motor2 _motor3 ))

(defmethod sena_message::motor
  (:init
   (&key
    ((:motor1 __motor1) 0.0)
    ((:motor2 __motor2) 0.0)
    ((:motor3 __motor3) 0.0)
    )
   (send-super :init)
   (setq _motor1 (float __motor1))
   (setq _motor2 (float __motor2))
   (setq _motor3 (float __motor3))
   self)
  (:motor1
   (&optional __motor1)
   (if __motor1 (setq _motor1 __motor1)) _motor1)
  (:motor2
   (&optional __motor2)
   (if __motor2 (setq _motor2 __motor2)) _motor2)
  (:motor3
   (&optional __motor3)
   (if __motor3 (setq _motor3 __motor3)) _motor3)
  (:serialization-length
   ()
   (+
    ;; float32 _motor1
    4
    ;; float32 _motor2
    4
    ;; float32 _motor3
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _motor1
       (sys::poke _motor1 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _motor2
       (sys::poke _motor2 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _motor3
       (sys::poke _motor3 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _motor1
     (setq _motor1 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _motor2
     (setq _motor2 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _motor3
     (setq _motor3 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get sena_message::motor :md5sum-) "65986bed022cdc1fac2edc1016acb2c6")
(setf (get sena_message::motor :datatype-) "sena_message/motor")
(setf (get sena_message::motor :definition-)
      "float32 motor1
float32 motor2
float32 motor3
")



(provide :sena_message/motor "65986bed022cdc1fac2edc1016acb2c6")



;; Auto-generated. Do not edit!


(when (boundp 'sena_message::yoloPos)
  (if (not (find-package "SENA_MESSAGE"))
    (make-package "SENA_MESSAGE"))
  (shadow 'yoloPos (find-package "SENA_MESSAGE")))
(unless (find-package "SENA_MESSAGE::YOLOPOS")
  (make-package "SENA_MESSAGE::YOLOPOS"))

(in-package "ROS")
;;//! \htmlinclude yoloPos.msg.html


(defclass sena_message::yoloPos
  :super ros::object
  :slots (_x_bola _y_bola _x_kotak _y_kotak ))

(defmethod sena_message::yoloPos
  (:init
   (&key
    ((:x_bola __x_bola) 0.0)
    ((:y_bola __y_bola) 0.0)
    ((:x_kotak __x_kotak) 0.0)
    ((:y_kotak __y_kotak) 0.0)
    )
   (send-super :init)
   (setq _x_bola (float __x_bola))
   (setq _y_bola (float __y_bola))
   (setq _x_kotak (float __x_kotak))
   (setq _y_kotak (float __y_kotak))
   self)
  (:x_bola
   (&optional __x_bola)
   (if __x_bola (setq _x_bola __x_bola)) _x_bola)
  (:y_bola
   (&optional __y_bola)
   (if __y_bola (setq _y_bola __y_bola)) _y_bola)
  (:x_kotak
   (&optional __x_kotak)
   (if __x_kotak (setq _x_kotak __x_kotak)) _x_kotak)
  (:y_kotak
   (&optional __y_kotak)
   (if __y_kotak (setq _y_kotak __y_kotak)) _y_kotak)
  (:serialization-length
   ()
   (+
    ;; float64 _x_bola
    8
    ;; float64 _y_bola
    8
    ;; float64 _x_kotak
    8
    ;; float64 _y_kotak
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _x_bola
       (sys::poke _x_bola (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y_bola
       (sys::poke _y_bola (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _x_kotak
       (sys::poke _x_kotak (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y_kotak
       (sys::poke _y_kotak (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x_bola
     (setq _x_bola (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y_bola
     (setq _y_bola (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _x_kotak
     (setq _x_kotak (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y_kotak
     (setq _y_kotak (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get sena_message::yoloPos :md5sum-) "01818e6dac8eb5be630fe9157773ca48")
(setf (get sena_message::yoloPos :datatype-) "sena_message/yoloPos")
(setf (get sena_message::yoloPos :definition-)
      "float64 x_bola
float64 y_bola
float64 x_kotak
float64 y_kotak

")



(provide :sena_message/yoloPos "01818e6dac8eb5be630fe9157773ca48")



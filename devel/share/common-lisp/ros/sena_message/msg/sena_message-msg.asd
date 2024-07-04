
(cl:in-package :asdf)

(defsystem "sena_message-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "encoder" :depends-on ("_package_encoder"))
    (:file "_package_encoder" :depends-on ("_package"))
    (:file "motor" :depends-on ("_package_motor"))
    (:file "_package_motor" :depends-on ("_package"))
    (:file "yoloPos" :depends-on ("_package_yoloPos"))
    (:file "_package_yoloPos" :depends-on ("_package"))
  ))
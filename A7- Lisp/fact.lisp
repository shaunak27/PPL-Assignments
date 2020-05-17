(print "Enter a number")
(terpri)
(defvar n (read))
(setq f 1)
(loop for x from 1 to n
do (setq f (* f x)
))
(format t "Result : ~a " f)
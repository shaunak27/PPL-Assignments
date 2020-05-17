(print " Enter the list in ( 1 2 3...) format")
(terpri)
(defvar l (read) )
(print " Enter the index to be searched ")
(defvar n (read))

(setq c 0)
(loop for x in l
do (setq c (+ c 1))
(when ( equal c n) (print x) ))

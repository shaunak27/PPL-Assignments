(print "Enter a number")
(terpri)
(defvar n (read))
(defun fact (num)
( cond (( equal num 0)
(return-from fact 1))
( ( * (fact (- num 1)) num)
)
)
)


(write(fact n))


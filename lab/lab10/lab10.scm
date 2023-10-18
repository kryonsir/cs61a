(define (over-or-under num1 num2)
  'YOUR-CODE-HERE
  (if (= num1 num2) 
    	0
	(if (> num1 num2)
	  1
	  -1)
	)
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0


(define (filter-lst fn lst)
  'YOUR-CODE-HERE
  (if (eq? lst nil)
    nil

  (if (eq? (cdr lst) nil)
    (if (fn (car lst))
      (cons (car lst) nil)
      nil)
    (if (fn (car lst))
      (cons (car lst) (filter-lst fn (cdr lst)))
      (filter-lst fn (cdr lst))
      )
    )
  )


)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)


(define (make-adder num)
  'YOUR-CODE-HERE
  (lambda (x) (+ num x))
)

;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13


(define lst
    (cons (list 1) (cons 2 (cons (list 3 4) (list 5))))
    
)


(define (composed f g)
  'YOUR-CODE-HERE
  (lambda (x) (f (g x)))
)


(define (remove item lst)
  'YOUR-CODE-HERE
  (filter-lst (lambda (x) (not (= item x))) lst)
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)


(define (no-repeats s)
  'YOUR-CODE-HERE
  (if (eq? s nil)
    nil
    (if (eq? (cdr s) nil)
      (cons (car s) nil)
      (cons (car s) (no-repeats (filter-lst (lambda (x) (not (= (car s) x))) (cdr s))))
    )
    )
)


(define (substitute s old new)
  'YOUR-CODE-HERE
  (if (eq? s nil)
    nil
   (if (pair? (car s))
     (cons (substitute (car s) old new) (substitute (cdr s) old new))
     (if (eq? (car s) old)
       (cons new (substitute (cdr s) old new))
       (cons (car s) (substitute (cdr s) old new))
       )
     )
   )

)


(define (sub-all s olds news)
  'YOUR-CODE-HERE
  (if (eq? olds nil)
    s
    (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news))
    )
)


(define (cddr s)
    (cdr (cdr s)))

(define (cadr s)
    (car (cdr s)))

(define (caddr s)
    (car (cdr (cdr s))))

(define (sign num)
    (cond
        ((< num 0) -1)
        ((= num 0) 0)
        ((> num 0) 1)))
    

(define (square x) (* x x))

(define (pow x y)
    (if (= y 0) 1
        
    (if (even? y )
        (square (pow x (/ y 2)))
        (* x (square (pow x (/ (- y 1) 2))))
        )
    )
    )

(define (unique s)
    (if (eq? s nil)
        nil
        (if ((cdr s) nil)
        (cons (car s) nil) 
        (cons (car s) (unique (filter (lambda (x) (not(= (car s) x))) (cdr s))))
        )
    )
)
    
(define (replicate x n)
    (define (replicate_tail x n result)
        (if (= n 0)
            result 
            (replicate_tail x (- n 1) (append (list x) result))))
    (replicate_tail x n '())
    )

(define (accumulate combiner start n term)
    (if (= n 1)
        (combiner start (term n))
        (combiner (term n) (accumulate combiner start (- n 1) term)))
    )

(define (accumulate-tail combiner start n term)
    (define (tail combiner n term res)
        (cond 
              ((= n 0) res)
              (else (tail combiner (- n 1) term (combiner res (term n)))))
          )
    (tail combiner n term start)
)

(define-macro (list-of map-expr for var in lst if filter-expr)
    `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst)))




    
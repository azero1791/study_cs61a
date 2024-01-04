(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (cadr (cdr s))
)


(define (sign num)
  'YOUR-CODE-HERE
  (cond ((< num 0) -1)
        ((= num 0) 0)
        (else 1))
)


(define (square x) (* x x))

(define (pow x y)
  'YOUR-CODE-HERE
  (define (helper x y end)
          (cond ((= y 0) end)
                ((even? y) (helper x (/ y 2) (* end end)))
                (else (helper x (- y 1) (* end x)))))
  (helper x y 1)
)


(define (unique s)
  'YOUR-CODE-HERE
  (if (null? s)
      nil
      (cons (car s) (unique (filter (lambda (item) (not(eq? item (car s)))) (cdr s)))))
)


(define (replicate x n)
  'YOUR-CODE-HERE
  (define (helper x n lst)
          (if (zero? n)
          lst
          (helper x (- n 1) (cons x lst))))
  (helper x n nil)
)


(define (accumulate combiner start n term)
  'YOUR-CODE-HERE
  (define (helper combiner n term i)
          (if (= i n)
              (term n)
              (combiner (term i) (helper combiner n term (+ i 1)))))
  (combiner start (helper combiner n term 1))
)


(define (accumulate-tail combiner start n term)
  'YOUR-CODE-HERE
  (define (helper combiner n term i end)
          (if (< n i)
              end
              (helper combiner n term (+ i 1) (combiner end (term i)))))
  (helper combiner n term 1 start)
)


(define-macro (list-of map-expr for var in lst if filter-expr)
  'YOUR-CODE-HERE
  (list 'map (list 'lambda (list var) map-expr) (list 'filter (list 'lambda (list var) filter-expr) lst))
)



(define-macro (def func args body)
    `(define ,(cons func args) ,body)
    )


(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define all-three-multiples
  (map-stream (lambda (x) (+ x 3)) (cons-stream 0 all-three-multiples))
)


(define (compose-all funcs)
  (define (helper funcs ans)  
    (if (null? funcs)
        (lambda (x) (ans x))
        (helper (cdr funcs) (lambda (x) ((car funcs) (ans x))))))
  (helper funcs (lambda (x) x))
)


(define (partial-sums stream)
  (define (helper added stream)
          (if (null? stream)
          nil
          (cons-stream (+ added (car stream)) (helper (+ added (car stream)) (cdr-stream stream)))))
  (helper 0 stream)
)


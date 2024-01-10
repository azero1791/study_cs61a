(define (reverse lst)
    (define (helper lst ans)
            (if (null? lst)
                ans
                (helper (cdr lst) (append (list (car lst)) ans))))
    
    (helper lst '())
)


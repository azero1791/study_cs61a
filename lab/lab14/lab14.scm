(define (split-at lst n)
  (define (helper lst n ans)
  		  (if (null? lst) (append (list ans) lst)
		  	  (if (zero? n) (append (list ans) lst)
			  	  (helper (cdr lst) (- n 1) (append ans (list (car lst))))
				  )
		  	  		)
			  	)
	(helper lst n '())
)


(define-macro (switch expr cases)
	(cons 'cond
		(map (lambda (case) (cons `(eq? ,expr ,(car case)) (cdr case)))
    			cases) )
)


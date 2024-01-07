(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.

(define (cons-all first rests)
  (define (add_pre lst)
          (cons first lst))
  
  (map add_pre rests)
  )

(define (zip pairs)
    (define (helper s first second)
        (if (null? s) (list first second)
            (helper (cdr s) (append first (list (caar s))) (append second (list (car (cdar s)))))
        )
    )
    (helper pairs nil nil)
)

;; Problem 16
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 16
  (define (helper s index ans)
          (if (null? s)
              ans
              (helper (cdr s) (+ index 1) (append ans (cons (cons index (cons (car s) nil)) nil)))))
  
  (helper s 0 nil)
  )
  ; END PROBLEM 16

;; Problem 17
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ; BEGIN PROBLEM 17
  (cond ((zero? total) (list nil))
        ((null? denoms) nil)
        ((>= total (car denoms))
         (append (cons-all (car denoms) (list-change (- total (car denoms)) denoms))
                 (list-change total (cdr denoms))))
        (else (list-change total (cdr denoms))))
  )
  ; END PROBLEM 17

;; Problem 18
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 18
         expr
         ; END PROBLEM 18
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 18
         expr
         ; END PROBLEM 18
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
           (cons form (cons params (let-to-lambda body) ))
           ; END PROBLEM 18
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
           (append (list (cons 'lambda (cons (car (zip values))  (map let-to-lambda body)))) (cadr (map let-to-lambda (zip values))) )
           ; END PROBLEM 18
           ))
        (else
         ; BEGIN PROBLEM 18
         (map let-to-lambda expr)
         ; END PROBLEM 18
         )))

(define (cadr s)
        (car (cdr s)))

(define (append_s s l)
        (if (null? s)
            l
            (cons-stream (car s) (append_s (cdr-stream s) l))))

(define (rle s)
    (define (helper s last ans)
            (cond ((null? s) (if (null? last) ans (append_s ans (cons-stream last nil))))
                  ((null? last) (helper (cdr-stream s) (cons (car s) (cons 1 nil)) ans))
                  ((= (car last) (car s)) (helper (cdr-stream s) (cons (car last) (cons (+ (cadr last) 1) nil)) ans))
                  (else (helper (cdr-stream s) (cons (car s) (cons 1 nil)) (append_s ans (cons-stream last nil))))))
    (helper s '() '())
)

(define (get_item_lst item s ans)
        (cond ((or (null? s) (< (car s) item)) ans) 
               (else (get_item_lst (car s) (cdr-stream s) (append ans (list (car s)))))
            ))

(define (left_s item s)
        (if (or (null? s) (< (car s) item)) s
            (left_s (car s) (cdr-stream s))))

(define (group-by-nondecreasing s)
    (if (null? s)
         nil
         (cons-stream (get_item_lst (car s) s '()) (group-by-nondecreasing (left_s (car s) s))))
    
    )


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))


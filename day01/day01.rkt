#lang racket

(define (inverse-captcha data increment)
  (println (for/sum ([c1 (in-string data)]
                     [c2 (in-string (string-append (substring data increment)
                                                   (substring data 0 increment)))]
                     #:when (char=? c1 c2))
             (string->number (string c1)))))

(let ([data (string-trim (file->string "input.txt"))])
  (inverse-captcha data 1)
  (inverse-captcha data (/ (string-length data) 2)))

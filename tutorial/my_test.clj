(definst foo [] (saw 300))

(definst trem [freq 220 depth 500 rate 90 length 60]
    (* 0.3
       (line:kr 0 1 length FREE)
       (saw (+ freq (* depth (sin-osc:kr rate))))))

(foo)

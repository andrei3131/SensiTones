(ns tutorial.core)

(use 'overtone.live)

(definst sin-wave [freq 440 attack 0.01 sustain 0.4 release 0.1 vol 0.4] 
    (* (env-gen (lin attack sustain release) 1 1 0 1 FREE)
       (sin-osc freq)
        vol))
(comment
   (sin-wave)
)

(definst saw-wave [freq 440 attack 0.01 sustain 0.4 release 0.1 vol 0.4] 
    (* (env-gen (lin attack sustain release) 1 1 0 1 FREE)
       (saw freq)
        vol))
(comment
   (saw-wave)
)

(definst square-wave [freq 440 attack 0.01 sustain 0.4 release 0.1 vol 0.4] 
    (* (env-gen (lin attack sustain release) 1 1 0 1 FREE)
       (lf-pulse:ar freq)
        vol))
(comment
   (square-wave)
)

(definst noisey [freq 440 attack 0.01 sustain 0.4 release 0.1 vol 0.4] 
    (* (env-gen (lin attack sustain release) 1 1 0 1 FREE)
       (pink-noise) ; also have (white-noise) and others...
        vol))
(comment
   (noisey)
)

(definst triangle-wave [freq 440 attack 0.01 sustain 0.1 release 0.4 vol 0.4] 
    (* (env-gen (lin attack sustain release) 1 1 0 1 FREE)
       (lf-tri freq)
       vol))
(comment
   (triangle-wave)
)

(definst spooky-house [freq 440 width 0.2 attack 0.3 sustain 4 release 0.3 vol 0.4] 
    (* (env-gen (lin attack sustain release) 1 1 0 1 FREE)
       (sin-osc (+ freq (* 20 (lf-pulse:kr 0.5 0 width))))
        vol))
(comment
  (spooky-house)  
)

;;;;;;;;;;;;;;;;
;; Mouse Moves;;
;;;;;;;;;;;;;;;;
(demo 10 (lpf (saw 100) (mouse-x 40 5000 EXP)))
;; low-pass; move the mouse left and right to change the threshold frequency

(demo 10 (hpf (saw 100) (mouse-x 40 5000 EXP)))
;; high-pass; move the mouse left and right to change the threshold frequency

(demo 30 (bpf (saw 100) (mouse-x 40 5000 EXP) (mouse-y 0.01 1 LIN)))
;; band-pass; move mouse left/right to change threshold frequency; up/down to change bandwidth (top is narrowest)

;; here we generate a pulse of white noise, and pass it through a pluck filter
;; with a delay based on the given frequency
(let [freq 220]
   (demo (pluck (* (white-noise) (env-gen (perc 0.001 2) :action FREE)) 1 3 (/ 1 freq))))

;;Multi-channel/stereo
(defsynth sin1 [freq 440]
    (out 1 (sin-osc freq)))
(comment
    (sin1)
)

;;;;;;;;;;;;;;;;;;;
;;Musical Sources;;
;;;;;;;;;;;;;;;;;;;

(def nodoubt (sample "resources/dont_speak-no_doubt.wav"))
(def nodoubt-buf (load-sample "resources/dont_speak-no_doubt.wav"))
; (scope :buf nodoubt-buf)

(def sample-buf (load-sample "resources/dont_speak-no_doubt.wav"))
(defsynth reverb-on-left []
    (let [dry (play-buf 1 sample-buf)
          wet (free-verb dry 1)]
          (out 0 [wet dry])))

(comment
  (reverb-on-left)
)


;;;;;;;;;;;;;;;
;;Swing Music;;
;;;;;;;;;;;;;;;
; define a metronome at a given tempo, expressed in beats per minute.
(def metro (metronome 120))

(definst c-hat [amp 0.8 t 0.04]
    (let [env (env-gen (perc 0.001 t) 1 1 0 1 FREE)
                  noise (white-noise)
                          sqr (* (env-gen (perc 0.01 0.04)) (pulse 880 0.2))
                                  filt (bpf (+ sqr noise) 9000 0.5)]
          (* amp env filt)))


(definst o-hat [amp 0.8 t 0.5]
    (let [env (env-gen (perc 0.001 t) 1 1 0 1 FREE)
                  noise (white-noise)
                          sqr (* (env-gen (perc 0.01 0.04)) (pulse 880 0.2))
                                  filt (bpf (+ sqr noise) 9000 0.5)]
          (* amp env filt)))

(defn swinger [beat]
    (at (metro beat) (o-hat))
      (at (metro (inc beat)) (c-hat))
        (at (metro (+ 1.65 beat)) (c-hat))
          (apply-at (metro (+ 2 beat)) #'swinger (+ 2 beat) []))

(comment
  (swinger (metro))
)

(definst quux [freq 440] (* 0.3 (saw freq)))
(comment
  (quux)
)
(comment
  (ctl quux :freq 660)
)

;;;;;;;;
;;STOP;;
;;;;;;;;
(comment
  (stop)
)

;;;;;;;;;;;;;;;App;;;;;;;;;;;;;;;;;;;
(defn choosesong [value] (print value))


(defn receive [] 
   (let [value (read-line)]
       (choosesong (value))))

(defn -main
      "Sentient Note"
      []
      (while true (receive)))

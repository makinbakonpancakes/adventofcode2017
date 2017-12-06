(require '[clojure.string :as str])

(def rows (->> (str/split-lines (slurp "input.txt"))
           (map #(str/split % #"\t"))
           (map #(map read-string %))))

(prn (->> rows (map #(- (apply max %) (apply min %))) (apply +)))
(prn (->> rows (map #(first
                      (for [a % b % :when (> a b) :when (zero? (mod a b))]
                        (/ a b))))
          (apply +)))

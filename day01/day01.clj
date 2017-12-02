(require '[clojure.string :as str])
(defn inverse-captcha [data shift]
  (->> data
       (map vector (vec (concat (subvec data shift) (subvec data 0 shift))))
       (filter #(= (nth % 0) (nth % 1)))
       (map #(nth % 0))
       (reduce +)))

(def data (vec (map #(Character/digit % 10) (str/trim (slurp "input.txt")))))
(println (inverse-captcha data 1))
(println (inverse-captcha data (/ (count data) 2)))

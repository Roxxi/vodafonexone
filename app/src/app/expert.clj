(ns app.expert
  (:use app.utils)
  (:require  
   [ring.util.codec :as ring-codec]
   [clj-http.client :as client]))

(def client-config {:throw-entire-message? true})

(def url-template "http://habitat.expertmaker.com/api/thorwords?text=%s&long=1")

(defn- make-url-for-title [article-title]
  (format url-template (ring-codec/url-encode article-title)))

(defn- get-recommendation [article-title]
  (read-xml-response
   (client/get (make-url-for-title article-title) client-config)))

(defn- extract-recommentation-info [rec]
  (map (fn [val] (list (:value (:attrs val)) (:relevance (:attrs val))))
       (get-in rec [:content 0 :content 0 :content])))

(defn- indeterminant? [info]
  (= (reduce + 0  (map (fn [pair] (Double/parseDouble (second pair))) info)) 0))

(defn- good-interesting? [info]
  (= (Integer/parseInt (first (first info))) 0))

(defn- bad-interesting? [info]
  (= (Integer/parseInt (first (first info))) 4))





;; Egor's computer provides ticker- indicators
(def ticker-ind-url-template "http://192.168.40.98/getIndicators.php?ticker=%s")

(defn make-url-for-ticker-ind [ticker]
  (format ticker-ind-url-template ticker))

(defn get-current-ticker-indicators-map [ticker]
  (read-response (client/get (make-url-for-ticker-ind ticker) client-config)))

(def ticker-info-url-template "http://habitat.expertmaker.com/api/thorindicators?%s")

(defn make-url-for-ticker-info [ticker-ind-map]
  (format
   ticker-info-url-template
    (with-out-str
     (doseq [kv ticker-ind-map] (print (str (key kv) "=" (val kv) "&"))))))

(defn get-ticker-info-match-xml [ticker]
 (read-xml-response
  (client/get
   (make-url-for-ticker-info (get-current-ticker-indicators-map ticker))
   client-config)))

(defn extract-ticker-info-from-xml [parsed-xml]
  (let [nums (map
              #(Double/parseDouble %)
              (map #(get-in % [:content 0 :content 0]) (get-in parsed-xml [:content])))]
    (/ (reduce + 0 nums) (count nums))))

(defn examine-ticker [ticker]
  (extract-ticker-info-from-xml (get-ticker-info-match-xml ticker)))
  





(defn get-headline-notification
  ;; this is for the original chrome plugin where we just have a title, and no ticker
  ([title]
     (let [result (extract-recommentation-info (get-recommendation title))]
       (cond (indeterminant? result) "Pass"
             (good-interesting? result) "Increase"
             (bad-interesting? result) "Decrease"
             :else "Pass")))
  ;; here if we have a title AND a ticker, we can get more information
  ([ticker title]
     (let [headline-interest (get-headline-notification title)
           ticker-status (examine-ticker ticker)]
       (if (or (and ;(> ticker-status 0)
                    (= headline-interest "Increase"))
               (and ;(< ticker-status 0)
                    (= headline-interest "Decrease")))
         (->json {:ticker ticker, :interest headline-interest, :headline title})
         (->json {:ticker ticker})))
     (->json {:ticker ticker})))
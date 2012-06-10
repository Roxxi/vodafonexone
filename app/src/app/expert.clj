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

(defn get-notification [title]
  (let [result (extract-recommentation-info (get-recommendation title))]
    (cond (indeterminant? result) "Pass"
          (good-interesting? result) "Increase"
          (bad-interesting? result) "Decrease"
          :else "Pass")))



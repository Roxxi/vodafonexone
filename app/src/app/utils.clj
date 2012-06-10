(ns app.utils
  "These are common utils shared among the other libraries."
  (:import java.io.ByteArrayInputStream)
  (:require
   [clojure.xml :as xml]
   [clojure.pprint :as pprint]
            [clojure.string :as string]
            [cheshire.core :as cheshire]))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; ## JSON and Web helpers
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defn json-> 
  "Turns a JSON string into a Clojure datastructure."
  [json-string]
  (cheshire/parse-string json-string))

(defn ->json 
  "Turns a JSON-able datastructure into a JSON String."
  [jsonable-thing]
  (cheshire/generate-string jsonable-thing))

(defn read-response 
  "Given a Web response, read the response out of the body (which we presume to be JSON) and create a Clojure datastructure."
  [resp]
  (json-> (get resp :body)))

(defn read-xml-response [resp]
  (xml/parse
   (ByteArrayInputStream.
    (.getBytes
     (with-out-str (print (get resp :body))) "UTF-8"))))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; ## Generic Helpers
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


(defn member? [item coll]
  "Semantics of Scheme's srfi-1 `member` "
  (some #(= item %) coll))


(defn make-counter
  "Returns a function such that each invocation returns the next number in the series. Providing a parameter (`n`) starts the sequence at that value."   
  ([] (make-counter 0))
  ([n] (let [x (atom n)]
         (fn [] (swap! x inc)))))

(defn uniqueify-name
  "Given `my-name` and a sequence of `other-names`, if this `my-name` is contained in the sequence of `other-names`, append the first possible value from a `next-val-fn` to its name until `my-name` is unique amongst `other-names`."
  ([my-name other-names]
     (uniqueify-name my-name other-names (make-counter)))
  ([my-name other-names next-val-fn]
     (let [proposed-name (str my-name "-" (next-val-fn))]
       (if (member? proposed-name other-names)
         (uniqueify-name my-name other-names next-val-fn)
         proposed-name))))

(defn log [obj]
  "Print and return!"
  (pprint/pprint obj)
  obj)

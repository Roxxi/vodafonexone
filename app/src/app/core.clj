(ns app.core
  (:use app.utils)
  (:require
   [app.expert :as expert]
   [ring.util.codec :as ring-codec]
   [clj-http.client :as client]))
  

(defn my-tickers []
  (->json
   {:response
    {:results [{:ticker "NICE" :news "Something great happened!" :action "STRONG BUY"}
               {:ticker "GOOG" :news "Something bad happened!" :action "Sell"}
               {:ticker "FLWS" :news "Something good happened." :action "Buy"}
               {:ticker "SPRT" :news "Something terrible!" :action "Strong Sell"}
               {:ticker "SWA" :news "Something great happened!" :action "STRONG BUY"}]
     :total 5}}))




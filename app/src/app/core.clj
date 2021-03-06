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


(def tickers=>headlines
  {"VOD" [ "Telstra Corp Ltd In Talks To Sell NZ Operations To Vodafone Group&nbsp;Plc-Reuters"
           "Hi" "Hello" "how are you"
           "Vodafone Said to Consider European&nbsp;Reorganization"
           "Hi" "Hello" "how are you"
          ]
   "GOOG" ["No elegant technical fixes for distracted driving"
           "Hi" "Hello" "how are you"
           "Analysis: US companies in sales struggle as global downturn bites"
           "Hi" "Hello" "how are you"
           "PREVIEW-Apple's war with Google heats up"
           "Hi" "Hello" "how are you"
           "Google wins partial repeal of Swiss privacy ruling on Street View"
           "Hi" "Hello" "how are you"
           ]
   "ALU" ["ALCATEL-LUCENT : Results of Annual Shareholders Meeting of June 8, 2012"
          "Hi" "Hello" "how are you"
          "Hi" "Hello" "how are you"
          "Hi" "Hello" "how are you"          
          "Alcatel-Lucent's Americas President Robert Vrij urges telecom operators to tap"
          "Hi" "Hello" "how are you"]
   "FB" []})

(defn make-ticker-news-generator []
  (let [t=>h (java.util.HashMap.)]
    (.putAll t=>h tickers=>headlines)
    (fn [ticker]
      (let [headline (first (get t=>h ticker))]
        (.put t=>h ticker (rest (get t=>h ticker)))
        headline))))

(def ticker-new-gen (make-ticker-news-generator))

(defn news-for-ticker [ticker]
  (let [headline (ticker-new-gen ticker)]
    (if (not (nil? headline))
      (let [headline-interest (expert/get-headline-notification headline)
            ticker-status (expert/examine-ticker ticker)]
        (if (or (and ;(> ticker-status 0)
                     (= headline-interest "Increase"))
                (and ;(< ticker-status 0)
                     (= headline-interest "Decrease")))
          (->json {:ticker ticker, :interest headline-interest, :headline headline})
          (->json {:ticker ticker})))
      (->json {:ticker ticker}))))


    
  
  




(defproject app "1.0.1-SNAPSHOT"
  :description "Proxy for ExpertMaker"
  :dependencies [[org.clojure/clojure "1.3.0"]
                 ;; Here is our webserver
                 [ring "1.1.0"]
                 ;; web framework!
                 [compojure "1.0.2"]
                 ;; HttpClient for Clojure based on Apache libs
                 [clj-http "0.4.1"]
                 ;; JSON
                 [cheshire "4.0.0"]]
  :dev-dependencies [[lein-marginalia "0.7.0"]
                     [lein-localrepo "0.3"]]
  :ring {:handler app.web/app}
  :plugins [[lein-ring "0.6.3"]]
  :main app.core)
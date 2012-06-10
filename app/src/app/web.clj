(ns app.web
  (:use compojure.core)
  (:require [compojure.route :as route]
            [compojure.handler :as handler]
            [ring.adapter.jetty :as jetty]
            [app.expert :as expert]
            [app.core :as core]))


(defroutes main-routes
  ;; route/resources serves things like js and css
  ;; :root would specify the root directory with respect
  ;; to the project from where these files are served from
  (route/resources "/" {:root "web"})
  ;; route files servers static files, like HTML
  ;; :root would specify the root directory with respect
  ;; to the project from where these files are served from
  (route/files "/" {:root "web"})
  ;; GET is a macro (from compojure.core) that
  ;; filters GET requests to / to be answered as such
  (GET "/tickers" [] (core/my-tickers))
  ;;
  (GET "/news/ticker/:ticker" [ticker] (core/news-for-ticker ticker))
  ;; This is for the Chrome Plugin to service page mark up
  (GET "/news/:title" [title]
       {:status 200
        :headers {"Content-Type" "application/json"
                  "Access-Control-Allow-Origin" "*"} ;; yay XSS!
        :body (expert/get-headline-notification title)})
  (GET "/news/:ticker/:title" [ticker title]
       {:status 200
        :headers {"Content-Type" "application/json"
                  "Access-Control-Allow-Origin" "*"} ;; yay XSS!
        :body (expert/get-headline-notification ticker title)})
  ;; This is the default catch all if something isn't found
  (route/not-found "Try localhost:3000/[ticker]"))


(def app
  (handler/site main-routes))
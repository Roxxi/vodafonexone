import gntp.notifier

# Simple "fire and forget" notification
gntp.notifier.mini("Alerts will appear here")

class Growler:
    # More complete example
    def __init__(self):
        self._growl = gntp.notifier.GrowlNotifier(
            applicationName = "Thorium",
            notifications = ["New Updates","New Messages"],
            defaultNotifications = ["New Messages"],
            # hostname = "computer.example.com", # Defaults to localhost
            # password = "abc123" # Defaults to a blank password
            )    
        self._growl.register()

    # Send one message
    def alert(self, indicator, articleTitle):
        self._growl.notify(
            noteType = "New Messages",
            title = indicator,
            description = articleTitle,
#        icon = "/Users/Roxxi/Developer/vodafonexone/app/web/derpy_small.png",
#        icon = "http://localhost:3000/derpy_small.png",
            sticky = False,
            priority = 1,
            )



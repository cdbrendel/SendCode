import sublime
import os
from ..clipboard import clipboard

plat = sublime.platform()

if plat == "osx":
    from ..applescript import osascript

    RSTUDIOAPPLESCRIPT = os.path.join(os.path.dirname(__file__), "rstudio.applescript")

    def send_to_rstudio(cmd):
        osascript(RSTUDIOAPPLESCRIPT, cmd)

elif plat == "windows":
    from ..autohotkey import autohotkey

    RSTUDIOAHK = os.path.join(os.path.dirname(__file__), "rstudio.ahk")

    def send_to_rstudio(cmd):
        clipboard.set_clipboard(cmd)
        autohotkey(RSTUDIOAHK)
        clipboard.reset_clipboard()

elif plat == "linux":
    from xdotool import xdotool

    def send_to_rstudio(cmd):
        wid = xdotool("search", "--onlyvisible", "--class", "rstudio")
        if wid:
            wid = wid.decode("utf-8").strip().split("\n")[-1]
            clipboard.set_clipboard(cmd)
            xdotool("key", "--window", wid, "--clearmodifiers", "ctrl+v")
            xdotool("key", "--window", wid, "--clearmodifiers", "Return")
            clipboard.reset_clipboard()

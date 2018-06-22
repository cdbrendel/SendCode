import sublime


def send_to_sublimely(cmd, bracketed=False):
    window = sublime.active_window()
    if bracketed:
        cmd = "\x1b[200~" + cmd + "\x1b[201~"

    cmd = cmd + "\r"
    window.run_command("sly_term_send_string", args={"string": cmd})

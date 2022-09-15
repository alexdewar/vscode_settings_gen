import platform
win = platform.system() == "Windows"

overrides = {
    "editor.fontFamily": "Fira Code" if win else "Jetbrains Mono",
    "terminal.integrated.fontFamily": None if win else "MesloLGS NF",
}

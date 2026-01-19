#! /usr/bin/python3

import subprocess # https://docs.python.org/3/library/subprocess.html

dnf_params = (
    "defaultyes=True",
    "max_parallel_downloads=10",
    "gpgcheck=True"
)

dnf_packages = (
    "git",
    "vim",
    "alacritty",
    "wireshark",
    "nmap",
    "qbittorrent",
    "papirus-icon-theme",
    "gnome-tweaks"
)

flathub_apps = (
    "com.github.tchx84.Flatseal",
    "org.mozilla.firefox",
    "md.obsidian.Obsidian",
    "net.ankiweb.Anki",
    "io.bassi.Amberol",
    "com.bitwarden.desktop",
    "com.mattjakeman.ExtensionManager"
)

### dnf ###
# setup
for param in dnf_params:
    subprocess.run(f"echo {param} '|' sudo tee -a /etc/dnf/dnf.conf", shell=True)

subprocess.run(["echo", "sudo", "dnf", "upgrade", "--assumeyes"])

# install packages
subprocess.run(["echo", "sudo", "dnf", "install", "--assumeyes", *dnf_packages])

### flatpak ###
# setup
subprocess.run(["echo", "flatpak", "remote-add", "--if-not-exists", "--user flathub", "https://dl.flathub.org/repo/flathub.flatpakrepo"])

# install flatpaks
subprocess.run(["echo", "flatpak", "install", "--user", "--assumeyes", "--noninteractive", "flathub", *flathub_apps])
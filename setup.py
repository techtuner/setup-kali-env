# Importing Libraries
import os
import time
import subprocess

# Variables
GREEN = "\033[0;32m"
RED = "\033[0;31m"
NC = "\033[0m"
current_path = os.getcwd()
user = os.getlogin()
home = f"/home/{user}"
tools_path = f"{home}/tools"
git_tools_path = f"{tools_path}/GitTools"


# Check if the script is being run as root
def root_check():
    if not os.geteuid() == 0:
        print(f"{RED}This script has to be run as a root!{NC}")
        time.sleep(1)
        exit()
    else:
        print(f"{GREEN}Running as Root!{NC}\n")
        print("Setup in progress")
        time.sleep(1)


# Main function to Setup the environment
def setup():
    root_check()
    update_system()
    install_apps()
    tools_dir()
    install_tools()
    config_files()


def update_system():
    print(f"{GREEN} Updating and Upgrading the System {NC}")
    os.system("sudo apt --fix-broken install -y")
    os.system("sudo apt-get update -y")
    os.system("sudo apt-get full-upgrade -y")
    os.system("sudo apt autoremove -y")
    os.system("clear")


def tools_dir():
    print(f"{GREEN}Creating tools folder for installing the tools {NC}")
    os.makedirs(f"{tools_path}", exist_ok=True)
    os.chdir(tools_path)
    os.system("clear")


def install_apps():
    print(f"{GREEN} Installing the required applications {NC}")
    os.system("snap install code --classic")
    os.system("snap install nvim --classic")
    os.system("snap install spotify --classic")


def install_tools():
    print(f"{GREEN}Installing the dependencies and tools{NC}")
    # Some of the apps which is available in the apt repository of Ubuntu
    os.system("curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh")
    os.system(f'source "{home}/.cargo/env"')
    apps = "bless adb python3-pip curl dnsrecon gobuster python3-impacket nbtscan nikto onesixtyone redis-tools smbclient smbmap snmp sslscan sipvicious whatweb wkhtmltopdf libimage-exiftool-perl golang-go python3-ldap3 python3-yaml ldnsutils strace dnsutils yersinia dhcpstarv steghide protobuf-compiler httrack ruby libglib2.0-dev openvpn sqlmap hashcat software-properties-common ffuf liblzma-dev patch hping3 libcurl4-openssl-dev make zlib1g-dev gawk g++ gcc libreadline6-dev libssl-dev libyaml-dev liblzma-dev autoconf libgdbm-dev libncurses5-dev automake libtool bison pkg-config ruby-bundler ruby-dev libsqlite3-dev sqlite3 libfuse2 libfuse3-3"
    apps_list = apps.split(" ")
    for app in apps_list:
        os.system(f"apt-get install {app} -y")
    os.system("python3 -m pip3 install pip==22.2.2 --upgrade --break-system-packages")
    update_system()
    os.chdir(tools_path)

    # AutoRecon : Recon tool
    print(f"Installing {GREEN}AutoRecon{NC} : Recon tool")
    os.system("python3 -m pip install git+https://github.com/Tib3rius/AutoRecon.git")
    os.chdir(tools_path)
    os.system("clear")
    # WPScan : WordPress Scanner
    print(f"Installing {GREEN}wpscan{NC}: Wordpress Scanner")
    os.system("git clone https://github.com/wpscanteam/wpscan")
    os.chdir(f"{tools_path}/wpscan")
    os.system("bundle install")
    os.system("rake install")
    os.chdir(tools_path)
    os.system("clear")

    # Download PSTools
    print(f"Installing {GREEN}PSTools{NC}: PowerShell scripts")
    os.system("wget https://download.sysinternals.com/files/PSTools.zip")
    os.system("mkdir PSTools")
    os.system("unzip PSTools.zip -d PSTools")
    os.system("rm -rf PSTools.zip")
    os.chdir(tools_path)
    os.system("clear")

    # Caido : Proxy Tools Alternative to Burpsuite
    print(
        f"Installing {GREEN}Caido{NC} : Proxy tools as well as an alteranative to Burpsuite with GPT support"
    )
    os.system(
        f"sudo wget https://storage.googleapis.com/caido-releases/v0.28.0/caido-desktop-linux-v0.28.0-9799aa77.AppImage"
    )
    os.system(f"chmod +x {tools_path}/caido-desktop-linux-v0.28.0-9799aa77.AppImage")
    os.system(
        f"ln -s {tools_path}/caido-desktop-linux-v0.28.0-9799aa77.AppImage /usr/bin/caido"
    )
    os.chdir(tools_path)
    os.system("clear")

    # GitTools : Tools for pwning websites with `.git` directory
    print(
        f"Installing {GREEN}Git Tools{NC} : A tools for pwning websites with `{RED}.git{NC}` directories"
    )
    os.system("git clone https://github.com/internetwache/GitTools")
    os.chdir(f"{git_tools_path}/Dumper/")
    os.system("chmod +x gitdumper.sh")
    os.system(f"ln -s {git_tools_path}/Dumper/gitdumper.sh /usr/bin/gitdumper")
    os.chdir(git_tools_path)
    os.chdir(f"{git_tools_path}/Finder/")
    os.system("pip3 install -r requirements.txt")
    os.system("chmod +x gitfinder.py")
    os.system(f"ln -s {git_tools_path}/Finder/gitfinder.py /usr/bin/gitfinder")
    os.chdir(git_tools_path)
    os.chdir(f"{git_tools_path}/Extractor/")
    os.system("chmod +x extractor.sh")
    os.system(f"ln -s {git_tools_path}/Extractor/extractor.sh /usr/bin/gitextractor")
    os.chdir(tools_path)
    os.system("clear")

    # DHCP-Starvation : Attack DHCP servers
    print(f"Installing {GREEN}DHCP-Starvation{NC} : Tools for DHC Starvation Attack")
    os.system("git clone https://github.com/yoelbassin/DHCP-starvation.git")
    os.chdir(f"{tools_path}/DHCP-starvation")
    os.system("chmod +x dhcpStarvation.py")
    os.system(
        f"ln -s {tools_path}/DHCP-starvation/dhcpStarvation.py /usr/bin/dhcpStarvation"
    )
    os.chdir(tools_path)
    os.system("clear")

    # Responder :LLMNR, NBT-NS and MDNS poisoner
    print(
        f"Installing {GREEN}Responder{NC} : Tools for LLMNR, NBT-NS and MDNS poisoner"
    )
    os.system("git clone https://github.com/lgandx/Responder.git")
    os.chdir(f"{tools_path}/Responder")
    os.system("pip3 install -r requirements.txt")
    os.system(f"ln -s {tools_path}/Responder/Responder.py /usr/bin/responder")
    os.chdir(tools_path)
    os.system("clear")

    # RevShellgen : Reverse Shell Generator
    print(f"Installing {GREEN}revshellgen{NC} : Tool for creating reverse shells")
    os.system("git clone https://github.com/cwinfosec/revshellgen.git")
    os.chdir(f"{tools_path}/revshellgen")
    os.system(f"chmod +x {tools_path}/revshellgen/revshellgen.py")
    os.system(f"ln -s {tools_path}/revshellgen/revshellgen.py /usr/bin/revshellgen")
    os.chdir(tools_path)
    os.system("clear")

    # Arduino IDE : IDE for Arduino boards
    print(f"Installing {GREEN}Arduino IDE{NC} : IDE for working with Arduino Board")
    os.system(
        "wget https://downloads.arduino.cc/arduino-ide/arduino-ide_2.2.1_Linux_64bit.AppImage"
    )
    os.system("chmod +x arduino-ide_2.2.1_Linux_64bit.AppImage")
    os.system(
        f"ln -s {tools_path}/arduino-ide_2.2.1_Linux_64bit.AppImage /usr/bin/arduinoide"
    )
    os.chdir(tools_path)
    os.system("clear")

    # GoPhish : Open Source Phishing Framework
    print(f"Installing {GREEN}GoPhish{NC} : Open Source Phishing framework")
    os.system("go install github.com/gophish/gophish@latest")
    os.system(f"ln -s {home}/go/bin/gophish /usr/bin/gophish")
    os.chdir(tools_path)
    os.system("clear")

    # Habu : Network hacking tools
    print(f"Installing {GREEN}Habu{NC} : Network hacking tool")
    os.system(
        "python3 -m pip install --upgrade git+https://github.com/fportantier/habu.git"
    )
    os.chdir(tools_path)
    os.system("clear")

    # Metasploit : Exploit Framework
    print(f"Installing {GREEN}Metaploit Framework{NC}")
    os.mkdir("metasploit")
    os.chdir(f"{tools_path}/metasploit")
    os.system(
        "curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall"
    )
    os.system("chmod +x msfinstall")
    os.system("./msfinstall")
    os.chdir(tools_path)
    os.system("clear")

    # setoolkit : Social Engineering Toolkit
    print(f"Installing {GREEN}settoolkit{NC} : Social Enginnering Toolkit")
    os.system(
        "git clone https://github.com/trustedsec/social-engineer-toolkit/ setoolkit/"
    )
    os.chdir(f"{tools_path}/setoolkit")
    os.system("pip3 install -r requirements.txt")
    os.system("python3 setup.py")
    os.chdir(tools_path)
    os.system("clear")

    # BillCipher : Information Gathering Tool for a website or IP
    print(
        f"Installing {GREEN}BillCipher{NC} : Information Gathering Tool for a website or IP"
    )
    os.system("git clone https://github.com/bahatiphill/BillCipher")
    os.chdir(f"{tools_path}/BillCipher")
    os.system("pip3 install -r requirements.txt")
    os.system(f"chmod +x {tools_path}/BillCipher/")
    os.chdir(tools_path)
    os.system("clear")

    # Sherlock : OSINT Tool for Social Media
    print(f"Installing {GREEN}Sherlock {NC} : OSINT Tool for Social Media")
    os.system("git clone https://github.com/sherlock-project/sherlock.git")
    os.chdir(f"{tools_path}/sherlock")
    os.system(f"python3 -m pip install -r requirements.txt")
    os.system(f"chmod +x {tools_path}/sherlock/sherlock/sherlock.py")
    os.system(f"ln -s {tools_path}/sherlock/sherlock/sherlock.py /usr/bin/sherlock")
    os.system("clear")

    # theHarvester : E-mails, subdomains and names Harvester - OSINT
    print(
        f"Installing {GREEN}theHarvester{NC} : OSINT Tools for E-mails, subdomains and names"
    )
    os.system("git clone https://github.com/laramies/theHarvester")
    os.chdir(f"{tools_path}theHarvester")
    os.system("python3 -m pip install -r requirements.txt")
    os.system(f"ln -s {tools_path}/theHarvester/theHarvester.py /usr/bin/theHarvester")
    os.chdir(tools_path)
    os.system("clear")

    # Photon : OSINT crawler
    print(f"Installing {GREEN}Photon{NC} : OSINT Crawler")
    os.system("git clone https://github.com/s0md3v/Photon")
    os.chdir(f"{tools_path}Photon")
    os.system(f"python3 -m pip install -r requirements.txt")
    os.system(f"chmod +x {tools_path}/Photon/photon.py")
    os.chdir(tools_path)
    os.system("clear")

    # Th3Inspector : All in one tool for Information gathering
    print(
        f"Installing {GREEN}Th3Inspector{NC} : All in one tool for Information gathering"
    )
    os.system("git clone https://github.com/Moham3dRiahi/Th3inspector.git")
    os.chdir(f"{tools_path}/Th3inspector")
    os.system(f"chmod +x {tools_path}/Th3inspector/install.sh")
    os.system(f"{tools_path}Th3inspector/install.sh")
    os.chdir(tools_path)
    os.system("clear")

    # ReconDog : Reconnaissance Swiss Army Knife
    print(f"Installing {GREEN}ReconDog{NC} : Reconnaissance Swiss Army Knife")
    os.system("git clone https://github.com/s0md3v/ReconDog")
    os.chdir(f"{tools_path}/ReconDog")
    os.system(f"chmod +x {tools_path}/ReconDog/dog")
    os.system(f"ln -s {tools_path}/ReconDog/dog /usr/bin/recondog")
    os.chdir(tools_path)
    # PSPY  :Monitor linux processes without root permissions
    print(
        f"Installing {GREEN}PSPY{NC}  :Monitor linux processes without root permissions"
    )
    os.system(
        "wget https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64"
    )
    os.system("chmod +x ./pspy64")
    os.system(f"ln -s {tools_path}/pspy64 /usr/bin/pspy")
    os.chdir(tools_path)
    os.system("clear")

    # Sublist3r : Subdomain Enumeration tool
    print(f"Installing {GREEN}Sublist3r{NC} : Subdomain Enumeration tool")
    os.system("git clone https://github.com/aboul3la/Sublist3r.git")
    os.chdir(f"{tools_path}/Sublist3r")
    os.system("pip3 install -r requirements.txt")
    os.system(f"ln -s {tools_path}/Sublist3r/sublist3r.py /usr/bin/sublist3r")
    os.chdir(tools_path)
    os.system("clear")

    # JWT_Tool :Toolkit for testing, tweaking and cracking JSON web tokens
    print(
        f"Installing {GREEN}JWT_Tool{NC} :Toolkit for testing, tweaking and cracking JSON web tokens"
    )
    os.system("git clone https://www.github.com/ticarpi/jwt_tool")
    os.chdir(f"{tools_path}/jwt_tool")
    os.system(
        "pip3 install termcolor cprint arjun requests pycryptodomex prowler raccoon-scanner"
    )
    os.system("chmod +x jwt_tool.py")
    os.system(f"ln -s {tools_path}/jwt_tool/jwt_tool.py /usr/bin/jwt_tool")
    os.chdir(tools_path)
    os.system("clear")

    # Kiterunner : Contextual Content Discovery tool
    print(f"Installing {GREEN}Kiterunner{NC} : Contextual Content Discovery tool")
    os.system("sudo git clone https://www.github.com/assetnote/kiterunner")
    os.chdir(f"{tools_path}/kiterunner")
    os.system("sudo make build")
    os.chdir(f"{tools_path}/kiterunner/dist/")
    os.system(f"sudo ln -s {tools_path}/kiterunner/dist/kr /usr/bin/kr")
    os.chdir(tools_path)
    os.system("clear")

    # Go gRPC Tools : grpcurl grpcui
    print(f"Installing {GREEN}grpcurl{NC}, {GREEN}grpcui{NC} GogRPC tools")
    os.system("go install github.com/fullstorydev/grpcurl/cmd/grpcurl@latest")
    os.system("go install github.com/fullstorydev/grpcui/cmd/grpcui@latest")
    os.system(f"ln -s {home}/go/bin/grpcui /usr/bin/grpcui")
    os.system(f"ln -s {home}/go/bin/grpcurl /usr/bin/grpcurl")
    os.chdir(tools_path)
    os.system("clear")

    # kerbrute : Kereberos pre-auth bruteforcing
    print(f"Installing {GREEN}Kerbrute{NC} : Kereberos Pre-Auth Bruteforcing")
    os.system("go install github.com/ropnop/kerbrute@latest")
    os.system(f"ln -s {home}/go/bin/kerbrute /usr/bin/kerbrute")
    os.chdir(tools_path)
    os.system("clear")

    # GRecon : Google based passive recon
    print(f"Installing {GREEN}GRecon{NC} : Google based Passive Recon")
    os.system("git clone https://github.com/TebbaaX/GRecon.git")
    os.chdir(f"{tools_path}/GRecon")
    os.system("pip3 install -r requirements.txt")
    os.chdir(tools_path)
    os.system("clear")

    # Postman : API Client Platform
    print(f"Installing {GREEN}Postman{NC} : API Client Testing Platform")
    os.system(
        "wget https://dl.pstmn.io/download/latest/linux_64 -O postman-linux-x64.tar.gz"
    )
    os.system("tar -xvzf postman-linux-x64.tar.gz")
    os.system(f"ln -s {tools_path}/Postman/Postman /usr/bin/postman")
    os.system("rm -rf postman-linux-x64.tar.gz")
    os.chdir(tools_path)
    os.system("clear")

    # Jython : For Burpsuite extensions
    print(f"Downloading {GREEN}Jython{NC} : Used for Burpsuite extensions")
    os.system(
        "wget https://repo1.maven.org/maven2/org/python3/jython-standalone/2.7.3/jython-standalone-2.7.3.jar"
    )
    os.system("clear")

    # SuperEnum : Basic enumeration of open ports with screenshots
    print(
        f"Installing {GREEN}SuperEnum{NC} : Tool for basic enumerration of open ports with screenshots"
    )
    os.system("git clone https://github.com/p4pentest/SuperEnum.git && cd SuperEnum")
    os.system("chmod +x superenum")
    os.system(f"ln -s {tools_path}/SuperEnum/superenum /usr/bin/superenum")
    os.chdir(tools_path)
    os.system("clear")

    # WifiPhisher : The Rogue Access Point Framework
    print(f"Installing {GREEN}WifiPhisher{NC} : The Rogue Access Point Framework")
    os.system("git clone https://github.com/wifiphisher/wifiphisher.git")
    os.chdir(f"{tools_path}/wifiphisher")
    os.system("python3 setup.py install")
    os.chdir(tools_path)
    os.system("clear")

    # Routersploit : Exploitation tool for Routers
    print(f" Installing {GREEN}Routersploit{NC} : Exploitation tool for Routers")
    os.system("sudo git clone https://github.com/threat9/routersploit")
    os.chdir(f"{tools_path}/routersploit")
    os.system("python3 -m pip install -r requirements.txt")
    os.system("python3 -m pip install bluepy")
    os.system(f"sudo ln -s {tools_path}/routersploit/rsf.py /usr/bin/routersploit")
    os.chdir(current_path)
    os.system("clear")

    # Seclists : Wordlist
    print(f"Download {GREEN}Seclists{NC} wordlists")
    os.mkdir("/usr/share/wordlists")
    os.chdir("/usr/share/wordlists")
    os.system("git clone https://github.com/danielmiessler/SecLists.git")
    os.system("clear")
    os.chdir(current_path)


def config_files():
    choice = input("Do you want to copy my config files (y/n): ")
    if choice is "y" or choice is "Y":
        os.system(f"cp -r{current_path}/wallpapers {home}/Pictures/")
        os.system(f"cp -r {current_path}/nvim/ {home}/.config")
        os.system(f"cp -r {current_path}/.bashrc {home}")
        os.system(f"cp -r {current_path}/fonts/'Fira Code' /usr/share/fonts/truetype")
        labs()
        code_extensions()
    else:
        os.system(
            'echo "alias grecon="sudo python ~/tools/GRecon/grecon.py"\
                  alias python="python3"\
                  alias pip="pip3"\
                  alias bcipher="sudo python ~/tools/BillCipher/billcipher.py"\
                  alias e="exit"\
                  alias photon="sudo python ~/tools/Photon/photon.py"\
                  alias setoolkit="sudo setoolkit"\
                  alias arduinoide = "sudo arduinoide"\ >> ~/.bashrc'
        )


def labs():
    os.mkdir(f"{home}/Desktop/Labs")
    os.mkdir(f"{home}/Desktop/Bug-Bounty")
    folder_list = ["HTB", "THM", "CTF", "CTF/Pico", "CTF/Meta", "CTF/Embed"]
    for folder in folder_list:
        os.mkdir(f"{home}/Desktop/Labs/{folder}")


def code_extensions():
    extensions = [
        "golang.go",
        "christian-kohler.path-intellisense",
        "ms-python.python",
        "ms-python.black-formatter",
        "rust-lang.rust-analyzer",
        "ms-python.vscode-pylance",
        "vadimcn.vscode-lldb",
        "serayuzgur.crates",
        "tamasfe.even-better-toml",
        "antfu.theme-vitesse",
        "ms-azuretools.vscode-docker",
        "auiworks.amvim",
        "rangav.vscode-thunder-client",
    ]
    for extension in extensions:
        os.system(f"code --install-extension {extension}")
    os.system(f"cp {current_path}/code/settings.json {home}/.config/Code/User/")
    os.system(f"cp {current_path}/code/keybindings.json {home}/.config/Code/User/")


setup()

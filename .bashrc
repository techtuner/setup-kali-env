export PS1='\u@\h:\[\e[01;32m\]\w\[\e[0m\]\$ '
export EDITOR='nvim'
export CLICOLOR=1

export PATH=~/.local/bin:/snap/bin:/usr/sandbox/:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/usr/share/games:/usr/local/sbin:/usr/sbin:/sbin:~/.cargo/bin:$PATH

export NVM_DIR="$HOME/.nvm"
[ -s "/usr/local/opt/nvm/nvm.sh" ] && . "/usr/local/opt/nvm/nvm.sh"  # This loads nvm
[ -s "/usr/local/opt/nvm/etc/bash_completion.d/nvm" ] && . "/usr/local/opt/nvm/etc/bash_completion.d/nvm"  # This loads nvm bash_completion

alias grecon="sudo python /opt/GRecon/grecon.py"
alias python="python3"
alias pip="pip3"
alias src="source ~/.bashrc"
alias bcipher="sudo python /opt/BillCipher/billcipher.py"
#alias theHarvester="sudo python /opt/theHarvester/theHarvester.py"
alias dots="cd ~/Downloads/dotfiles && ls"
alias wall="cd ~/Pictures/wallpapers && ls"
alias e="exit"
alias photon="sudo python ~/tools/Photon/photon.py"
alias htbo="sudo openvpn ~/vpns/htb.ovpn"
alias thmo="sudo openvpn ~/vpns/thm.ovpn"
alias tmux="tmux -u"
alias setoolkit="sudo setoolkit"
alias vim="nvim"
alias arduinoide = "sudo arduinoide&"

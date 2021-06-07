As a part of this webinar, here you will install xOpera.

This tool will be used as the orchestration tool. More about xOpera tool is [here](https://xlab-si.github.io/xopera-docs/)

### Quick xOpera CLI installation steps:
```bash
sudo apt update
sudo apt install -y python3-venv python3-wheel python-wheel-common
mkdir ~/opera && cd ~/opera
python3 -m venv .venv && . .venv/bin/activate
pip install --upgrade pip
pip install opera
pip install -U opera[openstack]
```
Detailed steps to install xOpera are available [here](https://xlab-si.github.io/xopera-docs/opera_cli.html)


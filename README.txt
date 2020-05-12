#### ./docker-util start will start ELK stacksby default, excluding sebp/elk
# 

# install docker
apt install docker.io

# Download docker-compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# using swarm mode
sudo docker swarm init

# install yq
sudo apt update
sudo apt install snapd
sudo snap install yq

# set vm.max_map_count and swapiness
sudo sysctl vm.max_map_count
sudo sysctl -w vm.max_map_count=262144
sudo sysctl -w vm.swappiness=1

# start cluster
./docker-util.sh start

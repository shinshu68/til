# dockerとは
コンテナを立ててその中で色々できる  
同じ環境をどこでも作ることができる  
作成した環境を破壊したり再構築するのが早い  
などいろいろな利点がある

## install
elementary osの場合
```bash
$ agi apt-transport-https ca-certificates
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
$ sudo apt-get install docker-ce
$ sudo systemctl start docker
```

## command
色々あるしそれぞれが奥深いのでディレクトリ分けてあとで書く

## option

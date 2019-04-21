# direnvとは
ディレクトリ内だけで有効な環境変数を定義してくれるやつ  

## 導入
```
sudo apt install direnv  
direnv edit .  
```
をすることでカレントディレクトリに `.envrc` が作られる。  
この.envrcに使用したい環境変数を書き込む。  
.envrcは使用しているシェルに関係なく `bash` で書かないといけない。


# clang
LLVMで動かす中間コードを吐くので、構文解析する部分を取り出せる  
  
`clang -cc1 -ast-dump <something cpp file>`  
でAST(抽象構文木)を吐く  

`clang -cc1 -ast-print <file>`  
 でASTにされた内容を吐く？
  
`clang -cc1 -dump-tokens <file>`  
でトークンを吐く

`clang -cc1 -ast-dump -I /usr/include/c++/7.3.0/ -I /usr/include/x86_64-linux-gnu/c++/7/ -I /usr/include/ -I /usr/lib/llvm-6.0/lib/clang/6.0.0/include/`  
ヘッダが見つからないのを無理やり解決させたやつ

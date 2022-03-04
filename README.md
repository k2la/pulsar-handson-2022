# Pulsar ハンズオン #2

## 配布物

- [0.pdf](0.pdf) 前半資料
- [1.pdf](1.pdf) 後半資料
- [handson](handson) コードなど

## 事前準備

### Docker の導入

すでに導入している方は飛ばしてください。

#### Homebrew

```
brew install --cask docker
```

#### installer

https://www.docker.com/products/docker-desktop

### Docker の memory 割当を変更

Docker を起動し、Preference > resources で memory を 4GB 以上に設定してください。

### image を pull する

```sh
# 配布 directory 内で
docker-compose up

# 数分掛かります
# 立ち上がったら終了します
^C
```

### Pulsar IO Cassandra Connectorの導入

「Pulsar Functions/Pulsar IO」のハンズオンで、メッセージをCassandraに流すために下記の準備が必要となります。

1. [こちら](https://www.apache.org/dyn/mirrors/mirrors.cgi?action=download&filename=pulsar/pulsar-2.9.1/connectors/pulsar-io-cassandra-2.9.1.nar) をクリックして、`pulsar-io-cassandra-2.9.1.nar`をダウンロード
2. `functions`や`io`ディレクトリと同じ階層に`connectors`ディレクトリを作成
3. `connectors`ディレクトリに`pulsar-io-cassandra-2.9.1.nar`を移動

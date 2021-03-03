# AozoraBunko Extractor

青空文庫のテキストデータをShift-JISからUTF-8へと変換し、ルビやその他の記号を削除、元ファイルごとに二重改行で区切った単一のテキストファイルを生成します。
(非公式ツールです)

## Usage

青空文庫のテキストデータとして、[aozorahack/aozorabunko_text](https://github.com/aozorahack/aozorabunko_text)のデータを利用すると便利です。
200MB程度のzipファイルがダウンロードされます。通信環境にご留意ください。
また、青空文庫内のテキストには著作権で保護されているものも含まれているようなので、権利にはご注意ください。


```bash
# download data
curl -OL https://github.com/aozorahack/aozorabunko_text/archive/master.zip
unzip master.zip

# install cli
pip install aozorabunko-extractor

# run this command
aozorabunko-extractor --input_dir aozorabunko_text-master --output_dir out --break_sentence --min_chars 3
```

## Options

```
-i, --input_dir aozorabunko_text-master # 入力データが存在するディレクトリを指定、指定ディレクトリ以下の.txtファイルを全て対象にします
-o, --output_dir out # 抽出したテキストを出力するディレクトリを指定
--break_sentence # フラグを有効にすると、文を「。」を基準に改行区切り
--min_chars 3 # 一行の最小文字数を指定
--num_process 8 # 最大並列実行プロセス数を指定
```


## Run with poetry (please download this source code)


```bash
poetry install
poetry run aozorabunko-extractor --input_dir aozorabunko_text-master --output_dir out --break_sentence --min_chars 3
```

## Run with local python (please download this source code)

```
pip install konoha argparse
python src/aozorabunko_extractor/cli.py --input_dir aozorabunko_text-master --output_dir out --break_sentence --min_chars 3
```
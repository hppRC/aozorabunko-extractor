import argparse
import codecs
import re
import itertools

from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from konoha import SentenceTokenizer


def replace_symbols(text):
    text = text.replace("｜", "")
    text = re.sub(r"※［＃.*?］", r"", text)
    text = re.sub(r"［＃.*?］", r"", text)
    text = re.sub(r"《.*?》", r"", text)
    # text = re.sub(r"(..)／＼", r"\1\1", text)
    return text.strip()


def clean_text(text):
    new = replace_symbols(text)
    while new != text:
        text = new
        new = replace_symbols(text)
    return text


def run(args):
    txt_path, output_dir, config = args
    tokenizer = SentenceTokenizer()
    res = []
    with codecs.open(txt_path, 'r', encoding='shift-jis') as f:
        try:
            title = next(f).strip()
            line = next(f).strip()
        except:
            return ""

        cnt = 2
        while True:
            if re.match(r"-+", line):
                cnt -= 1
            try:
                line = next(f)
                if cnt == 0:
                    break
            except:
                break

        while True:
            if re.match(r"底本", line) or re.match(r"このファイルは", line):
                break
            text = clean_text(line)
            if text:
                if config.break_sentence:
                    res += tokenizer.tokenize(text)
                else:
                    res += [text]
            try:
                line = next(f)
            except:
                break

    ret = "\n".join(x for x in res if len(x) > config.min_chars)
    (output_dir / "works").mkdir(exist_ok=True, parents=True)
    output_path = output_dir / "works" / (title+".txt")

    is_addition = output_path.exists()
    with codecs.open(output_path, "a", encoding="utf-8") as f:
        if is_addition:
            f.write("\n\n"+ret)
        else:
            f.write(ret)
    return ret


def main():
    args = configure()
    input_dir, output_dir = Path(args.input_dir), Path(args.output_dir)
    if not input_dir.exists():
        raise ValueError(
            "Please be sure to the given --input_dir exists.")

    if not input_dir.is_dir():
        raise ValueError(
            "Please be sure to the given --input_dir is the path to the data directory.")

    output_dir.mkdir(exist_ok=True, parents=True)

    with ProcessPoolExecutor(max_workers=args.num_process) as executor:
        results = executor.map(run, zip(input_dir.glob(
            "**/*.txt"), itertools.repeat(output_dir), itertools.repeat(args)))

    with (output_dir / "all.txt").open("w") as f:
        f.write("\n\n".join(results))


def configure():
    parser = argparse.ArgumentParser(description='AozoraBunko Extractor')
    parser.add_argument('-i', '--input_dir',
                        help='input data directory', type=str)
    parser.add_argument('-o', '--output_dir',
                        help="output directory", type=str)
    parser.add_argument(
        "--num_process", help="num of processes", default=16, type=int)

    parser.add_argument("--break_sentence", help="", action='store_true')
    parser.add_argument("--min_chars", help="", default=0, type=int)

    args = parser.parse_args()

    if args.input_dir is None:
        raise ValueError("\nPlease specify input data directory.")
    if args.output_dir is None:
        raise ValueError("\nPlease specify output directory.")

    return args


if __name__ == "__main__":
    main()

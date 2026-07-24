"""CLI app for live translation."""

import sys
import argparse
from .pipeline import TranslationPipeline


def main():
    parser = argparse.ArgumentParser(description='Live Translate — Multi-provider translation')
    parser.add_argument('text', nargs='?', help='Text to translate')
    parser.add_argument('-s', '--source', default='auto', help='Source language (default: auto)')
    parser.add_argument('-t', '--target', default='en', help='Target language (default: en)')
    parser.add_argument('-p', '--provider', default='google', help='Translation provider')
    parser.add_argument('--list', action='store_true', help='List available providers')

    args = parser.parse_args()

    if args.list:
        print("Available providers: google, gemini, mock")
        return

    pipeline = TranslationPipeline(primary=args.provider)

    if args.text:
        result = pipeline.translate(args.text, args.source, args.target)
        print(result)
    else:
        print("Live Translation Mode (Ctrl+C to exit)")
        try:
            for line in sys.stdin:
                line = line.strip()
                if line:
                    result = pipeline.translate(line, args.source, args.target)
                    print(result)
        except KeyboardInterrupt:
            print("\nExiting.")


if __name__ == '__main__':
    main()

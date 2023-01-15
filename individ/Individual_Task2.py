#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse
import pathlib


def tree(directory):
    print(f'>>> {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = ' ' * depth
        print(f'{spacer} >> {path.name}')
        for new_path in sorted(directory.joinpath(path).glob('*')):
            depth = len(new_path.relative_to(directory.joinpath(path)).parts)
            spacer = '\t' * depth
            print(f'{spacer} > {new_path.name}')


def main(command_line=None):
    current = pathlib.Path.cwd()
    file_parser = argparse.ArgumentParser(add_help=False)

    # Создаем основной парсер командной строки
    parser = argparse.ArgumentParser("tree")
    parser.add_argument(
        "--version",
        action="version",
        help="The main parser",
        version="%(prog)s 0.1.0"
    )

    subparsers = parser.add_subparsers(dest="command")

    # Создаем субпарсер для создания новой папки
    create = subparsers.add_parser(
        "mkdir",
        parents=[file_parser]
    )
    create.add_argument(
        "filename",
        action="store"
    )

    # Субпарсер для удаления папок
    create = subparsers.add_parser(
        "rmdir",
        parents=[file_parser]
    )
    create.add_argument(
        "filename",
        action="store"
    )

    # Субпарсер для создания файлов
    create = subparsers.add_parser(
        "touch",
        parents=[file_parser]
    )
    create.add_argument(
        "filename",
        action="store"
    )
    # Субпарсер для удаления файлов
    create = subparsers.add_parser(
        "rm",
        parents=[file_parser]
    )
    create.add_argument(
        "filename",
        action="store"
    )
    args = parser.parse_args(command_line)
    if args.command == 'mkdir':
        directory_path = current / args.filename
        directory_path.mkdir()
        tree(current)
    elif args.command == "rmdir":
        directory_path = current / args.filename
        directory_path.rmdir()
        tree(current)
    elif args.command == "touch":
        directory_path = current / args.filename
        directory_path.touch()
        tree(current)
    elif args.command == "rm":
        directory_path = current / args.filename
        directory_path.unlink()
        tree(current)
    else:
        tree(current)


if __name__ == "__main__":
    main()

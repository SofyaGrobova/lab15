#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def decorator_function(func):
    def wrapper(args):
        result = f"Периметр фигуры равен = {func(args)}"
        return result

    return wrapper


@decorator_function
def individual_func(data):
    return sum(data)


def main():
    string = tuple(map(int, input(
        "Введите стороны прямоугольника, через запятую:\n"
    ).split(',')))
    result = individual_func(string)
    print(result)


if __name__ == "__main__":
    main()

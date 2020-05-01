import functools

def main():
    width, height = 20, 20

    @functools.lru_cache(maxsize=100_000)
    def n_path(w, h):
        if w > 20 or h > 20:
            return 0

        if w == width and h == height:
            return 1

        return n_path(w + 1, h) + n_path(w, h + 1)

    print(n_path(0, 0))


if __name__ == '__main__':
    main()

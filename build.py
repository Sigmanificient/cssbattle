import os
from html2image import Html2Image

hti = Html2Image(output_path='img')


def get_png_output_path(battles):
    png_paths = []
    for battle in battles:
        with open(battle, 'r') as f:
            html = f.read()

        png_filename = battle.split('/')[-1].replace('.html', '.png')
        hti.screenshot(html, size=(400, 300), save_as=png_filename)
        png_paths.append(png_filename)

    return png_paths


def retrieve_battles():
    battles = []
    for d in os.listdir('src'):
        battles.extend(
            f"src/{d}/{f}"
            for f in os.listdir(f'src/{d}')
            if f.endswith('.html')
        )

    return battles


def get_title(png):
    return png.split('/')[-1].split('.')[0].replace('_', ' ')


def main():
    png_paths = get_png_output_path(retrieve_battles())

    with open('index.html', 'w') as f, open('template/_template.html', 'r') as t:
        f.write(t.read().replace('{{ content }}', '\n\t\t'.join(
            f'<div data-title="{(t := get_title(png))}">'
            f'<img src="img/{png}" width="400" height="300" alt="{t}">'
            f'</div>'
            for png in png_paths
        )))


if __name__ == '__main__':
    main()

<p align="center">
  <img src="https://raw.githubusercontent.com/remarkablegames/sat-prep/master/game/gui/window_icon.png" alt="SAT Prep">
</p>

# SAT Prep

![release](https://img.shields.io/github/v/release/remarkablegames/sat-prep)
[![build](https://github.com/remarkablegames/sat-prep/actions/workflows/build.yml/badge.svg)](https://github.com/remarkablegames/sat-prep/actions/workflows/build.yml)
[![lint](https://github.com/remarkablegames/sat-prep/actions/workflows/lint.yml/badge.svg)](https://github.com/remarkablegames/sat-prep/actions/workflows/lint.yml)

📖 SAT Prep

Play the game on:

- [remarkablegames](https://remarkablegames.org/sat-prep)

## Credits

- [Kenney](https://kenney.nl/assets/interface-sounds)
- [Noraneko Games](https://noranekogames.itch.io/yumebackground)
- [Uncle Mugen](https://lemmasoft.renai.us/forums/viewtopic.php?t=17302)

## Prerequisites

Download [Ren'Py SDK](https://www.renpy.org/latest.html):

```sh
git clone https://github.com/remarkablegames/renpy-sdk.git
```

Symlink `renpy`:

```sh
sudo ln -sf "$(realpath renpy-sdk/renpy.sh)" /usr/local/bin/renpy
```

Check the version:

```sh
renpy --version
```

## Install

Clone the repository to the `Projects Directory`:

```sh
git clone https://github.com/remarkablegames/sat-prep.git
cd sat-prep
```

_Optional:_ install the Python dependencies:

```sh
python3 -m venv venv
source venv/bin/activate
```

```sh
pip3 install -r requirements.txt
```

Generate the chart images:

```sh
python3 game/images/chart/chart.py
```

## Run

Launch the project:

```sh
renpy .
```

Or open the `Ren'Py Launcher`:

```sh
renpy
```

Press `Shift`+`R` to reload the game.

Press `Shift`+`D` to open the developer menu.

## Cache

Clear the cache:

```sh
find game -name "*.rpyc" -delete
```

Or open `Ren'Py Launcher` > `Force Recompile`:

```sh
renpy
```

## Lint

Lint the game:

```sh
renpy game lint
```

## License

[MIT](LICENSE)

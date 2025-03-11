<p align="center">
  <img src="https://raw.githubusercontent.com/remarkablegames/sat-prep/master/game/gui/window_icon.png" alt="Renpy Template">
</p>

# Renpy Template

![release](https://img.shields.io/github/v/release/remarkablegames/sat-prep)
[![build](https://github.com/remarkablegames/sat-prep/actions/workflows/build.yml/badge.svg)](https://github.com/remarkablegames/sat-prep/actions/workflows/build.yml)
[![lint](https://github.com/remarkablegames/sat-prep/actions/workflows/lint.yml/badge.svg)](https://github.com/remarkablegames/sat-prep/actions/workflows/lint.yml)

📖 Write visual novels with Ren'Py Template.

Play the game on:

- [remarkablegames](https://remarkablegames.org/sat-prep)

## Credits

### Art

- [Uncle Mugen](https://lemmasoft.renai.us/forums/viewtopic.php?t=17302)

### Audio

- [Kenney Interface Sounds](https://kenney.nl/assets/interface-sounds)

## Prerequisites

Download [Ren'Py SDK](https://www.renpy.org/latest.html):

```sh
git clone https://github.com/remarkablegames/renpy-sdk.git
```

Symlink `renpy`:

```sh
sudo ln -sf "$(realpath renpy-sdk/renpy.sh)" /usr/local/bin/renpy
```

## Install

Clone the repository to the `Projects Directory`:

```sh
git clone https://github.com/remarkablegames/sat-prep.git
cd sat-prep
```

Rename the project:

```sh
git grep -l 'Renpy Template' | xargs sed -i '' -e 's/Renpy Template/My Novel/g'
```

```sh
git grep -l 'sat-prep' | xargs sed -i '' -e 's/sat-prep/my-novel/g'
```

Replace the assets:

- [ ] `web-presplash.jpg`
- [ ] `game/gui/main_menu.png`
- [ ] `game/gui/window_icon.png`

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

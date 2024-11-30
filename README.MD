# Color Swatch API

A simple API using the Django REST Framework to generate random color swatches in various color spaces.

## Quickstart

Start the python virtual environment

```bash
# Mac/Linux
source env/bin/activate

# Windows
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Open Django project folder

```bash
cd color_swatch
```

Run server

```bash
python manage.py runserver
```

The server will run on `http://127.0.0.1:8000/` by default.

## API

### Get random colors in random color spaces

Endpoint

```
GET /api/colors/
```

<details>
    <summary>Example response</summary>

```json
[
  {
    "type": "rgb",
    "red": 3,
    "green": 168,
    "blue": 186
  },
  {
    "type": "rgb",
    "red": 155,
    "green": 88,
    "blue": 136
  },
  {
    "type": "hsl",
    "hue": 310,
    "saturation": 24,
    "lightness": 97
  },
  {
    "type": "hsl",
    "hue": 55,
    "saturation": 97,
    "lightness": 0
  },
  {
    "type": "hsl",
    "hue": 116,
    "saturation": 95,
    "lightness": 40
  }
]
```

</details>

Query params

`n: int` (min = 1, max = 50, default = 5): number of colors to include in the response

E.g., `GET api/colors?n=10`

### Get random colors in one color space

Endpoint

```
GET /api/colors/<color_space>
```

<details>
    <summary>Example Response (rbg)</summary>

```
GET /api/colors/rbg
```

```json

[
  {
    "type": "rgb",
    "red": 163,
    "green": 162,
    "blue": 133
  },
  {
    "type": "rgb",
    "red": 230,
    "green": 22,
    "blue": 76
  },
  {
    "type": "rgb",
    "red": 26,
    "green": 87,
    "blue": 157
  },
  {
    "type": "rgb",
    "red": 75,
    "green": 15,
    "blue": 208
  },
  {
    "type": "rgb",
    "red": 23,
    "green": 136,
    "blue": 182
  }
]
```

</details>

<details>
    <summary>Example Response (hsl)</summary>

```
GET /api/colors/hsl
```

```json
[
  {
    "type": "hsl",
    "hue": 191,
    "saturation": 94,
    "lightness": 19
  },
  {
    "type": "hsl",
    "hue": 130,
    "saturation": 23,
    "lightness": 77
  },
  {
    "type": "hsl",
    "hue": 188,
    "saturation": 93,
    "lightness": 58
  },
  {
    "type": "hsl",
    "hue": 301,
    "saturation": 5,
    "lightness": 18
  },
  {
    "type": "hsl",
    "hue": 109,
    "saturation": 38,
    "lightness": 75
  }
]
```

</details>

Query params

`n: int` (min = 1, max = 50, default = 5): number of colors to include in the response

E.g., `GET api/colors/rbg?n=10`, `GET api/colors/hsl?n=10`



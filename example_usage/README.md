# Example Django Project

This repository contains an example of a tiny django project that uses the components made in this repository.

All it does it manage a simple django project, a simple css / js pipeline with `vite`, and gives you a way to see the demo site in action.

I have decided to call this sample web app `sausage` as a way to unambiguiously identify this sample project instead of sprinkling `example` or `test` everywhere.

## Usage

After you install everything `uv sync` and `npm i`.

In two separate terminals, run the server with python and the css/js pipeline in watch mode.

### Python

```
python manage.py runserver
```

### Javascript

```
npm run watch
```

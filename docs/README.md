# Python from the Ground Up

A comprehensive Python reference covering fundamentals, standard library, OOP, and idiomatic patterns. Built with [mdBook](https://rust-lang.github.io/mdBook/).

📖 [Read online](https://lansky1.github.io/python/)

## Local Preview

```bash
# Install mdBook: https://rust-lang.github.io/mdBook/guide/installation.html
cargo install mdbook

cd docs
mdbook serve --open
```

## Build

```bash
cd docs
mdbook build
```

Output goes to `docs/book/`.

## Deploy

Pushes to `main` that touch `docs/**` trigger `.github/workflows/deploy-docs.yml`, which builds the book and publishes via GitHub Pages (using `deploy-pages`).

**One-time setup:** in the repo settings → **Pages**, set source to **GitHub Actions**.

Live site: <https://lansky1.github.io/python/>

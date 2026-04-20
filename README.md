# CS2 Skin Price Tracker - Backend

Jednostavan Flask backend koji dohvaća cijene skinova s Skinport, Waxpeer i DMarket API-ja.

## Deploy na Railway

1. Idi na [railway.app](https://railway.app) i prijavi se s GitHub računom
2. Klikni **"New Project"** → **"Deploy from GitHub repo"**
3. Odaberi ovaj repo
4. Railway automatski detektira Python i deploya

## Endpointi

- `GET /items` — lista svih skinova s Skinport (za autocomplete)
- `GET /prices/waxpeer?skin=AK-47 | Redline (Field-Tested)` — cijena s Waxpeer
- `GET /prices/dmarket?skin=AK-47 | Redline (Field-Tested)` — cijena s DMarket

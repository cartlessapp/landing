# Cartless — landing

Одностраничный лендинг продукта Cartless. Ссылка для трафика (Reddit / TikTok bio /
Twitter / аутрич). Объясняет оффер за 5 секунд и ведёт на App Store / в waitlist.

Отдельный проект — **не трогает** iOS-код в `../CartLess/`.

## Стек

Чистый статичный `index.html` (HTML/CSS/JS, без сборки и зависимостей). Деплоится
куда угодно одним файлом + папкой `assets/`. Шрифт Inter и иконка лежат локально в
`assets/` — внешних запросов нет.

## Структура контента (JTBD-воронка)

Собрана по `1-2-MVP/prompts/landing-page-text.md`, адаптировано под Cartless:

1. **Hero** — oneliner «Pause before you buy. Keep the money.» + мокап реального Home + CTA.
2. **What Cartless does** — Core Job + ценность + 3 micro-jobs.
3. **Sound familiar? (точка А)** — триггеры / эмоции / цена импульсивных покупок.
4. **How it works** — 3 шага (urge → pause → keep the money).
5. **Stat band** — 24–48h / $860 / 0 guilt.
6. **What you get** — 4 ценности + второй мокап.
7. **Where this takes you (точка Б)** — how you'll feel / what you'll have done.
8. **Honest questions** — снятие 3 барьеров (shame / willpower / tracking).
9. **Why this, not the usual fixes** — «увольняем» СТАРЫЕ СПОСОБЫ (сила воли / таблицы /
   no-buy challenge), НЕ бренды-конкуренты (память `feedback_no_defensive_competitor_framing`).
10. **Final CTA / waitlist** — email-capture + App Store бейдж.
11. **Footer** — Privacy / Terms (внешние ссылки на `cartless-legal` GitHub Pages).

## Локальный просмотр

```
open index.html
```

## Деплой

Любой статик-хостинг (Vercel / Netlify / GitHub Pages / Cloudflare Pages). Залить
`index.html` + `assets/`. **Платный домен НЕ обязателен** — бесплатный адрес
`<username>.github.io/...` уже годится для Reddit/TikTok-трафика. Короткий домен
(cartless.app) — апгрейд на потом, привязывается без переделки.

### Публикация на GitHub Pages (рекомендуется, бесплатно)

Папка `landing/` — уже git-репозиторий (первый коммит сделан). Осталось залить на
GitHub и включить Pages. Подставь свой `<username>` и `<repo>` (напр. `cartless` / `landing`):

```
# 1) создать пустой репозиторий на github.com (без README/gitignore — они уже есть)
# 2) привязать и запушить:
cd cart-less/landing
git remote add origin https://github.com/<username>/<repo>.git
git branch -M main
git push -u origin main
```

Включить Pages: репозиторий → **Settings → Pages → Source: Deploy from a branch →
Branch: `main` / `/ (root)` → Save**. Через ~1 мин лендинг будет на
`https://<username>.github.io/<repo>/`.

Альтернатива без терминала: **Netlify** (netlify.com → «Add new site» → drag-and-drop
папки `landing/`) — даёт адрес `<имя>.netlify.app` за минуту.

### Кастомный домен (опционально, потом)

Купить короткий домен (Namecheap/Porkbun, ~10–20 €/год), в GitHub Pages указать
Custom domain, у регистратора добавить CNAME на `<username>.github.io`. Хостинг
остаётся бесплатным — платишь только за домен.

## TODO перед публикацией

- **App Store ссылка.** Сейчас CTA-бейджи ведут на `#waitlist` с плашкой «Coming soon»
  (приложение на ревью Apple с 2026-06-14). Когда пройдёт ревью: заменить `href="#waitlist"`
  у `.appstore` на ссылку App Store и убрать класс `soon` (плашку «Coming soon»).
- **Сбор email.** Форма waitlist сейчас пишет в `localStorage` (заглушка). Чтобы собирать
  по-настоящему — вписать URL Formspree/Buttondown в `EMAIL_ENDPOINT` в `<script>` внизу
  `index.html`. Никаких секретов в коде не нужно (Formspree-эндпоинт публичный).
- **OG-картинка.** Сейчас в og:image иконка `assets/icon.png`. Для красивого превью в соцсетях
  опционально отрисовать отдельный 1200×630 баннер.

## Ассеты

- `assets/icon.png` — иконка приложения (копия `../design-explorations/AppIcon-new.png`).
- `assets/Inter.ttf` — шрифт (копия из `../design-explorations/`).
- Мокап телефона в `index.html` — верстка реального экрана Home (источник:
  `../design-explorations/home-v2.html`), не скриншот.

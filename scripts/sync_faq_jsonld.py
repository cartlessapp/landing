#!/usr/bin/env python3
"""Пересобирает JSON-LD FAQPage в <head> из видимого блока #faq в index.html.

Источник правды — видимый FAQ: правишь вопросы/ответы там, потом
    python3 scripts/sync_faq_jsonld.py
Ответ = текст первого <p> внутри <details> (кнопки и прочее после него в
разметку не идут). Без аргументов, только stdlib.
"""
import html
import json
import os
import re
import sys

PAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html')

s = open(PAGE).read()
faq = re.search(r'<section[^>]*id="faq".*?</section>', s, re.S)
if not faq:
    sys.exit('Нет <section id="faq">')
qa = []
for q, a in re.findall(r'<summary>(.*?)</summary>\s*<p>(.*?)</p>', faq.group(0), re.S):
    clean = lambda t: ' '.join(html.unescape(re.sub(r'<[^>]+>', '', t)).split())
    qa.append({'@type': 'Question', 'name': clean(q),
               'acceptedAnswer': {'@type': 'Answer', 'text': clean(a)}})

ld = {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': qa}
block = '<script type="application/ld+json">\n' + json.dumps(ld, ensure_ascii=False, indent=2) + '\n</script>'
pat = re.compile(r'<script type="application/ld\+json">\s*\{\s*"@context": "https://schema.org",\s*"@type": "FAQPage".*?</script>', re.S)
if not pat.search(s):
    sys.exit('Нет блока FAQPage в <head>')
s = pat.sub(lambda _: block, s, count=1)
open(PAGE, 'w').write(s)
print(f'FAQPage: {len(qa)} вопросов синхронизировано')

#!/usr/bin/env python3
"""
Health Samjho — build script
Combines all data JSON files into a single self-contained index.html

Usage:
    python3 build.py

This reads:
    data/medicines.json
    data/tests.json
    data/diseases.json
    data/nutrition.json

and generates:
    index.html  (single file, no fetch — works anywhere)
"""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))

def load(name):
    with open(os.path.join(BASE, 'data', name), encoding='utf-8') as f:
        return json.load(f)

def main():
    med = json.dumps(load('medicines.json')['medicines'], ensure_ascii=False)
    tests = json.dumps(load('tests.json')['tests'], ensure_ascii=False)
    diseases = json.dumps(load('diseases.json'), ensure_ascii=False)
    nutrition = json.dumps(load('nutrition.json'), ensure_ascii=False)

    with open(os.path.join(BASE, 'unified-template.html'), encoding='utf-8') as f:
        tpl = f.read()

    out = (tpl
           .replace('__MED__', med)
           .replace('__TESTS__', tests)
           .replace('__DIS__', diseases)
           .replace('__NUT__', nutrition))

    outpath = os.path.join(BASE, 'index.html')
    with open(outpath, 'w', encoding='utf-8') as f:
        f.write(out)

    print('✅ index.html generated')
    print(f'   💊 Medicines: {len(json.loads(med))}')
    print(f'   🧪 Tests:     {len(json.loads(tests))}')
    print(f'   🦠 Diseases:  {len(json.loads(diseases))}')
    print(f'   🥗 Nutrition: {len(json.loads(nutrition))}')

if __name__ == '__main__':
    main()

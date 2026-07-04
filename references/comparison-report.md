# ecoMode vs Caveman

Benchmark command:

```bash
python scripts/benchmark_compare.py --cases tests/benchmark_cases.json
```

Latest expanded local result:

- upstream caveman SHA: `0d95a81d35a9f2d123a5e9430d1cfc43d55f1bb0`
- cases: 16
- ecoMode wins: 16/16
- exact preservation: 16/16
- caveman tokens: 513
- ecoMode tokens: 252
- ecoMode advantage: 261 tokens
- caveman savings vs normal: 29.9%
- ecoMode savings vs normal: 65.6%
- core skill instruction tokens: caveman 1245, ecoMode 1049

## Why ecoMode Wins

Caveman compresses sentence style. ecoMode removes unnecessary ideas first, then
compresses wording. This makes whole-answer output smaller while staying easier
to read.

## Remaining Reality

90% savings is possible only for verbose source or delta-only answers. The skill
must never promise universal 90% savings. It should say "up to 90%" or measure.

## Upgrade Targets

- Add more benchmark cases before claiming broad superiority.
- Add human clarity scoring if real users compare outputs.
- Keep exact text preservation at 100%.
- Keep benchmark runnable without network.

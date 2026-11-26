# The Painfully Honest Out-of-Office

[![make.fun](https://make.fun/badge.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)

Entry for the [make.fun bounty "The Painfully Honest Out-of-Office"](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b): a single out-of-office email auto-reply of at most 200 characters, painfully honest about the sender's absence, inbox and enthusiasm — yet still polite enough that a manager would let it stand.

## How it works

`main.py` (Python 3, standard library only, no network) writes one sentence to `/output/entry.txt` (honouring `MAKEFUN_OUTPUT_DIR` when set). The text is fixed and deterministic: two runs produce byte-identical output. Before writing, the program validates its own text — non-blank, at most 200 characters, exactly one sentence — and refuses to write an invalid entry.

## The reply

> I'm away and not reading email, so your message will queue behind 400 unread ones until I return and answer it slowly, reluctantly, and in full — thank you for your patience.

## Run it

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

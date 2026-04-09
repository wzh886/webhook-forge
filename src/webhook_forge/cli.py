from __future__ import annotations

import argparse
import sys

from .signing import sign_payload, verify_signature


def main() -> None:
    parser = argparse.ArgumentParser(prog="webhook-forge")
    sub = parser.add_subparsers(dest="command", required=True)

    sign = sub.add_parser("sign", help="Sign a webhook payload")
    sign.add_argument("--secret", required=True)
    sign.add_argument("--timestamp", required=True)
    sign.add_argument("--payload", required=True)

    verify = sub.add_parser("verify", help="Verify a webhook signature")
    verify.add_argument("--secret", required=True)
    verify.add_argument("--timestamp", required=True)
    verify.add_argument("--payload", required=True)
    verify.add_argument("--signature", required=True)

    args = parser.parse_args()

    if args.command == "sign":
        print(sign_payload(args.secret, args.timestamp, args.payload))
        return

    ok = verify_signature(args.secret, args.timestamp, args.payload, args.signature)
    print("valid" if ok else "invalid")
    raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()

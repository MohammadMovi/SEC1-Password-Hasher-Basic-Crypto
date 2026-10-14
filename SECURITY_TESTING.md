# Local security abuse tests

This repository is a command-line learning tool and Python library. It does not expose an HTTP service, authentication endpoint, or remotely reachable target, so a network penetration test is not applicable to this project as it stands.

The local security suite sends synthetic adversarial inputs directly to the hashing APIs. It checks empty, NUL-containing, Unicode, and overlong passwords; malformed and oversized encoded hashes; invalid bcrypt cost settings; valid bcrypt boundary inputs; and accidental password output from the CLI. It runs entirely offline and never uses real credentials.

Run it from the repository root after installing the project dependency:

```bash
python -m unittest discover -s test -p "test_security.py" -v
```

These are security regression and abuse-case tests, not a substitute for a professional penetration test. If this code is later placed behind a network service, that service will need a separate authorized assessment covering its authentication flow, storage, sessions, rate limiting, deployment, and dependencies.

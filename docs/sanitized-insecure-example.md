# Sanitized Insecure Example

This file is intentionally safe. It shows what a risky commit might look like without using real credentials.

Do not copy real secrets into source code.

```text
SANITIZED_API_KEY=fake_example_value_not_real
SANITIZED_PASSWORD=example_password_not_real
SANITIZED_PRIVATE_TOKEN=fake_token_for_training_only
```

Why this matters:

- Real API keys can be abused if they are committed to GitHub.
- Even deleted secrets can remain in Git history.
- Secret scanning should run before code is merged.
- Real incidents should rotate the exposed secret, remove it from history if required, and review access logs.

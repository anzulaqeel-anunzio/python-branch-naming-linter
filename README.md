# Git Branch Naming Convention Linter

A hook-friendly script to enforce standardized git branch names. Ideally used as a git `pre-push` hook.

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Conventions

Enforces the pattern: `type/description`
*   **Types**: `feature`, `bugfix`, `hotfix`, `release`, `chore`, `docs`, `test`
*   **Description**: lowercase, alphanumeric, hyphens only.
*   **Exceptions**: `main`, `master`, `develop`, `staging`

## Usage

```bash
python run_linter.py [branch_name]
```

### Examples

**1. Check Current Branch**
```bash
python run_linter.py
```

**2. Check Specific Name**
```bash
python run_linter.py feature/fancy-ui
# Output: Branch 'feature/fancy-ui' is valid.
```

**3. Invalid Name**
```bash
python run_linter.py "MyFeature"
# Output: Error: Branch 'MyFeature' is invalid.
```

## Requirements

*   Python 3.x
*   Git (for auto-detection)

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.

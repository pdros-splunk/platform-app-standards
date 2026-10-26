# Conventions in use by `splunk-platform-apps` repositories

> [!NOTE]
> Repositories are regularly scanned by our AI-powered cloud vetting service to ensure compliance with Splunk standards and guarantee compatibility with Splunk Cloud distributions.

## Code and Style
We would ask that you adhere to the following guidelines when developing your App to ensure consistency within our platform.

### Python
Projects using Python will be expected to standardize to [PEP8](https://peps.python.org/pep-0008/). Code will be automatically linted using [ruff](https://docs.astral.sh/ruff/). It is an _extremely_ good idea to lint your code with the provided [configuration](https://github.com/splunk-platform-apps/.github/tree/main/actions/lint/ruff.toml) before committing your code.

### Apps Navigation
To ensure a consistent user experience and ease of support, all applications must include the following two links in their navigation menu:
- **Documentation**: A link directing the user to the official documentation for the app (e.g. `https://splunk-platform-apps.github.io/<your_app_name>`).
- **Report an issue**: A link directing the user to the issue reporting page for the app (e.g. `https://splunk-platform-apps.github.io/<your_app_name>/issues`).

Private customer apps without a public listing or customer-accessible GitHub project may instead ship **Documentation** and **Support** views under their **Help** menu. Pass both `private-help-view` and `private-support-view` to the reusable build workflow. The readiness check requires distinct view identifiers, actual navigation entries and valid packaged view XML. The support view must explain the private delivery/support route; do not invent a Splunkbase URL. With neither input set, the existing public-link requirements still apply.

### Apps Branding & Logos
All applications must include a logo that adheres to the official Splunk branding specifications.

- **Specifications**: Ensure the logo dimensions, file format, and transparency meet the current [Splunk app development guidelines](https://dev.splunk.com/enterprise/docs/developapps/createapps#add-icons-to-your-app).
- **Copyright Compliance**: Developers must ensure they have the legal right to use any custom imagery. Be vigilant regarding copyrights and licensing when selecting a logo.
- **Fallback**: If there is any doubt regarding the copyright of a custom logo, or if a custom logo is unavailable, use the standard Splunk logo as provided in [this folder](https://github.com/splunk-platform-apps/.github/tree/main/documentation/templates/app-logo).

## Commit Messages
[Conventional Commits](https://www.conventionalcommits.org/) specification for commit messages provides a standardized format that makes the commit history more readable and enables automated generation of changelogs.

The basic structure is:

<type>[optional scope]: <description>
[optional body]
[optional footer(s)]

Common types include:
- feat: A new feature
- fix: A bug fix
- docs: Documentation changes
- style: Changes that don't affect code functionality (formatting, etc.)
- refactor: Code changes that neither fix bugs nor add features
- test: Adding or modifying tests
- chore: Changes to build process or auxiliary tools

It's recommended to follow this convention when contributing to the repositories.

## App Naming Convention
Apps should follow the [Splunkbase naming guidelines](https://dev.splunk.com/enterprise/docs/releaseapps/splunkbase/namingguidelines/). Further details for Splunk naming conventions can be found [here](https://lantern.splunk.com/Splunk_Success_Framework/Data_Management/Naming_conventions).

## Renovate (Automated Dependency Updates)
Renovate is configured to automatically manage dependency updates across all repositories in this organization.

### How It Works
- Renovate runs on a schedule via GitHub Actions
- It scans all repositories for outdated dependencies
- PRs are automatically created with updates

### Supported Managers
- GitHub Actions
- Splunk Docker images
- npm (`package.json`)
- Pre-commit hooks (`.pre-commit-config.yaml`)

### Configuration
- **Global config**: `.github/renovate-config.js` (applies to all repos)
- **Repo-level overrides**: `.github/renovate.json` (added in each repo in need for specific settings)

:point_right: More about [configuration options](https://docs.renovatebot.com/configuration-options/)

### Automerge
- PRs with `automerge: true` will auto-merge via GitHub's platform automerge
- Branch protection rules and reviewer approval are still required
- Reviewers are assigned even on automerge PRs (`assignAutomerge: true`)

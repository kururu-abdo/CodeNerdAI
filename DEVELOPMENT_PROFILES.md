# Development profiles

Select a profile using `--profile auto|fullstack|flutter`. Auto detects Flutter when the root `pubspec.yaml` declares `sdk: flutter`; otherwise it chooses Full Stack. For a mixed monorepo, point the CLI at the relevant subproject or select the profile explicitly.

| Profile | Typical tasks | Human checks |
| --- | --- | --- |
| `fullstack` | API endpoints, data models, migrations, UI integration, tests | Security, database migrations, API compatibility, accessibility and deployment |
| `flutter` | Screens, state management, navigation, plugins, unit/widget tests | Device checks, platform permissions, signing and app-store submission |

The profile changes the agent's task guidance. It does **not** install an SDK, add dependencies, run extra tools automatically, or establish expertise by itself. Tests run only when you specify `--test-command`, in the image selected by `--test-image`. Use an image with the correct SDK and dependencies, already available locally.

## Examples

Full Stack Python project:

```bash
python3 codenerd.py /path/to/backend 'Add pagination to orders API' \
  --profile fullstack --test-image my-python-test-image:local \
  --test-command 'pytest -q'
```

Flutter project:

```bash
python3 codenerd.py /path/to/flutter_app 'Fix checkout loading state' \
  --profile flutter --test-image my-flutter-test-image:local \
  --test-command 'flutter analyze && flutter test'
```

Build a test image with the dependencies for your project before running either command. The agent sees source sent to the configured model provider. Remove secrets and obtain client permission first.

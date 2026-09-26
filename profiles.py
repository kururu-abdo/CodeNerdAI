"""Task guidance for the supported development domains."""
from pathlib import Path

PROFILE_GUIDES = {
    'fullstack': '''Full Stack skill profile:
First identify the existing framework, language, entry points, package manager, and test layout. Follow the project's established architecture instead of replacing it.
For backend work consider input validation, authorization on every protected operation, database migrations, transactions, idempotency, error handling, and backwards compatibility.
For frontend work consider accessible controls, loading/error/empty states, responsive layouts, state ownership, and API contract alignment.
For integrations consider secrets in environment configuration, timeouts, retries only where safe, and observability without leaking user data.
Implement the smallest coherent change across API, data, UI and tests as appropriate. Never invent a passing test; report tests that could not run.''',
    'flutter': '''Flutter developer skill profile:
Inspect pubspec.yaml, lib/, test/, existing architecture and state management before editing. Preserve the project's conventions (Riverpod, BLoC, Provider, or otherwise).
Handle widget lifecycle, async cancellation, mounted checks when relevant, null safety, localization, accessibility, adaptive layouts, and Android/iOS differences.
Keep business rules testable outside widgets where practical; add meaningful unit/widget tests for behavior. Check loading/error/empty states and navigation state.
For platform plugins, permissions, builds, signing and store publishing, describe required human configuration rather than guessing credentials or claiming deployment.
Use dart format, flutter analyze, and flutter test when available through the operator-configured test environment; report any checks that could not run.'''
}


def detect_profile(root: Path) -> str:
    """Prefer Flutter only when pubspec.yaml declares a Flutter SDK dependency."""
    pubspec = root / 'pubspec.yaml'
    if pubspec.is_file() and not pubspec.is_symlink():
        try:
            contents = pubspec.read_text(encoding='utf-8')[:50_000]
            if 'sdk: flutter' in contents or 'sdk: "flutter"' in contents or "sdk: 'flutter'" in contents:
                return 'flutter'
        except (OSError, UnicodeError):
            pass
    return 'fullstack'

EVAL_CASES = [
    {
        "repo": "pallets/flask",
        "issue": {
            "title": "deprecate should_ignore_error",
            "body": """
This was added in f191809 as part of the original code to keep the context around for use in the debugger, tests, etc.

The intention seems to be to allow ignoring certain errors during debugging, so that cleanup is still run immediately.

This can be deprecated then removed.
"""
        },
        "expected": [
            "src/flask/sansio/app.py",
            "src/flask/app.py"
        ]
    }
]
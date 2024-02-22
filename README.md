1. `my-language.so` doesn't work on arm MacOS. Need to rebuild it through:
   ```bash
   bash build.sh --> build.py

However, we have to change the build.py a little bit because the structure of project "tree-sitter-php" has changed.

In detail: we need to replace the
```bash
Language.build_library(
    # Store the library in the `build` directory
    'my-languages.so',

    # Include one or more languages
    [
        'tree-sitter-go',
        'tree-sitter-javascript',
        'tree-sitter-python',
        'tree-sitter-php',
        'tree-sitter-java',
        'tree-sitter-ruby',
        'tree-sitter-c-sharp',
    ]
)
```

to 
```bash
Language.build_library(
    # Store the library in the `build` directory
    'my-languages.so',

    # Include one or more languages
    [
        'tree-sitter-go',
        'tree-sitter-javascript',
        'tree-sitter-python',
        'tree-sitter-php/php',
        'tree-sitter-php/php\_only',
        'tree-sitter-java',
        'tree-sitter-ruby',
        'tree-sitter-c-sharp',
    ]
)
```

or it will fail to generate my-language.so.

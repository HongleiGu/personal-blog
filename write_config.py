import os
import yaml
import re

# === Configurations ===

DOCS_DIR = "docs"  # Adjust this to your actual docs folder
MKDOCS_FILE = "mkdocs.yml"

IMPERIAL_FOLDER = os.path.join(DOCS_DIR, "en", "Imperial")

PASSWORD_INVENTORY = {
    "SED1": "SED1-hg1523",
    "SED2": "SED2-hg1523",
    "SED3": "SED3-hg1523",
    "pintos": "pintos-48",
    "Imperial": "Raymond#1234"
}

USERNAME_FOR_IMPERIAL = "hg1523"

# === Functions ===

def build_tree(path):
    """Recursively build tree structure of files and directories for nav."""
    tree = {}
    entries = sorted(os.listdir(path), key=lambda s: s.lower())
    for entry in entries:
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            subtree = build_tree(full_path)
            if subtree:
                tree[entry] = subtree
        elif entry.endswith(".md"):
            key = entry[:-3]  # remove '.md'
            rel_path = os.path.relpath(full_path, DOCS_DIR).replace("\\", "/")
            tree[key] = rel_path
    return tree

def tree_to_nav(tree):
    """Convert tree dict to MkDocs nav list structure."""
    nav = []
    for key, value in tree.items():
        if isinstance(value, dict):
            nav.append({key.title(): tree_to_nav(value)})
        else:
            title = key.replace("-", " ").replace("_", " ").title()
            nav.append({title: value})
    return nav

def clean_and_set_level(md_path, level="Imperial"):
    """Update 'level' field and remove 'username'/'password' if present."""
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    fm_match = re.match(r"^(---\n.*?\n---\n)(.*)$", content, re.DOTALL)
    if fm_match:
        fm_text = fm_match.group(1)
        rest = fm_match.group(2)
        frontmatter = yaml.safe_load(fm_text.strip('-\n')) or {}
    else:
        frontmatter = {}
        rest = content

    # Clean and update fields
    frontmatter["level"] = level
    frontmatter.pop("username", None)
    frontmatter.pop("password", None)

    new_fm_text = "---\n" + yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False) + "---\n"
    new_content = new_fm_text + rest

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated frontmatter in: {md_path}")

def update_imperial_md_files():
    """Recursively update all .md files in Imperial folder."""
    if not os.path.exists(IMPERIAL_FOLDER):
        print(f"Imperial folder not found: {IMPERIAL_FOLDER}, skipping.")
        return

    for root, _, files in os.walk(IMPERIAL_FOLDER):
        for file in files:
            if file.endswith(".md"):
                md_path = os.path.join(root, file)
                clean_and_set_level(md_path)

def generate_mkdocs_config():
    tree = build_tree(DOCS_DIR)
    nav = tree_to_nav(tree)

    config = {
        "site_name": "Honglei Gu's personal blog",
        "repo_url": "https://github.com/everythingfades/personal-blog.git",
        "site_author": "Honglei Gu(everythingfades)",
        "copyright": "2024 by Honglei Gu",
        "nav": nav,
        "markdown_extensions": [
            {"pymdownx.highlight": {"anchor_linenums": True}},
            "pymdownx.inlinehilite",
            "pymdownx.snippets",
            "pymdownx.superfences",
            "admonition",
            "pymdownx.details",
            {"pymdownx.tabbed": {"alternate_style": True}},
            "attr_list",
            {"pymdownx.arithmatex": {"generic": True}},
            "md_in_html",
        ],
        "theme": {
            "name": "material",
            "features": [
                "content.code.annotate",
                "mermaid"
            ],
            "icon": {
                "admonition": {
                    "note": "octicons/tag-16",
                    "abstract": "octicons/checklist-16",
                    "info": "octicons/info-16",
                    "tip": "octicons/squirrel-16",
                    "success": "octicons/check-16",
                    "question": "octicons/question-16",
                    "warning": "octicons/alert-16",
                    "failure": "octicons/x-circle-16",
                    "danger": "octicons/zap-16",
                    "bug": "octicons/bug-16",
                    "example": "octicons/beaker-16",
                    "quote": "octicons/quote-16",
                }
            },
        },
        "dev_addr": "0.0.0.0:9000",
        "site_url": "http://localhost:9000/",
        "use_directory_urls": False,
        "extra_javascript": [
            "theme/js/mathjax.js",
            "https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.0/es5/tex-mml-chtml.js",
            "https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.0/es5/tex-chtml.js",
            "https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.0/es5/tex-chtml-full.js",
            "https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.0/es5/tex-svg-full.js",
        ],
        "plugins": [
            {"search": {}},
            {
                "encryptcontent": {
                    "password_inventory": PASSWORD_INVENTORY,
                    "username_inventory": {
                        "Imperial": USERNAME_FOR_IMPERIAL
                    }
                }
            },
        ],
        "docs_dir": DOCS_DIR,
    }

    with open(MKDOCS_FILE, "w", encoding="utf-8") as f:
        yaml.dump(config, f, sort_keys=False, allow_unicode=True)

    print(f"{MKDOCS_FILE} generated successfully.")

# === Main ===
if __name__ == "__main__":
    if not os.path.exists(DOCS_DIR):
        print(f"❌ Docs folder '{DOCS_DIR}' not found.")
    else:
        generate_mkdocs_config()
        update_imperial_md_files()

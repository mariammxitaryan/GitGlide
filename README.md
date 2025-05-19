````markdown
# GHPush CLI 🚀

A simple, opinionated Python CLI tool to bootstrap a local directory as a Git repository, create a corresponding GitHub repo under your account, and push your code with a single command.


## 🎯 Features

- **GitHub Authentication**: Securely authenticate via a Personal Access Token (PAT).
- **Repo Creation**: Automatically create public or private GitHub repositories under your account.
- **Local Git Initialization**: Initialize a Git repo if one doesn’t exist, or reuse an existing `.git`.
- **Commit & Push**: Stage all changes, commit with your message, and push to the `main` branch.
- **Customizable**: Options for repo name, local directory, commit message, and privacy.

## 🚀 Installation

1. **Clone this project**

2. **Create a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\\Scripts\\activate  # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## 🔧 Configuration

Set your GitHub Personal Access Token in an environment variable:

```bash
export GITHUB_TOKEN="<your_personal_access_token>"
```

> **Note**: Your token needs the `repo` scope to create and push to repositories.

## 💡 Usage

```bash
python src/main.py \
  --repo-name my-new-repo \
  --local-dir ./my-project \
  --commit-message "Initial commit" \
  [--private]
```

| Argument           | Description                                       |
| ------------------ | ------------------------------------------------- |
| `--repo-name`      | **Required**. Name for the new GitHub repository. |
| `--local-dir`      | **Required**. Path to your local project folder.  |
| `--commit-message` | Commit message (default: `Initial commit`).       |
| `--private`        | Flag to create a **private** repository.          |

After running, your code will be available at:

```
https://github.com/<your-username>/my-new-repo.git
```

## 🛠️ Project Structure

```text
├── README.md           # This file
├── requirements.txt    # Python dependencies
└── src
    └── main.py         # CLI entrypoint and logic
```

requirements.txt
```

PyGithub>=1.55
gitpython>=3.1

````

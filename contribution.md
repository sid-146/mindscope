# 🤝 Contributing to **mindscope**

First off, thanks for taking the time to contribute! 🎉
Whether you’re fixing bugs, adding features, improving documentation, or sharing ideas, we welcome your support to make **mindscope** better for everyone.

---

## 🧰 Getting Started

1. **Fork** the repository

2. **Clone** your fork locally:

   ```bash
   git clone https://github.com/your-username/mindscope.git
   cd mindscope
   ```

3. **Create a virtual environment** (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🛠️ Contributing Workflow

### 📌 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### ✏️ 2. Make Your Changes

Write clean, well-documented code. Follow existing style conventions (PEP8).

### ✅ 3. Test Your Changes

Ensure all tests pass:

```bash
pytest
```

If adding a new feature, include new unit tests in the `tests/` directory.

### 📤 4. Commit & Push

```bash
git add .
git commit -m "Add: description of your change"
git push origin feature/your-feature-name
```

### 🧷 5. Create a Pull Request

Go to the original repo and submit a **pull request** from your feature branch.
Describe **what** you changed and **why** in the PR description.

---

## 🧪 Code Standards

- Use clear, readable Python (PEP8 compliant)
- Add docstrings to functions and classes
- Keep functions modular and testable
- Use type hints where appropriate
- All contributions must pass pre-commit checks (if configured)

---

## 💬 Need Help?

If you're unsure about something—open an issue or start a discussion.
We’re happy to support new contributors and collaborate on ideas.

---

## 🙏 Code of Conduct

This project adheres to the [Contributor Covenant](https://www.contributor-covenant.org/).
By participating, you’re expected to uphold respectful and inclusive communication.

---

## 👏 Thank You!

Your contributions help make **mindscope** smarter, more usable, and more impactful for the community.

# 📦 voltrace

**voltrace** is a simple CLI tool that helps you trace where Docker volumes are mounted inside running or stopped containers. Just pass one or more volume names or IDs, and get clear output showing which containers use them — and where! 🔍

---

## 🚀 Features

- 🔍 Find exact mount points of Docker volumes inside containers
- 📋 Works with both running and stopped containers
- 🐳 Lightweight, no dependencies except Docker & Python 3
- 💡 Helpful `--help` output for quick reference

---

## 📥 Installation

You can install **voltrace** using Kevin's Package Manager:

```bash
pkgmgr install voltrace
```

🔗 Kevin's Package Manager: [https://github.com/kevinveenbirkenbach/package-manager](https://github.com/kevinveenbirkenbach/package-manager)

---

## 🧪 Usage

To run the tool, simply call:

```bash
voltrace <VOLUME_ID_OR_NAME> [MORE_VOLUMES...]
```

Example:

```bash
voltrace f9add43bcbda3 my_named_volume
```

To display help:

```bash
voltrace --help
```

---

## 📄 License

MIT License © 2025  
Developed by [Kevin Veen-Birkenbach](https://www.veen.word/)

---

Happy tracing! 🧭

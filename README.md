# Dev Container Setup and Python API Exploration

This guide provides instructions for setting up a development container and experimenting with APIs using Python.

## Prerequisites

- [Visual Studio Code](https://code.visualstudio.com/)
- [Docker](https://www.docker.com/get-started)
- [VS Code Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## Setting Up the Dev Container

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Open in VS Code**

   Open the project directory in Visual Studio Code.

3. **Reopen Folder in Container**

   Press `F1`, select **Remote-Containers: Reopen in Container**, and wait for the container to build.

## Working with Python APIs

Inside the dev container, you can start working with Python to interact with APIs using `urllib3`.

### Install Dependencies

Install any required Python packages:

```bash
pip install -r requirements.txt
```

### Run Python Scripts

Execute your Python scripts as needed:

```bash
python api.py
```

## Additional Resources

- [Python Requests Library](https://docs.python-requests.org/en/latest/)
- [VS Code Dev Containers Documentation](https://code.visualstudio.com/docs/remote/containers)

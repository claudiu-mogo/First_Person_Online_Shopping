#Requirements

To run the application you need to have `git-lfs` installed. This extension to git can be installed with
```
    sudo apt install git-lfs
```

Once that is installed, after cloning the repo input the following commands:

```
    git lfs install
    git lfs fetch origin main
    git lfs checkout
```

#Installation

Run the following script:
```
    python serve.py
```
The web interface is available at `localhost:5000`

# Referencing the GitHub Repository in `requirements.txt`

In the `requirements.txt` of the project where you want to reference this library, you need to add a line specifying the GitHub repository URL.

## Example for a Public GitHub Repository

```plaintext
git+https://github.com/username/repo-name.git@branch-or-tag#egg=package-name
```

- **username**: Your GitHub username.
- **repo-name**: The name of the GitHub repository where the Python library is hosted.
- **branch-or-tag**: Specify the branch (e.g., main) or a tag (e.g., v1.0.0) you want to use.
- **package-name**: The name of the package if you're installing it like a Python package (if setup.py or pyproject.toml is present).

### Check Permissions on the Repository
If the repository is private, you must authenticate to access it via pip. If the repository is public, this step isn't necessary. For private repositories, you can provide your credentials in the requirements.txt entry like this:

```plaintext
git+https://<username>:<token>@github.com/michael-riha/github-python-mono-libs.git@main#egg=lib1&subdirectory=lib1
```

#### In case of `GITHUB_TOKEN`


```plaintext
git+https://${GITHUB_USER}:${GITHUB_TOKEN}@ithub.com/michael-riha/github-python-mono-libs.git@main#egg=lib1&subdirectory=lib1
```

More here: 
- https://docs.readthedocs.io/en/stable/guides/private-python-packages.html#github
- 🔑 How to create a Token in `github` 
  - https://github.com/ByteInternet/pip-install-privates?tab=readme-ov-file#github

# Structure

https://setuptools.pypa.io/en/latest/userguide/package_discovery.html

## Debug

- `pip list`
- `pip show lib1`
- `python -c "import sys; print(sys.path)"`
- Find the path of `site-packages` -> `python -m site`
  - `/usr/local/lib/python3.10/site-packages`
  - `whereis python` -> `/usr/local/bin/python`
- `pip install --upgrade --force-reinstall -r requirements.txt`
  ### Debug and observe depedancies

1) `cd /usr/src/app` WORKDIR of the Container
2) `pip install --no-cache-dir -r requirements.txt`
  1) check the installation `pip list` & `pip show lib1`
3) check the file strcutre of the package `cd /usr/local/lib/python3.10/site-packages`
4) test the import
```
python
>> import lib1
>> lib1.some_function()
```
5) OPTIONAL: uninstall if needed `pip uninstall lib1 lib2`
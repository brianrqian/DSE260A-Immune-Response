# CMI-PB Challenge Summary

## How to use `api_requests.py`

The `api_request.py` file attempts to hit the [CMI-PB PostGREST database](https://www.cmi-pb.org/docs/api/) which is structured as a RESTful API created from a PostgreSQL database. There are two intended ways of of using that file. In that file you will find constants to change the API version, the API endpoint, the accepted file format, and the years pulled from the database.

### Option 1: As a local CLI tool

By running the script using your local python version, you can download all of the data files onto the `data` directory of this project. Every time the script is ran, it will purge any files that exist in that directory.

```bash
python api_requests.py
```

### Option 2: Use the helper methods in a python file

You can opt to use many of the methods defined. They are intended to run independently of each other, and can be used as helper functions within other logic throughout the project

```python
# simplest is an import in the same directory
import api_requests

# if you're working on a file in a different directory, you will need to change ops.path.abspath('../your/intended/path/') to the intended relative path
directory_path = os.path.abspath('../')
if directory_path not in sys.path:
    sys.path.append(directory_path)
import api_requests

# usage
api_requests.create_subdirectory()

```

# flaskr

### install python vitrualenv
```
$ sudo pip install virtualenv
```

### create vitrualenv folder
```
$ virtualenv venv
```

### activate virtualenv
```
$ . venv/bin/activate
```

### setup environment
```
$ pip setup.py --editable .
```

### start server
```
$ sh export.sh
$ flask run --host=0.0.0.0
```

### Test
```
$ py.test
$ py.test -f (Automatically run test when files changed, need install pytest-xdist)
```

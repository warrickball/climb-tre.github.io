# Onyx Client Installation Guide 

This guide walks through how to install the Onyx client in a CLIMB Jupyter notebook.

## Download the client

Launch a Jupyter notebook, and clone the repository for the client:

```
$ git clone https://github.com/CLIMB-COVID/onyx-client.git
```

## Install the client

Create a Python virtual environment for the client:

```
$ python -m venv onyx-env
```

Install the client within this environment:

```
$ source onyx-env/bin/activate
(onyx-env) $ pip install ./onyx-client/
```

## Create a config

Generate a config folder with the `onyx config create` command.

For this you need to provide:

* `Domain`: this should be `https://onyx-test.climb.ac.uk`
* `Config directory`: specify a folder that does not exist, e.g. `onyx-config`

For example:

```
(onyx-env) $ onyx config create --domain https://onyx-test.climb.ac.uk --config-dir onyx-config
```

Once this is done, you **must** export the environment variable `ONYX_CLIENT_CONFIG` as the path to the config directory.

## Register

Register for an Onyx account with the `onyx register` command.

For this you need to provide:

* `First name`
* `Last name`
* `Email address`
* `Site code`: set this to `users`
* `Password`: this will need to be entered twice

For example:

```
(onyx-env) $ onyx register
```

And then follow the instructions.

## Log in

To log in to your Onyx account, run the following command and enter your password:

```
(onyx-env) $ onyx login
```

## View data

Once logged in, contact an admin to get permission to view specific projects. 

Then, to view all data from a project:

```
(onyx-env) $ onyx filter <project-name>
```

To export that data to a `.tsv` file:

```
(onyx-env) $ onyx filter <project-name> --format tsv > data.tsv
```

To view the set of filterable fields in a project:

```
(onyx-env) $ onyx fields <project-name>
```

### Examples

To filter for all samples published on a specific date (e.g. `2023-09-18`):

```
(onyx-env) $ onyx filter <project-name> --field published_date 2023-09-18
```

To filter for all samples published on the current date, you can use the keyword `today`:

```
(onyx-env) $ onyx filter <project-name> --field published_date today
```

To filter for all samples with a `published_date` within the dates `2023-09-01` and `2023-09-18`, you can use the `range` filter: 

```
(onyx-env) $ onyx filter <project-name> --field published_date__range 2023-09-01,2023-09-18
```

## Further guidance

For further guidance using the Onyx client, use the `--help` option.

```
(onyx-env) $ onyx --help
(onyx-env) $ onyx filter --help
```

Or, check out the README file on the Onyx client's [GitHub page](https://github.com/CLIMB-TRE/onyx-client).

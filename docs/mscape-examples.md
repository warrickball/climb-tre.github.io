# Analysis examples for mSCAPE

## Retrieve all samples that contain a particular taxa e.g. `pseudomonas`

This can be done through the CLI:

```
$ onyx filter mscape --field taxa_files.human_readable.icontains=pseudomonas
```

Or through the Python API:

```
import os
from onyx import OnyxConfig, OnyxClient, OnyxEnv, OnyxField

config = OnyxConfig(
    domain=os.environ[OnyxEnv.DOMAIN],
    token=os.environ[OnyxEnv.TOKEN],
)

with OnyxClient(config) as client:
    # Filter for read sets containing "pseudomonas"
    for metadata in client.query(
        "mscape",
        query=OnyxField(taxa_files__human_readable__icontains="pseudomonas"),
    ):
        # Do analysis here
        print("CLIMB ID:", metadata["climb_id"])
        print("Published date:", metadata["published_date"])

        # The query command by default does not return taxonomic information
        # To get this, we have to call the `get` method and retrieve the samples individually
        full_metadata = client.get("mscape", metadata["climb_id"])

        # Now we can inspect the taxonomic information for the readset
        print(
            "Number of binned reads:", len(full_metadata["taxa_files"])
        )  # etc. Do more analysis
        print("Pseudomonas taxa:")
        for taxa in full_metadata["taxa_files"]:
            if "pseudomonas" in taxa["human_readable"].lower():
                print(taxa["human_readable"])
```

## Get a CSV distribution of all binned taxa present in the dataset

Through the CLI:

```
$ onyx filter mscape --summarise taxa_files.taxon_id,taxa_files.human_readable --format csv
```

Or through the Python API:

```
import os
from onyx import OnyxConfig, OnyxClient, OnyxEnv, OnyxField

config = OnyxConfig(
    domain=os.environ[OnyxEnv.DOMAIN],
    token=os.environ[OnyxEnv.TOKEN],
)

with OnyxClient(config) as client:
    for summary_data in client.query(
        "mscape",
        summarise=["taxa_files__taxon_id", "taxa_files__human_readable"],
    ):
        # Do analysis here
        print("Taxon ID:", summary_data["taxa_files__taxon_id"])
        print("Taxon name:", summary_data["taxa_files__human_readable"])
        print("Number of readsets present:", summary_data["count"])
```
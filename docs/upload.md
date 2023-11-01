# Uploading data

## Overview

Data in CLIMB-TRE is managed through a database called Onyx.
To upload data into Onyx, you must deposit the appropriate files
(including the metadata) into the relevant S3 bucket on CLIMB.
We recommend doing this using the AWS or `s3cmd` command-line tools.
For general information about how to upload data to CLIMB,
see the CLIMB docs on
[setting up `s3cmd` locally](https://docs.climb.ac.uk/storage/upload-local-to-s3/#using-s3cmd-on-the-command-line)
and [running `s3cmd` locally or on BRYN](https://docs.climb.ac.uk/storage/fetch-s3-to-notebook/).
You may also wish to review the overall
[CLIMB storage documentation](https://docs.climb.ac.uk/storage/).

Each CLIMB-TRE project requires data (e.g. FASTQ sequencing
reads) and metadata (e.g. a CSV file).  These must match
the relevant specification ("spec") and be uploaded to the appropriate
S3 bucket.  Doing so will trigger the ingest process.  Data that doesn't
meet the spec will not be ingested.

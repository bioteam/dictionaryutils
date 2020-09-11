# Data Dictionary

The data dictionary provides the first level of validation for all data
stored in and generated by BMS. Written in YAML, JSON schemas define all the individual entities
(nodes) in the data model. Moreover, these schemas define all of the relationships (links)
between the nodes. Finally, the schemas define the valid key-value pairs that can be used to
describe the nodes.

Each [**branch**](https://github.com/bioteam/dictionaryutils/branches) within this repository holds the portion of the data dictionary representing a single BMS data domain. The [**root**](https://github.com/bioteam/dictionaryutils/tree/bar) branch holds the central root of the dictionary that is common to all BMS data domains. The [**master**](https://github.com/bioteam/dictionaryutils) branch holds the current merge of the dictionaries from all participating BMS data domains. The [**tagged releases**](https://github.com/bioteam/dictionaryutils/releases) are **MAJOR.MINOR.PATCH** releases of the master branch.

## Visualization

These links below will be automatically updated by a [Github Action](https://github.com/bioteam/dictionaryutils/actions) within a few minutes after creating a branch.

* Travis Build Status BRANCH **stdh-al** [![Build Status](https://travis-ci.com/bioteam/dictionaryutils.svg?branch=stdh-al)](https://travis-ci.com/github/bioteam/dictionaryutils/branches)
* Dictionary Schema BRANCH **stdh-al** [schema.json](https://bms-gen3-dev.s3.amazonaws.com/datadictionary/stdh-al/schema.json)
* Dictionary Visualization BRANCH **stdh-al** [dictionary-visualizer](https://bms-gen3-dev.s3.amazonaws.com/datadictionary/master/viz/index.html#https://bms-gen3-dev.s3.amazonaws.com/datadictionary/stdh-al/schema.json)

## Data Dictionary Structure

The Data Model covers all of the nodes within the as well as the relationships between
the different types of nodes. All of the nodes in the data model are strongly typed and individually
defined for a specific data type. For example, submitted files can come in different forms, such as
aligned or unaligned reads; within the model we have two separately defined nodes for
`Submitted Unaligned Reads` and `Submitted Aligned Reads`. Doing such allows for faster querying of
the data model as well as providing a clear and concise representation of the data in the BPA.

Beyond node type, there are also a number of extensions used to further define the nodes within
the data model. Nodes are grouped up into categories that represent broad roles for the node such
as `analysis` or `biospecimen`. Additionally, nodes are defined within their `Program` or `Project`
and have descriptions of their use. All nodes also have a series of `systemProperties`; these
properties are those that will be automatically filled by the system unless otherwise defined by
the user.  These basic properties define the node itself but still need to be placed into the model.

The model itself is represented as a graph. Within the schema are defined `links`; these links
point from child to parent with Program being the root of the graph. The links also contain a
`backref` that allows for a parent to point back to a child. Other features of the link include a
semantic `label` that describes the relationship between the two nodes, a `multiplicity` property
that describes the numeric relationship from the child to the parent, and a requirement property
to define whether a node must have that link. Taken all together the nodes and links create the
directed graph of the Data Model.

## Node Properties and Examples

Each node contains a series of potential key-value pairs (`properties`) that can be used to
characterize the data they represent. Some properties are categorized as `required` or `preferred`.
If a submission lacks a required property, it cannot be accepted. Preferred properties can denote
two things: the property is being highlighted as it has become more desired by the community or
the property is being promoted to required. All properties not designated either `required` or
`preferred` are still sought by BPA, but submissions without them are allowed.

The properties have further validation through their entries. Legal values are defined in each
property. For the most part these are represented in the `enum` categories although some keys,
such as `submitter_id`, will allow any string value as a valid entry. Other numeric properties
can have maximum and minimum values to limit valid entries.  For examples of what a valid entry
would look like, each node has a mock submission located in the `examples/valid/` directory.

## Contributing

Configure continuous integration (test, build, deploy) of a Gen3 dictionary with Travis CI.

## Prerequisites

* Public dictionary repository (e.g. [bioteam/dictionaryutils](https://github.com/bioteam/dictionaryutils.git))
* Public S3 bucket ([how-to](https://www.simplified.guide/aws/create-public-s3-bucket))
* Travis CI account ([sign up free for public repos](https://travis-ci.com/))
* Development Environment ([for Mac](#development-environment))

## Configure Dictionary

### Clone dictionary repository

```bash
git clone https://github.com/bioteam/dictionaryutils.git
cd dictionaryutils
python setup.py develop
```

### Create IAM Policy for travis-ci user

From within the AWS console, create an IAM policy e.g. *travis-ci-policy* granting access to **only** your public bucket.

```bash
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::bms-gen3-dev"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "arn:aws:s3:::bms-gen3-dev/*"
        }
    ]
}
```

### Create IAM user for travis-ci

From within the AWS console, create an IAM user e.g. *travis-ci* with `Programmatic access`, adding the above inline policy.

### Modify travis.yml

```bash
access_key_id: <Travis_AWS_Access_Key_ID>
...
bucket: <your-public-s3-bucket>
...
upload-dir: <folder-within-s3-bucket>/$TRAVIS_BRANCH
...
repo: <your-git-org/your-public-repo>
```

### Encrypt AWS Secret Access Key

```bash
travis login --pro
# Username: <github_user@example.com>
# Password for <github_user@example.com>: ***************
travis encrypt <travis_aws_secret_access_key> --add deploy.secret_access_key --pro
```

### Development Cycle

1. Modify `gdcdictionary/schemas/*.yaml`
2. Test (iterate until tests pass)
3. Commit
4. Tag
5. Push
6. Observe
7. Verify

```bash
testdict
git commit -am "tagged release 1.0.0"
git tag -a 1.0.0
git push origin master --follow-tags
open https://travis-ci.com/github/bioteam/dictionaryutils
open https://bms-gen3-dev.s3.amazonaws.com/datadictionary/1.0.0/schema.json
```

## Development Environment

### Install CLI tools

```bash
xcode-select --install
```

### Install homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

### Install python 3.6

```bash
brew install pyenv
pyenv install 3.6.10
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc
```

### Install travis

```bash
brew install travis
```

### Install Docker ([Mac](https://hub.docker.com/editions/community/docker-ce-desktop-mac/))

### Install tesdict

```bash
echo -e '\ntestdict() { docker run --rm -v $(pwd):/dictionary quay.io/cdis/dictionaryutils:master; }\n' >> ~/.zshrc
```

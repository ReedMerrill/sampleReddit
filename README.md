# 🫴 sampleReddit: Easily snowball sample Reddit data in Python

sampleReddit provides a streamlined interface for generating documented snowball samples of Reddit data. 

Snowball sampling is a data collection method that starts with a small set of seeds and iteratively collects data from their connections. This method is particularly useful for collecting data from social media platforms, where the connections between users and communities are often of primary interest to academics and data scientists.

## Usage

The core functionality of sampleReddit resides in the `sample_reddit` function:

```python
from sampleReddit import sample_reddit

sampling_frame, users_df = sr.sample_reddit(
    api_instance=instance,
    seed_subreddits=["politics", "news"],
    post_filter="top",
    time_period="year",
    n_posts="3",
    log_file_path="path/to/log/file.log",
)
```

The above function will conduct a snowball of Reddit users by collecting the top 3 posts from the "politics" and "news" subreddits from the past year, and then collecting the usernames of all the users who commented on those posts. The function returns a Python dictionary object with the sampling frame and a pandas DataFrame with the list of the users who were sampled.

A full and annotated example that goes from a list of seed subreddits to a snowball sample of Reddit comments can be found in the [example script](https://github.com/ReedMerrill/sampleReddit-example-files/blob/main/scripts/example-comment-sampling.py).

Any access to the Reddit API requires a Reddit account and a registered application. The `setup_access` function can be used to create an authenticated Reddit API instance. For instructions on how to set up access to the Reddit API, refer to [this guide](https://praw.readthedocs.io/en/stable/getting_started/authentication.html#password-flow). You will also need a regular Reddit to before you can complete the setup.

## Installation

sampleReddit can be installed from PyPI using pip:

```bash
pip install sampleReddit
```

It has been tested on Python 3.10, but should work on 3.6 or later.

## Documentation

Full package documentation can be found in this repo's [wiki](https://github.com/ReedMerrill/sampleReddit/wiki).

## Acknowledgments

sampleReddit is built on top of the [PRAW](https://github.com/praw-dev/praw) (Python Reddit API Wrapper) library, which provides a comprehensive and flexible interface with the Reddit API.

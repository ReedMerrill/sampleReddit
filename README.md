# sampleReddit 🫴

A streamlined interface for generating snowball samples of Reddit data. 

Snowball sampling is a data collection method that starts with a small set of seeds and iteratively collects data from their connections. This method is particularly useful for collecting data from social media platforms, where the connections between users and communities are often of primary interest. sampleReddit also outputs full documentation of each sampling process.

## Installation

sampleReddit can be installed from PyPI using pip:

```bash
pip install sampleReddit
```

## Quick Start

An annotated example of how to go from a list of seed subreddits to a snowball sample of Reddit comments can be found in this [script](https://github.com/ReedMerrill/sampleReddit-example-files/blob/main/scripts/example-comment-sampling.py).

## Usage

The core functionality of sampleReddit resides in the `sample_reddit` function:

```python
import sampleReddit as sr

sampling_frame, users_df = sr.sample_reddit(
    api_instance=instance,
    seed_subreddits=["politics", "news"],
    post_filter="top",
    time_period="year",
    n_posts="3",
    log_file_path="path/to/log/file.log",
)
```

The above function will conduct a snowball sample of Reddit users by collecting the top 3 posts from the "politics" and "news" subreddits from the past year and then the usernames of all the users who commented on those posts. The function returns two things:

1. A Python dictionary object that documents the sampling frame. It maps subreddits to posts and posts to comments.
2. A `pandas` `DataFrame` with a single column called "users" that lists the users who were sampled.

The library also provides lower-level functions that only sample posts from a subreddit, or comments from a list of posts IDs. For a full list of functions, see the [documentation](https://github.com/ReedMerrill/sampleReddit/wiki).

**Note:** Any access to the Reddit API requires an application that is registered with Reddit via their developer portal. Once your app is registered the `setup_access` function can be used to create an authenticated Reddit API instance. For instructions on how to set up a registered Reddit API application, refer to [this guide](https://github.com/reddit-archive/reddit/wiki/OAuth2-App-Types#script-app).[^1]

[^1]: You will need a regular Reddit user account to complete the app authentication setup.

Testing is performed on Python 3.10, but everything should work on 3.6 or later.

## Documentation

Full package documentation can be found in this repo's [wiki](https://github.com/ReedMerrill/sampleReddit/wiki).

## Acknowledgments

sampleReddit is built on top of the [PRAW](https://github.com/praw-dev/praw) (Python Reddit API Wrapper) library, which provides a comprehensive and flexible interface for the Reddit API.

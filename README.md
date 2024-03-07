# sampleReddit 🫴

A streamlined interface for generating snowball samples of Reddit data. 

Snowball sample is a data collection method that starts with a small set of seeds and iteratively collects data that is connected to seed entities. This method is particularly useful for collecting data from social media platforms, where the connections between users and communities are often of primary interest. sampleReddit outputs full documentation of each sampling process.

## Installation

sampleReddit can be installed from PyPI using pip:

```bash
pip install sampleReddit
```

## Quick Start

An annotated example of how to go from a list of seed subreddits to a snowball sample of Reddit comments can be found in this [guide](https://github.com/ReedMerrill/sampleReddit/wiki/Data-Collection-Example) in the repo's wiki.

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

This function is the default implementation of a snowball sampling frame used by sampleReddit. It that starts with a list of subreddits as seeds. It then identifies posts from those subreddits, and users who have commented on those posts in order to generate a snowball sample of Reddit users.[^1]

In the example above the function will collect the usernames of everyone who commented on any of the top 3 posts in the "politics" and "news" subreddits from the past year. The function returns two things:

1. A Python dictionary object that documents the sampling frame. It maps subreddits to posts and posts to comments.
2. A `pandas` `DataFrame` with a single column called "users" that lists the users who were sampled.

The library also provides lower-level functions that only sample posts from a subreddit, or comments from a list of posts IDs. This facilitates the use of sampleReddit to generate custom snowball samples that can use any type of Reddit entity as a seed and snowball its connections to collect a sample of the entity of interest -- you can snowball sample subreddits based on the communities that a seed of users engage with, and so on. For a full list of sampleReddit's functions, see the [documentation](https://github.com/ReedMerrill/sampleReddit/wiki/User-Manual).

[^1]: Any access to the Reddit API requires an application that is registered with Reddit via their developer portal. Once your app is registered the `setup_access` function can be used to create an authenticated Reddit API instance. For instructions on how to set up a registered Reddit API application, refer to [this guide](https://github.com/reddit-archive/reddit/wiki/OAuth2-App-Types#script-app). You will need a regular Reddit user account to complete the app authentication setup.

Testing is performed on Python 3.10, but everything should work on 3.6 or later.

## Documentation

Full documentation can be found in this repo's [wiki](https://github.com/ReedMerrill/sampleReddit/wiki/User-Manual).

## Acknowledgments

sampleReddit is built on top of the [PRAW](https://github.com/praw-dev/praw) (Python Reddit API Wrapper) library, which provides a comprehensive and flexible interface for the Reddit API.

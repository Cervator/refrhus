# The `github-pages` gem pins Jekyll and every plugin to the exact versions
# GitHub Pages runs, so a local build and the deployed one cannot drift.
#
# That matters more here than it might elsewhere: the documents in this
# repository carry no front matter, which works only because Pages enables
# `jekyll-optional-front-matter` and `jekyll-relative-links` by default. A
# hand-picked Jekyll without those plugins renders this site as a directory of
# raw `.md` files.
source "https://rubygems.org"

gem "github-pages", group: :jekyll_plugins

# Not in the default gem set from Ruby 3.4 on, and Jekyll needs them.
gem "csv"
gem "base64"
gem "bigdecimal"
gem "logger"

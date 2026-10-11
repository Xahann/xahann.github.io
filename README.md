# Xane Photography

A responsive Jekyll portfolio for photographer, videographer, and editor Xane.
The photo library includes an optimized local copy of the `WEBSITE` automotive
collection. Only images from that local collection are displayed in the photo
library.

## Publish with GitHub Pages

1. Create a GitHub repository and add these files to its default branch.
2. If this is a project site (not `yourname.github.io`), set `baseurl` in
   `_config.yml` to `"/your-repository-name"`. Leave it empty for a user or
   organization site.
3. In the repository, open **Settings → Pages** and set the build source to
   **Deploy from a branch**, select the default branch and the `/ (root)` folder,
   then save. GitHub Pages builds the Jekyll site and publishes it.
4. Visit [Pages CMS](https://pagescms.org/), sign in with GitHub, and grant it
   access to this repository. Select the repository to edit the site.

## Update your site

- **Site settings** changes the name, homepage headline, work focus, and portfolio
  and Instagram links.
- **Projects** adds or edits featured photos. Upload images in the project
  editor; images are stored in `assets/uploads`.
- **Website photo archive** images are listed in `_data/website_photos.yml` and
  optimized copies live in `assets/uploads/website`. The original JPEGs are not
  modified.
- **Journal posts** creates and edits dated posts. The homepage shows the four
  newest.
- **About page** edits the long-form introduction.

Pages CMS saves changes as commits to the repository. GitHub Pages rebuilds the
site after each commit. For drafts, keep a post's date in the future; Jekyll
does not publish future-dated posts by default.

## Preview locally (optional)

Install Ruby and Jekyll, then run:

```sh
jekyll serve
```

For project sites, preview using the same base path, for example:

```sh
jekyll serve --baseurl "/your-repository-name"
```

# Xane Photography

A responsive Jekyll portfolio for photographer, videographer, and editor Xane.
The photo library includes the automotive `WEBSITE` collection and the music
artist images in `Music artists`.

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

- **Site settings** changes the name, homepage headline, work focus, Instagram
  link, and booking email. Set the booking email address to your
  own inbox; the booking form opens a prefilled message in the visitor's email app.
- **Homepage** features a randomly selected carousel from the photo archive
  and links to the other site sections.
- **Work** is the searchable photo archive, **Journal** lists all published
  notes, and **Booking** collects project details for an email inquiry.
- **Projects** adds or edits featured photos. Upload images in the project
  editor; images are stored in `assets/uploads`.
- **Work photo archive** images are listed in `_data/website_photos.yml`.
  Automotive images use optimized copies in `assets/uploads/website`, and the
  music artist images are served from `Music artists`. Add an `instagram_url` to
  a photo entry only when you have verified that the Instagram post contains
  that photo; the Work page then shows a link to that post when the photo is
  selected.
- **Journal posts** creates and edits dated posts. New posts appear on the
  Journal page.
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

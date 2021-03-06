![icon](https://github.com/y330/scanlendar/blob/master/scanlendarapp/svelte/public/assets/android-chrome-512x512.png)

# Scanlendar


### (ignore below)

svelte pwa starter template
=============

includes elements from [cerivitos/svelte-pwa-now](https://github.com/cerivitos/svelte-pwa-now)

## getting started

0 - make sure [Node.js](https://nodejs.org) is installed

1 - clone or degit the repo

```bash
npx degit OliwerDrywa/svelte-pwa
```

2 - install dependencies

```bash
npm install
```

3 - start in development mode

```bash
npm run dev
```

4 - go to [localhost:3000](http://localhost:3000)

#### for production

build using

```bash
npm run build
```

and serve the `public` folder.

## details

#### icons

the commonly required icons are at `public/assets/`. Be sure to use the same filenames as they are referred to in the metadata at `public/index.html`.
tip: use [Real Favicon Generator](https://realfavicongenerator.net/) which automatically creates all the required icon sizes, and simply unzip the generated asset bundle into `public/assets`.

#### index.html metadata

the icons are all utilized in the `<meta></meta>` tags for Facebook, Twitter and Google indexing among others. be sure to customize your app title and descriptions in all the tags.

#### service worker

registers a workbox-based service worker located at `public/service-worker.js`. this service worker implements workbox's StaleWhileRevalidate for all routes.

#### manifest

customize `public/manifest.json` with your pwa's info for installation. note that the manifest requires a 512x512 icon which is not generated by [Real Favicon Generator](https://realfavicongenerator.net/). you have to manually create that one on your own using something like [https://onlinepngtools.com/resize-png](https://onlinepngtools.com/resize-png).

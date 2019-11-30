# pylint: disable=invalid-name,protected-access,too-many-lines
import unittest

from python.lib.tmdbscraper import imdbratings

# TODO: **requests** error handling in `_get_ratinginfo` is not covered

class TestIMDBRatings(unittest.TestCase):
    def test_parse_imdb_page__goldenpath_2019_08(self):
        # region large `input_model` golden path IMDB page
        input_model = '''






<!DOCTYPE html>
<html
    xmlns:og="http://ogp.me/ns#"
    xmlns:fb="http://www.facebook.com/2008/fbml">
    <head>

        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <meta name="apple-itunes-app" content="app-id=342792525, app-argument=imdb:///title/tt0076759?src=mdot">



        <script type="text/javascript">var IMDbTimer={starttime: new Date().getTime(),pt:'java'};</script>

<script>
    if (typeof uet == 'function') {
      uet("bb", "LoadTitle", {wb: 1});
    }
</script>
  <script>(function(t){ (t.events = t.events || {})["csm_head_pre_title"] = new Date().getTime(); })(IMDbTimer);</script>
        <title>Star Wars: Episode IV - A New Hope (1977) - IMDb</title>
  <script>(function(t){ (t.events = t.events || {})["csm_head_post_title"] = new Date().getTime(); })(IMDbTimer);</script>
<script>
    if (typeof uet == 'function') {
      uet("be", "LoadTitle", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "LoadTitle", {wb: 1});
    }
</script>

        <link rel="canonical" href="https://www.imdb.com/title/tt0076759/" />
        <meta property="og:url" content="http://www.imdb.com/title/tt0076759/" />
        <link rel="alternate" media="only screen and (max-width: 640px)" href="https://m.imdb.com/title/tt0076759/">

<script>
    if (typeof uet == 'function') {
      uet("bb", "LoadIcons", {wb: 1});
    }
</script>
  <script>(function(t){ (t.events = t.events || {})["csm_head_pre_icon"] = new Date().getTime(); })(IMDbTimer);</script>
        <link href="https://m.media-amazon.com/images/G/01/imdb/images/safari-favicon-517611381._CB483525257_.svg" mask rel="icon" sizes="any">
        <link rel="icon" type="image/ico" href="https://m.media-amazon.com/images/G/01/imdb/images/favicon-2165806970._CB470047330_.ico" />
        <meta name="theme-color" content="#000000" />
        <link rel="shortcut icon" type="image/x-icon" href="https://m.media-amazon.com/images/G/01/imdb/images/desktop-favicon-2165806970._CB484110913_.ico" />
        <link href="https://m.media-amazon.com/images/G/01/imdb/images/mobile/apple-touch-icon-web-4151659188._CB483525313_.png" rel="apple-touch-icon">
        <link href="https://m.media-amazon.com/images/G/01/imdb/images/mobile/apple-touch-icon-web-76x76-53536248._CB484146059_.png" rel="apple-touch-icon" sizes="76x76">
        <link href="https://m.media-amazon.com/images/G/01/imdb/images/mobile/apple-touch-icon-web-120x120-2442878471._CB483525250_.png" rel="apple-touch-icon" sizes="120x120">
        <link href="https://m.media-amazon.com/images/G/01/imdb/images/mobile/apple-touch-icon-web-152x152-1475823641._CB470042035_.png" rel="apple-touch-icon" sizes="152x152">
        <link rel="search" type="application/opensearchdescription+xml" href="https://m.media-amazon.com/images/G/01/imdb/images/imdbsearch-3349468880._CB470047351_.xml" title="IMDb" />
  <script>(function(t){ (t.events = t.events || {})["csm_head_post_icon"] = new Date().getTime(); })(IMDbTimer);</script>
<script>
    if (typeof uet == 'function') {
      uet("be", "LoadIcons", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "LoadIcons", {wb: 1});
    }
</script>

        <meta property="pageId" content="tt0076759" />
        <meta property="pageType" content="title" />
        <meta property="subpageType" content="main" />


        <link rel='image_src' href="https://m.media-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY1200_CR71,0,630,1200_AL_.jpg">
        <meta property='og:image' content="https://m.media-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY1200_CR71,0,630,1200_AL_.jpg" />

        <meta property='og:type' content="video.movie" />
    <meta property='fb:app_id' content='115109575169727' />

      <meta property='og:title' content="Star Wars: Episode IV - A New Hope (1977) - IMDb" />
    <meta property='og:site_name' content='IMDb' />
    <meta name="title" content="Star Wars: Episode IV - A New Hope (1977) - IMDb" />
        <meta name="description" content="Directed by George Lucas.  With Mark Hamill, Harrison Ford, Carrie Fisher, Alec Guinness. Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee and two droids to save the galaxy from the Empire's world-destroying battle station, while also attempting to rescue Princess Leia from the mysterious Darth Vader." />
        <meta property="og:description" content="Directed by George Lucas.  With Mark Hamill, Harrison Ford, Carrie Fisher, Alec Guinness. Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee and two droids to save the galaxy from the Empire's world-destroying battle station, while also attempting to rescue Princess Leia from the mysterious Darth Vader." />
        <meta name="keywords" content="Reviews, Showtimes, DVDs, Photos, Message Boards, User Ratings, Synopsis, Trailers, Credits" />
        <meta name="request_id" content="BB2A6ADN39XGB92DM688" />
<script type="application/ld+json">{
  "@context": "http://schema.org",
  "@type": "Movie",
  "url": "/title/tt0076759/",
  "name": "Star Wars",
  "image": "https://m.media-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
  "genre": [
    "Action",
    "Adventure",
    "Fantasy",
    "Sci-Fi"
  ],
  "contentRating": "PG",
  "actor": [
    {
      "@type": "Person",
      "url": "/name/nm0000434/",
      "name": "Mark Hamill"
    },
    {
      "@type": "Person",
      "url": "/name/nm0000148/",
      "name": "Harrison Ford"
    },
    {
      "@type": "Person",
      "url": "/name/nm0000402/",
      "name": "Carrie Fisher"
    },
    {
      "@type": "Person",
      "url": "/name/nm0000027/",
      "name": "Alec Guinness"
    }
  ],
  "director": {
    "@type": "Person",
    "url": "/name/nm0000184/",
    "name": "George Lucas"
  },
  "creator": [
    {
      "@type": "Person",
      "url": "/name/nm0000184/",
      "name": "George Lucas"
    },
    {
      "@type": "Organization",
      "url": "/company/co0071326/"
    },
    {
      "@type": "Organization",
      "url": "/company/co0000756/"
    }
  ],
  "description": "Star Wars is a movie starring Mark Hamill, Harrison Ford, and Carrie Fisher. Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee and two droids to save the galaxy from the Empire\u0027s world-destroying battle...",
  "datePublished": "1977-05-25",
  "keywords": "rebellion,galactic war,empire,princess,droid",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingCount": 1133953,
    "bestRating": "10.0",
    "worstRating": "1.0",
    "ratingValue": "8.6"
  },
  "review": {
    "@type": "Review",
    "itemReviewed": {
      "@type": "CreativeWork",
      "url": "/title/tt0076759/"
    },
    "author": {
      "@type": "Person",
      "name": "Nazi_Fighter_David"
    },
    "dateCreated": "2008-11-30",
    "inLanguage": "English",
    "name": "An adventure story, replacing six-shooters or swords with laser guns and horses with rockers",
    "reviewBody": "The film turn on the endlessly renewed battle between good and evil, the former represented by the Jedi knights and the mystical Force which they are in touch with, and the latter by the Galactic Empire with its Nazi-like storm-troopers \n\nLuke Skywalker\u0027s simple farming life on a remote planet is dramatically changed when he intercepts a distress call from rebel leader Princess Leia Organa The message leads him to Ben Obi-Wan Kenobi and with the two droids C3PO and R2D2, and later Chewbacca and Han Solo, their journey to release the princess from the evil Empire begins \n\nNow a quarter of a century old, Lucas\u0027 project has benefited from improvements in special effects technology, but his vision has remained the same: a naive, even childlike belief in absolute good and evil, a preference for action over character and spectacle over everything",
    "reviewRating": {
      "@type": "Rating",
      "worstRating": "1",
      "bestRating": "10",
      "ratingValue": "9"
    }
  },
  "duration": "PT2H1M",
  "trailer": {
    "@type": "VideoObject",
    "name": "Original Teaser Trailer",
    "embedUrl": "/video/imdb/vi1317709849",
    "thumbnail": {
      "@type": "ImageObject",
      "contentUrl": "https://m.media-amazon.com/images/M/MV5BMTUzNDY0NjY4Nl5BMl5BanBnXkFtZTgwNjY4MTQ0NzE@._V1_.jpg"
    },
    "thumbnailUrl": "https://m.media-amazon.com/images/M/MV5BMTUzNDY0NjY4Nl5BMl5BanBnXkFtZTgwNjY4MTQ0NzE@._V1_.jpg",
    "description": "Watch the original teaser trailer for Star Wars.",
    "uploadDate": "2013-10-13T13:57:04Z"
  }
}</script>
<script>
    if (typeof uet == 'function') {
      uet("bb", "LoadCSS", {wb: 1});
    }
</script>
  <script>(function(t){ (t.events = t.events || {})["csm_head_pre_css"] = new Date().getTime(); })(IMDbTimer);</script>


<!-- h=ics-c52xl-6-1a-e455e862.us-east-1 -->

            <link rel="stylesheet" type="text/css" href="https://m.media-amazon.com/images/G/01/imdb/css/collections/title-flat-v2-23946716._CB439344244_.css" />
        <noscript>
            <link rel="stylesheet" type="text/css" href="https://m.media-amazon.com/images/G/01/imdb/css/wheel/nojs-2827156349._CB470041026_.css">
        </noscript>
  <script>(function(t){ (t.events = t.events || {})["csm_head_post_css"] = new Date().getTime(); })(IMDbTimer);</script>
<script>
    if (typeof uet == 'function') {
      uet("be", "LoadCSS", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "LoadCSS", {wb: 1});
    }
</script>

<script>
    if (typeof uet == 'function') {
      uet("bb", "LoadJS", {wb: 1});
    }
</script>
<script>
    if (typeof uet == 'function') {
      uet("bb", "LoadHeaderJS", {wb: 1});
    }
</script>
  <script>(function(t){ (t.events = t.events || {})["csm_head_pre_ads"] = new Date().getTime(); })(IMDbTimer);</script>

        <script  type="text/javascript">
            // ensures js doesn't die if ads service fails.
            // Note that we need to define the js here, since ad js is being rendered inline after this.
            (function(f) {
                // Fallback javascript, when the ad Service call fails.

                if((window.csm == null || window.generic == null || window.consoleLog == null)) {
                    if (window.console && console.log) {
                        console.log("one or more of window.csm, window.generic or window.consoleLog has been stubbed...");
                    }
                }

                window.csm = window.csm || { measure:f, record:f, duration:f, listen:f, metrics:{} };
                window.generic = window.generic || { monitoring: { start_timing: f, stop_timing: f } };
                window.consoleLog = window.consoleLog || f;
            })(function() {});
        </script>
  <script>
    if ('csm' in window) {
      csm.measure('csm_head_delivery_finished');
    }
  </script>
<script>
    if (typeof uet == 'function') {
      uet("be", "LoadHeaderJS", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "LoadHeaderJS", {wb: 1});
    }
</script>
<script>
    if (typeof uet == 'function') {
      uet("be", "LoadJS", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "LoadJS", {wb: 1});
    }
</script>

    </head>
    <body id="styleguide-v2" class="fixed">

<script>
    if (typeof uet == 'function') {
      uet("bb");
    }
</script>
  <script>
    if ('csm' in window) {
      csm.measure('csm_body_delivery_started');
    }
  </script>
        <div id="wrapper">
            <div id="root" class="redesign">
                <div id="nb20" class="navbarSprite">
                    <div id="supertab">
	<!-- no content received for slot: top_ad -->

</div>

<script>
    if (typeof uet == 'function') {
      uet("ns");
    }
</script>
  <div id="navbar" class="navbarSprite">
<noscript>
    <style>
        #pagecontent{margin-top:-17px}
    </style>
</noscript>
<span id="home_img_holder">
<a href="/"
title="Home" class="navbarSprite" id="home_img" ></a>  <span class="alt_logo">
    <a href="/"
title="Home" >IMDb</a>
  </span>
</span>
<form
 method="get"
 action="/find"
 class="nav-searchbar-inner"
 id="navbar-form"

>
  <div id="nb_search">
    <noscript><div id="more_if_no_javascript"><a href="/search/">More</a></div></noscript>
    <button id="navbar-submit-button" class="primary btn" type="submit" aria-label="Submit Search"><div class="magnifyingglass navbarSprite"></div></button>
    <input type="hidden" name="ref_" value="nv_sr_fn" />
    <input type="text" autocomplete="off" value="" name="q" id="navbar-query" placeholder="Find Movies, TV shows, Celebrities and more...">
    <div class="quicksearch_dropdown_wrapper">
      <select name="s" id="quicksearch" class="quicksearch_dropdown navbarSprite hidden">
        <option value="all" >All</option>
        <option value="tt" >Titles</option>
        <option value="ep" >TV Episodes</option>
        <option value="nm" >Names</option>
        <option value="co" >Companies</option>
        <option value="kw" >Keywords</option>
      </select>
    </div>
    <div id="navbar-suggestionsearch" class='celwidget' cel_widget_id='SuggestionSearchWidget'></div>
  </div>
</form>
<div id="megaMenu">
    <ul id="consumer_main_nav" class="main_nav">
            <li class="spacer"></li>
            <li class="css_nav_item freediveNavMenu" id="navFreediveMenu">
                <p class="navCategory">
<a href="/tv/"
> Watch Now For Free
</a>                </p>
                <span class="downArrow"></span>
                <div id="navMenu0" class="sub_nav freediveNavMenu__container">
                    <h5>
                        <span class="headerText">Featured</span>
                        <span class="seeAll">
                            <a href="/tv/"
>Browse more titles &raquo;</a>
                        </span>
                    </h5>
                    <ul id="freediveNavMenuList" class="freediveNavMenu__list"></ul>
                </div>
                <script>
                    if (!('imdb' in window)) { window.imdb = {}; }
                    window.imdb.freediveTitleData = [
                             {
                                imageUrl: "https://m.media-amazon.com/images/M/MV5BMTM2MTI5NzA3MF5BMl5BanBnXkFtZTcwODExNTc0OA@@._V1_SY209_CR0,0,140,209_AL_.jpg",
                                link: "https://www.imdb.com/tv/watch/tt1045658",
                                title: "Silver Linings Playbook"
                             },
                             {
                                imageUrl: "https://m.media-amazon.com/images/M/MV5BNDdhMzMxOTctNDMyNS00NTZmLTljNWEtNTc4MDBmZTYxY2NmXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY209_CR0,0,140,209_AL_.jpg",
                                link: "https://www.imdb.com/tv/watch/tt0190332",
                                title: "Crouching Tiger, Hidden Dragon"
                             },
                             {
                                imageUrl: "https://m.media-amazon.com/images/M/MV5BMTQ5NjQ0NDI3NF5BMl5BanBnXkFtZTcwNDI0MjEzMw@@._V1_SY209_CR0,0,140,209_AL_.jpg",
                                link: "https://www.imdb.com/tv/watch/tt0454921",
                                title: "The Pursuit of Happyness"
                             },
                    ];
                </script>
            </li>
        <li class="spacer"></li>
        <li class="css_nav_item" id="navTitleMenu">
            <p class="navCategory">
                <a href="/movies-in-theaters/"
>Movies</a>,
                <a href="/chart/toptv/"
>TV</a><br />
                & <a href="/showtimes/"
>Showtimes</a></p>
            <span class="downArrow"></span>
            <div id="navMenu1" class="sub_nav">
                    <div id="titleMenuImage" style="background: url('https://ia.media-imdb.com/images/M/MV5BMjA5ODU3NTI0Ml5BMl5BanBnXkFtZTcwODczMTk2Mw@@._V1._SY315_CR180,0,410,315_.jpg')">
                        <a title="                            The Dark Knight
, #4 on IMDb Top Rated Movies"
                            href="/title/tt0468569/?ref_=nv_mv_dflt_1" class="fallback">
                        </a>
                        <div class="overlay">
                            <p>
                                <a href="/title/tt0468569/?ref_=nv_mv_dflt_2" id="titleMenuImageClick">
                                    <strong>                            The Dark Knight
</strong> (2008)
                                </a>
                                <br />
                                <a href="/chart/top?ref_=nv_mv_dflt_3" id="titleMenuImageSecondaryClick">
                                    #<strong>4</strong> on IMDb Top Rated Movies
                                </a> &raquo;
                            </p>
                        </div>
                    </div>
                <div class="subNavListContainer">
                    <h5>MOVIES</h5>
                    <ul>
                        <li><a href="/movies-in-theaters/"
>In Theaters</a></li>
                        <li><a href="/showtimes/"
>Showtimes & Tickets</a></li>
                        <li><a href="/trailers/"
>Latest Trailers</a></li>
                        <li><a href="/movies-coming-soon/"
>Coming Soon</a></li>
                        <li><a href="/calendar/"
>Release Calendar</a></li>
                        <li><a href="/chart/top"
>Top Rated Movies</a></li>
                        <li><a href="/india/top-rated-indian-movies"
>Top Rated Indian Movies</a></li>
                        <li><a href="/chart/moviemeter"
>Most Popular Movies</a></li>
                    </ul>
                        <h5>CHARTS & TRENDS</h5>
                        <ul>
                            <li><a href="/chart/"
>Box Office</a></li>
                            <li><a href="/search/title?count=100&groups=oscar_best_picture_winners&sort=year,desc"
>Oscar Winners</a></li>
                            <li><a href="/genre/"
>Most Popular by Genre</a></li>
                        </ul>
                </div>
                <div class="subNavListContainer">
                    <h5>TV & VIDEO</h5>
                    <ul>
                        <li><a href="/chart/toptv/"
>Top Rated TV Shows</a></li>
                        <li><a href="/chart/tvmeter"
>Most Popular TV Shows</a></li>
                        <li><a href="/sections/dvd/"
>DVD & Blu-Ray</a></li>
                    </ul>
                    <h5>SPECIAL FEATURES</h5>
                    <ul>
                        <li><a href="/amazon-originals/"
>Amazon Originals</a></li>
                        <li><a href="/streaming/"
>Streaming Now</a></li>
                        <li><a href="/scary-good/"
>Horror Guide</a></li>
                        <li><a href="/imdbpicks/"
>IMDb Picks</a></li>
                        <li><a href="/originals/"
>IMDb Original Series</a></li>
                        <li><a href="/family-entertainment-guide/"
>Family Movie/TV Guide</a></li>
                    </ul>
                </div>
            </div>
        </li>
        <li class="spacer"></li>
        <li class="css_nav_item" id="navNameMenu">
            <p class="navCategory">
                <a href="/search/name?gender=male,female"
>Celebs</a>,
                <a href="/awards-central/"
>Events</a><br />
                & <a href="/gallery/rg1859820288"
>Photos</a></p>
            <span class="downArrow"></span>
            <div id="navMenu2" class="sub_nav">
                    <div id="nameMenuImage" style="background: url('https://ia.media-imdb.com/images/M/MV5BMjAyOTgyMjUzNV5BMl5BanBnXkFtZTcwODM1MTU0Nw@@._V1._SX250_CR0,0,250,315_.jpg')">
                        <a title="Emma Stone, #185 on STARmeter"
                            href="/name/nm1297015/?ref_=nv_cel_dflt_1" class="fallback">
                        </a>
                        <div class="overlay">
                            <p>
                                <a href="/name/nm1297015/?ref_=nv_cel_dflt_2" id="nameAdClick">
                                    <strong>Emma Stone</strong>
                                </a> &raquo;
                                <br />
                                #<strong>185</strong> on STARmeter
                            </p>
                        </div>
                    </div>
                <div class="subNavListContainer">
                    <h5>CELEBS</h5>
                    <ul>
                            <li><a href="/search/name?birth_monthday=08-25&refine=birth_monthday"
>Born Today</a></li>
                        <li><a href="/news/celebrity"
>Celebrity News</a></li>
                        <li><a href="/search/name?gender=male,female"
>Most Popular Celebs</a></li>
                    </ul>
                    <h5>PHOTOS</h5>
                    <ul>
                        <li><a href="/gallery/rg1859820288"
>Latest Stills</a></li>
                        <li><a href="/gallery/rg1624939264"
>Latest Posters</a></li>
                        <li><a href="/gallery/rg1641716480"
>Photos We Love</a></li>
                    </ul>
                </div>
                <div class="subNavListContainer">
                    <h5>EVENTS</h5>
                    <ul>
                        <li><a href="/awards-central/"
>Awards Central</a></li>
                        <li><a href="/festival-central/"
>Festival Central</a></li>
                        <li><a href="/oscars/"
>Oscars</a></li>
                        <li><a href="/golden-globes/"
>Golden Globes</a></li>
                        <li><a href="/sundance/"
>Sundance</a></li>
                        <li><a href="/cannes/"
>Cannes</a></li>
                        <li><a href="/comic-con/"
>San Diego Comic-Con</a></li>
                        <li><a href="/emmys/"
>Emmy Awards</a></li>
                        <li><a href="/venice/"
>Venice Film Festival</a></li>
                        <li><a href="/toronto/"
>Toronto Film Festival</a></li>
                        <li><a href="/festival-central/tribeca"
>Tribeca</a></li>
                        <li><a href="/lafilmfest/"
>LA Film Festival</a></li>
                        <li><a href="/event/all/"
>All Events</a></li>
                    </ul>
                </div>
            </div>
        </li>
        <li class="spacer"></li>
        <li class="css_nav_item" id="navNewsMenu">
            <p class="navCategory">
                <a href="/news/top"
>News</a> &<br />
                <a href="/czone/"
>Community</a>
            </p>
            <span class="downArrow"></span>
            <div id="navMenu3" class="sub_nav">
                <div id="latestHeadlines">
                    <div class="subNavListContainer">
                        <h5>LATEST HEADLINES</h5>
    <ul class="ipl-simple-list">
            <li class="news_item">
<a href="/news/ni62594746"
> 'Angel Has Fallen' Rises to Weekend #1 as 'Hobbs & Shaw' Delivers in China Bow
</a><br />
                <small>
                <span>25 August 2019</span>
                <span>|</span>
                <span>Box Office Mojo</span>
                </small>
            </li>
            <li class="news_item">
<a href="/news/ni62594343"
> Disney+ TV Shows to Stream Episodes Weekly – Won’t Be Dropped All at Once
</a><br />
                <small>
                <span>24 August 2019</span>
                <span>|</span>
                <span>The Wrap</span>
                </small>
            </li>
            <li class="news_item">
<a href="/news/ni62594538"
> D23: 9 Things We Learned About Disney’s Monster Slate, From ‘Black Widow’ to ‘Star Wars’
</a><br />
                <small>
                <span>25 August 2019</span>
                <span>|</span>
                <span>Indiewire</span>
                </small>
            </li>
    </ul>
                    </div>
                </div>
                <div class="subNavListContainer">
                    <h5>NEWS</h5>
                    <ul>
                        <li><a href="/news/top"
>Top News</a></li>
                        <li><a href="/news/movie"
>Movie News</a></li>
                        <li><a href="/news/tv"
>TV News</a></li>
                        <li><a href="/news/celebrity"
>Celebrity News</a></li>
                        <li><a href="/news/indie"
>Indie News</a></li>
                    </ul>
                    <h5>COMMUNITY</h5>
                    <ul>
                        <li><a href="/czone/"
>Contributor Zone</a></li>
                        <li><a href="/poll/"
>Polls</a></li>
                    </ul>
                </div>
            </div>
        </li>
        <li class="spacer"></li>
        <li class="css_nav_item" id="navWatchlistMenu">
<p class="navCategory singleLine watchlist">
    <a href="/list/watchlist"
>Watchlist</a>
</p>
<span class="downArrow"></span>
<div id="navMenu4" class="sub_nav">
    <h5>
            YOUR WATCHLIST
    </h5>
    <ul id="navWatchlist">
    </ul>
    <script>
    if (!('imdb' in window)) { window.imdb = {}; }
    window.imdb.watchlistTeaserData = [
                {
                        href : "/list/watchlist",
                src : "https://m.media-amazon.com/images/G/01/wprs/images/navbar/watchlist_slot1_logged_out._CB484021159_.jpg"
                },
                {
                    href : "/search/title?count=100&title_type=feature,tv_series",
                src : "https://m.media-amazon.com/images/G/01/wprs/images/navbar/watchlist_slot2_popular._CB484021159_.jpg"
                },
                {
                    href : "/chart/top",
                src : "https://m.media-amazon.com/images/G/01/wprs/images/navbar/watchlist_slot3_top250._CB484021159_.jpg"
                }
    ];
    </script>
</div>
        </li>
        <li class="spacer"></li>
    </ul>
</div>
<div id="nb_extra">
    <ul id="nb_extra_nav" class="main_nav">
        <li class="css_nav_item" id="navProMenu">
    <p class="navCategory">
<a href="https://pro.imdb.com/login/ap?u=/login/lwa&imdbPageAction=signUp&rf=cons_nb_hm"
> <img alt="IMDbPro Menu" src="https://m.media-amazon.com/images/G/01/wprs/images/navbar/imdbpro_logo_nb._CB484021162_.png" />
</a>    </p>
    <span class="downArrow"></span>

<div id="navMenuPro" class="imdb-pro-ad-shared imdb-pro-ad-redesign sub_nav">
<a href="https://pro.imdb.com/login/ap?u=/login/lwa&imdbPageAction=signUp&rf=cons_nb_hm"
class="imdb-pro-ad__link" > <div id="proAd" class="imdb-pro-ad__image">
<img alt="Go to IMDbPro" height="145" width="127"
src="https://m.media-amazon.com/images/G/01/wprs/images/navbar/imdbpro_navbar_menu_user._CB484021156_.png"
srcset="https://m.media-amazon.com/images/G/01/wprs/images/navbar/imdbpro_navbar_menu_user._CB484021156_.png 1x, https://m.media-amazon.com/images/G/01/wprs/images/navbar/imdbpro_navbar_menu_user_2x._CB484021157_.png 2x"/>
</div>
<section class="imdb-pro-ad__content">
<div class="imdb-pro-ad__title">The essential resource for entertainment professionals</div>
<p class="imdb-pro-ad__line">Find industry contacts &amp; talent representation</p>
<p class="imdb-pro-ad__line">Access in-development titles not available on IMDb</p>
<p class="imdb-pro-ad__line">Get the latest news from leading industry trades</p>
<p class="imdb-pro-ad__line">Claim your page and control your brand across IMDb & Amazon</p>
<div class="imdb-pro-new__button">
<svg width="175px" height="30px" viewBox="0 0 172 29" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<title>TryIMDbProFree</title>
<g id="tryIMDbProFree" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
<rect id="tryIMDbProFreeButton" stroke="#A88734" fill="#F1C241" x="1" y="1" width="170" height="28" rx="3"></rect>
<text id="tryIMDbProFreeText">
<tspan x="33" y="19">Try IMDbPro Free</tspan>
</text>
</g>
</svg>
</div>
</section>
</a></div>
        </li>
        <li class="spacer"><span class="ghost">|</span></li>
        <li>
            <a href="https://help.imdb.com/imdb"
>Help</a>
        </li>
        <li class="spacer"><span class="ghost">|</span></li>

    <li class="nb-social-links">
    <a href="/offsite/?page-action=fol_fb&token=BCYvOaLHDDiFxpJs8XPYqxYZ3wdEmAMnrptNos2FWaz_y5oNclRtGR2MRrUzreqvYobOlnGKN935%0D%0AK-qVk_uB2AVodi1ywOknYTAnkhOZvXL-vEcMVpi-ftwg1wD_e8Vjv2-ZbVUvLuPWZhAQnsNDcyKc%0D%0AEKajjWrtfKiBoU2zfdypbhMRvgVR4KMYE-fzJyX3apDw8OfhSFyglUxVChN49xwiCw%0D%0A"
title="Follow IMDb on Facebook" class="nb-social-links__link" target="_blank" > <svg class="ipl-icon ipl-facebook-icon ipl-icon--inherit-color ipl-icon--inline" width="24" height="24" xmlns="http://www.w3.org/2000/svg" fill="#000000" viewBox="0 0 24 24">
<path d="M20.896 2H3.104C2.494 2 2 2.494 2 3.104v17.792C2 21.506 2.494 22 3.104 22h9.579v-7.745h-2.607v-3.018h2.607V9.01c0-2.584 1.577-3.99 3.882-3.99 1.104 0 2.052.082 2.329.119v2.7h-1.598c-1.254 0-1.496.595-1.496 1.47v1.927h2.989l-.39 3.018h-2.6V22h5.097c.61 0 1.104-.494 1.104-1.104V3.104C22 2.494 21.506 2 20.896 2"/>
</svg>
</a>
    <a href="/offsite/?page-action=fol_inst&token=BCYvDPkGkLZ0-IK18BFfgRol5zOOMeJjdu3sRW1YSJkozzjm1Czx5ZN6XlaoGF6StynCqrQa7fd2%0D%0Aadp0EOXGha31PcGXtiC5O4C4LcuoeOBj4Zyrar-Hnfa16NzrTStH4YQJpcgRzEEpSLrJwNiWB_3c%0D%0ABhOBEWF_OIIRjo0WKxqhuMD8gjPWgdqGvt4623pqt7c9HAvAtemUexmb9KK6m1DL1w%0D%0A"
title="Follow IMDb on Instagram" class="nb-social-links__link" target="_blank" > <svg class="ipl-icon ipl-instagram-icon ipl-icon--inherit-color ipl-icon--inline" width="24" height="24" xmlns="http://www.w3.org/2000/svg" fill="#000000" viewBox="0 0 24 24">
<path d="M11.997 2.04c-2.715 0-3.056.011-4.122.06-1.064.048-1.79.217-2.426.463a4.901 4.901 0 0 0-1.771 1.151 4.89 4.89 0 0 0-1.153 1.767c-.247.635-.416 1.36-.465 2.422C2.011 8.967 2 9.307 2 12.017s.011 3.049.06 4.113c.049 1.062.218 1.787.465 2.422a4.89 4.89 0 0 0 1.153 1.767 4.901 4.901 0 0 0 1.77 1.15c.636.248 1.363.416 2.427.465 1.066.048 1.407.06 4.122.06s3.055-.012 4.122-.06c1.064-.049 1.79-.217 2.426-.464a4.901 4.901 0 0 0 1.77-1.15 4.89 4.89 0 0 0 1.154-1.768c.247-.635.416-1.36.465-2.422.048-1.064.06-1.404.06-4.113 0-2.71-.012-3.05-.06-4.114-.049-1.062-.218-1.787-.465-2.422a4.89 4.89 0 0 0-1.153-1.767 4.901 4.901 0 0 0-1.77-1.15c-.637-.247-1.363-.416-2.427-.464-1.067-.049-1.407-.06-4.122-.06m0 1.797c2.67 0 2.985.01 4.04.058.974.045 1.503.207 1.856.344.466.181.8.397 1.15.746.349.35.566.682.747 1.147.137.352.3.88.344 1.853.048 1.052.058 1.368.058 4.032 0 2.664-.01 2.98-.058 4.031-.044.973-.207 1.501-.344 1.853a3.09 3.09 0 0 1-.748 1.147c-.35.35-.683.565-1.15.746-.352.137-.88.3-1.856.344-1.054.048-1.37.058-4.04.058-2.669 0-2.985-.01-4.039-.058-.974-.044-1.504-.207-1.856-.344a3.098 3.098 0 0 1-1.15-.746 3.09 3.09 0 0 1-.747-1.147c-.137-.352-.3-.88-.344-1.853-.049-1.052-.059-1.367-.059-4.031 0-2.664.01-2.98.059-4.032.044-.973.207-1.501.344-1.853a3.09 3.09 0 0 1 .748-1.147c.35-.349.682-.565 1.149-.746.352-.137.882-.3 1.856-.344 1.054-.048 1.37-.058 4.04-.058"/><path d="M11.997 15.342a3.329 3.329 0 0 1-3.332-3.325 3.329 3.329 0 0 1 3.332-3.326 3.329 3.329 0 0 1 3.332 3.326 3.329 3.329 0 0 1-3.332 3.325m0-8.449a5.128 5.128 0 0 0-5.134 5.124 5.128 5.128 0 0 0 5.134 5.123 5.128 5.128 0 0 0 5.133-5.123 5.128 5.128 0 0 0-5.133-5.124M18.533 6.69c0 .662-.537 1.198-1.2 1.198a1.198 1.198 0 1 1 1.2-1.197"/>
</svg>
</a>
    <a href="/offsite/?page-action=fol_twch&token=BCYmTa0sG-I-RzF5Q9hNTEhFfCO6Aog65eqWWnyc9kdgJ0xm55I9Pnrnltd5qwIST380CxI0Wzev%0D%0AMTSeOHkksiI6NgBF7AF3gAQDJPm3z1rMIu-cqu3D3E_Q-_kodqQgoAlGe54qxx7kBgScaWq1GWaK%0D%0A8okCvGMQRiJTX41WsnwdEQv5i1aEu9AFMNU7gJGfJGv-25Vg95bl28isQCw63Ac1qw%0D%0A"
title="Follow IMDb on Twitch" class="nb-social-links__link" target="_blank" > <svg class="ipl-icon ipl-twitch-icon ipl-icon--inherit-color ipl-icon--inline" width="24" height="24" xmlns="http://www.w3.org/2000/svg" fill="#000000" viewBox="0 0 24 24">
<g><path d="M3.40641795,2 L22.0023886,2 L22.0023886,14.8140302 L16.5329854,20.2834333 L12.4700003,20.2834333 L9.81343304,22.9400005 L7.00059714,22.9400005 L7.00059714,20.2834333 L2,20.2834333 L2,5.5941792 L3.40641795,2 Z M20.1271646,13.8764182 L20.1271646,3.87522393 L5.12537321,3.87522393 L5.12537321,17.0017914 L9.34462705,17.0017914 L9.34462705,19.6583587 L12.0011943,17.0017914 L17.0017914,17.0017914 L20.1271646,13.8764182 Z"></path><polygon points="17.0017914 7.46940312 17.0017914 12.9388062 15.1265675 12.9388062 15.1265675 7.46940312"></polygon><polygon points="12.0011943 7.46940312 12.0011943 12.9388062 10.1259704 12.9388062 10.1259704 7.46940312"></polygon></g>
<path d="M0 0h24v24H0z" fill="none"/>
</svg>
</a>
    <a href="/offsite/?page-action=fol_tw&token=BCYkZqmF_TkcRFC9dBJl9yubPScgJrc32UAaHZ6LDDjAMAlaTc-EqZ2k6V-HfE_yrZd7PlIUfm9v%0D%0AkD8FXDwWfGXuMUB_44wlrSorj8Mk_IwLdtuUUqlv22ZVDiXt06nB68fVxn4JbTdKQjNbiHg_TAez%0D%0A9xIDgORJP1HX8pkn5rpuQwoUQR-gYrwvVrsJhbXzE_32pAZiV1MkBqb1Ib-pNRehgA%0D%0A"
title="Follow IMDb on Twitter" class="nb-social-links__link" target="_blank" > <svg class="ipl-icon ipl-twitter-icon ipl-icon--inherit-color ipl-icon--inline" width="24" height="24" xmlns="http://www.w3.org/2000/svg" fill="#000000" viewBox="0 0 24 24">
<path d="M8.29 19.936c7.547 0 11.675-6.13 11.675-11.446 0-.175-.004-.348-.012-.52A8.259 8.259 0 0 0 22 5.886a8.319 8.319 0 0 1-2.356.633 4.052 4.052 0 0 0 1.804-2.225c-.793.46-1.67.796-2.606.976A4.138 4.138 0 0 0 15.847 4c-2.266 0-4.104 1.802-4.104 4.023 0 .315.036.622.107.917a11.728 11.728 0 0 1-8.458-4.203 3.949 3.949 0 0 0-.556 2.022 4 4 0 0 0 1.826 3.348 4.136 4.136 0 0 1-1.858-.503l-.001.051c0 1.949 1.415 3.575 3.292 3.944a4.193 4.193 0 0 1-1.853.07c.522 1.597 2.037 2.76 3.833 2.793a8.34 8.34 0 0 1-5.096 1.722A8.51 8.51 0 0 1 2 18.13a11.785 11.785 0 0 0 6.29 1.807"/>
</svg>
</a>
    <a href="/offsite/?page-action=fol_yt&token=BCYvnGNaTE4KxrDVhPNetMNJd72s-FV9T0vIK7z0R7ZQVIIRX9YcaFieLsPJrf7ARNfHFElN0m8D%0D%0A77o9CaIzx_Zh4Rr1q-0OM1Knrr2DJIisgAFIlm9IyzF2ZTRecbd0nZoLtiPu0u2KvL5w4c_rucLD%0D%0AWbXlKUebvlG_HtO9D3miQ2-TwJTAnakeah3Pige0KP45ygkWsU79dtFy9IXepGt2Yw%0D%0A"
title="Follow IMDb on YouTube" class="nb-social-links__link" target="_blank" > <svg class="ipl-icon ipl-youtube-icon ipl-icon--inherit-color ipl-icon--inline" width="24" height="24" xmlns="http://www.w3.org/2000/svg" fill="#000000" viewBox="0 0 24 24">
<path d="M9.955 14.955v-5.91L15.182 12l-5.227 2.955zm11.627-7.769a2.505 2.505 0 0 0-1.768-1.768C18.254 5 12 5 12 5s-6.254 0-7.814.418c-.86.23-1.538.908-1.768 1.768C2 8.746 2 12 2 12s0 3.254.418 4.814c.23.86.908 1.538 1.768 1.768C5.746 19 12 19 12 19s6.254 0 7.814-.418a2.505 2.505 0 0 0 1.768-1.768C22 15.254 22 12 22 12s0-3.254-.418-4.814z"/>
<path d="M0 0h24v24H0z" fill="none"/>
</svg>
</a>
    </li>

    </ul>
</div>
<div id="nb_personal">
    <ul id="consumer_user_nav" class="main_nav">
            <li class="css_nav_menu no_arrow" id="navUserMenu">
            <p class="navCategory singleLine">
<a href="/registration/signin?u=https%3A//www.imdb.com/title/tt0076759/"
class="signin-button" id="imdb-signin-link" > <span class="signin-imdb-text">Sign in</span>
</a>            </p>
        </li>
    </ul>
</div>
  </div>
<script>
    if (typeof uet == 'function') {
      uet("ne");
    }
</script>

	<!-- no content received for slot: navstrip -->


	<!-- no content received for slot: injected_navstrip -->

                </div>


                <div id="pagecontent" class="pagecontent">

	<!-- no content received for slot: injected_billboard -->
















	<!-- no content received for slot: navboard -->











<div id="content-2-wide" class="flatland">
    <div id="main_top" class="main">














            <div class="title-overview">


  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleOverviewWidget_started');
    }
  </script>
        <div id="title-overview-widget" class="heroic-overview">
            <div class="vital">
      <div id="quicklinksBar" class="subnav">
  <div id="quicklinksMainSection">
         <a href="/title/tt0076759/fullcredits"
class="quicklink" >FULL CAST AND CREW</a> <span class="ghost">|</span>
         <a href="/title/tt0076759/trivia"
class="quicklink" >TRIVIA</a> <span class="ghost">|</span>
         <a href="/title/tt0076759/reviews"
class="quicklink" >USER REVIEWS</a> <span class="ghost">|</span>
      <a href="https://pro.imdb.com/title/tt0076759?rf=cons_tt_contact"
class="quicklink" >IMDbPro</a>
        <span class="ghost">|</span>
        <span class="show_more quicklink">
            MORE<span class="titleOverviewSprite quicklinksArrowUp"></span>
        </span>
        <span class="show_less quicklink" style="display:none">
           LESS<span class="titleOverviewSprite quicklinksArrowDown"></span>
        </span>
  </div>

    <span id="title-social-sharing-widget"></span>

        <div id="share-checkin">
<div class="add_to_checkins" data-const="tt0076759" data-lcn="title-maindetails">
<span class="btn2_wrapper"><a onclick='' class="btn2 large btn2_text_on disabled checkins_action_btn"><span class="btn2_glyph">0</span><span class="btn2_text">Check in</span></a></span>    <div class="popup checkin-dialog">
        <a class="dialog-close-button">X</a>
        <span class="title">I'm Watching This!</span>
        <div class="body">
            <div class="info">Keep track of everything you watch; tell your friends.
            </div>
            <div class="small message_box">
                <div class="hidden error"><h2><div class="checkin-error">Error</div></h2> Please try again!</div>
                <div class="hidden success"><h2><div class="checkin-success">Added to Your Check-Ins.</div></h2> <a href="/list/checkins">View</a></div>
            </div>
            <textarea data-msg="Enter a comment..."></textarea>
            <div class="share">
                <button class="checkin-button"><span>Check in</span></button>
<!--
                    Check-ins are more fun when<br>
                    you <a href="/register/sharing">enable Facebook sharing</a>!
-->
            </div>
        </div>
    </div>
    <input type="hidden" name="49e6c" value="da29">
</div>
        </div>

   <div class="quicklinkSection" id="full_subnav" style="display:none">
               <div class="quicklinkSectionColumn">
    <div class="quicklinkGroup">
        <div class="quicklinkSectionHeader">DETAILS</div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/fullcredits"
class="quicklink" >Full Cast and Crew</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/releaseinfo"
class="quicklink" >Release Dates</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/officialsites"
class="quicklink" >Official Sites</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/companycredits"
class="quicklink" >Company Credits</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/locations"
class="quicklink" >Filming & Production</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/technical"
class="quicklink" >Technical Specs</a>            </div>
    </div>
               </div>
               <div class="quicklinkSectionColumn">
    <div class="quicklinkGroup">
        <div class="quicklinkSectionHeader">STORYLINE</div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/taglines"
class="quicklink" >Taglines</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/plotsummary"
class="quicklink" >Plot Summary</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/synopsis"
class="quicklink" >Synopsis</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/keywords"
class="quicklink" >Plot Keywords</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/parentalguide"
class="quicklink" >Parents Guide</a>            </div>
    </div>
    <div class="quicklinkGroup">
        <div class="quicklinkSectionHeader">RELATED ITEMS</div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/news"
class="quicklink" >News</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/externalsites"
class="quicklink" >External Sites</a>            </div>
    </div>
               </div>
               <div class="quicklinkSectionColumn">
    <div class="quicklinkGroup">
        <div class="quicklinkSectionHeader">OPINION</div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/awards"
class="quicklink" >Awards</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/faq"
class="quicklink" >FAQ</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/reviews"
class="quicklink" >User Reviews</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/ratings"
class="quicklink" >User Ratings</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/externalreviews"
class="quicklink" >External Reviews</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/criticreviews"
class="quicklink" >Metacritic Reviews</a>            </div>
    </div>
    <div class="quicklinkGroup">
        <div class="quicklinkSectionHeader">PHOTO & VIDEO</div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/mediaindex"
class="quicklink" >Photo Gallery</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/videogallery"
class="quicklink" >Trailers and Videos</a>            </div>
    </div>
               </div>
               <div class="quicklinkSectionColumn">
    <div class="quicklinkGroup">
        <div class="quicklinkSectionHeader">DID YOU KNOW?</div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/trivia"
class="quicklink" >Trivia</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/goofs"
class="quicklink" >Goofs</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/crazycredits"
class="quicklink" >Crazy Credits</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/quotes"
class="quicklink" >Quotes</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/alternateversions"
class="quicklink" >Alternate Versions</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/movieconnections"
class="quicklink" >Connections</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt0076759/soundtrack"
class="quicklink quicklinkGray" >Soundtracks</a>            </div>
    </div>
               </div>
   </div>
      </div>

                <div class="title_block">
                    <div class="title_bar_wrapper">

    <div class="ratings_wrapper">
            <div class="imdbRating" itemtype="http://schema.org/AggregateRating" itemscope="" itemprop="aggregateRating">
                    <div class="ratingValue">
<strong title="8.6 based on 1,133,953 user ratings"><span itemprop="ratingValue">8.6</span></strong><span class="grey">/</span><span class="grey" itemprop="bestRating">10</span>                    </div>
                    <a href="/title/tt0076759/ratings"
><span class="small" itemprop="ratingCount">1,133,953</span></a>
                        <div class="hiddenImportant">
                                <span itemprop="reviewCount">1,657 user</span>
                                <span itemprop="reviewCount">309 critic</span>
                        </div>
            </div>

  <div id="star-rating-widget" class="star-rating-widget" data-tconst="tt0076759" data-rating="0" data-user=""
  data-auth="" data-tracking-tag="title-maindetails" data-rating-share-enabled="false" data-title="Star Wars: Episode IV - A New Hope"
  data-rating-next-share-time="2000-01-01T00:00:00.000Z" data-rating-share-treatment="C">
    <div class="star-rating-button">
      <button>
        <span class="star-rating-star no-rating"></span>
            <span class="star-rating-text">Rate This</span>
      </button>
    </div>
  </div>
    </div>
    <div class="titleBar">
        <div class="primary_ribbon">
            <div class="ribbonize" data-tconst="tt0076759" data-caller-name="title"></div>
            <div class="wlb_dropdown_btn" data-tconst="tt0076759" data-size="large" data-caller-name="title" data-type="primary"></div>
            <div class="wlb_dropdown_list" style="display:none"></div>
        </div>

        <div class="title_wrapper">
<h1 class="">Star Wars: Episode IV - A New Hope&nbsp;<span id="titleYear">(<a href="/year/1977/"
>1977</a>)</span>            </h1>
                <div class="originalTitle">Star Wars<span class="description"> (original title)</span></div>
            <div class="subtext">
                    PG
    <span class="ghost">|</span>                    <time datetime="PT121M">
                        2h 1min
                    </time>
    <span class="ghost">|</span>
<a href="/search/title?genres=action&explore=title_type,genres"
>Action</a>,
<a href="/search/title?genres=adventure&explore=title_type,genres"
>Adventure</a>,
<a href="/search/title?genres=fantasy&explore=title_type,genres"
>Fantasy</a>
    <span class="ghost">|</span>
<a href="/title/tt0076759/releaseinfo"
title="See more release dates" >25 May 1977 (USA)
</a>            </div>
        </div>
    </div>
                    </div>
                </div>




                    <div class="slate_wrapper">
    <div class="poster">
<a href="/title/tt0076759/mediaviewer/rm3263717120"
> <img alt="Star Wars: Episode IV - A New Hope Poster" title="Star Wars: Episode IV - A New Hope Poster"
src="https://m.media-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX182_CR0,0,182,268_AL_.jpg" />
</a>    </div>
    <div class="slate">
<a href="/video/imdb/vi1317709849?playlistId=tt0076759"
class="slate_button prevent-ad-overlay video-modal" data-type='recommends' data-tconst='tt0076759' data-video='vi1317709849' data-context='imdb' data-refsuffix='tt_ov_vi' data-pixels=''> <img alt="Trailer"
title="Trailer"
src="https://m.media-amazon.com/images/M/MV5BMTUzNDY0NjY4Nl5BMl5BanBnXkFtZTgwNjY4MTQ0NzE@._V1_CR0,60,640,360_AL_UX477_CR0,0,477,268_AL_.jpg" />
<div class="slate_fade_top"></div>
<div class="slate_fade_bottom"></div>
</a>        <div class="caption">
            <div style="float: left;">2:02 <span class="ghost">|</span> Trailer</div>
                <div style="float: right;">        <a href="/title/tt0076759/videogallery"
>15 VIDEOS</a>
    <span class="ghost">|</span>        <a href="/title/tt0076759/mediaindex"
>482 IMAGES</a>
</div>
            <div style="clear: both;"></div>
        </div>
    </div>
                    </div>
            </div>



        <a name="slot_center-2"></a>







            <script type="text/javascript">if(typeof uet === 'function'){uet('bb','TitleWatchBar',{wb:1});}</script>




        <span class="ab_widget">
                <div class="watchbar2 article">
    <div class="showtime full-table ">
        <div class="winner-option watch-option "
                    data-offsite="1"
                    data-href="/offsite/?page-action=watch-aiv&token=BCYoowbi2BjKQOgYMqV03CNzX7X1Cy88-dVsug8Mtw_kegYX0CDrkGQv1Eqxdl0-81BRRiZOonTX%0D%0AiSUVsNvXzUTw_8gZhPr3URfeEjQTbznE4rVD8Y4iPMu2qb44UPl384x4MypdEZOsLiA4YEwaAHqv%0D%0AFCVO0XNGk8eJmJ7uMrJnN4U1I41PcSBqKTH7Y8C-XLKXA86g2iEqS2jjddS9SSOR1muv3JjSgup7%0D%0AJxBvfmR49XiEg16_1p0lW1kVmzAOg3Fi0o4-_GRh5MbA0WKtF2-AhWSTLNvi1wTVJgxtyGtv_ZU%0D%0A"
             title="Watch Now">
            <div id="watchbar2" class="watch-icon winner provider amazon-instant-video">
            </div>
            <div class="info table-cell">
                <h2>

<a href="/offsite/?page-action=watch-aiv&token=BCYoowbi2BjKQOgYMqV03CNzX7X1Cy88-dVsug8Mtw_kegYX0CDrkGQv1Eqxdl0-81BRRiZOonTX%0D%0AiSUVsNvXzUTw_8gZhPr3URfeEjQTbznE4rVD8Y4iPMu2qb44UPl384x4MypdEZOsLiA4YEwaAHqv%0D%0AFCVO0XNGk8eJmJ7uMrJnN4U1I41PcSBqKTH7Y8C-XLKXA86g2iEqS2jjddS9SSOR1muv3JjSgup7%0D%0AJxBvfmR49XiEg16_1p0lW1kVmzAOg3Fi0o4-_GRh5MbA0WKtF2-AhWSTLNvi1wTVJgxtyGtv_ZU%0D%0A"
class="segment-link " target="_blank"> Watch Now
</a>                </h2>
                <p>

            From $19.99 on
Prime Video                </p>
            </div>
        </div>
    <script type="text/javascript">
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.open("POST","/tr/",true);
        xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
        xmlhttp.send("ref_=tt_wbr_aiv&pt=title&spt=main&pageAction=showing-aiv&ht=clickstreamIgnore");
    </script>
            <div title="On TV" class="watch-option secondary-watch-option " data-href="/title/tt0076759/tvschedule" data-optiontype="tv">
                <div class="watch-icon tv"></div>
                <div class="secondary-info">ON&nbsp;TV</div>
            </div>
            <div title="On Disc" class="watch-option secondary-watch-option " data-href="/offsite/?page-action=watch-amazon&token=BCYg_reQXrvbdVZuVSl71Mr5HCOzefVn8kCFm-oz5OcEHGaqrTr6ng8d8NWcSLUI-gGRuBRgyGo3%0D%0A7BJVc7dGrL2z9u-It-1_FEIjeHOE5IHXwHYHGTEA4PTwLHnaintXqHZlAQ1wAX8GR0FJULkvZ4Ae%0D%0AEliSxkp_cn0Zdl6f6GDTEWBPkaBMiV4Kd6-3h5QTJMfTs8pVZ5hKfo0KMQ7-3g_ILZFohpnlZ5CF%0D%0ArVNtZrLoHXCZomPxD5Otq18wSJaeCNwc%0D%0A" data-optiontype="physical">
                <div class="watch-icon physical"></div>
                <div class="secondary-info">ON&nbsp;DISC</div>
            </div>
        <div title="All Watch Options" class="watch-option secondary-watch-option has-watchoptions" data-href="/watch/_ajax/box/tt0076759#watchoptions">
                <div class="watch-icon all"></div>
                <div class="secondary-info">ALL</div>
            </div>
    </div>
        </div>


        </span>



            <script type="text/javascript">
                if(typeof uex === 'function'){uex('ld','TitleWatchBar',{wb:1});}
            </script>







    <div class="plot_summary_wrapper">
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitlePlotAndCreditSummaryWidget_started');
    }
  </script>
    <div class="plot_summary ">
            <div class="summary_text">
                    Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee and two droids to save the galaxy from the Empire's world-destroying battle station, while also attempting to rescue Princess Leia from the mysterious Darth Vader.
            </div>

    <div class="credit_summary_item">
        <h4 class="inline">Director:</h4>
<a href="/name/nm0000184/"
>George Lucas</a>    </div>
    <div class="credit_summary_item">
        <h4 class="inline">Writer:</h4>
<a href="/name/nm0000184/"
>George Lucas</a>    </div>
    <div class="credit_summary_item">
        <h4 class="inline">Stars:</h4>
<a href="/name/nm0000434/"
>Mark Hamill</a>, <a href="/name/nm0000148/"
>Harrison Ford</a>, <a href="/name/nm0000402/"
>Carrie Fisher</a>            <span class="ghost">|</span>
<a href="fullcredits/"
>See full cast & crew</a>&nbsp;&raquo;
    </div>
    </div>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitlePlotAndCreditSummaryWidget_finished');
    }
  </script>
        <!--To display Pro Title CTA above the watchlist for in-development titles -->
    <div class="wlb-title-main-details">
        <span class="full-wl-button ribbonize" data-tconst="tt0076759" data-recordmetrics=true></span>
    </div>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleReviewsAndPopularityWidget_started');
    }
  </script>
      <div class="titleReviewBar ">
    <div class="titleReviewBarItem">
<a href="criticreviews"
> <div class="metacriticScore score_favorable titleReviewBarSubItem">
<span>90</span>
</div></a>        <div class="titleReviewBarSubItem">
            <div><a href="criticreviews"
>
Metascore
</a>            </div>
            <div><span class="subText">
               From <a href="http://www.metacritic.com"
target='_blank'>metacritic.com</a>
               </span>
            </div>
        </div>
    </div>
                   <div class="divider"></div>

    <div class="titleReviewBarItem titleReviewbarItemBorder">
        <div>
        Reviews
        </div>
        <div>
            <span class="subText">
                   <a href="reviews"
>1,657 user</a>
                       <span class="ghostText">|</span>
                   <a href="externalreviews"
>309 critic</a>
             </span>
        </div>
    </div>
                   <div class="divider"></div>

    <div class="titleReviewBarItem">
  <div class="titleOverviewSprite popularityTrendUp"></div>
        <div class="titleReviewBarSubItem">
            <div>
            Popularity
            </div>
            <div>
                <span class="subText">
                    328
      (<span class="titleOverviewSprite popularityImageUp"></span> <span class="popularityUpOrFlat">133</span>)
                </span>
            </div>
        </div>
    </div>
      </div>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleReviewsAndPopularityWidget_finished');
    }
  </script>
    </div>
                <!--To display Pro Title CTA below the review bar for completed titles -->

            <div class="pro_logo_main_title">
    <div id=title_completed_pro_link class=pro_title_link_with_separator>
<a href="https://pro.imdb.com/title/tt0076759?rf=cons_tt_atf"
class="pro_title_href" > <img src="https://m.media-amazon.com/images/G/01/imdb/IMDbConsumerSiteProTitleViews/images/logo/pro_logo_dark-3176609149._CB455053166_.png" class="pro_logo" />
<span class="pro_title_link_text">
View production, box office, & company info
</span>
<img src="https://m.media-amazon.com/images/G/01/imdb/IMDbConsumerSiteProTitleViews/images/icons/link_2x-1783866327._CB454438608_.png"
class="pro_link_icon">
</a>    </div>
            </div>
        </div>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleOverviewWidget_finished');
    }
  </script>
            </div>

<script>
    if (typeof uet == 'function') {
      uet("af");
    }
</script>
  <script>
    if ('csm' in window) {
      csm.measure('csm_atf_main');
    }
  </script>

    </div>

<script>
    if (typeof uet == 'function') {
      uet("cf");
    }
</script>


    <div id="sidebar">


	<!-- no content received for slot: top_rhs -->

  <script>
    if ('csm' in window) {
      csm.measure('csm_atf_sidebar');
    }
  </script>















        <a name="slot_right-3"></a>
        <div class="mini-article">






            <script type="text/javascript">if(typeof uet === 'function'){uet('bb','NinjaWidget',{wb:1});}</script>




        <span class="ab_widget">



    <div class="ab_ninja">
<span class="widget_header"> <span class="oneline"> <a href="/list/ls025849840/videoplayer/vi2957949977" > <h3> Even Emmy Nominees Love a Good Alligator Flick</h3> </a> </span> </span> <div class="widget_content no_inline_blurb"> <div class="widget_nested"> <div class="ninja_image_pack"> <div class="ninja_center"> <div class="ninja_image first_image last_image" style="width:307px;height:auto;" > <div style="width:307px;height:auto;margin:0 auto;"> <div class="widget_image"> <div class="image"> <a href="/list/ls025849840/videoplayer/vi2957949977" class="video-modal" data-refsuffix="tt_ecw_367_mm_watchlist" data-ref="tt_ecw_367_mm_watchlist_i_1"> <img class="pri_image" title="The IMDb Show (2017-)" alt="The IMDb Show (2017-)" src="https://m.media-amazon.com/images/M/MV5BZGFkZjhjYzktNTg0Yi00MThkLWEwNzItMzFhZTgzYjMxNzFmXkEyXkFqcGdeQXRyYW5zY29kZS13b3JrZmxvdw@@._CR457,58,1284,962_UX614_UY460._SY230_SX307_AL_.jpg" /> <img alt="The IMDb Show (2017-)" title="The IMDb Show (2017-)" class="image_overlay overlay_mouseout" src="https://m.media-amazon.com/images/G/01/IMDb/icon/play-button._CB318667375_.png" data-src-x2="https://m.media-amazon.com/images/G/01/IMDb/icon/play-button._CB318667375_.png" /> <img alt="The IMDb Show (2017-)" title="The IMDb Show (2017-)" class="image_overlay overlay_mouseover" src="https://m.media-amazon.com/images/G/01/IMDb/icon/play-button-hover._CB318667374_.png" data-src-x2="https://m.media-amazon.com/images/G/01/IMDb/icon/play-button-hover._CB318667374_.png" /> </a> </div> </div> </div> </div> </div> </div> </div> </div> <p class="blurb"><a href="/name/nm0571106">Michael McKean</a> shares a surprising pick that made his Watchlist.</p> <p class="seemore"><a href="/list/ls025849840/videoplayer/vi2957949977" class="position_bottom supplemental" > Watch now</a></p>    </div>



        </span>



            <script type="text/javascript">
                if(typeof uex === 'function'){uex('ld','NinjaWidget',{wb:1});}
            </script>





        </div>








	<!-- no content received for slot: rhs_cornerstone -->







<script>
    if (typeof uet == 'function') {
      uet("bb", "RelatedNewsWidgetRHS", {wb: 1});
    }
</script>
    <script>
      if ('csm' in window) {
        csm.measure('csm_RelatedNewsWidgetRHS_started');
      }
    </script>

        <div class="mini-article" >
            <h3>Related News</h3>
    <ul class="ipl-simple-list">
            <li class="news_item">
<a href="/news/ni62467791"
> Peter Mayhew Remembered: Mark Hamill Calls Chewbacca Actor "A Big Man With an Even Bigger Heart"
</a><br />
                <small>
                <span>03 May 2019</span>
                <span>|</span>
                <span>The Wrap</span>
                </small>
            </li>
            <li class="news_item">
<a href="/news/ni62461630"
> Check Out This Star Wars Death Star Trench Art Made Out of Wood
</a><br />
                <small>
                <span>28 April 2019</span>
                <span>|</span>
                <span>GeekTyrant</span>
                </small>
            </li>
            <li class="news_item">
<a href="/news/ni62453737"
> Seven Seas to publish Dirty Pair manga in December
</a><br />
                <small>
                <span>20 April 2019</span>
                <span>|</span>
                <span>Flickeringmyth</span>
                </small>
            </li>
    </ul>

            <div class="see-more">
                <a href="/title/tt0076759/news"
>See all related articles</a>&nbsp;&raquo;
            </div>
        </div>

    <script>
      if ('csm' in window) {
        csm.measure('csm_RelatedNewsWidgetRHS_finished');
      }
    </script>
<script>
    if (typeof uet == 'function') {
      uet("be", "RelatedNewsWidgetRHS", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "RelatedNewsWidgetRHS", {wb: 1});
    }
</script>







	<!-- no content received for slot: middle_rhs -->










        <a name="slot_right-7"></a>
        <div class="mini-article">






            <script type="text/javascript">if(typeof uet === 'function'){uet('bb','ZergnetWidget',{wb:1});}</script>




        <span class="ab_widget">
            <div class="ab_zergnet">
<span class="widget_header"> <span class="oneline"> <h3> Around The Web</h3> <span>&nbsp;|&nbsp;</span> <h4> Powered by ZergNet</h4> </span> </span> <div class="widget_content no_inline_blurb"> <div class="widget_nested"> <iframe class="zergnet-frame__sidebar" scrolling="no" seamless src="https://m.media-amazon.com/images/G/01/imdb/html/zergnet-3826556079._CB470047339_.html?widgetId=46653"></iframe> </div> </div>    </div>


        </span>



            <script type="text/javascript">
                if(typeof uex === 'function'){uex('ld','ZergnetWidget',{wb:1});}
            </script>





        </div>


<script>
    if (typeof uet == 'function') {
      uet("bb", "RelatedEditorialListsWidget", {wb: 1});
    }
</script>
        <div class="mini-article">
            <div id="relatedEditorialListsWidget">
                <h3>Editorial Lists</h3>
                <p>Related lists from IMDb editors</p>

    <div class="list-preview even">
        <div class="list-preview-item-narrow">
<a href="/list/ls046118590"
><img height="86" width="86" alt="list image" title="list image" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/medium/film-3385785534._CB483791896_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BYTRhNjcwNWQtMGJmMi00NmQyLWE2YzItODVmMTdjNWI0ZDA2XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UX86_CR0,0,86,86_AL_.jpg" /></a>        </div>
        <div class="list_name">
            <strong><a href="/list/ls046118590"
>
All 'Star Wars' Movies
</a></strong>
        </div>
        <div class="list_meta">
            a list of 12 titles

            <br />updated 5&nbsp;months&nbsp;ago
        </div>
        <div class="clear">&nbsp;</div>
    </div>
    <div class="list-preview odd">
        <div class="list-preview-item-narrow">
<a href="/list/ls043291557"
><img height="86" width="86" alt="list image" title="list image" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/medium/film-3385785534._CB483791896_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BMTU0OTQyODQzN15BMl5BanBnXkFtZTcwNTg3ODQyMQ@@._V1_UX86_CR0,0,86,86_AL_.jpg" /></a>        </div>
        <div class="list_name">
            <strong><a href="/list/ls043291557"
>
Tamannaah Bhatia, Parul Yadav, and Kajal Aggarwal's Watchlist
</a></strong>
        </div>
        <div class="list_meta">
            a list of 20 titles

            <br />updated 6&nbsp;months&nbsp;ago
        </div>
        <div class="clear">&nbsp;</div>
    </div>
    <div class="list-preview even">
        <div class="list-preview-item-narrow">
<a href="/list/ls033096238"
><img height="86" width="86" alt="list image" title="list image" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/medium/film-3385785534._CB483791896_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BMTAzNjIyMzY3NjNeQTJeQWpwZ15BbWU4MDU5MTA1NTYz._V1_UX86_CR0,0,86,86_AL_.jpg" /></a>        </div>
        <div class="list_name">
            <strong><a href="/list/ls033096238"
>
Biggest Golden Globe-Nominated Transformations Over the Years
</a></strong>
        </div>
        <div class="list_meta">
            a list of 88 images

            <br />updated 7&nbsp;months&nbsp;ago
        </div>
        <div class="clear">&nbsp;</div>
    </div>
    <div class="list-preview odd">
        <div class="list-preview-item-narrow">
<a href="/list/ls022515677"
><img height="86" width="86" alt="list image" title="list image" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/medium/film-3385785534._CB483791896_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BOTkxMTAxNTg4Nl5BMl5BanBnXkFtZTgwNDkzNTE1NTM@._V1_UY86_CR21,0,86,86_AL_.jpg" /></a>        </div>
        <div class="list_name">
            <strong><a href="/list/ls022515677"
>
'Star Wars' References and Easter Eggs in 'Solo'
</a></strong>
        </div>
        <div class="list_meta">
            a list of 13 images

            <br />updated 09&nbsp;Jun&nbsp;2018
        </div>
        <div class="clear">&nbsp;</div>
    </div>
    <div class="list-preview even">
        <div class="list-preview-item-narrow">
<a href="/list/ls033953605"
><img height="86" width="86" alt="list image" title="list image" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/medium/film-3385785534._CB483791896_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX86_CR0,0,86,86_AL_.jpg" /></a>        </div>
        <div class="list_name">
            <strong><a href="/list/ls033953605"
>
Top 100 Movies as Rated by Women on IMDb in 2016
</a></strong>
        </div>
        <div class="list_meta">
            a list of 100 titles

            <br />updated 27&nbsp;Apr&nbsp;2018
        </div>
        <div class="clear">&nbsp;</div>
    </div>
            </div>
        </div>
<script>
    if (typeof uet == 'function') {
      uet("be", "RelatedEditorialListsWidget", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "RelatedEditorialListsWidget", {wb: 1});
    }
</script>

<script>
    if (typeof uet == 'function') {
      uet("bb", "RelatedListsWidget", {wb: 1});
    }
</script>
        <div class="mini-article">
            <div id="relatedListsWidget">
                <div class="rightcornerlink">
                    <a href="/list/create"
>Create a list</a>&nbsp;&raquo;
                </div>
                <h3>User Lists</h3>
                <p>Related lists from IMDb users</p>

    <div class="list-preview even">
        <div class="list-preview-item-narrow">
<a href="/list/ls052436693"
><img height="86" width="86" alt="list image" title="list image" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/medium/film-3385785534._CB483791896_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX86_CR0,0,86,86_AL_.jpg" /></a>        </div>
        <div class="list_name">
            <strong><a href="/list/ls052436693"
>
Favourites: Sci-Fi
</a></strong>
        </div>
        <div class="list_meta">
            a list of 46 titles
            <br />created 10&nbsp;Nov&nbsp;2013

        </div>
        <div class="clear">&nbsp;</div>
    </div>
    <div class="list-preview odd">
        <div class="list-preview-item-narrow">
<a href="/list/ls041819603"
><img height="86" width="86" alt="list image" title="list image" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/medium/film-3385785534._CB483791896_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BMjQ2NzE1MjYxMV5BMl5BanBnXkFtZTgwMjM3MDQxNzM@._V1_UX86_CR0,0,86,86_AL_.jpg" /></a>        </div>
        <div class="list_name">
            <strong><a href="/list/ls041819603"
>
watched in 2019
</a></strong>
        </div>
        <div class="list_meta">
            a list of 49 titles
            <br />created 7&nbsp;months&nbsp;ago

        </div>
        <div class="clear">&nbsp;</div>
    </div>
    <div class="list-preview even">
        <div class="list-preview-item-narrow">
<a href="/list/ls013315479"
><img height="86" width="86" alt="list image" title="list image" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/medium/film-3385785534._CB483791896_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UX86_CR0,0,86,86_AL_.jpg" /></a>        </div>
        <div class="list_name">
            <strong><a href="/list/ls013315479"
>
Fantasy
</a></strong>
        </div>
        <div class="list_meta">
            a list of 49 titles
            <br />created 28&nbsp;Oct&nbsp;2015

        </div>
        <div class="clear">&nbsp;</div>
    </div>
    <div class="list-preview odd">
        <div class="list-preview-item-narrow">
<a href="/list/ls047924520"
><img height="86" width="86" alt="list image" title="list image" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/medium/film-3385785534._CB483791896_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BNGYyZGM5MGMtYTY2Ni00M2Y1LWIzNjQtYWUzM2VlNGVhMDNhXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX86_CR0,0,86,86_AL_.jpg" /></a>        </div>
        <div class="list_name">
            <strong><a href="/list/ls047924520"
>
Favorite Movies
</a></strong>
        </div>
        <div class="list_meta">
            a list of 46 titles
            <br />created 8&nbsp;months&nbsp;ago

        </div>
        <div class="clear">&nbsp;</div>
    </div>
    <div class="list-preview even">
        <div class="list-preview-item-narrow">
<a href="/list/ls046320261"
><img height="86" width="86" alt="list image" title="list image" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/medium/film-3385785534._CB483791896_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UX86_CR0,0,86,86_AL_.jpg" /></a>        </div>
        <div class="list_name">
            <strong><a href="/list/ls046320261"
>
Sifi &amp; Fantasy
</a></strong>
        </div>
        <div class="list_meta">
            a list of 33 titles
            <br />created 5&nbsp;months&nbsp;ago

        </div>
        <div class="clear">&nbsp;</div>
    </div>
                <div class="see-more">
                    <a href="/lists/tt0076759"
>See all related lists</a>&nbsp;&raquo;
                </div>
            </div>
        </div>
<script>
    if (typeof uet == 'function') {
      uet("be", "RelatedListsWidget", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "RelatedListsWidget", {wb: 1});
    }
</script>





        <a name="slot_right-8"></a>
        <div class="mini-article">






            <script type="text/javascript">if(typeof uet === 'function'){uet('bb','MessageWidget',{wb:1});}</script>




        <span class="ab_widget">



    <div class="ab_message">
<span class="widget_header"> <h3> Related Items</h3> </span> <div class="widget_content inline_blurb"> <div class="widget_nested"> <div class="ninja_image_pack"> <div class="ninja_left"> <div class="ninja_image first_image last_image" style="width:38px;height:auto;" > <div style="width:38px;height:auto;margin:0 auto;"> <div class="widget_image"> <div class="image"> <a href="/offsite/?page-action=offsite-amazon&token=BCYr81ladvGS6t9KTPkOpBr71orQmAVa8wp8jEDqJ6qorfN6AEYP2DGWkICgE5TP06v3Cd8sb-GJ%0D%0APIyzuxAfKvNbWv-yB__uhHdGHZNXjNz-n8pL2RcwbzIbfH8rNv2r3n42FMmMSPLWC_GIPp_774XI%0D%0ArzO7pl44Sg_DUkgcbG_CEFEzNql-TZNzm_fH8ATvgKg-pHgOAW2sZ_MnLwmgjriikaFG9CI1fsh1%0D%0AWVvc0BRg_ntwde6n8XVpkCXU2BMwqEx1UH5Yh2fYbIDVOHECPB2ZeZf30SL-isV5mLMxH8-35wsM%0D%0AIMeuVlGFIDD80sPeB1pmRPo3F9X2RVoLpo_8GXsO_g%0D%0A" > <img class="pri_image" title="Search for &quot;Star Wars: Episode IV - A New Hope&quot; on Amazon.com" alt="Search for &quot;Star Wars: Episode IV - A New Hope&quot; on Amazon.com" src="https://m.media-amazon.com/images/G/01/imdb/images/widget/amazon._CB339202444_.png" /> </a> </div> </div> </div> </div> </div> </div> </div> <div class="ninja_image ninja_image_fixed_padding widget_padding"></div><div class="widget_inline_blurb"><p class="blurb">Search for "<a href="/offsite/?page-action=offsite-amazon&token=BCYlWnt_0QGKyfHwCBlc3qQNpqNkZiNH5UY2typBA0iHxCaLVG45cLGnPBNy1uKwbSqhzs_2qZHn%0D%0AH905z3tYIRwOtvfSwikjDy7_sCqrIKuh3pAmXVbTsxV1nkK6fnVWyOaMNwGMSkuY4ln0fFHpkxDo%0D%0ANr1casBU5gPfVLhz4yJQQ7HvTvmkXqXax6F_q4FmtFDhGzYwtPhnJjYxy1cLCgCIz7i3oLXWQ3y-%0D%0AqQ1ycc9BXaRIrZopVjVqdAY2OK6qI8Fg9niprRkoFHPXVZELb_CdDQs96q9eTvxhLEtar2kQ2QHs%0D%0AEqqcUefi1M2Eg8_V-EfWekxhayS_q17f37XoBlZNYQ%0D%0A">Star Wars: Episode IV - A New Hope</a>" on <a href="/offsite/?page-action=offsite-amazon&token=BCYlkWqhCbiDAujI-LbZ2FxajuLs0TYhKt3ecZWZyHyvltCwhVzu-ZBvqujn-wLRiJ3AiNQ07ejc%0D%0A9RHcGU6IXqF262FLMcSgKxQ-cHMChyhBgKJk9Xw87h0sqMXx07FEIwFHYqLYagStmUXRQg_OLvWK%0D%0AYkau6uylcCeENH8QwtEbt7o6m6g5osDOD3fxM8eaWaO1yGORwdS0hXnj5h8GEO1d3uT2xw1IlAf9%0D%0AQVMCB1kO68CjXISjRyVq5KR0WhtFuo92s8fUIua6O1pPUmlFh4ZibsjW-yQvmWwXNX5MdyMt4bJB%0D%0AaWGeJhJ9d8HUIstW6ZYUpJUox0c8QCgsYVN4iqbVZw%0D%0A">Amazon.com</a></p> </div> </div>    </div>



        </span>



            <script type="text/javascript">
                if(typeof uex === 'function'){uex('ld','MessageWidget',{wb:1});}
            </script>





        </div>



	<!-- no content received for slot: btf_rhs1 -->















    <div class="mini-article">
        <div id="ratingWidget">
            <h3>Share this Rating</h3>
            <p>
                Title:
                <strong>Star Wars: Episode IV - A New Hope</strong>
                (1977)
            </p>
            <span class="imdbRatingPlugin imdbRatingStyle1" data-user="" data-title="tt0076759" data-style="t1">
<a href="/title/tt0076759/"
> <img alt="Star Wars: Episode IV - A New Hope (1977) on IMDb"
src="https://m.media-amazon.com/images/G/01/imdb/images/plugins/imdb_46x22-2264473254._CB470047279_.png">
</a>                <span class="rating">8.6<span class="ofTen">/10</span></span>
<img src="https://m.media-amazon.com/images/G/01/imdb/images/plugins/imdb_star_22x21-2889147855._CB483525256_.png" class="star">
            </span>
            <p>Want to share IMDb's rating on your own site? Use the HTML below.</p>
            <div id="ratingPluginHTML" class="hidden">
                <div class="message_box small">
                    <div class="error">
                        <p>
                        You must be a registered user to use the IMDb rating plugin.
                        </p>
                        <a href="/register/login"
class="cboxElement" rel='login'>Login</a>
                    </div>
                </div>
            </div>
            <div id="ratingWidgetLinks">
                <span class="titlePageSprite arrows show"></span>
                <a href="/plugins?titleId=tt0076759"
id="toggleRatingPluginHTML" >Show HTML</a>
                <a href="/plugins?titleId=tt0076759"
>View more styles</a>
            </div>
        </div>
    </div>











<script>
    if (typeof uet == 'function') {
      uet("bb", "TitleMainDetailsRelatedPolls", {wb: 1});
    }
</script>
    <script>
      if ('csm' in window) {
        csm.measure('csm_TitleMainDetailsRelatedPolls_started');
      }
    </script>
<div class="mini-article poll-widget-rhs ">
    <style>
        .mini-article.poll-widget-rhs ul li { margin-bottom: 0.5em; clear: left; font-weight: bold;}
        .mini-article.poll-widget-rhs span { margin-bottom: 0.5em; clear: left;}
        .mini-article.poll-widget-rhs img { float: left; padding: 0 5px 5px 0; height: 86px; width: 86px;}
    </style>
    <h3>User Polls</h3>
    <ul>
        <li>
<a href="/poll/GWkQC0D-5SA/"
><img height="86" width="86" alt="poll image" title="poll image" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/medium/unknown-4203433384._CB470041824_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BYjUyZWZkM2UtMzYxYy00ZmQ3LWFmZTQtOGE2YjBkNjA3YWZlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX86_CR0,0,86,86_.jpg" /></a>        <a href="/poll/GWkQC0D-5SA/"
>RUN-OFF Poll: 100 Greatest Movie Quotes (Part 1)</a>
        <li>
<a href="/poll/JxCKauFA6xw/"
><img height="86" width="86" alt="poll image" title="poll image" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/medium/unknown-4203433384._CB470041824_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BYjBiOTYxZWItMzdiZi00NjlkLWIzZTYtYmFhZjhiMTljOTdkXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX86_CR0,0,86,86_.jpg" /></a>        <a href="/poll/JxCKauFA6xw/"
>AFI Greatest American Films</a>
        <li>
<a href="/poll/JcGZnP7-bGk/"
><img height="86" width="86" alt="poll image" title="poll image" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/medium/unknown-4203433384._CB470041824_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX86_CR0,0,86,86_.jpg" /></a>        <a href="/poll/JcGZnP7-bGk/"
>Classic Movie &quot;Arc&quot; Quotes</a>
        <li>
<a href="/poll/ARZ74FzQf64/"
><img height="86" width="86" alt="poll image" title="poll image" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/medium/unknown-4203433384._CB470041824_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BNjFhMzNhNmMtMjhkYS00YWQyLWJhYWEtMTYxYzdmZjQ4ZDhjXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SX86_CR0,0,86,86_.jpg" /></a>        <a href="/poll/ARZ74FzQf64/"
>Everybody Wants to Rule the World</a>
        <li>
<a href="/poll/ZUAsDCYooEg/"
><img height="86" width="86" alt="poll image" title="poll image" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/medium/unknown-4203433384._CB470041824_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BN2EyZjM3NzUtNWUzMi00MTgxLWI0NTctMzY4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_SX86_CR0,0,86,86_.jpg" /></a>        <a href="/poll/ZUAsDCYooEg/"
>Oscar's Favorite Movie Franchises</a>
        <li>
<a href="/poll/NBaTklgoUzE/"
><img height="86" width="86" alt="poll image" title="poll image" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/medium/unknown-4203433384._CB470041824_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BMTc2Mzg0NjA2N15BMl5BanBnXkFtZTcwOTc5NjQzMw@@._V1_SX86_CR0,0,86,86_.jpg" /></a>        <a href="/poll/NBaTklgoUzE/"
>Weapons Unleashed!</a>
    </ul>
    <div class="see-more"><a href="/poll/"
>See more polls &raquo;</a></div>
</div>
    <script>
      if ('csm' in window) {
        csm.measure('csm_TitleMainDetailsRelatedPolls_finished');
      }
    </script>
<script>
    if (typeof uet == 'function') {
      uet("be", "TitleMainDetailsRelatedPolls", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "TitleMainDetailsRelatedPolls", {wb: 1});
    }
</script>







	<!-- no content received for slot: bottom_rhs -->








	<!-- no content received for slot: btf_rhs2 -->



































































    </div>

    <div id="main_bottom" class="main">



        <a name="slot_center-3"></a>
        <div class="article">






            <script type="text/javascript">if(typeof uet === 'function'){uet('bb','NinjaWidget',{wb:1});}</script>




        <span class="ab_widget">



    <div class="ab_ninja">
<span class="widget_header"> <span class="oneline"> <a href="/imdbpicks/harrison-ford-through-the-years/rg3569654528" > <h3> The Life and Times of Harrison Ford</h3> </a> </span> </span> <p class="blurb">Take a look back at <a href="/name/nm0000148/">Harrison Ford</a>'s movie career in photos.</p> <div class="widget_content no_inline_blurb"> <div class="widget_nested"> <div class="ninja_image_pack"> <div class="ninja_left"> <div class="ninja_image first_image" style="width:201px;height:auto;" > <div style="width:201px;height:auto;margin:0 auto;"> <div class="widget_image"> <div class="image"> <a href="/imdbpicks/harrison-ford-through-the-years/rg3569654528/mediaviewer/rm590527232" > <img class="pri_image" src="https://images-na.ssl-images-amazon.com/images/M/MV5BOTkwNDgwNjUwMV5BMl5BanBnXkFtZTcwODk0MzA4NA@@._CR137,171,778,778_UX402_UY402._SY201_SX201_AL_.jpg" /> </a> </div> </div> </div> </div><div class="ninja_image ninja_image_fixed_padding widget_padding"></div><div class="ninja_image" style="width:201px;height:auto;" > <div style="width:201px;height:auto;margin:0 auto;"> <div class="widget_image"> <div class="image"> <a href="/imdbpicks/harrison-ford-through-the-years/rg3569654528/mediaviewer/rm3553310976" > <img class="pri_image" src="https://images-na.ssl-images-amazon.com/images/M/MV5BMjM3Njc2MjYzNF5BMl5BanBnXkFtZTgwMDQwODAxMTI@._CR184,106,898,898_UX402_UY402._SY201_SX201_AL_.jpg" /> </a> </div> </div> </div> </div><div class="ninja_image ninja_image_fixed_padding widget_padding"></div><div class="ninja_image last_image" style="width:201px;height:auto;" > <div style="width:201px;height:auto;margin:0 auto;"> <div class="widget_image"> <div class="image"> <a href="/imdbpicks/harrison-ford-through-the-years/rg3569654528/mediaviewer/rm2611461888" > <img class="pri_image" src="https://images-na.ssl-images-amazon.com/images/M/MV5BMTkwMzY1MzI4Ml5BMl5BanBnXkFtZTcwOTE3MTU5NQ@@._CR299,195,823,823_UX402_UY402._SY201_SX201_AL_.jpg" /> </a> </div> </div> </div> </div> </div> </div> </div> </div> <p class="seemore"><a href="/imdbpicks/harrison-ford-through-the-years/rg3569654528" class="position_bottom supplemental" > See more Harrison</a></p>    </div>



        </span>



            <script type="text/javascript">
                if(typeof uex === 'function'){uex('ld','NinjaWidget',{wb:1});}
            </script>





        </div>








<script>
    if (typeof uet == 'function') {
      uet("bb", "TitleAwardsWidget", {wb: 1});
    }
</script>
    <script>
      if ('csm' in window) {
        csm.measure('csm_TitleAwardsWidget_started');
      }
    </script>
      <div class="article highlighted" id="titleAwardsRanks">
          <strong>
<a href="/chart/top"
> Top Rated Movies #24
</a>          </strong>
          |

<script>
    if (typeof uet == 'function') {
      uet("bb", "TitleAwardsSummaryWidget", {wb: 1});
    }
</script>
    <script>
      if ('csm' in window) {
        csm.measure('csm_TitleAwardsSummaryWidget_started');
      }
    </script>
    <span class="awards-blurb">
        <b>
            Won
            6
            Oscars.
        </b>
    </span>
    <span class="awards-blurb">
            Another
        52 wins &amp; 28 nominations.
    </span>
            <span class="see-more inline">
<a href="/title/tt0076759/awards"
class="btn-full" >See more awards</a>&nbsp;&raquo;            </span>
    <script>
      if ('csm' in window) {
        csm.measure('csm_TitleAwardsSummaryWidget_finished');
      }
    </script>
<script>
    if (typeof uet == 'function') {
      uet("be", "TitleAwardsSummaryWidget", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "TitleAwardsSummaryWidget", {wb: 1});
    }
</script>
      </div>
    <script>
      if ('csm' in window) {
        csm.measure('csm_TitleAwardsWidget_finished');
      }
    </script>
<script>
    if (typeof uet == 'function') {
      uet("be", "TitleAwardsWidget", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "TitleAwardsWidget", {wb: 1});
    }
</script>




























<script>
    if (typeof uet == 'function') {
      uet("bb", "TitleMediaStripWidget", {wb: 1});
    }
</script>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleMediaStripWidget_started');
    }
  </script>

        <div class="article" id="titleVideoStrip">
            <h2>Videos</h2>
    <div class="mediastrip_big">
                <span class="video_slate">

<a href="/title/tt0076759/videoplayer/vi1317709849"
class="video-modal" data-video="vi1317709849" data-context="imdb" data-rid="BB2A6ADN39XGB92DM688" widget-context="titleMainDetails"><img height="" width="" alt="" title="" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/small/no-video-slate-856072904._CB470041628_.png" class="loadlate hidden video" loadlate="https://m.media-amazon.com/images/M/MV5BMTUzNDY0NjY4Nl5BMl5BanBnXkFtZTgwNjY4MTQ0NzE@._V1_SP330,330,0,C,0,0,0_CR65,90,200,150_PIimdb-blackband-204-14,TopLeft,0,0_PIimdb-blackband-204-28,BottomLeft,0,1_CR0,0,200,150_PIimdb-bluebutton-big,BottomRight,-1,-1_ZATrailer,4,123,16,196,verdenab,8,255,255,255,1_ZAon%2520IMDb,4,1,14,196,verdenab,7,255,255,255,1_ZA02%253A02,164,1,14,36,verdenab,7,255,255,255,1_PIimdb-HDIconMiniWhite,BottomLeft,4,-2_ZAStar%2520Wars,24,138,14,176,arialbd,7,255,255,255,1_.jpg" viconst="vi1317709849" /></a>            </span>
                <span class="video_slate">

<a href="/title/tt0076759/videoplayer/vi3981163545"
class="video-modal" data-video="vi3981163545" data-context="imdb" data-rid="BB2A6ADN39XGB92DM688" widget-context="titleMainDetails"><img height="" width="" alt="" title="" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/small/no-video-slate-856072904._CB470041628_.png" class="loadlate hidden video" loadlate="https://m.media-amazon.com/images/M/MV5BZWI5MGFiNmUtNjBkYS00YzU5LWJjMWUtYTQwZTg4YWEwOThjXkEyXkFqcGdeQWFsZWxvZw@@._V1_SP330,330,0,C,0,0,0_CR65,90,200,150_PIimdb-blackband-204-14,TopLeft,0,0_PIimdb-blackband-204-28,BottomLeft,0,1_CR0,0,200,150_PIimdb-bluebutton-big,BottomRight,-1,-1_ZAClip,4,123,16,196,verdenab,8,255,255,255,1_ZAon%2520IMDb,4,1,14,196,verdenab,7,255,255,255,1_ZA03%253A07,164,1,14,36,verdenab,7,255,255,255,1_PIimdb-HDIconMiniWhite,BottomLeft,4,-2_ZAStar%2520Wars,24,138,14,176,arialbd,7,255,255,255,1_.jpg" viconst="vi3981163545" /></a>            </span>
                <span class="video_slate_last">

<a href="/title/tt0076759/videoplayer/vi2046344217"
class="video-modal" data-video="vi2046344217" data-context="imdb" data-rid="BB2A6ADN39XGB92DM688" widget-context="titleMainDetails"><img height="" width="" alt="" title="" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/small/no-video-slate-856072904._CB470041628_.png" class="loadlate hidden video" loadlate="https://m.media-amazon.com/images/M/MV5BOGI2OGY5MmMtNTYzZS00NWEyLWEwODUtNmVjNDIxM2E1OGZkXkEyXkFqcGdeQWFhcm9uYmVy._V1_SP330,330,0,C,0,0,0_CR65,90,200,150_PIimdb-blackband-204-14,TopLeft,0,0_PIimdb-blackband-204-28,BottomLeft,0,1_CR0,0,200,150_PIimdb-bluebutton-big,BottomRight,-1,-1_ZAClip,4,123,16,196,verdenab,8,255,255,255,1_ZAon%2520IMDb,4,1,14,196,verdenab,7,255,255,255,1_ZA03%253A23,164,1,14,36,verdenab,7,255,255,255,1_PIimdb-HDIconMiniWhite,BottomLeft,4,-2_ZAStar%2520Wars,24,138,14,176,arialbd,7,255,255,255,1_.jpg" viconst="vi2046344217" /></a>            </span>
    </div>
            <div class="combined-see-more see-more">
<a href="/title/tt0076759/videogallery"
> See all 15 videos
</a>&nbsp;&raquo;
            </div>
        </div>
            <div class="article" id="titleImageStrip">
                <h2>Photos</h2>
    <div class="mediastrip">

<a href="/title/tt0076759/mediaviewer/rm2709085696?context=default"
><img height="99" width="99" alt="Carrie Fisher and David Prowse in Star Wars: Episode IV - A New Hope (1977)" title="Carrie Fisher and David Prowse in Star Wars: Episode IV - A New Hope (1977)" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/small/unknown-1394846836._CB470041629_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BMjUyNDE4MTAwOF5BMl5BanBnXkFtZTgwNTgyMzQyNDM@._V1_UX99_CR0,0,99,99_AL_.jpg" /></a>
<a href="/title/tt0076759/mediaviewer/rm2809748992?context=default"
><img height="99" width="99" alt="David Prowse and Leslie Schofield in Star Wars: Episode IV - A New Hope (1977)" title="David Prowse and Leslie Schofield in Star Wars: Episode IV - A New Hope (1977)" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/small/unknown-1394846836._CB470041629_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BMTk3MTkzNTk3Ml5BMl5BanBnXkFtZTgwOTcyMzQyNDM@._V1_UY99_CR15,0,99,99_AL_.jpg" /></a>
<a href="/title/tt0076759/mediaviewer/rm2776194560?context=default"
><img height="99" width="99" alt="Mark Hamill in Star Wars: Episode IV - A New Hope (1977)" title="Mark Hamill in Star Wars: Episode IV - A New Hope (1977)" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/small/unknown-1394846836._CB470041629_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BMjE1NzI5OTAwMl5BMl5BanBnXkFtZTgwMTgyMzQyNDM@._V1_UY99_CR12,0,99,99_AL_.jpg" /></a>
<a href="/title/tt0076759/mediaviewer/rm2927189504?context=default"
><img height="99" width="99" alt="Carrie Fisher in Star Wars: Episode IV - A New Hope (1977)" title="Carrie Fisher in Star Wars: Episode IV - A New Hope (1977)" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/small/unknown-1394846836._CB470041629_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BMTkyODQ3ODE1MF5BMl5BanBnXkFtZTgwODgyMzQyNDM@._V1_UY99_CR37,0,99,99_AL_.jpg" /></a>
<a href="/title/tt0076759/mediaviewer/rm3052172032?context=default"
><img height="99" width="99" alt="Star Wars: Episode IV - A New Hope (1977)" title="Star Wars: Episode IV - A New Hope (1977)" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/small/unknown-1394846836._CB470041629_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BNGIwNDg3MGMtZmY4OS00ODM4LWJjM2YtMGFmZTIwMWUxNDgyXkEyXkFqcGdeQXVyMjk3NTUyOTc@._V1_UY99_CR67,0,99,99_AL_.jpg" /></a>
<a href="/title/tt0076759/mediaviewer/rm3926263808?context=default"
><img height="99" width="99" alt="Mark Hamill in Star Wars: Episode IV - A New Hope (1977)" title="Mark Hamill in Star Wars: Episode IV - A New Hope (1977)" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/small/unknown-1394846836._CB470041629_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BMTg2NDI2MzQzNV5BMl5BanBnXkFtZTgwMjAyNzM3OTE@._V1_UY99_CR13,0,99,99_AL_.jpg" /></a>    </div>
                    <div class="combined-see-more see-more">
<a href="/title/tt0076759/mediaindex"
><span class="titlePageSprite showAllVidsAndPics"></span></a>
<a href="/title/tt0076759/mediaindex"
> See all
482 photos</a>&nbsp;&raquo;                    </div>
            </div>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleMediaStripWidget_finished');
    }
  </script>
<script>
    if (typeof uet == 'function') {
      uet("be", "TitleMediaStripWidget", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "TitleMediaStripWidget", {wb: 1});
    }
</script>







<script>
    if (typeof uet == 'function') {
      uet("bb", "TitleRecsWidget", {wb: 1});
    }
</script>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleRecsWidget_started');
    }
  </script>


                <div class="article" id="titleRecs">
                                 <span class="rightcornerlink">
             <a href="https://help.imdb.com/article/imdb/discover-watch/what-is-the-more-like-this-section/GPE7SPGZREKKY7YN"
>Learn more</a>
             </span>

             <h2 class="rec_heading_wrapper">
                     <span class="rec_heading" data-spec="p13nsims:tt0076759">More Like This&nbsp;</span>
             </h2>

                        <div class="rec_wrapper" id="title_recs"
                            data-items-per-request="24"
                            data-items-per-page="6"
                            data-specs="p13nsims:tt0076759"
                            data-caller-name="p13nsims-title"
                            data-type=sims>

    <div class="rec_const_picker">
        <div class="rec_view">
            <div class="rec_grave" style="display:none"></div>
            <div class="rec_slide">
                        <div class="rec_page">


    <div class="rec_item" data-info="" data-spec="p13nsims:tt0076759" data-tconst="tt0080684">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>
        </div>
<a href="/title/tt0080684/"
><img height="113" width="76" alt="Star Wars: Episode V - The Empire Strikes Back" title="Star Wars: Episode V - The Empire Strikes Back" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/small/film-293970583._CB483525279_.png" class="loadlate hidden rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BYmU1NDRjNDgtMzhiMi00NjZmLTg5NGItZDNiZjU5NTU4OTE0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX76_CR0,0,76,113_AL_.jpg" /> <br/>
</a>    </div>



    <div class="rec_item" data-info="" data-spec="p13nsims:tt0076759" data-tconst="tt0086190">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>
        </div>
<a href="/title/tt0086190/"
><img height="113" width="76" alt="Star Wars: Episode VI - Return of the Jedi" title="Star Wars: Episode VI - Return of the Jedi" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/small/film-293970583._CB483525279_.png" class="loadlate hidden rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BOWZlMjFiYzgtMTUzNC00Y2IzLTk1NTMtZmNhMTczNTk0ODk1XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UX76_CR0,0,76,113_AL_.jpg" /> <br/>
</a>    </div>



    <div class="rec_item" data-info="" data-spec="p13nsims:tt0076759" data-tconst="tt0121766">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>
        </div>
<a href="/title/tt0121766/"
><img height="113" width="76" alt="Star Wars: Episode III - Revenge of the Sith" title="Star Wars: Episode III - Revenge of the Sith" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/small/film-293970583._CB483525279_.png" class="loadlate hidden rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BNTc4MTc3NTQ5OF5BMl5BanBnXkFtZTcwOTg0NjI4NA@@._V1_UY113_CR4,0,76,113_AL_.jpg" /> <br/>
</a>    </div>



    <div class="rec_item" data-info="" data-spec="p13nsims:tt0076759" data-tconst="tt0120915">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>
        </div>
<a href="/title/tt0120915/"
><img height="113" width="76" alt="Star Wars: Episode I - The Phantom Menace" title="Star Wars: Episode I - The Phantom Menace" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/small/film-293970583._CB483525279_.png" class="loadlate hidden rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BYTRhNjcwNWQtMGJmMi00NmQyLWE2YzItODVmMTdjNWI0ZDA2XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UX76_CR0,0,76,113_AL_.jpg" /> <br/>
</a>    </div>



    <div class="rec_item" data-info="" data-spec="p13nsims:tt0076759" data-tconst="tt2488496">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>
        </div>
<a href="/title/tt2488496/"
><img height="113" width="76" alt="Star Wars: Episode VII - The Force Awakens" title="Star Wars: Episode VII - The Force Awakens" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/small/film-293970583._CB483525279_.png" class="loadlate hidden rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BOTAzODEzNDAzMl5BMl5BanBnXkFtZTgwMDU1MTgzNzE@._V1_UY113_CR0,0,76,113_AL_.jpg" /> <br/>
</a>    </div>



    <div class="rec_item" data-info="" data-spec="p13nsims:tt0076759" data-tconst="tt0121765">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>
        </div>
<a href="/title/tt0121765/"
><img height="113" width="76" alt="Star Wars: Episode II - Attack of the Clones" title="Star Wars: Episode II - Attack of the Clones" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/small/film-293970583._CB483525279_.png" class="loadlate hidden rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BMDAzM2M0Y2UtZjRmZi00MzVlLTg4MjEtOTE3NzU5ZDVlMTU5XkEyXkFqcGdeQXVyNDUyOTg3Njg@._V1_UX76_CR0,0,76,113_AL_.jpg" /> <br/>
</a>    </div>

                        </div>
                        <div class="rec_page">


    <div class="rec_item" data-info="" data-spec="p13nsims:tt0076759" data-tconst="tt0167261">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>
        </div>
<a href="/title/tt0167261/"
><img height="113" width="76" alt="The Lord of the Rings: The Two Towers" title="The Lord of the Rings: The Two Towers" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/small/film-293970583._CB483525279_.png" class="loadlate hidden rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BNGE5MzIyNTAtNWFlMC00NDA2LWJiMjItMjc4Yjg1OWM5NzhhXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY113_CR0,0,76,113_AL_.jpg" /> <br/>
</a>    </div>



    <div class="rec_item" data-info="" data-spec="p13nsims:tt0076759" data-tconst="tt0082971">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>
        </div>
<a href="/title/tt0082971/"
><img height="113" width="76" alt="Raiders of the Lost Ark" title="Raiders of the Lost Ark" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/small/film-293970583._CB483525279_.png" class="loadlate hidden rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BMjA0ODEzMTc1Nl5BMl5BanBnXkFtZTcwODM2MjAxNA@@._V1_UX76_CR0,0,76,113_AL_.jpg" /> <br/>
</a>    </div>



    <div class="rec_item" data-info="" data-spec="p13nsims:tt0076759" data-tconst="tt0120737">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>
        </div>
<a href="/title/tt0120737/"
><img height="113" width="76" alt="The Lord of the Rings: The Fellowship of the Ring" title="The Lord of the Rings: The Fellowship of the Ring" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/small/film-293970583._CB483525279_.png" class="loadlate hidden rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BN2EyZjM3NzUtNWUzMi00MTgxLWI0NTctMzY4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_UY113_CR0,0,76,113_AL_.jpg" /> <br/>
</a>    </div>



    <div class="rec_item" data-info="" data-spec="p13nsims:tt0076759" data-tconst="tt3748528">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>
        </div>
<a href="/title/tt3748528/"
><img height="113" width="76" alt="Rogue One" title="Rogue One" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/small/film-293970583._CB483525279_.png" class="loadlate hidden rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BMjEwMzMxODIzOV5BMl5BanBnXkFtZTgwNzg3OTAzMDI@._V1_UY113_CR0,0,76,113_AL_.jpg" /> <br/>
</a>    </div>



    <div class="rec_item" data-info="" data-spec="p13nsims:tt0076759" data-tconst="tt0088763">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>
        </div>
<a href="/title/tt0088763/"
><img height="113" width="76" alt="Back to the Future" title="Back to the Future" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/small/film-293970583._CB483525279_.png" class="loadlate hidden rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BZmU0M2Y1OGUtZjIxNi00ZjBkLTg1MjgtOWIyNThiZWIwYjRiXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX76_CR0,0,76,113_AL_.jpg" /> <br/>
</a>    </div>



    <div class="rec_item" data-info="" data-spec="p13nsims:tt0076759" data-tconst="tt0167260">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>
        </div>
<a href="/title/tt0167260/"
><img height="113" width="76" alt="The Lord of the Rings: The Return of the King" title="The Lord of the Rings: The Return of the King" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/small/film-293970583._CB483525279_.png" class="loadlate hidden rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BNzA5ZDNlZWMtM2NhNS00NDJjLTk4NDItYTRmY2EwMWZlMTY3XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY113_CR0,0,76,113_AL_.jpg" /> <br/>
</a>    </div>

                        </div>
            </div>
            <div class="rec_nav">
                <div class="rec_nav_page_num"></div>
                <a class="rec_nav_left">&#9668; Prev 6</a>
                <a class="rec_nav_right">Next 6 &#9658;</a>
            </div>
        </div>
    </div>

   <div class="rec_overviews">


      <div class="rec_overview" data-tconst="tt0080684">



    <div class="rec_poster" data-info="" data-spec="p13nsims:tt0076759" data-tconst="tt0080684">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>
        </div>
<a href="/title/tt0080684/"
><img height="190" width="128" alt="Star Wars: Episode V - The Empire Strikes Back" title="Star Wars: Episode V - The Empire Strikes Back" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" class="loadlate hidden rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BYmU1NDRjNDgtMzhiMi00NjZmLTg5NGItZDNiZjU5NTU4OTE0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX128_CR0,0,128,190_AL_.jpg" /> <br/>
</a>    </div>


       <div class="rec_actions">

         <div class="rec_action_divider">
           <div class="wlb_classic_wrapper">
             <span class="wlb_wrapper">
               <a class="rec_wlb_watchlist_btn" data-tconst="tt0080684" data-size="medium" data-caller-name="p13nsims-title" data-type="primary" data-tracking-tag="tt_sims_wl"></a>
             </span>
           </div>
         </div>


         <div class="rec_next_btn">
           <span class="btn2_wrapper">
             <a class="rec_next btn2 medium btn2_text_on" title="Show me the next title">
               <span class="btn2_text">Next &raquo;</span>
             </a>
           </span>
         </div>

             <input type="hidden" name="49e6c" value="da29">
       </div>

       <div class="rec_details">
         <div class="rec-info">

           <div class="rec-jaw-upper">

     <div class="rec-title">
       <a href="/title/tt0080684/"
><b>Star Wars: Episode V - The Empire Strikes Back</b></a>
            <span class="nobr">(1980)</span>
   </div>



    <div class="rec-cert-genre rec-elipsis">





                    <span title="Ratings certificate for Star Wars: Episode V - The Empire Strikes Back (1980)"
                          class="us_pg titlePageSprite absmiddle"></span>

                     Action
     <span class="ghost">|</span>
                     Adventure
     <span class="ghost">|</span>
                     Fantasy


    </div>

             <div class="rec-rating">





<div class="rating rating-list" data-starbar-class="rating-list" data-auth="" data-user="" id="tt0080684|imdb|8.7|8.7|p13nsims-title|tt0076759|title|main" data-ga-identifier=""
title="Users rated this 8.7/10 (1,064,986 votes) - click stars to rate" >
<span class="rating-bg">&nbsp;</span>
<span class="rating-imdb " style="width: 121.8px">&nbsp;</span>
<span class="rating-stars">
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>1</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>2</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>3</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>4</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>5</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>6</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>7</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>8</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>9</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>10</span></a>
</span>
<span class="rating-rating "><span class="value">8.7</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel "><a href="/title/tt0080684/vote?v=X;k=" title="Delete" rel="nofollow"><span>X</span></a></span>
&nbsp;</div>

               <div class="rec-outline">
    <p>
    After the Rebels are brutally overpowered by the Empire on the ice planet Hoth, Luke Skywalker begins Jedi training with Yoda, while his friends are pursued by Darth Vader.    </p>
               </div>

             </div>

           </div>

           <div class="rec-jaw-lower">
             <div class="rec-jaw-teeth"></div>
 <div class="rec-director rec-ellipsis">
      <b>Director:</b>
Irvin Kershner  </div>
<div class="rec-actor rec-ellipsis"> <span>
    <b>Stars:</b>
Mark Hamill,
Harrison Ford,
Carrie Fisher</span></div>
           </div>

         </div>
       </div>

      </div>


      <div class="rec_overview" data-tconst="tt0086190">



    <div class="rec_poster" data-info="" data-spec="p13nsims:tt0076759" data-tconst="tt0086190">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>
        </div>
<a href="/title/tt0086190/"
><img height="190" width="128" alt="Star Wars: Episode VI - Return of the Jedi" title="Star Wars: Episode VI - Return of the Jedi" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" class="loadlate hidden rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BOWZlMjFiYzgtMTUzNC00Y2IzLTk1NTMtZmNhMTczNTk0ODk1XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UX128_CR0,0,128,190_AL_.jpg" /> <br/>
</a>    </div>


       <div class="rec_actions">

         <div class="rec_action_divider">
           <div class="wlb_classic_wrapper">
             <span class="wlb_wrapper">
               <a class="rec_wlb_watchlist_btn" data-tconst="tt0086190" data-size="medium" data-caller-name="p13nsims-title" data-type="primary" data-tracking-tag="tt_sims_wl"></a>
             </span>
           </div>
         </div>


         <div class="rec_next_btn">
           <span class="btn2_wrapper">
             <a class="rec_next btn2 medium btn2_text_on" title="Show me the next title">
               <span class="btn2_text">Next &raquo;</span>
             </a>
           </span>
         </div>

             <input type="hidden" name="49e6c" value="da29">
       </div>

       <div class="rec_details">
         <div class="rec-info">

           <div class="rec-jaw-upper">

     <div class="rec-title">
       <a href="/title/tt0086190/"
><b>Star Wars: Episode VI - Return of the Jedi</b></a>
            <span class="nobr">(1983)</span>
   </div>



    <div class="rec-cert-genre rec-elipsis">





                    <span title="Ratings certificate for Star Wars: Episode VI - Return of the Jedi (1983)"
                          class="us_pg titlePageSprite absmiddle"></span>

                     Action
     <span class="ghost">|</span>
                     Adventure
     <span class="ghost">|</span>
                     Fantasy


    </div>

             <div class="rec-rating">





<div class="rating rating-list" data-starbar-class="rating-list" data-auth="" data-user="" id="tt0086190|imdb|8.3|8.3|p13nsims-title|tt0076759|title|main" data-ga-identifier=""
title="Users rated this 8.3/10 (871,893 votes) - click stars to rate" >
<span class="rating-bg">&nbsp;</span>
<span class="rating-imdb " style="width: 116.2px">&nbsp;</span>
<span class="rating-stars">
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>1</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>2</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>3</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>4</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>5</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>6</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>7</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>8</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>9</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>10</span></a>
</span>
<span class="rating-rating "><span class="value">8.3</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel "><a href="/title/tt0086190/vote?v=X;k=" title="Delete" rel="nofollow"><span>X</span></a></span>
&nbsp;</div>

               <div class="rec-outline">
    <p>
    After a daring mission to rescue Han Solo from Jabba the Hutt, the Rebels dispatch to Endor to destroy the second Death Star. Meanwhile, Luke struggles to help Darth Vader back from the dark side without falling into the Emperor's trap.    </p>
               </div>

             </div>

           </div>

           <div class="rec-jaw-lower">
             <div class="rec-jaw-teeth"></div>
 <div class="rec-director rec-ellipsis">
      <b>Director:</b>
Richard Marquand  </div>
<div class="rec-actor rec-ellipsis"> <span>
    <b>Stars:</b>
Mark Hamill,
Harrison Ford,
Carrie Fisher</span></div>
           </div>

         </div>
       </div>

      </div>


      <div class="rec_overview" data-tconst="tt0121766">



    <div class="rec_poster" data-info="" data-spec="p13nsims:tt0076759" data-tconst="tt0121766">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>
        </div>
<a href="/title/tt0121766/"
><img height="190" width="128" alt="Star Wars: Episode III - Revenge of the Sith" title="Star Wars: Episode III - Revenge of the Sith" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" class="loadlate hidden rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BNTc4MTc3NTQ5OF5BMl5BanBnXkFtZTcwOTg0NjI4NA@@._V1_UY190_CR7,0,128,190_AL_.jpg" /> <br/>
</a>    </div>


       <div class="rec_actions">

         <div class="rec_action_divider">
           <div class="wlb_classic_wrapper">
             <span class="wlb_wrapper">
               <a class="rec_wlb_watchlist_btn" data-tconst="tt0121766" data-size="medium" data-caller-name="p13nsims-title" data-type="primary" data-tracking-tag="tt_sims_wl"></a>
             </span>
           </div>
         </div>


         <div class="rec_next_btn">
           <span class="btn2_wrapper">
             <a class="rec_next btn2 medium btn2_text_on" title="Show me the next title">
               <span class="btn2_text">Next &raquo;</span>
             </a>
           </span>
         </div>

             <input type="hidden" name="49e6c" value="da29">
       </div>

       <div class="rec_details">
         <div class="rec-info">

           <div class="rec-jaw-upper">

     <div class="rec-title">
       <a href="/title/tt0121766/"
><b>Star Wars: Episode III - Revenge of the Sith</b></a>
            <span class="nobr">(2005)</span>
   </div>



    <div class="rec-cert-genre rec-elipsis">





                    <span title="Ratings certificate for Star Wars: Episode III - Revenge of the Sith (2005)"
                          class="us_pg_13 titlePageSprite absmiddle"></span>

                     Action
     <span class="ghost">|</span>
                     Adventure
     <span class="ghost">|</span>
                     Fantasy


    </div>

             <div class="rec-rating">





<div class="rating rating-list" data-starbar-class="rating-list" data-auth="" data-user="" id="tt0121766|imdb|7.5|7.5|p13nsims-title|tt0076759|title|main" data-ga-identifier=""
title="Users rated this 7.5/10 (647,232 votes) - click stars to rate" >
<span class="rating-bg">&nbsp;</span>
<span class="rating-imdb " style="width: 105px">&nbsp;</span>
<span class="rating-stars">
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>1</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>2</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>3</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>4</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>5</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>6</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>7</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>8</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>9</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>10</span></a>
</span>
<span class="rating-rating "><span class="value">7.5</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel "><a href="/title/tt0121766/vote?v=X;k=" title="Delete" rel="nofollow"><span>X</span></a></span>
&nbsp;</div>

               <div class="rec-outline">
    <p>
    Three years into the Clone Wars, the Jedi rescue Palpatine from Count Dooku. As Obi-Wan pursues a new threat, Anakin acts as a double agent between the Jedi Council and Palpatine and is lured into a sinister plan to rule the galaxy.    </p>
               </div>

             </div>

           </div>

           <div class="rec-jaw-lower">
             <div class="rec-jaw-teeth"></div>
 <div class="rec-director rec-ellipsis">
      <b>Director:</b>
George Lucas  </div>
<div class="rec-actor rec-ellipsis"> <span>
    <b>Stars:</b>
Hayden Christensen,
Natalie Portman,
Ewan McGregor</span></div>
           </div>

         </div>
       </div>

      </div>


      <div class="rec_overview" data-tconst="tt0120915">



    <div class="rec_poster" data-info="" data-spec="p13nsims:tt0076759" data-tconst="tt0120915">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>
        </div>
<a href="/title/tt0120915/"
><img height="190" width="128" alt="Star Wars: Episode I - The Phantom Menace" title="Star Wars: Episode I - The Phantom Menace" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" class="loadlate hidden rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BYTRhNjcwNWQtMGJmMi00NmQyLWE2YzItODVmMTdjNWI0ZDA2XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UX128_CR0,0,128,190_AL_.jpg" /> <br/>
</a>    </div>


       <div class="rec_actions">

         <div class="rec_action_divider">
           <div class="wlb_classic_wrapper">
             <span class="wlb_wrapper">
               <a class="rec_wlb_watchlist_btn" data-tconst="tt0120915" data-size="medium" data-caller-name="p13nsims-title" data-type="primary" data-tracking-tag="tt_sims_wl"></a>
             </span>
           </div>
         </div>


         <div class="rec_next_btn">
           <span class="btn2_wrapper">
             <a class="rec_next btn2 medium btn2_text_on" title="Show me the next title">
               <span class="btn2_text">Next &raquo;</span>
             </a>
           </span>
         </div>

             <input type="hidden" name="49e6c" value="da29">
       </div>

       <div class="rec_details">
         <div class="rec-info">

           <div class="rec-jaw-upper">

     <div class="rec-title">
       <a href="/title/tt0120915/"
><b>Star Wars: Episode I - The Phantom Menace</b></a>
            <span class="nobr">(1999)</span>
   </div>



    <div class="rec-cert-genre rec-elipsis">





                    <span title="Ratings certificate for Star Wars: Episode I - The Phantom Menace (1999)"
                          class="us_pg titlePageSprite absmiddle"></span>

                     Action
     <span class="ghost">|</span>
                     Adventure
     <span class="ghost">|</span>
                     Fantasy


    </div>

             <div class="rec-rating">





<div class="rating rating-list" data-starbar-class="rating-list" data-auth="" data-user="" id="tt0120915|imdb|6.5|6.5|p13nsims-title|tt0076759|title|main" data-ga-identifier=""
title="Users rated this 6.5/10 (660,949 votes) - click stars to rate" >
<span class="rating-bg">&nbsp;</span>
<span class="rating-imdb " style="width: 91px">&nbsp;</span>
<span class="rating-stars">
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>1</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>2</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>3</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>4</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>5</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>6</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>7</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>8</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>9</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>10</span></a>
</span>
<span class="rating-rating "><span class="value">6.5</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel "><a href="/title/tt0120915/vote?v=X;k=" title="Delete" rel="nofollow"><span>X</span></a></span>
&nbsp;</div>

               <div class="rec-outline">
    <p>
    Two Jedi escape a hostile blockade to find allies and come across a young boy who may bring balance to the Force, but the long dormant Sith resurface to claim their old glory.    </p>
               </div>

             </div>

           </div>

           <div class="rec-jaw-lower">
             <div class="rec-jaw-teeth"></div>
 <div class="rec-director rec-ellipsis">
      <b>Director:</b>
George Lucas  </div>
<div class="rec-actor rec-ellipsis"> <span>
    <b>Stars:</b>
Ewan McGregor,
Liam Neeson,
Natalie Portman</span></div>
           </div>

         </div>
       </div>

      </div>


      <div class="rec_overview" data-tconst="tt2488496">



    <div class="rec_poster" data-info="" data-spec="p13nsims:tt0076759" data-tconst="tt2488496">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>
        </div>
<a href="/title/tt2488496/"
><img height="190" width="128" alt="Star Wars: Episode VII - The Force Awakens" title="Star Wars: Episode VII - The Force Awakens" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" class="loadlate hidden rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BOTAzODEzNDAzMl5BMl5BanBnXkFtZTgwMDU1MTgzNzE@._V1_UY190_CR0,0,128,190_AL_.jpg" /> <br/>
</a>    </div>


       <div class="rec_actions">

         <div class="rec_action_divider">
           <div class="wlb_classic_wrapper">
             <span class="wlb_wrapper">
               <a class="rec_wlb_watchlist_btn" data-tconst="tt2488496" data-size="medium" data-caller-name="p13nsims-title" data-type="primary" data-tracking-tag="tt_sims_wl"></a>
             </span>
           </div>
         </div>


         <div class="rec_next_btn">
           <span class="btn2_wrapper">
             <a class="rec_next btn2 medium btn2_text_on" title="Show me the next title">
               <span class="btn2_text">Next &raquo;</span>
             </a>
           </span>
         </div>

             <input type="hidden" name="49e6c" value="da29">
       </div>

       <div class="rec_details">
         <div class="rec-info">

           <div class="rec-jaw-upper">

     <div class="rec-title">
       <a href="/title/tt2488496/"
><b>Star Wars: Episode VII - The Force Awakens</b></a>
            <span class="nobr">(2015)</span>
   </div>



    <div class="rec-cert-genre rec-elipsis">





                    <span title="Ratings certificate for Star Wars: Episode VII - The Force Awakens (2015)"
                          class="us_pg_13 titlePageSprite absmiddle"></span>

                     Action
     <span class="ghost">|</span>
                     Adventure
     <span class="ghost">|</span>
                     Sci-Fi


    </div>

             <div class="rec-rating">





<div class="rating rating-list" data-starbar-class="rating-list" data-auth="" data-user="" id="tt2488496|imdb|8|8|p13nsims-title|tt0076759|title|main" data-ga-identifier=""
title="Users rated this 8/10 (791,727 votes) - click stars to rate" >
<span class="rating-bg">&nbsp;</span>
<span class="rating-imdb " style="width: 112px">&nbsp;</span>
<span class="rating-stars">
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>1</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>2</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>3</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>4</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>5</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>6</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>7</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>8</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>9</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>10</span></a>
</span>
<span class="rating-rating "><span class="value">8</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel "><a href="/title/tt2488496/vote?v=X;k=" title="Delete" rel="nofollow"><span>X</span></a></span>
&nbsp;</div>

               <div class="rec-outline">
    <p>
    Three decades after the Empire's defeat, a new threat arises in the militant First Order. Defected stormtrooper Finn and the scavenger Rey are caught up in the Resistance's search for the missing Luke Skywalker.    </p>
               </div>

             </div>

           </div>

           <div class="rec-jaw-lower">
             <div class="rec-jaw-teeth"></div>
 <div class="rec-director rec-ellipsis">
      <b>Director:</b>
J.J. Abrams  </div>
<div class="rec-actor rec-ellipsis"> <span>
    <b>Stars:</b>
Daisy Ridley,
John Boyega,
Oscar Isaac</span></div>
           </div>

         </div>
       </div>

      </div>


      <div class="rec_overview" data-tconst="tt0121765">



    <div class="rec_poster" data-info="" data-spec="p13nsims:tt0076759" data-tconst="tt0121765">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>
        </div>
<a href="/title/tt0121765/"
><img height="190" width="128" alt="Star Wars: Episode II - Attack of the Clones" title="Star Wars: Episode II - Attack of the Clones" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" class="loadlate hidden rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BMDAzM2M0Y2UtZjRmZi00MzVlLTg4MjEtOTE3NzU5ZDVlMTU5XkEyXkFqcGdeQXVyNDUyOTg3Njg@._V1_UX128_CR0,0,128,190_AL_.jpg" /> <br/>
</a>    </div>


       <div class="rec_actions">

         <div class="rec_action_divider">
           <div class="wlb_classic_wrapper">
             <span class="wlb_wrapper">
               <a class="rec_wlb_watchlist_btn" data-tconst="tt0121765" data-size="medium" data-caller-name="p13nsims-title" data-type="primary" data-tracking-tag="tt_sims_wl"></a>
             </span>
           </div>
         </div>


         <div class="rec_next_btn">
           <span class="btn2_wrapper">
             <a class="rec_next btn2 medium btn2_text_on" title="Show me the next title">
               <span class="btn2_text">Next &raquo;</span>
             </a>
           </span>
         </div>

             <input type="hidden" name="49e6c" value="da29">
       </div>

       <div class="rec_details">
         <div class="rec-info">

           <div class="rec-jaw-upper">

     <div class="rec-title">
       <a href="/title/tt0121765/"
><b>Star Wars: Episode II - Attack of the Clones</b></a>
            <span class="nobr">(2002)</span>
   </div>



    <div class="rec-cert-genre rec-elipsis">





                    <span title="Ratings certificate for Star Wars: Episode II - Attack of the Clones (2002)"
                          class="us_pg titlePageSprite absmiddle"></span>

                     Action
     <span class="ghost">|</span>
                     Adventure
     <span class="ghost">|</span>
                     Fantasy


    </div>

             <div class="rec-rating">





<div class="rating rating-list" data-starbar-class="rating-list" data-auth="" data-user="" id="tt0121765|imdb|6.6|6.6|p13nsims-title|tt0076759|title|main" data-ga-identifier=""
title="Users rated this 6.6/10 (581,299 votes) - click stars to rate" >
<span class="rating-bg">&nbsp;</span>
<span class="rating-imdb " style="width: 92.4px">&nbsp;</span>
<span class="rating-stars">
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>1</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>2</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>3</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>4</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>5</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>6</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>7</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>8</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>9</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>10</span></a>
</span>
<span class="rating-rating "><span class="value">6.6</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel "><a href="/title/tt0121765/vote?v=X;k=" title="Delete" rel="nofollow"><span>X</span></a></span>
&nbsp;</div>

               <div class="rec-outline">
    <p>
    Ten years after initially meeting, Anakin Skywalker shares a forbidden romance with Padmé Amidala, while Obi-Wan Kenobi investigates an assassination attempt on the senator and discovers a secret clone army crafted for the Jedi.    </p>
               </div>

             </div>

           </div>

           <div class="rec-jaw-lower">
             <div class="rec-jaw-teeth"></div>
 <div class="rec-director rec-ellipsis">
      <b>Director:</b>
George Lucas  </div>
<div class="rec-actor rec-ellipsis"> <span>
    <b>Stars:</b>
Hayden Christensen,
Natalie Portman,
Ewan McGregor</span></div>
           </div>

         </div>
       </div>

      </div>


      <div class="rec_overview" data-tconst="tt0167261">



    <div class="rec_poster" data-info="" data-spec="p13nsims:tt0076759" data-tconst="tt0167261">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>
        </div>
<a href="/title/tt0167261/"
><img height="190" width="128" alt="The Lord of the Rings: The Two Towers" title="The Lord of the Rings: The Two Towers" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" class="loadlate hidden rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BNGE5MzIyNTAtNWFlMC00NDA2LWJiMjItMjc4Yjg1OWM5NzhhXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY190_CR1,0,128,190_AL_.jpg" /> <br/>
</a>    </div>


       <div class="rec_actions">

         <div class="rec_action_divider">
           <div class="wlb_classic_wrapper">
             <span class="wlb_wrapper">
               <a class="rec_wlb_watchlist_btn" data-tconst="tt0167261" data-size="medium" data-caller-name="p13nsims-title" data-type="primary" data-tracking-tag="tt_sims_wl"></a>
             </span>
           </div>
         </div>


         <div class="rec_next_btn">
           <span class="btn2_wrapper">
             <a class="rec_next btn2 medium btn2_text_on" title="Show me the next title">
               <span class="btn2_text">Next &raquo;</span>
             </a>
           </span>
         </div>

             <input type="hidden" name="49e6c" value="da29">
       </div>

       <div class="rec_details">
         <div class="rec-info">

           <div class="rec-jaw-upper">

     <div class="rec-title">
       <a href="/title/tt0167261/"
><b>The Lord of the Rings: The Two Towers</b></a>
            <span class="nobr">(2002)</span>
   </div>



    <div class="rec-cert-genre rec-elipsis">





                    <span title="Ratings certificate for The Lord of the Rings: The Two Towers (2002)"
                          class="us_pg titlePageSprite absmiddle"></span>

                     Adventure
     <span class="ghost">|</span>
                     Drama
     <span class="ghost">|</span>
                     Fantasy


    </div>

             <div class="rec-rating">





<div class="rating rating-list" data-starbar-class="rating-list" data-auth="" data-user="" id="tt0167261|imdb|8.7|8.7|p13nsims-title|tt0076759|title|main" data-ga-identifier=""
title="Users rated this 8.7/10 (1,368,520 votes) - click stars to rate" >
<span class="rating-bg">&nbsp;</span>
<span class="rating-imdb " style="width: 121.8px">&nbsp;</span>
<span class="rating-stars">
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>1</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>2</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>3</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>4</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>5</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>6</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>7</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>8</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>9</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>10</span></a>
</span>
<span class="rating-rating "><span class="value">8.7</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel "><a href="/title/tt0167261/vote?v=X;k=" title="Delete" rel="nofollow"><span>X</span></a></span>
&nbsp;</div>

               <div class="rec-outline">
    <p>
    While Frodo and Sam edge closer to Mordor with the help of the shifty Gollum, the divided fellowship makes a stand against Sauron's new ally, Saruman, and his hordes of Isengard.    </p>
               </div>

             </div>

           </div>

           <div class="rec-jaw-lower">
             <div class="rec-jaw-teeth"></div>
 <div class="rec-director rec-ellipsis">
      <b>Director:</b>
Peter Jackson  </div>
<div class="rec-actor rec-ellipsis"> <span>
    <b>Stars:</b>
Elijah Wood,
Ian McKellen,
Viggo Mortensen</span></div>
           </div>

         </div>
       </div>

      </div>


      <div class="rec_overview" data-tconst="tt0082971">



    <div class="rec_poster" data-info="" data-spec="p13nsims:tt0076759" data-tconst="tt0082971">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>
        </div>
<a href="/title/tt0082971/"
><img height="190" width="128" alt="Raiders of the Lost Ark" title="Raiders of the Lost Ark" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" class="loadlate hidden rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BMjA0ODEzMTc1Nl5BMl5BanBnXkFtZTcwODM2MjAxNA@@._V1_UX128_CR0,0,128,190_AL_.jpg" /> <br/>
</a>    </div>


       <div class="rec_actions">

         <div class="rec_action_divider">
           <div class="wlb_classic_wrapper">
             <span class="wlb_wrapper">
               <a class="rec_wlb_watchlist_btn" data-tconst="tt0082971" data-size="medium" data-caller-name="p13nsims-title" data-type="primary" data-tracking-tag="tt_sims_wl"></a>
             </span>
           </div>
         </div>


         <div class="rec_next_btn">
           <span class="btn2_wrapper">
             <a class="rec_next btn2 medium btn2_text_on" title="Show me the next title">
               <span class="btn2_text">Next &raquo;</span>
             </a>
           </span>
         </div>

             <input type="hidden" name="49e6c" value="da29">
       </div>

       <div class="rec_details">
         <div class="rec-info">

           <div class="rec-jaw-upper">

     <div class="rec-title">
       <a href="/title/tt0082971/"
><b>Raiders of the Lost Ark</b></a>
            <span class="nobr">(1981)</span>
   </div>



    <div class="rec-cert-genre rec-elipsis">





                    <span title="Ratings certificate for Raiders of the Lost Ark (1981)"
                          class="us_pg titlePageSprite absmiddle"></span>

                     Action
     <span class="ghost">|</span>
                     Adventure



    </div>

             <div class="rec-rating">





<div class="rating rating-list" data-starbar-class="rating-list" data-auth="" data-user="" id="tt0082971|imdb|8.4|8.4|p13nsims-title|tt0076759|title|main" data-ga-identifier=""
title="Users rated this 8.4/10 (822,593 votes) - click stars to rate" >
<span class="rating-bg">&nbsp;</span>
<span class="rating-imdb " style="width: 117.6px">&nbsp;</span>
<span class="rating-stars">
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>1</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>2</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>3</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>4</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>5</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>6</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>7</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>8</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>9</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>10</span></a>
</span>
<span class="rating-rating "><span class="value">8.4</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel "><a href="/title/tt0082971/vote?v=X;k=" title="Delete" rel="nofollow"><span>X</span></a></span>
&nbsp;</div>

               <div class="rec-outline">
    <p>
    In 1936, archaeologist and adventurer Indiana Jones is hired by the U.S. government to find the Ark of the Covenant before <a href="/name/nm0386944">Adolf Hitler</a>'s Nazis can obtain its awesome powers.    </p>
               </div>

             </div>

           </div>

           <div class="rec-jaw-lower">
             <div class="rec-jaw-teeth"></div>
 <div class="rec-director rec-ellipsis">
      <b>Director:</b>
Steven Spielberg  </div>
<div class="rec-actor rec-ellipsis"> <span>
    <b>Stars:</b>
Harrison Ford,
Karen Allen,
Paul Freeman</span></div>
           </div>

         </div>
       </div>

      </div>


      <div class="rec_overview" data-tconst="tt0120737">



    <div class="rec_poster" data-info="" data-spec="p13nsims:tt0076759" data-tconst="tt0120737">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>
        </div>
<a href="/title/tt0120737/"
><img height="190" width="128" alt="The Lord of the Rings: The Fellowship of the Ring" title="The Lord of the Rings: The Fellowship of the Ring" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" class="loadlate hidden rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BN2EyZjM3NzUtNWUzMi00MTgxLWI0NTctMzY4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_UY190_CR0,0,128,190_AL_.jpg" /> <br/>
</a>    </div>


       <div class="rec_actions">

         <div class="rec_action_divider">
           <div class="wlb_classic_wrapper">
             <span class="wlb_wrapper">
               <a class="rec_wlb_watchlist_btn" data-tconst="tt0120737" data-size="medium" data-caller-name="p13nsims-title" data-type="primary" data-tracking-tag="tt_sims_wl"></a>
             </span>
           </div>
         </div>


         <div class="rec_next_btn">
           <span class="btn2_wrapper">
             <a class="rec_next btn2 medium btn2_text_on" title="Show me the next title">
               <span class="btn2_text">Next &raquo;</span>
             </a>
           </span>
         </div>

             <input type="hidden" name="49e6c" value="da29">
       </div>

       <div class="rec_details">
         <div class="rec-info">

           <div class="rec-jaw-upper">

     <div class="rec-title">
       <a href="/title/tt0120737/"
><b>The Lord of the Rings: The Fellowship of the Ring</b></a>
            <span class="nobr">(2001)</span>
   </div>



    <div class="rec-cert-genre rec-elipsis">





                    <span title="Ratings certificate for The Lord of the Rings: The Fellowship of the Ring (2001)"
                          class="us_pg_13 titlePageSprite absmiddle"></span>

                     Adventure
     <span class="ghost">|</span>
                     Drama
     <span class="ghost">|</span>
                     Fantasy


    </div>

             <div class="rec-rating">





<div class="rating rating-list" data-starbar-class="rating-list" data-auth="" data-user="" id="tt0120737|imdb|8.8|8.8|p13nsims-title|tt0076759|title|main" data-ga-identifier=""
title="Users rated this 8.8/10 (1,528,739 votes) - click stars to rate" >
<span class="rating-bg">&nbsp;</span>
<span class="rating-imdb " style="width: 123.2px">&nbsp;</span>
<span class="rating-stars">
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>1</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>2</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>3</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>4</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>5</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>6</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>7</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>8</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>9</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>10</span></a>
</span>
<span class="rating-rating "><span class="value">8.8</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel "><a href="/title/tt0120737/vote?v=X;k=" title="Delete" rel="nofollow"><span>X</span></a></span>
&nbsp;</div>

               <div class="rec-outline">
    <p>
    A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.    </p>
               </div>

             </div>

           </div>

           <div class="rec-jaw-lower">
             <div class="rec-jaw-teeth"></div>
 <div class="rec-director rec-ellipsis">
      <b>Director:</b>
Peter Jackson  </div>
<div class="rec-actor rec-ellipsis"> <span>
    <b>Stars:</b>
Elijah Wood,
Ian McKellen,
Orlando Bloom</span></div>
           </div>

         </div>
       </div>

      </div>


      <div class="rec_overview" data-tconst="tt3748528">



    <div class="rec_poster" data-info="" data-spec="p13nsims:tt0076759" data-tconst="tt3748528">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>
        </div>
<a href="/title/tt3748528/"
><img height="190" width="128" alt="Rogue One" title="Rogue One" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" class="loadlate hidden rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BMjEwMzMxODIzOV5BMl5BanBnXkFtZTgwNzg3OTAzMDI@._V1_UY190_CR0,0,128,190_AL_.jpg" /> <br/>
</a>    </div>


       <div class="rec_actions">

         <div class="rec_action_divider">
           <div class="wlb_classic_wrapper">
             <span class="wlb_wrapper">
               <a class="rec_wlb_watchlist_btn" data-tconst="tt3748528" data-size="medium" data-caller-name="p13nsims-title" data-type="primary" data-tracking-tag="tt_sims_wl"></a>
             </span>
           </div>
         </div>


         <div class="rec_next_btn">
           <span class="btn2_wrapper">
             <a class="rec_next btn2 medium btn2_text_on" title="Show me the next title">
               <span class="btn2_text">Next &raquo;</span>
             </a>
           </span>
         </div>

             <input type="hidden" name="49e6c" value="da29">
       </div>

       <div class="rec_details">
         <div class="rec-info">

           <div class="rec-jaw-upper">

     <div class="rec-title">
       <a href="/title/tt3748528/"
><b>Rogue One</b></a>
            <span class="nobr">(2016)</span>
   </div>



    <div class="rec-cert-genre rec-elipsis">





                    <span title="Ratings certificate for Rogue One (2016)"
                          class="us_pg_13 titlePageSprite absmiddle"></span>

                     Action
     <span class="ghost">|</span>
                     Adventure
     <span class="ghost">|</span>
                     Sci-Fi


    </div>

             <div class="rec-rating">





<div class="rating rating-list" data-starbar-class="rating-list" data-auth="" data-user="" id="tt3748528|imdb|7.8|7.8|p13nsims-title|tt0076759|title|main" data-ga-identifier=""
title="Users rated this 7.8/10 (485,985 votes) - click stars to rate" >
<span class="rating-bg">&nbsp;</span>
<span class="rating-imdb " style="width: 109.2px">&nbsp;</span>
<span class="rating-stars">
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>1</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>2</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>3</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>4</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>5</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>6</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>7</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>8</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>9</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>10</span></a>
</span>
<span class="rating-rating "><span class="value">7.8</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel "><a href="/title/tt3748528/vote?v=X;k=" title="Delete" rel="nofollow"><span>X</span></a></span>
&nbsp;</div>

               <div class="rec-outline">
    <p>
    The daughter of an Imperial scientist joins the Rebel Alliance in a risky move to steal the Death Star plans.    </p>
               </div>

             </div>

           </div>

           <div class="rec-jaw-lower">
             <div class="rec-jaw-teeth"></div>
 <div class="rec-director rec-ellipsis">
      <b>Director:</b>
Gareth Edwards  </div>
<div class="rec-actor rec-ellipsis"> <span>
    <b>Stars:</b>
Felicity Jones,
Diego Luna,
Alan Tudyk</span></div>
           </div>

         </div>
       </div>

      </div>


      <div class="rec_overview" data-tconst="tt0088763">



    <div class="rec_poster" data-info="" data-spec="p13nsims:tt0076759" data-tconst="tt0088763">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>
        </div>
<a href="/title/tt0088763/"
><img height="190" width="128" alt="Back to the Future" title="Back to the Future" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" class="loadlate hidden rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BZmU0M2Y1OGUtZjIxNi00ZjBkLTg1MjgtOWIyNThiZWIwYjRiXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX128_CR0,0,128,190_AL_.jpg" /> <br/>
</a>    </div>


       <div class="rec_actions">

         <div class="rec_action_divider">
           <div class="wlb_classic_wrapper">
             <span class="wlb_wrapper">
               <a class="rec_wlb_watchlist_btn" data-tconst="tt0088763" data-size="medium" data-caller-name="p13nsims-title" data-type="primary" data-tracking-tag="tt_sims_wl"></a>
             </span>
           </div>
         </div>


         <div class="rec_next_btn">
           <span class="btn2_wrapper">
             <a class="rec_next btn2 medium btn2_text_on" title="Show me the next title">
               <span class="btn2_text">Next &raquo;</span>
             </a>
           </span>
         </div>

             <input type="hidden" name="49e6c" value="da29">
       </div>

       <div class="rec_details">
         <div class="rec-info">

           <div class="rec-jaw-upper">

     <div class="rec-title">
       <a href="/title/tt0088763/"
><b>Back to the Future</b></a>
            <span class="nobr">(1985)</span>
   </div>



    <div class="rec-cert-genre rec-elipsis">





                    <span title="Ratings certificate for Back to the Future (1985)"
                          class="us_pg titlePageSprite absmiddle"></span>

                     Adventure
     <span class="ghost">|</span>
                     Comedy
     <span class="ghost">|</span>
                     Sci-Fi


    </div>

             <div class="rec-rating">





<div class="rating rating-list" data-starbar-class="rating-list" data-auth="" data-user="" id="tt0088763|imdb|8.5|8.5|p13nsims-title|tt0076759|title|main" data-ga-identifier=""
title="Users rated this 8.5/10 (950,803 votes) - click stars to rate" >
<span class="rating-bg">&nbsp;</span>
<span class="rating-imdb " style="width: 119px">&nbsp;</span>
<span class="rating-stars">
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>1</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>2</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>3</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>4</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>5</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>6</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>7</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>8</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>9</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>10</span></a>
</span>
<span class="rating-rating "><span class="value">8.5</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel "><a href="/title/tt0088763/vote?v=X;k=" title="Delete" rel="nofollow"><span>X</span></a></span>
&nbsp;</div>

               <div class="rec-outline">
    <p>
    Marty McFly, a 17-year-old high school student, is accidentally sent thirty years into the past in a time-traveling DeLorean invented by his close friend, the maverick scientist Doc Brown.    </p>
               </div>

             </div>

           </div>

           <div class="rec-jaw-lower">
             <div class="rec-jaw-teeth"></div>
 <div class="rec-director rec-ellipsis">
      <b>Director:</b>
Robert Zemeckis  </div>
<div class="rec-actor rec-ellipsis"> <span>
    <b>Stars:</b>
Michael J. Fox,
Christopher Lloyd,
Lea Thompson</span></div>
           </div>

         </div>
       </div>

      </div>


      <div class="rec_overview" data-tconst="tt0167260">



    <div class="rec_poster" data-info="" data-spec="p13nsims:tt0076759" data-tconst="tt0167260">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>
        </div>
<a href="/title/tt0167260/"
><img height="190" width="128" alt="The Lord of the Rings: The Return of the King" title="The Lord of the Rings: The Return of the King" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" class="loadlate hidden rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BNzA5ZDNlZWMtM2NhNS00NDJjLTk4NDItYTRmY2EwMWZlMTY3XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY190_CR0,0,128,190_AL_.jpg" /> <br/>
</a>    </div>


       <div class="rec_actions">

         <div class="rec_action_divider">
           <div class="wlb_classic_wrapper">
             <span class="wlb_wrapper">
               <a class="rec_wlb_watchlist_btn" data-tconst="tt0167260" data-size="medium" data-caller-name="p13nsims-title" data-type="primary" data-tracking-tag="tt_sims_wl"></a>
             </span>
           </div>
         </div>


         <div class="rec_next_btn">
           <span class="btn2_wrapper">
             <a class="rec_next btn2 medium btn2_text_on" title="Show me the next title">
               <span class="btn2_text">Next &raquo;</span>
             </a>
           </span>
         </div>

             <input type="hidden" name="49e6c" value="da29">
       </div>

       <div class="rec_details">
         <div class="rec-info">

           <div class="rec-jaw-upper">

     <div class="rec-title">
       <a href="/title/tt0167260/"
><b>The Lord of the Rings: The Return of the King</b></a>
            <span class="nobr">(2003)</span>
   </div>



    <div class="rec-cert-genre rec-elipsis">





                    <span title="Ratings certificate for The Lord of the Rings: The Return of the King (2003)"
                          class="us_pg_13 titlePageSprite absmiddle"></span>

                     Adventure
     <span class="ghost">|</span>
                     Drama
     <span class="ghost">|</span>
                     Fantasy


    </div>

             <div class="rec-rating">





<div class="rating rating-list" data-starbar-class="rating-list" data-auth="" data-user="" id="tt0167260|imdb|8.9|8.9|p13nsims-title|tt0076759|title|main" data-ga-identifier=""
title="Users rated this 8.9/10 (1,513,142 votes) - click stars to rate" >
<span class="rating-bg">&nbsp;</span>
<span class="rating-imdb " style="width: 124.6px">&nbsp;</span>
<span class="rating-stars">
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>1</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>2</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>3</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>4</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>5</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>6</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>7</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>8</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>9</span></a>
      <a href="/register/login?why=vote"
rel="nofollow" title="Register or login to rate this title" ><span>10</span></a>
</span>
<span class="rating-rating "><span class="value">8.9</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel "><a href="/title/tt0167260/vote?v=X;k=" title="Delete" rel="nofollow"><span>X</span></a></span>
&nbsp;</div>

               <div class="rec-outline">
    <p>
    Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.    </p>
               </div>

             </div>

           </div>

           <div class="rec-jaw-lower">
             <div class="rec-jaw-teeth"></div>
 <div class="rec-director rec-ellipsis">
      <b>Director:</b>
Peter Jackson  </div>
<div class="rec-actor rec-ellipsis"> <span>
    <b>Stars:</b>
Elijah Wood,
Viggo Mortensen,
Ian McKellen</span></div>
           </div>

         </div>
       </div>

      </div>


   </div>


                    </div>
                </div>


  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleRecsWidget_finished');
    }
  </script>
<script>
    if (typeof uet == 'function') {
      uet("be", "TitleRecsWidget", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "TitleRecsWidget", {wb: 1});
    }
</script>


<script>
    if (typeof uet == 'function') {
      uet("bb", "TitleCastWidget", {wb: 1});
    }
</script>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleCastWidget_started');
    }
  </script>
    <div class="article" id="titleCast">
    <span class=rightcornerlink >
            <a href="/register/login?why=edit"
rel="login">Edit</a>
    </span>
        <h2>Cast</h2>

        <table class="cast_list">
  <tr><td colspan="4" class="castlist_label">Cast overview, first billed only:</td></tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0000434/"
><img height="44" width="32" alt="Mark Hamill" title="Mark Hamill" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BOGY2MjI5MDQtOThmMC00ZGIwLWFmYjgtYWU4MzcxOGEwMGVkXkEyXkFqcGdeQXVyMzM4MjM0Nzg@._V1_UY44_CR23,0,32,44_AL_.jpg" /></a>          </td>
          <td>
<a href="/name/nm0000434/"
> Mark Hamill
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt0076759/characters/nm0000434" >Luke Skywalker</a>

          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm0000148/"
><img height="44" width="32" alt="Harrison Ford" title="Harrison Ford" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BMTY4Mjg0NjIxOV5BMl5BanBnXkFtZTcwMTM2NTI3MQ@@._V1_UX32_CR0,0,32,44_AL_.jpg" /></a>          </td>
          <td>
<a href="/name/nm0000148/"
> Harrison Ford
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt0076759/characters/nm0000148" >Han Solo</a>

          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0000402/"
><img height="44" width="32" alt="Carrie Fisher" title="Carrie Fisher" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BMjM4ODU5MDY4MV5BMl5BanBnXkFtZTgwODY1MjQ5MDI@._V1_UX32_CR0,0,32,44_AL_.jpg" /></a>          </td>
          <td>
<a href="/name/nm0000402/"
> Carrie Fisher
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt0076759/characters/nm0000402" >Princess Leia Organa</a>

          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm0001088/"
><img height="44" width="32" alt="Peter Cushing" title="Peter Cushing" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BNTM4NzE4NTIwNl5BMl5BanBnXkFtZTYwMTYxNzM2._V1_UX32_CR0,0,32,44_AL_.jpg" /></a>          </td>
          <td>
<a href="/name/nm0001088/"
> Peter Cushing
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt0076759/characters/nm0001088" >Grand Moff Tarkin</a>

          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0000027/"
><img height="44" width="32" alt="Alec Guinness" title="Alec Guinness" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BMTIxMTA5OTI2M15BMl5BanBnXkFtZTYwNjEwNjU2._V1_UY44_CR1,0,32,44_AL_.jpg" /></a>          </td>
          <td>
<a href="/name/nm0000027/"
> Alec Guinness
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt0076759/characters/nm0000027" >Ben Obi-Wan Kenobi</a>

          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm0000355/"
><img height="44" width="32" alt="Anthony Daniels" title="Anthony Daniels" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BMzg3MzU2NTUxMF5BMl5BanBnXkFtZTcwMTE1NjI4NA@@._V1_UY44_CR0,0,32,44_AL_.jpg" /></a>          </td>
          <td>
<a href="/name/nm0000355/"
> Anthony Daniels
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt0076759/characters/nm0000355" >C-3PO</a>

          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0048652/"
><img height="44" width="32" alt="Kenny Baker" title="Kenny Baker" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BMTg1OTA3MzU0NV5BMl5BanBnXkFtZTcwNjY2Njk4Nw@@._V1_UX32_CR0,0,32,44_AL_.jpg" /></a>          </td>
          <td>
<a href="/name/nm0048652/"
> Kenny Baker
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt0076759/characters/nm0048652" >R2-D2</a>

          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm0562679/"
><img height="44" width="32" alt="Peter Mayhew" title="Peter Mayhew" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BNjg1NDUzMzM3NF5BMl5BanBnXkFtZTcwMDg4NTczMQ@@._V1_UY44_CR1,0,32,44_AL_.jpg" /></a>          </td>
          <td>
<a href="/name/nm0562679/"
> Peter Mayhew
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt0076759/characters/nm0562679" >Chewbacca</a>

          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0001190/"
><img height="44" width="32" alt="David Prowse" title="David Prowse" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BMTEyODc0MTUzODBeQTJeQWpwZ15BbWU4MDUyMjc3OTAx._V1_UX32_CR0,0,32,44_AL_.jpg" /></a>          </td>
          <td>
<a href="/name/nm0001190/"
> David Prowse
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt0076759/characters/nm0001190" >Darth Vader</a>

          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm0114436/"
><img height="44" width="32" alt="Phil Brown" title="Phil Brown" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BMDkxYTdkZjUtNDM4ZS00YTM3LWI2MzktODM1MTlhYjJkZjI5XkEyXkFqcGdeQXVyMjk3NTUyOTc@._V1_UY44_CR23,0,32,44_AL_.jpg" /></a>          </td>
          <td>
<a href="/name/nm0114436/"
> Phil Brown
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt0076759/characters/nm0114436" >Uncle Owen</a>

          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0292235/"
><img height="44" width="32" alt="Shelagh Fraser" title="Shelagh Fraser" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BNjVjMTVkZWItZDIyMy00ZDM4LTlhMWQtNWM4NTg4MDY3MjBmXkEyXkFqcGdeQXVyMjk3NTUyOTc@._V1_UY44_CR23,0,32,44_AL_.jpg" /></a>          </td>
          <td>
<a href="/name/nm0292235/"
> Shelagh Fraser
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt0076759/characters/nm0292235" >Aunt Beru</a>

          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm0701023/"
><img height="44" width="32" alt="Jack Purvis" title="Jack Purvis" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BMTM3OTkwNjk0NF5BMl5BanBnXkFtZTcwNjQzNTk0OA@@._V1_UX32_CR0,0,32,44_AL_.jpg" /></a>          </td>
          <td>
<a href="/name/nm0701023/"
> Jack Purvis
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt0076759/characters/nm0701023" >Chief Jawa</a>

          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0567018/"
><img height="44" width="32" alt="Alex McCrindle" title="Alex McCrindle" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BMTVlNWNhZjEtOTA4Ny00MjZjLWFhNjUtZDQxNDY5ZDU2ODFjL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMjk3NTUyOTc@._V1_UY44_CR4,0,32,44_AL_.jpg" /></a>          </td>
          <td>
<a href="/name/nm0567018/"
> Alex McCrindle
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt0076759/characters/nm0567018" >General Dodonna</a>

          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm0125952/"
><img height="44" width="32" alt="Eddie Byrne" title="Eddie Byrne" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BMGIyZjcxMDUtMjdhNy00NTkxLWE2OTEtMDZmNjAwZjZjNjYzXkEyXkFqcGdeQXVyNTEzNDY5MjM@._V1_UX32_CR0,0,32,44_AL_.jpg" /></a>          </td>
          <td>
<a href="/name/nm0125952/"
> Eddie Byrne
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt0076759/characters/nm0125952" >General Willard</a>

          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0377120/"
><img height="44" width="32" alt="Drewe Henley" title="Drewe Henley" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate hidden " loadlate="https://m.media-amazon.com/images/M/MV5BNjA1OTMxNDg5N15BMl5BanBnXkFtZTgwMzUwMzg4MDI@._V1_UY44_CR35,0,32,44_AL_.jpg" /></a>          </td>
          <td>
<a href="/name/nm0377120/"
> Drewe Henley
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt0076759/characters/nm0377120" >Red Leader</a>


  (as Drewe Hemley)


          </td>
      </tr>
        </table>
        <div class="see-more">
            <a href="fullcredits#cast"
>See full cast</a>&nbsp;&raquo;
        </div>
        <div class="pro_logo_main_title">
    <div id=cast_title_pro_link class=pro_title_cast_link>
<a href="https://pro.imdb.com/title/tt0076759?rf=cons_tt_btf_cc"
class="pro_title_href" > <img src="https://m.media-amazon.com/images/G/01/imdb/IMDbConsumerSiteProTitleViews/images/logo/pro_logo_light-2443528084._CB455053166_.png" class="pro_logo" />
<span class="pro_title_link_text">
View production, box office, & company info
</span>
<img src="https://m.media-amazon.com/images/G/01/imdb/IMDbConsumerSiteProTitleViews/images/icons/link_2x-1783866327._CB454438608_.png"
class="pro_link_icon">
</a>    </div>
        </div>
    </div>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleCastWidget_finished');
    }
  </script>
<script>
    if (typeof uet == 'function') {
      uet("be", "TitleCastWidget", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "TitleCastWidget", {wb: 1});
    }
</script>








	<!-- no content received for slot: maindetails_center_ad -->







<script>
    if (typeof uet == 'function') {
      uet("bb", "TitleStorylineWidget", {wb: 1});
    }
</script>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleStorylineWidget_started');
    }
  </script>
    <div class = "article" id="titleStoryLine">
    <span class=rightcornerlink >
            <a href="/register/login?why=edit"
rel="login">Edit</a>
    </span>

        <h2>Storyline</h2>

        <div class="inline canwrap">
            <p>
                <span>    The Imperial Forces, under orders from cruel Darth Vader, hold Princess Leia hostage in their efforts to quell the rebellion against the Galactic Empire. Luke Skywalker and Han Solo, captain of the Millennium Falcon, work together with the companionable droid duo R2-D2 and C-3PO to rescue the beautiful princess, help the Rebel Alliance and restore freedom and justice to the Galaxy.</span>
                <em class="nobr">Written by
<a href="/search/title?plot_author=Jwelch5742&view=simple&sort=alpha"
>Jwelch5742</a></em>            </p>
        </div>

        <span class="see-more inline">
                <a href="/title/tt0076759/plotsummary"
>Plot Summary</a>
    <span>|</span>
        <a href="/title/tt0076759/synopsis"
>Plot Synopsis</a>
    </span>
        <hr />
        <div class="see-more inline canwrap">
            <h4 class="inline">Plot Keywords:</h4>
<a href="/search/keyword?keywords=rebellion"
> <span class="itemprop">rebellion</span></a>
                        <span>|</span>
<a href="/search/keyword?keywords=galactic-war"
> <span class="itemprop">galactic war</span></a>
                        <span>|</span>
<a href="/search/keyword?keywords=empire"
> <span class="itemprop">empire</span></a>
                        <span>|</span>
<a href="/search/keyword?keywords=princess"
> <span class="itemprop">princess</span></a>
                        <span>|</span>
<a href="/search/keyword?keywords=droid"
> <span class="itemprop">droid</span></a>
            <span>|</span>&nbsp;<nobr><a href="/title/tt0076759/keywords"
>See All (363)</a>&nbsp;&raquo;</nobr>

        </div>
        <hr />
        <div class="txt-block">
            <h4 class="inline">Taglines:</h4>
The force will be with you (re-release)                <span class="see-more inline">
<a href="/title/tt0076759/taglines"
> See more</a>&nbsp;&raquo;
                </span>
        </div>
        <hr />
        <div class="see-more inline canwrap">
            <h4 class="inline">Genres:</h4>
<a href="/search/title?genres=action&explore=title_type,genres"
> Action</a>&nbsp;<span>|</span>
<a href="/search/title?genres=adventure&explore=title_type,genres"
> Adventure</a>&nbsp;<span>|</span>
<a href="/search/title?genres=fantasy&explore=title_type,genres"
> Fantasy</a>&nbsp;<span>|</span>
<a href="/search/title?genres=sci-fi&explore=title_type,genres"
> Sci-Fi</a>
        </div>

             <hr/>

    <div class="txt-block">
                <h4>Motion Picture Rating
                    (<a href="/mpaa"
>MPAA</a>)
                </h4>
            <span>Rated PG for sci-fi violence and brief mild language</span>
    <span class="ghost">|</span>            <span class="see-more inline">
<a href="/title/tt0076759/parentalguide#certification"
> See all certifications</a>&nbsp;&raquo;
            </span>
    </div>
    <div class="txt-block">
        <h4 class="inline">Parents Guide:</h4>
        <span class="see-more inline">
<a href="/title/tt0076759/parentalguide"
> View content advisory</a>&nbsp;&raquo;
        </span>
    </div>
    </div>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleStorylineWidget_finished');
    }
  </script>
<script>
    if (typeof uet == 'function') {
      uet("be", "TitleStorylineWidget", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "TitleStorylineWidget", {wb: 1});
    }
</script>






<script>
    if (typeof uet == 'function') {
      uet("bb", "TitleDetailsWidget", {wb: 1});
    }
</script>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleDetailsWidget_started');
    }
  </script>

    <div class = "article" id="titleDetails">
    <span class=rightcornerlink >
            <a href="/register/login?why=edit"
rel="login">Edit</a>
    </span>
        <h2>Details</h2>
      <div class="txt-block">
      <h4 class="inline">Official Sites:</h4>
    <a href="/offsite/?page-action=offsite-facebook&token=BCYrrXiCD8CatiJef_dbpTI3ZMuc0ykm-Ob3nQNvvd7ZEATwG5tl9_ijpWV65Wvj6GKmnAnH7UEA%0D%0AzgdHsIrCgSigRHLR2Rv1-I4xinsOenxVzIiDL9PijtGUohIxijblzpGChCZ0zKrOoY9JuM0K4nCW%0D%0AYZCRBVMZs6zOVD-_veYUd93Es60qQjkcTPZFTH_aT2Z_HbOxJwNsrEfM0W7vtWiwXfViYGwsenDD%0D%0AgPbLjrfZg04%0D%0A"
rel="nofollow" >Official Facebook</a>
          <span class="ghost">|</span>

    <a href="/offsite/?page-action=offsite-starwars&token=BCYvOvsVWCkVdRdkqYxELq67CjbDi3uWjLzMXRe26BVfvqfI6Kouh_33283gUiJ7DrW17HgcQkdk%0D%0AQKhMK_X2841LbnoxEw4RiNZDIHElW3EwoIT8sCKMObfOcxjqBGy-PWdVmioHoglPYl0vK-8--U2v%0D%0AC3vSMd9lvFh9CLwMg8EZn8PNM3KF0ZsuiBOM8C3RsX3ZYUdtsIUMh7qhR92Toes0EoQHxwfsmpC9%0D%0ApgpvE7zuF2QordGsIlgv85GcffLAjLzg%0D%0A"
rel="nofollow" >Official site</a>
               <span class="see-more inline">
      </span>
      </div>

    <div class="txt-block">
    <h4 class="inline">Country:</h4>
        <a href="/search/title?country_of_origin=us"
>USA</a>
    </div>

    <div class="txt-block">
    <h4 class="inline">Language:</h4>
        <a href="/search/title?title_type=feature&primary_language=en&sort=moviemeter,asc"
>English</a>
    </div>


    <div class="txt-block">
    <h4 class="inline">Release Date:</h4> 25 May 1977 (USA)
    <span class="see-more inline">
      <a href="releaseinfo"
>See more</a>&nbsp;&raquo;
    </span>
    </div>

      <div class="txt-block">
      <h4 class="inline">Also Known As:</h4> Star Wars: Episode IV - A New Hope
      <span class="see-more inline">
        <a href="releaseinfo#akas"
>See more</a>&nbsp;&raquo;
      </span>
      </div>

    <div class="txt-block">
    <h4 class="inline">Filming Locations:</h4>
    <a href="/search/title?locations=Cardington%20Airship%20Hangars,%20Bedfordshire,%20England,%20UK"
>Cardington Airship Hangars, Bedfordshire, England, UK</a>
      <span class="see-more inline">
        <a href="locations"
>See more</a>&nbsp;&raquo;
      </span>
    </div>

    <hr />
    <span class=rightcornerlink >
            <a href="/register/login?why=edit"
rel="login">Edit</a>
    </span>
    <h3 class="subheading">Box Office</h3>

        <div class="txt-block">
            <h4 class="inline">Budget:</h4>$11,000,000
            <span class="attribute">(estimated)</span>
        </div>

        <div class="txt-block">
            <h4 class="inline">Opening Weekend USA:</h4> $1,554,475,
<span class="attribute">30 May 1977</span>        </div>

        <div class="txt-block">
<h4 class="inline">Gross USA:</h4> $460,998,507        </div>

        <div class="txt-block">
<h4 class="inline">Cumulative Worldwide Gross:</h4> $775,512,064        </div>

    <span class="see-more inline">
        <a href="https://pro.imdb.com/title/tt0076759?rf=cons_tt_bo_tt"
>See more on IMDbPro</a>&nbsp;&raquo;
    </span>
  <hr />
  <h3 class="subheading">Company Credits</h3>
    <div class="txt-block">
    <h4 class="inline">Production Co:</h4>
<a href="/company/co0071326"
> Lucasfilm</a>,<a href="/company/co0000756"
> Twentieth Century Fox</a>      <span class="see-more inline">
        <a href="companycredits"
>See more</a>&nbsp;&raquo;
      </span>
    </div>
  <div class="txt-block">
  Show more on
  <a href="https://pro.imdb.com/title/tt0076759/companycredits?rf=cons_tt_cocred_tt"
>IMDbPro</a>&nbsp;&raquo;
  </div>


  <hr />
  <h3 class="subheading">Technical Specs</h3>

    <div class="txt-block">
      <h4 class="inline">Runtime:</h4>
        <time datetime="PT121M">121 min</time>
          <span class="ghost">|</span>
        <time datetime="PT125M">125 min</time>
            (special edition)
    </div>

    <div class="txt-block">
    <h4 class="inline">Sound Mix:</h4>
        <a href="/search/title?sound_mixes=70_mm_6_track"
>70 mm 6-Track</a>
(70 mm prints)<span class="ghost">|</span>        <a href="/search/title?sound_mixes=dolby"
>Dolby</a>
(as Dolby System)&nbsp;(35 mm prints)&nbsp;(1977 print)<span class="ghost">|</span>        <a href="/search/title?sound_mixes=dts_stereo"
>DTS-Stereo</a>
(as DTS Stereo® in selected theatres)&nbsp;(1997 print)<span class="ghost">|</span>        <a href="/search/title?sound_mixes=dolby_digital"
>Dolby Digital</a>
(as Dolby® Digital in selected theatres)&nbsp;(1997 print)<span class="ghost">|</span>        <a href="/search/title?sound_mixes=sdds"
>SDDS</a>
(as Sony Dynamic Digital SoundTM in selected theatres)&nbsp;(1997 print)<span class="ghost">|</span>        <a href="/search/title?sound_mixes=mono"
>Mono</a>
(some 35 mm prints)&nbsp;(other 16 mm prints)    </div>

    <div class="txt-block">
    <h4 class="inline">Color:</h4>
        <a href="/search/title?colors=color"
>Color</a>
(Technicolor)    </div>

    <div class="txt-block">
    <h4 class="inline">Aspect Ratio:</h4> 2.39 : 1
    </div>

  See <a href="technical"
>full technical specs</a>&nbsp;&raquo;
    </div>

  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleDetailsWidget_finished');
    }
  </script>
<script>
    if (typeof uet == 'function') {
      uet("be", "TitleDetailsWidget", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "TitleDetailsWidget", {wb: 1});
    }
</script>






<script>
    if (typeof uet == 'function') {
      uet("bb", "TitleDidYouKnowWidget", {wb: 1});
    }
</script>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleDidYouKnowWidget_started');
    }
  </script>
    <div id="titleDidYouKnow" class="article">
    <span class=rightcornerlink >
            <a href="/register/login?why=edit"
rel="login">Edit</a>
    </span>
        <h2>Did You Know?</h2>
    <div id="trivia" class="txt-block">
        <h4>Trivia</h4>
    <a href="/name/nm0144053">Sandra Peabody</a> auditioned for the role of Princess Leia.        <a href="trivia"
class="nobr" >See more</a>  &raquo;
    </div>
                <hr />
     <div id="goofs"  class="txt-block">
        <h4>Goofs</h4>
After the Millennium Falcon lands on the death star,the stormtrooper stood on the left that goes to help the scanning crew is missing the thermal detonator at the small of his back.        <a href="trivia?tab=gf"
class="nobr" >See more</a>  &raquo;
    </div>
                <hr />
    <div id="quotes" class="text-block">
        <h4>Quotes</h4>
[<span class="fine">first lines</span>]
<br /><a href="/name/nm0000355/"
><span class="character">C-3PO</span></a>:
Did you hear that? They shut down the main reactor. We'll be destroyed for sure. This is madness.
<br />        <a href="trivia?tab=qt"
class="nobr" >See more</a> &raquo;
    </div>
                <hr />
     <div id="crazyCredits"  class="txt-block">
        <h4>Crazy Credits</h4>
    The film's opening prologue: It is a period of civil war. Rebel spaceships, striking from a hidden base, have won their first victory against the evil Galactic Empire.  During the battle, Rebel spies managed to steal secret plans to the Emperor's ultimate weapon, the DEATH STAR, an armored space station with enough power to destroy an entire planet.  Pursued by the Emperor's sinister agents, Princess Leia races home aboard her starship, custodian of the stolen plans that can save her people and restore freedom to the galaxy ....        <a href="trivia?tab=cz"
class="nobr" >See more</a>  &raquo;
    </div>
                <hr />
     <div id="alternateVersions"  class="txt-block">
        <h4>Alternate Versions</h4>
In the 2004 DVD edition, Vader&#39;s lines are lowered very slightly in pitch so his voice sounds more like it does in the next two films.        <a href="alternateversions?tab=cz"
class="nobr" >See more</a>  &raquo;
    </div>
                <hr />
    <div id="connections" class="text-block">
        <h4>Connections</h4>
        Referenced in <a href="/title/tt1588124">Smallville: Escape</a>&nbsp;(2010)


        <a href="trivia?tab=mc"
class="nobr" >See more</a> &raquo;
    </div>
    </div>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleDidYouKnowWidget_finished');
    }
  </script>
<script>
    if (typeof uet == 'function') {
      uet("be", "TitleDidYouKnowWidget", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "TitleDidYouKnowWidget", {wb: 1});
    }
</script>











<script>
    if (typeof uet == 'function') {
      uet("bb", "TitleFAQWidget", {wb: 1});
    }
</script>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleFAQWidget_started');
    }
  </script>

    <div class="article" id="titleFAQ">
        <h2>Frequently Asked Questions</h2>

            <div class="faq" >
                    <div class="odd">
                    <b>Q:</b>
<a href="/title/tt0076759/faq#fq0009861"
> If Luke is supposed to be hidden from the Empire, why was he given the name "Skywalker"?</a>
                    </div>
                    <div class="even">
                    <b>Q:</b>
<a href="/title/tt0076759/faq#fq0009873"
> Why doesn't Obi-Wan remember the droids?</a>
                    </div>
                    <div class="odd">
                    <b>Q:</b>
<a href="/title/tt0076759/faq#fq0009870"
> What are the differences between the Special Edition and the DVD release?</a>
                    </div>
            </div>

            <span class="see-more inline" >
                <a href="/title/tt0076759/faq"
class="nobr" >See more</a>
            </span> &raquo;
    </div>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleFAQWidget_finished');
    }
  </script>
<script>
    if (typeof uet == 'function') {
      uet("be", "TitleFAQWidget", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "TitleFAQWidget", {wb: 1});
    }
</script>








<script>
    if (typeof uet == 'function') {
      uet("bb", "TitleUserReviewsWidget", {wb: 1});
    }
</script>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleUserReviewsWidget_started');
    }
  </script>
    <div class="article" id="titleUserReviewsTeaser">
        <h2>User Reviews</h2>
        <div class="user-comments">
                    <div class="tinystarbar" title="9/10">
                        <div style="width: 90px;">&nbsp;</div>
                    </div>
                <span>
                    <strong>An adventure story, replacing six-shooters or swords with laser guns and horses with rockers</strong>
                    <div class="comment-meta">
                        30 November 2008 | by <a href="/user/ur0176092/"
><span>Nazi_Fighter_David</span></a>
                        &ndash; <a href="/user/ur0176092/comments"
>See all my reviews</a>
                    </div>
                    <div>
                        <p>The film turn on the endlessly renewed battle between good and evil, the former represented by the Jedi knights and the mystical Force which they are in touch with, and the latter by the Galactic Empire with its Nazi-like storm-troopers <br/><br/>Luke Skywalker&#39;s simple farming life on a remote planet is dramatically changed when he intercepts a distress call from rebel leader Princess Leia Organa The message leads him to Ben Obi-Wan Kenobi and with the two droids C3PO and R2D2, and later Chewbacca and Han Solo, their journey to release the princess from the evil Empire begins <br/><br/>Now a quarter of a century old, Lucas&#39; project has benefited from improvements in special effects technology, but his vision has remained the same: a naive, even childlike belief in absolute good and evil, a preference for action over character and spectacle over everything</p>
                    </div>
                </span>
                <hr />


                <div class="yn" id="ynd_rw1983238">
                49 of 79 people found this review helpful.&nbsp;
                Was this review helpful to you?

                    <button class="btn small" value="Yes" name="ynb_rw1983238_yes" onclick="CS.TMD.user_review_vote('rw1983238', 'tt0076759', 'yes', 'true');" >Yes</button>
                    <button class="btn small" value="No" name="ynb_rw1983238_no" onclick="CS.TMD.user_review_vote('rw1983238', 'tt0076759', 'no', 'true');" >No</button>
                        | <a href="/registration/signin?u=/title/tt0076759/"
onclick="imdb.contribution.clickHandler(event)" >Report this</a>
                </div>

                <a href="/registration/signin?u=/title/tt0076759/"
onclick="imdb.contribution.clickHandler(event)" >Review this title</a>

            <span>|</span>
            <a href="/title/tt0076759/reviews"
>See all 1,657 user reviews</a>&nbsp;&raquo;
        </div>
    </div>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleUserReviewsWidget_finished');
    }
  </script>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleUserReviewsWidget_finished');
    }
  </script>
<script>
    if (typeof uet == 'function') {
      uet("be", "TitleUserReviewsWidget", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "TitleUserReviewsWidget", {wb: 1});
    }
</script>











  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleContributeWidget_started');
    }
  </script>
    <div class="article contribute">
        <div class="rightcornerlink">
<a href="https://help.imdb.com/article/contribution/contribution-information/adding-data/G6BXD2JFDCCETUF4"
>Getting Started</a>
            <span>|</span>
<a href="/czone/"
>Contributor Zone</a>&nbsp;&raquo;</div>
        <h2>Contribute to This Page</h2>

                <div class="button-box">
                    <form method="get" action="https://contribute.imdb.com/updates">
                        <input type="hidden" name="ref_" value="tt_cn_edt" />
                        <input type="hidden" name="edit" value="legacy/title/tt0076759/" />
                            <button class="btn primary large" rel="login" type="submit">Edit page</button>
                    </form>
                </div>





    </div>

  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleContributeWidget_finished');
    }
  </script>









        <a name="slot_center-20"></a>
        <div class="article">






            <script type="text/javascript">if(typeof uet === 'function'){uet('bb','NinjaWidget',{wb:1});}</script>




        <span class="ab_widget">



    <div class="ab_ninja">
<div class="widget_content no_inline_blurb"> <div class="widget_nested"> <div class="ninja_image_pack"> <div class="ninja_center"> <div class="ninja_image first_image last_image" style="width:624px;height:auto;" > <div style="width:624px;height:auto;margin:0 auto;"> <div class="widget_image"> <div class="image"> <a href="/tv" > <img class="pri_image" title="IMDb TV" alt="IMDb TV" src="https://m.media-amazon.com/images/G/01/IMDb/c1augkk._CB1564642207_SY351_SX624_AL_.jpg" /> </a> </div> </div> </div> </div> </div> </div> </div> </div>    </div>



        </span>



            <script type="text/javascript">
                if(typeof uex === 'function'){uex('ld','NinjaWidget',{wb:1});}
            </script>





        </div>




        <a name="slot_center-21"></a>
        <div class="article">






            <script type="text/javascript">if(typeof uet === 'function'){uet('bb','NinjaWidget',{wb:1});}</script>




        <span class="ab_widget">



    <div class="ab_ninja">
<span class="widget_header"> <span class="oneline"> <a href="/offsite/?page-action=offsite-amazon&token=BCYuGBNS0uEvY15yiKKwcmwq3eC8udGz4vC9-0Tv2iLkP22u1poJiUGOD3XhVso81D-H73hxdFH3%0D%0AbCmXkb3rjtbi8nNRzHawZXPpZTdm8_0ZHqV4taQLWXHYOnB1UWZKf340yQm9IJdPwIQQJ8FLZbEJ%0D%0A3sEIX6zxBqMfZ00FaqL47jyk4FWD_QSi9MdegjG6MyVa_tfaDP9bL3Q9mOELqv8K2LTD-D0h7aKV%0D%0AbE0N7Slsh7_tSblmHwtPUZ8-OEPOAwv2%0D%0A" > <h3> Stream Action and Adventure Titles With Prime Video</h3> </a> </span> </span> <div class="widget_content no_inline_blurb"> <div class="widget_nested"> <div class="ninja_image_pack"> <div class="ninja_left"> <div class="ninja_image first_image" style="width:116px;height:auto;" > <div style="width:116px;height:auto;margin:0 auto;"> <div class="widget_image"> <div class="image"> <a href="/offsite/?page-action=offsite-amazon&token=BCYorB_qPWtan1BKyNCAYIbTG6QSOnbxCgdbNtfHxSzLDwMp0flTnZSfJTCiav53UoCodC1-xkm8%0D%0A36LtSyBQo3Jc2hsE9qnFDUWdGmtPX0Ob_WbxA8e4jCrCUanxopEqbuUq5ODNRh2TWOosUe7JsP_U%0D%0AVqmh8lga3bhSbKYh8j36bduLcrBHUiJVOhKmySriUj-4_ItjD3vH2HKkiJtac-RuE7TuJrCqaacG%0D%0ABsbGj-0v8wFpXkkP4AJ8HxMqrC8ak5d-J4-W0srZaD8Oj4bPbBIhCg%0D%0A" > <img class="pri_image" title="Peter Franzén, Katheryn Winnick, Alexander Ludwig, Jordan Patrick Smith, and Alex Høgh Andersen in Vikings (2013)" alt="Peter Franzén, Katheryn Winnick, Alexander Ludwig, Jordan Patrick Smith, and Alex Høgh Andersen in Vikings (2013)" src="https://m.media-amazon.com/images/M/MV5BNDYyNzk1NzYwOF5BMl5BanBnXkFtZTgwMTQ0Nzc4MzI@._V1_SY172_CR5,0,116,172_AL_.jpg" /> <img alt="Peter Franzén, Katheryn Winnick, Alexander Ludwig, Jordan Patrick Smith, and Alex Høgh Andersen in Vikings (2013)" title="Peter Franzén, Katheryn Winnick, Alexander Ludwig, Jordan Patrick Smith, and Alex Høgh Andersen in Vikings (2013)" class="image_overlay overlay_mouseout" src="https://m.media-amazon.com/images/G/01/IMDb/icon/external-button._CB304896345_.png" data-src-x2="https://m.media-amazon.com/images/G/01/IMDb/icon/external-button._CB304896345_.png" /> <img alt="Peter Franzén, Katheryn Winnick, Alexander Ludwig, Jordan Patrick Smith, and Alex Høgh Andersen in Vikings (2013)" title="Peter Franzén, Katheryn Winnick, Alexander Ludwig, Jordan Patrick Smith, and Alex Høgh Andersen in Vikings (2013)" class="image_overlay overlay_mouseover" src="https://m.media-amazon.com/images/G/01/IMDb/icon/external-button-hover._CB304896345_.png" data-src-x2="https://m.media-amazon.com/images/G/01/IMDb/icon/external-button-hover._CB304896345_.png" /> </a> </div> </div> </div> </div><div class="ninja_image ninja_image_fixed_padding widget_padding"></div><div class="ninja_image" style="width:116px;height:auto;" > <div style="width:116px;height:auto;margin:0 auto;"> <div class="widget_image"> <div class="image"> <a href="/offsite/?page-action=offsite-amazon&token=BCYl4sIxe_2A7X0NXmIAvPLmDAG2fJnLmSufDHMI-KYzy_NWh0ZLqF72PBx2UIQTNFB6bIHmf5SQ%0D%0Ak9APkMN1J9R1mNTk5tW5v91-y3-yGownpgEKb-WA8gOog6cAE_sdnlX7-rKQlqAVQMOmAkdCxoG-%0D%0A-WFCGeaj1D4NWZp36JP0BskKZQiEDyuctSvULrcWyXtflaWjsE_73Io7ZKzniSfGdsNrJsXhSzVw%0D%0A6oW045Yu8m3_d-iuwNP-PXKtmO7OkgA9peyflgi-KNbQ2Kj_cxnz5Q%0D%0A" > <img class="pri_image" title="Esme Creed-Miles in Hanna (2019)" alt="Esme Creed-Miles in Hanna (2019)" src="https://m.media-amazon.com/images/M/MV5BNzQyNjlkMTItNzAxNC00YzM4LTk3NjktZjM2NzdlMzI3MWYwXkEyXkFqcGdeQXVyNjkwNzEwMzU@._V1_SX116_CR0,0,116,172_AL_.jpg" /> <img alt="Esme Creed-Miles in Hanna (2019)" title="Esme Creed-Miles in Hanna (2019)" class="image_overlay overlay_mouseout" src="https://m.media-amazon.com/images/G/01/IMDb/icon/external-button._CB304896345_.png" data-src-x2="https://m.media-amazon.com/images/G/01/IMDb/icon/external-button._CB304896345_.png" /> <img alt="Esme Creed-Miles in Hanna (2019)" title="Esme Creed-Miles in Hanna (2019)" class="image_overlay overlay_mouseover" src="https://m.media-amazon.com/images/G/01/IMDb/icon/external-button-hover._CB304896345_.png" data-src-x2="https://m.media-amazon.com/images/G/01/IMDb/icon/external-button-hover._CB304896345_.png" /> </a> </div> </div> </div> </div><div class="ninja_image ninja_image_fixed_padding widget_padding"></div><div class="ninja_image" style="width:116px;height:auto;" > <div style="width:116px;height:auto;margin:0 auto;"> <div class="widget_image"> <div class="image"> <a href="/offsite/?page-action=offsite-amazon&token=BCYiEX0NWSwm_vZ4gSL-y6nQWz0wnbw7M-MRsdx82rMUowPPBjbiGEb0XalHWJECtxDi5_FxM_TC%0D%0AiApxcKsF7KvRKX6E0m9vxJ2qZdlIm815kYkt8hgUzcDporhlyScUI3HNBzqbKSAnVO9NcHok81le%0D%0AlcloKdWSnx7_grpA4JC5XjfZeAiDajVTq3P2DiDjjyKywCEB5CJRqbnJjPSRUps0UB-O80_zFr44%0D%0AjWdeSJwNFibkTmy4fptooEoVXJGVcEKpn5pFB4BzaFSZ83xEHhi1Vw%0D%0A" > <img class="pri_image" title="John Krasinski in Jack Ryan (2018)" alt="John Krasinski in Jack Ryan (2018)" src="https://m.media-amazon.com/images/M/MV5BMjIzMDcyMDcxOV5BMl5BanBnXkFtZTgwMTg1NDk2NTM@._V1_SX116_CR0,0,116,172_AL_.jpg" /> <img alt="John Krasinski in Jack Ryan (2018)" title="John Krasinski in Jack Ryan (2018)" class="image_overlay overlay_mouseout" src="https://m.media-amazon.com/images/G/01/IMDb/icon/external-button._CB304896345_.png" data-src-x2="https://m.media-amazon.com/images/G/01/IMDb/icon/external-button._CB304896345_.png" /> <img alt="John Krasinski in Jack Ryan (2018)" title="John Krasinski in Jack Ryan (2018)" class="image_overlay overlay_mouseover" src="https://m.media-amazon.com/images/G/01/IMDb/icon/external-button-hover._CB304896345_.png" data-src-x2="https://m.media-amazon.com/images/G/01/IMDb/icon/external-button-hover._CB304896345_.png" /> </a> </div> </div> </div> </div><div class="ninja_image ninja_image_fixed_padding widget_padding"></div><div class="ninja_image" style="width:116px;height:auto;" > <div style="width:116px;height:auto;margin:0 auto;"> <div class="widget_image"> <div class="image"> <a href="/offsite/?page-action=offsite-amazon&token=BCYubdou0z7p1vp6xZ-tA54a3nhsUrK8jMbI2ZuqpZibjIPoemlnd6x1x7oe-euGHJp2-dTMfVCp%0D%0Acemb0aylzSNT9NNEDpHK4oZ_SPKLv1MpRZlNY948h-DMzPZhIGewkCGhB2Lw9Ws5AgiQnu4x58qN%0D%0AzeD6dTNgRKBLGdHxYTT5p2vJaGloG-HQ1zGGMcZmCuJiJ0KmYb4BQnYiDipNuH7xcPxKOOpHSjVq%0D%0AVrdLZPmpps4qTNaAEq-qWR9imeJZZOlS%0D%0A" > <img class="pri_image" title="Don Cheadle, Robert Downey Jr., Gwyneth Paltrow, and Scarlett Johansson in Iron Man 2 (2010)" alt="Don Cheadle, Robert Downey Jr., Gwyneth Paltrow, and Scarlett Johansson in Iron Man 2 (2010)" src="https://m.media-amazon.com/images/M/MV5BMTM0MDgwNjMyMl5BMl5BanBnXkFtZTcwNTg3NzAzMw@@._V1_SX116_CR0,0,116,172_AL_.jpg" /> <img alt="Don Cheadle, Robert Downey Jr., Gwyneth Paltrow, and Scarlett Johansson in Iron Man 2 (2010)" title="Don Cheadle, Robert Downey Jr., Gwyneth Paltrow, and Scarlett Johansson in Iron Man 2 (2010)" class="image_overlay overlay_mouseout" src="https://m.media-amazon.com/images/G/01/IMDb/icon/external-button._CB304896345_.png" data-src-x2="https://m.media-amazon.com/images/G/01/IMDb/icon/external-button._CB304896345_.png" /> <img alt="Don Cheadle, Robert Downey Jr., Gwyneth Paltrow, and Scarlett Johansson in Iron Man 2 (2010)" title="Don Cheadle, Robert Downey Jr., Gwyneth Paltrow, and Scarlett Johansson in Iron Man 2 (2010)" class="image_overlay overlay_mouseover" src="https://m.media-amazon.com/images/G/01/IMDb/icon/external-button-hover._CB304896345_.png" data-src-x2="https://m.media-amazon.com/images/G/01/IMDb/icon/external-button-hover._CB304896345_.png" /> </a> </div> </div> </div> </div><div class="ninja_image ninja_image_fixed_padding widget_padding"></div><div class="ninja_image last_image" style="width:116px;height:auto;" > <div style="width:116px;height:auto;margin:0 auto;"> <div class="widget_image"> <div class="image"> <a href="/offsite/?page-action=offsite-amazon&token=BCYkyMc91A52iLQXS-9vdRWb3YKbCQ674-PTxMfVLnuZ6754gTDuCJGfKDa-yStWMeddGFgSvJCu%0D%0AOMDOdPwAKFrnBOlhWaw5ib_5N-1SPqVHxy6KIrGUgD65VctTOF4fJflI-GP2Jnui6jQBkvwVdX7K%0D%0Agp_qsSb-awddU1y1AzpBQHT2fPu0KRTt5PP3W-Hr2VFrCAVuKXZ3Gw29MUZvvhvEHgKfH8TpGiwv%0D%0AxZLOtC3vNVAPOjLDmcUmBVgvDsgxxj8dkYLKxeZGtXw_dZWbZPOh_w%0D%0A" > <img class="pri_image" title="Dwayne Johnson, Alexandra Daddario, Zac Efron, Ilfenesh Hadera, Jon Bass, and Kelly Rohrbach in Baywatch (2017)" alt="Dwayne Johnson, Alexandra Daddario, Zac Efron, Ilfenesh Hadera, Jon Bass, and Kelly Rohrbach in Baywatch (2017)" src="https://m.media-amazon.com/images/M/MV5BNTA4MjQ0ODQzNF5BMl5BanBnXkFtZTgwNzA5NjYzMjI@._V1_SY172_CR0,0,116,172_AL_.jpg" /> <img alt="Dwayne Johnson, Alexandra Daddario, Zac Efron, Ilfenesh Hadera, Jon Bass, and Kelly Rohrbach in Baywatch (2017)" title="Dwayne Johnson, Alexandra Daddario, Zac Efron, Ilfenesh Hadera, Jon Bass, and Kelly Rohrbach in Baywatch (2017)" class="image_overlay overlay_mouseout" src="https://m.media-amazon.com/images/G/01/IMDb/icon/external-button._CB304896345_.png" data-src-x2="https://m.media-amazon.com/images/G/01/IMDb/icon/external-button._CB304896345_.png" /> <img alt="Dwayne Johnson, Alexandra Daddario, Zac Efron, Ilfenesh Hadera, Jon Bass, and Kelly Rohrbach in Baywatch (2017)" title="Dwayne Johnson, Alexandra Daddario, Zac Efron, Ilfenesh Hadera, Jon Bass, and Kelly Rohrbach in Baywatch (2017)" class="image_overlay overlay_mouseover" src="https://m.media-amazon.com/images/G/01/IMDb/icon/external-button-hover._CB304896345_.png" data-src-x2="https://m.media-amazon.com/images/G/01/IMDb/icon/external-button-hover._CB304896345_.png" /> </a> </div> </div> </div> </div> </div> </div> </div> </div> <p class="blurb">Explore popular action and adventure titles available to stream with Prime Video.</p> <p class="seemore"><a href="/offsite/?page-action=offsite-amazon&token=BCYgYEuSUYOJM05bSzz27dK_DA2Lh87o4u6iwMls8KDF9fDCX8JHXpJ1-ZR5g9Scu9OZi9fujWtU%0D%0Ag1LYHqazwgbPOmh0lP7eL_RJBx0C4XyhekzT-vZMTr8Jj-BxH6igLd0IkxIhLH5jWFKjmQLO0Wk0%0D%0AekwqQ3RUPU81tACcho_JMvAcYjnXs384iGIerMKACuxqw7TAJQUm09UN6VxejwsO8OddLMJmexQV%0D%0AqpOqnZOoldO_4C8XwcCVh2bQZpfM0Ius%0D%0A" class="position_bottom supplemental" > Start your free trial</a></p>    </div>



        </span>



            <script type="text/javascript">
                if(typeof uex === 'function'){uex('ld','NinjaWidget',{wb:1});}
            </script>





        </div>




































        <a name="slot_center-30"></a>
        <div class="article">






            <script type="text/javascript">if(typeof uet === 'function'){uet('bb','NinjaWidget',{wb:1});}</script>




        <span class="ab_widget">



    <div class="ab_ninja">
<div class="widget_content no_inline_blurb"> <div class="widget_nested"> <div class="ninja_image_pack"> <div class="ninja_center"> <div class="ninja_image first_image last_image" style="width:624px;height:auto;" > <div style="width:624px;height:auto;margin:0 auto;"> <div class="widget_image"> <div class="image"> <a href="/tv" > <img class="pri_image" title="IMDb TV" alt="IMDb TV" src="https://m.media-amazon.com/images/G/01/IMDb/Freedive/IMDb_HomepageAd-InTheHeart._SY351_SX624_AL_.jpg" /> </a> </div> </div> </div> </div> </div> </div> </div> </div>    </div>



        </span>



            <script type="text/javascript">
                if(typeof uex === 'function'){uex('ld','NinjaWidget',{wb:1});}
            </script>





        </div>


    </div>
    <br class="clear"/>
</div>










                   <br class="clear" />
                </div>


                    <div id="rvi-div">
                        <div class="recently-viewed">
                        <div class="header">
                            <div class="rhs">
                                <a id="clear_rvi" href="#">Clear your history</a>
                            </div>
                            <h3>Recently Viewed</h3>
                        </div>
                            <div class="items">&nbsp;</div>
                        </div>
                    </div>


	<!-- no content received for slot: bottom_ad -->


<script>
    if (typeof uet == 'function') {
      uet("bb", "desktopFooter", {wb: 1});
    }
</script>




    <div id="footer" class="ft">
        <div class="container footer-grid-wrapper">
            <div class="row footer-row">
                <div class="col outside">
    <h3>IMDb Everywhere</h3>
    <div class="app-links">
    <a href="/offsite/?page-action=ft_app_apple&token=BCYsZT9p0lPqmyRFOSpjOWPhiBM8ojVJaOZHkcMfQTWeVrwBBJEOu_pfWNNGCa-W-70rXi2eqUIY%0D%0An5k7MQBs7BNmA9MWQTGpcCG8axlpYJFcbKe4pXfO546h1E7rscwsIO1WTIL83lZ86XbU323M2fDB%0D%0APRBsWv_7457p_m7Ej6MXEi9UUr2K5HRddt-uGMOCb9FykbWg4blx7uSEpWuerrbzhi0PtCzcJNoM%0D%0A82CrA_ezec8%0D%0A"
title="Get the IMDb App on the Apple App Store" target="_blank" > <span class="desktop-sprite appstore-apple" ></span>
</a>
    <a href="/offsite/?page-action=ft_app_google&token=BCYoKIXcC8RDe8Y7yfzUjSCFt4bWARbUQAdjEH0ljVmJmNtZUs_5UeDGLKIC3ons5O4P6CExP_Qv%0D%0AZCbk2f7z0F86RvIlREL_yCvUl9ZtHI-niQpzPf2vW29EBunb-oI6l0UCwcQuCR4SytvrhUGBCQjY%0D%0ASHG0yFJrXk65pkTSGO3S341MxIEx5dAFWfqRiywnjS2hdQ4VbdO_hRWdCmwMBS4A0B8DHu99gcIK%0D%0AAyIfP1sOqjg%0D%0A"
title="Get the IMDb app on Google Play" target="_blank" > <span class="desktop-sprite appstore-google" ></span>
</a>
    <a href="/offsite/?page-action=ft_app_amazon&token=BCYiUOhm0cIjeFOTcD94F94A_r_Zz-paA_dJ8qNEjvj9FS5SJyAYKJTQXimB5gsyjksvSYjn-I6c%0D%0AwfZ2YO-lOlJEr3sSoADAtBD2UesM8awNYs826FlYLdk-bNG64y_lfreOQHXAIpiYWs6iQjnXPhaw%0D%0AOGH-3Alb-cpDaiYXfLvsL-TInP1i4SqUHI_sk3S3raJUQa5cgO5_7-JjxfM75CQNL1SZ3SA3Iv1q%0D%0AfCLCTlIvepH1Ha2D8tHU3NP49Cl6kJAukfrwqcfds4-IKW3xRCyCAcQ8dt4MqWvpLpNycN3Vdj0%0D%0A"
title="Get the IMDb app on Amazon Appstore for Android" target="_blank" > <span class="desktop-sprite appstore-amazon" ></span>
</a>
    </div>

    <p>Find showtimes, watch trailers, browse photos, track your Watchlist and rate your favorite movies and TV shows on your phone or tablet!</p>

    <a href="https://m.imdb.com"
class="touchlink" >IMDb Mobile site</a>
                </div>
                <div class="col center">

    <h3>
      Follow IMDb on
      <div class="ft-social-links">
    <a href="/offsite/?page-action=fol_fb&token=BCYu6X3jflOWNZfGbbzEaLT1oREFUPndXyI7cYL24VUIaGsQLshSDLCpEFmxOvw9fimVdz0s2MtH%0D%0A4_N7DYxo5IcHFFjV5bOLSqx1xgGDvE_CIv7GfOy0HbFngbBcsshaFpqiaoKIm1BhwcrwIkHqAgTG%0D%0A3tsQ7zkObe4gV6IllkOtr4NQCRPqMdZlpNnCJ6Iv7bW_SVPTCsadripBnV8ot5S1aA%0D%0A"
title="Follow IMDb on Facebook" class="ft-social-links__link" target="_blank" > <svg class="ipl-icon ipl-facebook-icon ipl-icon--inherit-color ipl-icon--inline" width="24" height="24" xmlns="http://www.w3.org/2000/svg" fill="#000000" viewBox="0 0 24 24">
<path d="M20.896 2H3.104C2.494 2 2 2.494 2 3.104v17.792C2 21.506 2.494 22 3.104 22h9.579v-7.745h-2.607v-3.018h2.607V9.01c0-2.584 1.577-3.99 3.882-3.99 1.104 0 2.052.082 2.329.119v2.7h-1.598c-1.254 0-1.496.595-1.496 1.47v1.927h2.989l-.39 3.018h-2.6V22h5.097c.61 0 1.104-.494 1.104-1.104V3.104C22 2.494 21.506 2 20.896 2"/>
</svg>
</a>
    <a href="/offsite/?page-action=fol_inst&token=BCYifOfwtyAkuoUl8kCdQ1dn3DDYn2XpKDRIL1oA3nzyY8SQW2NFgLuH9sCcMr2x4GYIHnCli1OW%0D%0Ap7ah8wBAvRhQ5U6pvk6pATKMbGpdqCCgn9tJTvcBfS4X9beFAXKhtMKWXvggIEIQqcxEebQxpFAN%0D%0ARgBrKl9R8cGzI_bWSEN7vsRL9EaeWss4pLModm50qIbieVxcGytBNU5Go0D-roa7Gg%0D%0A"
title="Follow IMDb on Instagram" class="ft-social-links__link" target="_blank" > <svg class="ipl-icon ipl-instagram-icon ipl-icon--inherit-color ipl-icon--inline" width="24" height="24" xmlns="http://www.w3.org/2000/svg" fill="#000000" viewBox="0 0 24 24">
<path d="M11.997 2.04c-2.715 0-3.056.011-4.122.06-1.064.048-1.79.217-2.426.463a4.901 4.901 0 0 0-1.771 1.151 4.89 4.89 0 0 0-1.153 1.767c-.247.635-.416 1.36-.465 2.422C2.011 8.967 2 9.307 2 12.017s.011 3.049.06 4.113c.049 1.062.218 1.787.465 2.422a4.89 4.89 0 0 0 1.153 1.767 4.901 4.901 0 0 0 1.77 1.15c.636.248 1.363.416 2.427.465 1.066.048 1.407.06 4.122.06s3.055-.012 4.122-.06c1.064-.049 1.79-.217 2.426-.464a4.901 4.901 0 0 0 1.77-1.15 4.89 4.89 0 0 0 1.154-1.768c.247-.635.416-1.36.465-2.422.048-1.064.06-1.404.06-4.113 0-2.71-.012-3.05-.06-4.114-.049-1.062-.218-1.787-.465-2.422a4.89 4.89 0 0 0-1.153-1.767 4.901 4.901 0 0 0-1.77-1.15c-.637-.247-1.363-.416-2.427-.464-1.067-.049-1.407-.06-4.122-.06m0 1.797c2.67 0 2.985.01 4.04.058.974.045 1.503.207 1.856.344.466.181.8.397 1.15.746.349.35.566.682.747 1.147.137.352.3.88.344 1.853.048 1.052.058 1.368.058 4.032 0 2.664-.01 2.98-.058 4.031-.044.973-.207 1.501-.344 1.853a3.09 3.09 0 0 1-.748 1.147c-.35.35-.683.565-1.15.746-.352.137-.88.3-1.856.344-1.054.048-1.37.058-4.04.058-2.669 0-2.985-.01-4.039-.058-.974-.044-1.504-.207-1.856-.344a3.098 3.098 0 0 1-1.15-.746 3.09 3.09 0 0 1-.747-1.147c-.137-.352-.3-.88-.344-1.853-.049-1.052-.059-1.367-.059-4.031 0-2.664.01-2.98.059-4.032.044-.973.207-1.501.344-1.853a3.09 3.09 0 0 1 .748-1.147c.35-.349.682-.565 1.149-.746.352-.137.882-.3 1.856-.344 1.054-.048 1.37-.058 4.04-.058"/><path d="M11.997 15.342a3.329 3.329 0 0 1-3.332-3.325 3.329 3.329 0 0 1 3.332-3.326 3.329 3.329 0 0 1 3.332 3.326 3.329 3.329 0 0 1-3.332 3.325m0-8.449a5.128 5.128 0 0 0-5.134 5.124 5.128 5.128 0 0 0 5.134 5.123 5.128 5.128 0 0 0 5.133-5.123 5.128 5.128 0 0 0-5.133-5.124M18.533 6.69c0 .662-.537 1.198-1.2 1.198a1.198 1.198 0 1 1 1.2-1.197"/>
</svg>
</a>
    <a href="/offsite/?page-action=fol_twch&token=BCYj0gaOpx6HwnZMagfUOYpxxdoYx4kUJbl-3Q_Rt17_P7nN8fhOaNEMBDf4mz7m44bCLeQA2XVR%0D%0ASBsEI_3CWaCPIr96hbIfuCqsO88NiTKfMjJ15s3bzKfo1g1qj_oWWMSItpn0W7ZbUWxdUlGqHwtl%0D%0AXn33s-in7RNk7sEUuufn2w7FayhTPCQ328O-mi99uNf-PxBZSw0Ndr2bjrMoqhlsmg%0D%0A"
title="Follow IMDb on Twitch" class="ft-social-links__link" target="_blank" > <svg class="ipl-icon ipl-twitch-icon ipl-icon--inherit-color ipl-icon--inline" width="24" height="24" xmlns="http://www.w3.org/2000/svg" fill="#000000" viewBox="0 0 24 24">
<g><path d="M3.40641795,2 L22.0023886,2 L22.0023886,14.8140302 L16.5329854,20.2834333 L12.4700003,20.2834333 L9.81343304,22.9400005 L7.00059714,22.9400005 L7.00059714,20.2834333 L2,20.2834333 L2,5.5941792 L3.40641795,2 Z M20.1271646,13.8764182 L20.1271646,3.87522393 L5.12537321,3.87522393 L5.12537321,17.0017914 L9.34462705,17.0017914 L9.34462705,19.6583587 L12.0011943,17.0017914 L17.0017914,17.0017914 L20.1271646,13.8764182 Z"></path><polygon points="17.0017914 7.46940312 17.0017914 12.9388062 15.1265675 12.9388062 15.1265675 7.46940312"></polygon><polygon points="12.0011943 7.46940312 12.0011943 12.9388062 10.1259704 12.9388062 10.1259704 7.46940312"></polygon></g>
<path d="M0 0h24v24H0z" fill="none"/>
</svg>
</a>
    <a href="/offsite/?page-action=fol_tw&token=BCYkQ6XIfnMCteyF5QZ_HE8zdP6U7sxb4CrFX2_gGAPb6tgqbXz7dnXA5t7l7yVUNjLNLG1B7wyy%0D%0ACLs7qdHmD953Fv2s6xZEfYRt7pOtz5YGBwWFSi_6fhUmXEwNSVQCuMsZmIAmeBpGj_5h6DyKUhYW%0D%0AhNDgcDXkQXsrXSD6x5kVQLQ1SlgoUjTozQ2irZJ_EgnxMcpG5agUjCMRNYA2PCUSWA%0D%0A"
title="Follow IMDb on Twitter" class="ft-social-links__link" target="_blank" > <svg class="ipl-icon ipl-twitter-icon ipl-icon--inherit-color ipl-icon--inline" width="24" height="24" xmlns="http://www.w3.org/2000/svg" fill="#000000" viewBox="0 0 24 24">
<path d="M8.29 19.936c7.547 0 11.675-6.13 11.675-11.446 0-.175-.004-.348-.012-.52A8.259 8.259 0 0 0 22 5.886a8.319 8.319 0 0 1-2.356.633 4.052 4.052 0 0 0 1.804-2.225c-.793.46-1.67.796-2.606.976A4.138 4.138 0 0 0 15.847 4c-2.266 0-4.104 1.802-4.104 4.023 0 .315.036.622.107.917a11.728 11.728 0 0 1-8.458-4.203 3.949 3.949 0 0 0-.556 2.022 4 4 0 0 0 1.826 3.348 4.136 4.136 0 0 1-1.858-.503l-.001.051c0 1.949 1.415 3.575 3.292 3.944a4.193 4.193 0 0 1-1.853.07c.522 1.597 2.037 2.76 3.833 2.793a8.34 8.34 0 0 1-5.096 1.722A8.51 8.51 0 0 1 2 18.13a11.785 11.785 0 0 0 6.29 1.807"/>
</svg>
</a>
    <a href="/offsite/?page-action=fol_yt&token=BCYq4-JDEXS6oap_z9K8B2icXAci-jd8FwLyX30hTL_YoLJJM_ltEn17uYjgbuyh-97sicA-Hxq5%0D%0AmLNtx7jy6n7i-Yjj_tnbR_Lu8fhJjc5PSUssjteCpuxwB04KmOy0dW1vkYMTJLMmX97j4fvsCNN2%0D%0AkichSvjVDErBh9vcHx3UIDe-oafTKDVd6RE76qqncIihLrybqycvMTpQ38F8YGqn9A%0D%0A"
title="Follow IMDb on YouTube" class="ft-social-links__link" target="_blank" > <svg class="ipl-icon ipl-youtube-icon ipl-icon--inherit-color ipl-icon--inline" width="24" height="24" xmlns="http://www.w3.org/2000/svg" fill="#000000" viewBox="0 0 24 24">
<path d="M9.955 14.955v-5.91L15.182 12l-5.227 2.955zm11.627-7.769a2.505 2.505 0 0 0-1.768-1.768C18.254 5 12 5 12 5s-6.254 0-7.814.418c-.86.23-1.538.908-1.768 1.768C2 8.746 2 12 2 12s0 3.254.418 4.814c.23.86.908 1.538 1.768 1.768C5.746 19 12 19 12 19s6.254 0 7.814-.418a2.505 2.505 0 0 0 1.768-1.768C22 15.254 22 12 22 12s0-3.254-.418-4.814z"/>
<path d="M0 0h24v24H0z" fill="none"/>
</svg>
</a>
      </div>
    </h3>
                </div>
                <div class="col outside">
    <div class="row">
        <div class="col col-4">
            <ul class="unstyled">
                <li><a href="/"
>Home</a></li>
                <li><a href="/chart/top"
>Top Rated Movies</a></li>
                <li><a href="/chart/"
>Box Office</a></li>
                <li><a href="/movies-coming-soon/"
>Coming Soon</a></li>
                <li><a href="/a2z"
>Site Index</a></li>
                <li><a href="/search"
>Search</a></li>
                <li><a href="/movies-in-theaters/"
>In Theaters</a></li>
            </ul>
        </div>
        <div class="col col-4">
            <ul class="unstyled">
                <li><a href="https://help.imdb.com/imdb"
>Contact Us</a></li>
                <li>        <a href="/registration/login"
>Register</a>
</li>
                <li><a href="/news/"
>News</a></li>
                <li class="spacer"></li>
                <li><a href="/pressroom/"
>Press Room</a></li>
                <li><a href="https://advertising.amazon.com/lp/imdb"
>Advertising</a></li>
                <li><a href="/jobs"
>Jobs</a></li>
            </ul>
        </div>
        <div class="col col-4">
            <ul class="unstyled">
                <li><a href="https://pro.imdb.com/signup/index.html?rf=cons_ft_hm"
>IMDbPro</a></li>
                <li>    <a href="/offsite/?page-action=ft-mojo&token=BCYua5lecWJbiWzWYVmnaS6mf1wN5Eagv6FsnAFUeQ4bbMEyB2XNO11YGg0yDZtL73rfvqARLnzn%0D%0AMpm23p6cpDz6f7PGqKXntobP757kWLQJP1G8hE32u06H-palj0TMQQaXMJJYXCk9AekOw7u8WCqb%0D%0A4008v-L_2c1YfFvMB-flOMuVrEXPU2MHEFEEpRj13Xq0Bb7nl-TgwR0Ad9RDlCQzEw%0D%0A"
>Box Office Mojo</a>
</li>
                <li class="spacer"></li>
                <li><a href="/conditions"
>Conditions of Use</a></li>
                <li><a href="/privacy"
>Privacy Policy</a></li>
                <li>    <a href="/offsite/?page-action=ft-iba&token=BCYnq6v6P868ux9S7-TOMvsTdol36zZ03QP_vzfo6l0pO_PQtXdoO9LdS5JAsNpwZ9PYxozfybzw%0D%0Ahh4QZhiRGPOnLTVyKU6g4uUl4SewhKgxPyNquYIQ5FVQPXQ-LTsJPQmkUP-k1b8aRMHHIoww-OB1%0D%0AXqawDQddnYVbNUdodoLPQ2hVgeHLi-WQpHPMczFEvnbv5WH6KKvzQNLKYi3-N3YTqHIQFCaZRlVb%0D%0AnRfzXAGOorFnrT9cDkyndNmv64Qyk9lc%0D%0A"
>Interest-Based Ads</a>
</li>
                <li class="spacer"></li>
            </ul>
        </div>
    </div>
                </div>
            </div>
        </div>

        <div class="container">
            <div class="ft-copy float-right">
                <a href="/conditions"
>Copyright &copy;</a> 1990-2019
                <a href="https://help.imdb.com/imdb"
>IMDb.com, Inc.</a>
            </div>
            <div>
                <span class="footer_logo" align="center">
                    <svg width="135" height="22" viewBox="0 0 267 28" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                        <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <path d="M97.231,21.898 C91.832,25.881 84.005,28 77.266,28 C67.821,28 59.314,24.508 52.878,18.696 C52.372,18.24 52.823,17.617 53.43,17.97 C60.375,22.011 68.963,24.445 77.833,24.445 C83.816,24.445 90.394,23.203 96.446,20.636 C97.359,20.249 98.123,21.237 97.231,21.898" fill="#FF9900"></path>
                            <path d="M99.477,19.332 C98.786,18.448 94.913,18.913 93.172,19.122 C92.645,19.186 92.564,18.725 93.038,18.391 C96.129,16.221 101.192,16.848 101.781,17.574 C102.373,18.308 101.625,23.384 98.73,25.806 C98.283,26.179 97.86,25.981 98.057,25.488 C98.71,23.86 100.168,20.217 99.477,19.332" fill="#FF9900"></path>
                            <path d="M93.324,3.058 L93.324,0.949 C93.326,0.628 93.567,0.414 93.859,0.415 L103.311,0.414 C103.614,0.414 103.856,0.634 103.856,0.946 L103.856,2.755 C103.853,3.059 103.597,3.454 103.144,4.082 L98.248,11.073 C100.065,11.031 101.988,11.304 103.64,12.232 C104.012,12.441 104.112,12.75 104.141,13.055 L104.141,15.306 C104.141,15.614 103.802,15.974 103.445,15.787 C100.536,14.263 96.675,14.097 93.457,15.806 C93.129,15.981 92.785,15.627 92.785,15.316 L92.785,13.178 C92.785,12.835 92.791,12.25 93.137,11.729 L98.81,3.59 L93.87,3.589 C93.568,3.589 93.326,3.374 93.324,3.058" fill="#232F3E"></path>
                            <path d="M58.843,16.231 L55.968,16.231 C55.694,16.213 55.476,16.007 55.453,15.744 L55.456,0.985 C55.456,0.69 55.703,0.454 56.01,0.454 L58.689,0.453 C58.968,0.468 59.194,0.68 59.212,0.949 L59.212,2.876 L59.265,2.876 C59.963,1.012 61.278,0.143 63.05,0.143 C64.848,0.143 65.976,1.012 66.781,2.876 C67.479,1.012 69.063,0.143 70.755,0.143 C71.962,0.143 73.278,0.639 74.083,1.758 C74.995,3 74.808,4.801 74.808,6.385 L74.805,15.699 C74.805,15.993 74.557,16.231 74.251,16.231 L71.379,16.231 C71.09,16.212 70.863,15.983 70.863,15.701 L70.862,7.875 C70.862,7.256 70.915,5.702 70.781,5.112 C70.566,4.117 69.922,3.838 69.09,3.838 C68.392,3.838 67.668,4.304 67.372,5.049 C67.077,5.795 67.103,7.037 67.103,7.875 L67.103,15.699 C67.103,15.993 66.855,16.231 66.549,16.231 L63.677,16.231 C63.388,16.212 63.16,15.983 63.16,15.701 L63.157,7.875 C63.157,6.23 63.426,3.808 61.385,3.808 C59.319,3.808 59.399,6.167 59.399,7.875 L59.398,15.699 C59.398,15.993 59.15,16.231 58.843,16.231" fill="#232F3E"></path>
                            <path d="M111.994,0.143 C116.262,0.143 118.57,3.808 118.57,8.466 C118.57,12.969 116.021,16.542 111.994,16.542 C107.806,16.542 105.525,12.876 105.525,8.312 C105.525,3.714 107.832,0.143 111.994,0.143 M112.02,3.155 C109.899,3.155 109.765,6.043 109.765,7.845 C109.765,9.647 109.739,13.497 111.994,13.497 C114.222,13.497 114.329,10.392 114.329,8.497 C114.329,7.255 114.276,5.764 113.899,4.584 C113.577,3.559 112.932,3.155 112.02,3.155" fill="#232F3E"></path>
                            <path d="M124.106,16.231 L121.24,16.231 C120.952,16.212 120.725,15.983 120.725,15.701 L120.719,0.936 C120.744,0.666 120.982,0.454 121.272,0.454 L123.94,0.453 C124.191,0.467 124.398,0.637 124.451,0.866 L124.451,3.124 L124.505,3.124 C125.311,1.105 126.437,0.143 128.424,0.143 C129.712,0.143 130.974,0.607 131.78,1.882 C132.531,3.062 132.531,5.049 132.531,6.478 L132.531,15.766 C132.499,16.027 132.264,16.231 131.98,16.231 L129.097,16.231 C128.831,16.213 128.616,16.018 128.585,15.766 L128.585,7.752 C128.585,6.137 128.773,3.776 126.787,3.776 C126.089,3.776 125.445,4.242 125.122,4.956 C124.719,5.857 124.666,6.758 124.666,7.752 L124.666,15.699 C124.66,15.993 124.412,16.231 124.106,16.231" fill="#232F3E"></path>
                            <path d="M90.909,13.525 C90.384,12.8 89.824,12.209 89.824,10.861 L89.824,6.381 C89.824,4.482 89.959,2.738 88.559,1.432 C87.457,0.372 85.628,0 84.228,0 C81.492,0 78.439,1.022 77.797,4.402 C77.73,4.762 77.991,4.95 78.227,5.004 L81.013,5.306 C81.274,5.293 81.463,5.036 81.513,4.776 C81.753,3.612 82.728,3.05 83.825,3.05 C84.417,3.05 85.089,3.268 85.439,3.797 C85.843,4.389 85.789,5.197 85.789,5.883 L85.789,6.256 C84.12,6.443 81.942,6.567 80.382,7.252 C78.579,8.03 77.315,9.618 77.315,11.953 C77.315,14.94 79.198,16.435 81.618,16.435 C83.664,16.435 84.781,15.952 86.36,14.345 C86.883,15.1 87.053,15.466 88.009,16.26 C88.223,16.376 88.497,16.364 88.688,16.193 L88.695,16.2 C89.269,15.689 90.313,14.782 90.9,14.29 C91.134,14.099 91.094,13.788 90.909,13.525 M85.789,9.183 C85.789,10.304 85.816,11.236 85.25,12.232 C84.794,13.042 84.066,13.54 83.26,13.54 C82.157,13.54 81.512,12.699 81.512,11.454 C81.512,9.005 83.708,8.56 85.789,8.56 L85.789,9.183" fill="#232F3E"></path>
                            <path d="M53.211,13.525 C52.685,12.8 52.125,12.209 52.125,10.861 L52.125,6.381 C52.125,4.482 52.26,2.738 50.861,1.432 C49.758,0.372 47.929,0 46.53,0 C43.792,0 40.739,1.022 40.099,4.402 C40.031,4.762 40.293,4.95 40.529,5.004 L43.316,5.306 C43.576,5.293 43.765,5.036 43.815,4.776 C44.054,3.612 45.03,3.05 46.127,3.05 C46.718,3.05 47.39,3.268 47.74,3.797 C48.144,4.389 48.09,5.197 48.09,5.883 L48.09,6.256 C46.423,6.443 44.242,6.567 42.683,7.252 C40.88,8.03 39.616,9.618 39.616,11.953 C39.616,14.94 41.499,16.435 43.921,16.435 C45.965,16.435 47.083,15.952 48.662,14.345 C49.183,15.1 49.354,15.466 50.31,16.26 C50.525,16.376 50.8,16.364 50.989,16.193 L50.996,16.2 C51.57,15.689 52.614,14.782 53.201,14.29 C53.436,14.099 53.394,13.788 53.211,13.525 M48.09,9.183 C48.09,10.304 48.117,11.236 47.552,12.232 C47.095,13.042 46.368,13.54 45.561,13.54 C44.459,13.54 43.812,12.699 43.812,11.454 C43.812,9.005 46.01,8.56 48.09,8.56 L48.09,9.183" fill="#232F3E"></path>
                            <path d="M4.85,16.634 C3.379,16.634 2.202,16.215 1.321,15.376 C0.44,14.535 0,13.411 0,12.002 C0,10.488 0.538,9.281 1.616,8.379 C2.694,7.478 4.146,7.026 5.97,7.026 C7.131,7.026 8.436,7.202 9.887,7.556 L9.887,5.503 C9.887,4.384 9.633,3.597 9.126,3.14 C8.617,2.684 7.753,2.456 6.53,2.456 C5.099,2.456 3.7,2.664 2.332,3.078 C1.854,3.224 1.554,3.295 1.43,3.295 C1.181,3.295 1.057,3.109 1.057,2.736 L1.057,1.897 C1.057,1.627 1.098,1.43 1.181,1.305 C1.264,1.181 1.43,1.068 1.679,0.963 C2.321,0.674 3.135,0.44 4.119,0.264 C5.104,0.088 6.083,0 7.058,0 C9.028,0 10.479,0.409 11.411,1.228 C12.344,2.047 12.81,3.295 12.81,4.974 L12.81,15.608 C12.81,16.023 12.603,16.231 12.188,16.231 L10.852,16.231 C10.457,16.231 10.229,16.033 10.167,15.64 L10.012,14.613 C9.266,15.256 8.442,15.754 7.54,16.106 C6.638,16.458 5.741,16.634 4.85,16.634 M5.597,14.303 C6.281,14.303 6.996,14.168 7.742,13.898 C8.488,13.63 9.204,13.235 9.887,12.716 L9.887,9.546 C8.768,9.276 7.67,9.141 6.592,9.141 C4.249,9.141 3.078,10.042 3.078,11.847 C3.078,12.635 3.295,13.24 3.731,13.665 C4.167,14.09 4.788,14.303 5.597,14.303" fill="#232F3E"></path>
                            <path d="M18.003,16.231 C17.588,16.231 17.381,16.023 17.381,15.608 L17.381,1.088 C17.381,0.673 17.588,0.466 18.003,0.466 L19.37,0.466 C19.578,0.466 19.738,0.508 19.852,0.59 C19.966,0.673 20.044,0.829 20.086,1.057 L20.273,2.207 C22.241,0.735 24.315,0 26.491,0 C28.004,0 29.155,0.398 29.942,1.196 C30.73,1.995 31.124,3.151 31.124,4.664 L31.124,15.608 C31.124,16.023 30.917,16.231 30.503,16.231 L28.668,16.231 C28.253,16.231 28.046,16.023 28.046,15.608 L28.046,5.69 C28.046,4.592 27.823,3.782 27.377,3.265 C26.931,2.746 26.232,2.486 25.279,2.486 C23.641,2.486 22.034,3.016 20.459,4.073 L20.459,15.608 C20.459,16.023 20.251,16.231 19.837,16.231 L18.003,16.231" fill="#232F3E"></path>
                            <path d="M148.483,16.572 C146.037,16.572 144.166,15.872 142.871,14.474 C141.575,13.074 140.927,11.048 140.927,8.395 C140.927,5.763 141.595,3.726 142.932,2.285 C144.27,0.845 146.161,0.124 148.607,0.124 C149.726,0.124 150.825,0.32 151.903,0.715 C152.131,0.798 152.292,0.901 152.385,1.025 C152.478,1.149 152.525,1.357 152.525,1.648 L152.525,2.486 C152.525,2.902 152.389,3.108 152.12,3.108 C152.016,3.108 151.851,3.078 151.624,3.016 C150.773,2.767 149.913,2.643 149.043,2.643 C147.302,2.643 146.047,3.083 145.28,3.964 C144.512,4.845 144.13,6.249 144.13,8.178 L144.13,8.581 C144.13,10.468 144.518,11.852 145.296,12.732 C146.073,13.613 147.302,14.054 148.98,14.054 C149.851,14.054 150.784,13.909 151.779,13.618 C152.007,13.557 152.162,13.525 152.245,13.525 C152.514,13.525 152.649,13.732 152.649,14.148 L152.649,14.986 C152.649,15.256 152.608,15.453 152.525,15.577 C152.442,15.701 152.276,15.815 152.027,15.92 C151.011,16.355 149.83,16.572 148.483,16.572" fill="#232F3E"></path>
                            <path d="M162.319,16.696 C159.956,16.696 158.11,15.961 156.785,14.489 C155.458,13.018 154.795,10.966 154.795,8.332 C154.795,5.722 155.458,3.679 156.785,2.207 C158.11,0.735 159.956,0 162.319,0 C164.682,0 166.527,0.735 167.853,2.207 C169.18,3.679 169.844,5.722 169.844,8.332 C169.844,10.966 169.18,13.018 167.853,14.489 C166.527,15.961 164.682,16.696 162.319,16.696 M162.319,14.21 C165.242,14.21 166.703,12.25 166.703,8.332 C166.703,4.436 165.242,2.487 162.319,2.487 C159.396,2.487 157.935,4.436 157.935,8.332 C157.935,12.25 159.396,14.21 162.319,14.21" fill="#232F3E"></path>
                            <path d="M174.259,16.231 C173.844,16.231 173.637,16.023 173.637,15.608 L173.637,1.088 C173.637,0.673 173.844,0.466 174.259,0.466 L175.627,0.466 C175.835,0.466 175.995,0.508 176.108,0.59 C176.222,0.673 176.301,0.829 176.342,1.057 L176.529,2.052 C178.519,0.684 180.457,0 182.344,0 C184.271,0 185.577,0.735 186.261,2.207 C188.313,0.735 190.365,0 192.417,0 C193.847,0 194.946,0.403 195.713,1.212 C196.48,2.021 196.864,3.171 196.864,4.664 L196.864,15.608 C196.864,16.023 196.657,16.231 196.242,16.231 L194.407,16.231 C193.992,16.231 193.785,16.023 193.785,15.608 L193.785,5.534 C193.785,4.498 193.588,3.731 193.195,3.232 C192.801,2.735 192.178,2.486 191.329,2.486 C189.815,2.486 188.292,2.953 186.759,3.886 C186.779,4.031 186.79,4.187 186.79,4.353 L186.79,15.608 C186.79,16.023 186.582,16.231 186.168,16.231 L184.333,16.231 C183.918,16.231 183.712,16.023 183.712,15.608 L183.712,5.534 C183.712,4.498 183.513,3.731 183.121,3.232 C182.726,2.735 182.104,2.486 181.255,2.486 C179.679,2.486 178.166,2.943 176.715,3.855 L176.715,15.608 C176.715,16.023 176.508,16.231 176.093,16.231 L174.259,16.231" fill="#232F3E"></path>
                            <path d="M202.025,22.636 C201.61,22.636 201.403,22.428 201.403,22.014 L201.403,1.088 C201.403,0.673 201.61,0.466 202.025,0.466 L203.393,0.466 C203.807,0.466 204.047,0.673 204.108,1.088 L204.263,2.083 C205.84,0.694 207.591,0 209.519,0 C211.529,0 213.115,0.731 214.276,2.191 C215.436,3.652 216.017,5.638 216.017,8.146 C216.017,10.695 215.406,12.737 214.182,14.272 C212.96,15.805 211.332,16.572 209.302,16.572 C207.435,16.572 205.829,15.961 204.481,14.738 L204.481,22.014 C204.481,22.428 204.273,22.636 203.859,22.636 L202.025,22.636 Z M208.586,14.085 C211.446,14.085 212.877,12.157 212.877,8.302 C212.877,6.332 212.529,4.871 211.835,3.918 C211.14,2.964 210.078,2.486 208.648,2.486 C207.176,2.486 205.788,2.964 204.481,3.918 L204.481,12.592 C205.829,13.587 207.196,14.085 208.586,14.085 Z" fill="#232F3E"></path>
                            <path d="M223.666,16.634 C222.194,16.634 221.017,16.215 220.136,15.376 C219.255,14.535 218.815,13.411 218.815,12.002 C218.815,10.488 219.354,9.281 220.432,8.379 C221.51,7.478 222.961,7.026 224.785,7.026 C225.946,7.026 227.252,7.202 228.703,7.556 L228.703,5.503 C228.703,4.384 228.448,3.597 227.941,3.14 C227.432,2.684 226.568,2.456 225.345,2.456 C223.915,2.456 222.515,2.664 221.147,3.078 C220.67,3.224 220.37,3.295 220.245,3.295 C219.997,3.295 219.872,3.109 219.872,2.736 L219.872,1.897 C219.872,1.627 219.914,1.43 219.997,1.305 C220.079,1.181 220.245,1.068 220.494,0.963 C221.136,0.674 221.95,0.44 222.934,0.264 C223.919,0.088 224.898,0 225.874,0 C227.843,0 229.294,0.409 230.226,1.228 C231.16,2.047 231.626,3.295 231.626,4.974 L231.626,15.608 C231.626,16.023 231.418,16.231 231.004,16.231 L229.667,16.231 C229.272,16.231 229.045,16.033 228.982,15.64 L228.827,14.613 C228.081,15.256 227.258,15.754 226.355,16.106 C225.453,16.458 224.556,16.634 223.666,16.634 M224.412,14.303 C225.095,14.303 225.811,14.168 226.557,13.898 C227.303,13.63 228.019,13.235 228.703,12.716 L228.703,9.546 C227.584,9.276 226.485,9.141 225.407,9.141 C223.064,9.141 221.893,10.042 221.893,11.847 C221.893,12.635 222.111,13.24 222.547,13.665 C222.982,14.09 223.603,14.303 224.412,14.303" fill="#232F3E"></path>
                            <path d="M236.818,16.231 C236.404,16.231 236.197,16.023 236.197,15.608 L236.197,1.088 C236.197,0.673 236.404,0.466 236.818,0.466 L238.186,0.466 C238.393,0.466 238.554,0.508 238.668,0.59 C238.782,0.673 238.86,0.829 238.901,1.057 L239.089,2.207 C241.057,0.735 243.131,0 245.306,0 C246.82,0 247.97,0.398 248.758,1.196 C249.546,1.995 249.94,3.151 249.94,4.664 L249.94,15.608 C249.94,16.023 249.732,16.231 249.318,16.231 L247.483,16.231 C247.068,16.231 246.861,16.023 246.861,15.608 L246.861,5.69 C246.861,4.592 246.638,3.782 246.193,3.265 C245.747,2.746 245.048,2.486 244.094,2.486 C242.457,2.486 240.85,3.016 239.274,4.073 L239.274,15.608 C239.274,16.023 239.067,16.231 238.652,16.231 L236.818,16.231" fill="#232F3E"></path>
                            <path d="M255.319,23.009 C254.655,23.009 254.064,22.937 253.547,22.791 C253.298,22.729 253.127,22.625 253.034,22.481 C252.94,22.335 252.893,22.128 252.893,21.858 L252.893,21.05 C252.893,20.656 253.049,20.458 253.36,20.458 C253.464,20.458 253.619,20.48 253.826,20.522 C254.033,20.563 254.313,20.584 254.666,20.584 C255.432,20.584 256.039,20.391 256.485,20.008 C256.93,19.624 257.329,18.945 257.682,17.972 L258.272,16.386 L252.271,1.585 C252.127,1.233 252.054,0.984 252.054,0.839 C252.054,0.591 252.199,0.466 252.49,0.466 L254.355,0.466 C254.686,0.466 254.915,0.518 255.039,0.622 C255.164,0.726 255.287,0.953 255.412,1.306 L259.765,13.37 L263.964,1.306 C264.088,0.953 264.212,0.726 264.336,0.622 C264.461,0.518 264.688,0.466 265.02,0.466 L266.76,0.466 C267.051,0.466 267.197,0.591 267.197,0.839 C267.197,0.984 267.124,1.233 266.979,1.585 L260.138,18.997 C259.579,20.428 258.926,21.453 258.179,22.075 C257.433,22.697 256.48,23.009 255.319,23.009" fill="#232F3E"></path>
                        </g>
                    </svg>
                </span>
            </div>
        </div>


    <table class="footer" id="amazon-affiliates">
        <tr>
            <td colspan="8">
                Amazon Affiliates
            </td>
        </tr>
        <tr>

    <td>
        <div>
            <a href="/offsite/?page-action=ft-piv&token=BCYvUoO4wzoAr7KEtRjs50PXQjP8CuodtszlUxND9VLWnQnODvLffAmQatVcQsUJzrNJ8PAxhoDB%0D%0AIL02gL-WgwmSOfURgTTIW9K5X7u_NDsmcilEJS9JPEiFKa66HT2vcqvst5OB5gQ4jKm6QLFZADOq%0D%0AdvIxYorDG_kD-t-G6ox7Q2OyJ4BhnJN_-BlJ8NIzQiTfmthIdzRb7sfDJ_Kc0wQFJqyNHRtqmx5L%0D%0A4DXLEa4wqkI%0D%0A" class="amazon-affiliate-site-link">
                <span class="amazon-affiliate-site-name">Prime Video</span><br>
                <span class="amazon-affiliate-site-desc">Unlimited Streaming<br>of Movies & TV</span>
            </a>
        </div>
    </td>

    <td>
        <div>
            <a href="/offsite/?page-action=ft-amzn-uk&token=BCYjrWjg6HxS44LQ1fFju1NlnKB1t6fC4q6IQFtAgYEwT-h3o3ycAmUYsSUWBnUqfrIinizYRM9x%0D%0AUl4_MSeQnpcaDC0UUw4Ic1h5JolL_LW9TxAvCG9Yp7bUaEuq7PApo2z9jFekyxi8GbM94di5s56t%0D%0AqFE6FUgoZAM60Thx4eZugQb57nBTnEv9sMorNuxikn9lsB4bpkxph1rxg-W9RAGlWSA03NvtwNnL%0D%0AfZp0AgcXU30%0D%0A" class="amazon-affiliate-site-link">
                <span class="amazon-affiliate-site-name">Amazon UK</span><br>
                <span class="amazon-affiliate-site-desc">Buy Movies on<br>DVD & Blu-ray</span>
            </a>
        </div>
    </td>

    <td>
        <div>
            <a href="/offsite/?page-action=ft-amzn-de&token=BCYkj8NlKbZzDoToPRMl8busY0Vvfv-smCq3NnqkqJqchOZ4TEtWzhHergJuc5dRLx8WMo8-S9X0%0D%0ACbrwe70iG2JdvG0D9slE55xjAUJ_avTtw4JYO-jr1xc9JqzViM-laVQ_LXxbYpelsE4FmxqGiDSN%0D%0ArjtBhlX2z5GtrZAJN3yqkTECVOV7aFW67-HaWsk8sZWYaJNxUNiX8H3MfN00DeNIZK-MeTD7dscM%0D%0AiJhmsowVsa0%0D%0A" class="amazon-affiliate-site-link">
                <span class="amazon-affiliate-site-name">Amazon Germany</span><br>
                <span class="amazon-affiliate-site-desc">Buy Movies on<br>DVD & Blu-ray</span>
            </a>
        </div>
    </td>

    <td>
        <div>
            <a href="/offsite/?page-action=ft-amzn-it&token=BCYuep9WMN_KGmPkcQfdSN08ZM2aPDEVp7ewDC-fUyfGhJEB3TJmR6xtiRUsYmX9g0NJWPrBt9v1%0D%0AA1A2uj6qXC9R9KSZP6J3rdSNjIa1KJNKC2teTrO8NZ0_HW5jxv8K1z6xMDAMjv1fVUG2xSapwH9F%0D%0AIHkcEqJXGhF2NzFRaOnmvs7Te4TGytsp7yY4KR61rSEN1jcdekMfRU3TPrgIoETELFD0h6-_B5fy%0D%0AVkcYNqD7shA%0D%0A" class="amazon-affiliate-site-link">
                <span class="amazon-affiliate-site-name">Amazon Italy</span><br>
                <span class="amazon-affiliate-site-desc">Buy Movies on<br>DVD & Blu-ray</span>
            </a>
        </div>
    </td>

    <td>
        <div>
            <a href="/offsite/?page-action=ft-amzn-fr&token=BCYtT4dT5MvMKdj9sGesEobijV1GwZxCan6RGFP6f5WSJxD25dTDQCPLnIckjT3rEh9hhxGAzO9i%0D%0AePLmtdFvPOHRpcJVD7GD9L_9AVgOXAGbocxWV3EOhDdz_G_C4v6GlGmUVxDAMry5JN-V7EwVqYXf%0D%0AsPyAJs2ON_FBsAdYBJkIVUcjDUKkXhiPNqPJLgUQy-W7yZShsVGqdOzK-MLU4N8bWovm-wFX8Yj5%0D%0A18GjkzfNdwY%0D%0A" class="amazon-affiliate-site-link">
                <span class="amazon-affiliate-site-name">Amazon France</span><br>
                <span class="amazon-affiliate-site-desc">Buy Movies on<br>DVD & Blu-ray</span>
            </a>
        </div>
    </td>

    <td>
        <div>
            <a href="/offsite/?page-action=ft-amzn-in&token=BCYgh7R-kWjdWobz6e5EfMWzG6BY7oXmKtalFIC7kcapZXHs56BywzS5OfOxRR-jwNCEAYffxKwF%0D%0A6-KwICzPkFA7q7fZ2CLO64X9ITdNOdi2HZ5saGniQNLsF-TK3BlRWqFTEVZpYhRQ1VlVKLtXlaSZ%0D%0At5nfT7aLAMPmPGD2GNDXrDyoGm5pds5IDxIKoD8s5sJd-WVPLKc2GU5tik9RBap7SQNKoWOvV_KS%0D%0AtD2IA_Ek_Qo4shELDpi7K_7_b7RzFbeQ%0D%0A" class="amazon-affiliate-site-link">
                <span class="amazon-affiliate-site-name">Amazon India</span><br>
                <span class="amazon-affiliate-site-desc">Buy Movie and<br>TV Show DVDs</span>
            </a>
        </div>
    </td>

    <td>
        <div>
            <a href="/offsite/?page-action=ft-amzn-dpr&token=BCYpzwuXx6RYuc2X1TtAToBygDN8b03A70aIQ6hDuVC93pWG0yQC6--eWhelGnHQ7--_BLKpxoJf%0D%0AaQXemijF4UiU3VX2goZAcfsNHTBm98fnjkBsa4wJ-YwPRvdwj13dIw-WwL_VrlrP3Kwnztgt0gyX%0D%0AcEQm8lYd0KiXDxgHLlhfHME%0D%0A" class="amazon-affiliate-site-link">
                <span class="amazon-affiliate-site-name">DPReview</span><br>
                <span class="amazon-affiliate-site-desc">Digital<br>Photography</span>
            </a>
        </div>
    </td>

    <td>
        <div>
            <a href="/offsite/?page-action=ft-amzn-aud&token=BCYikR4ZD_N844pF0VIfhSqrMZG0mS3axiBDpiAYlJ2YNpwoYdOYiWje27MbDlciKVwMu6s-nZsT%0D%0AULjj6QMzQDRQN0F8L3ZBNVikIvtdhmCd3wOYGlsMuROe8Gw0uOXAlK_C742hhT-B0ONgCwAugsgE%0D%0A75aQ3IyVVFAUHRtUmbSPH5A%0D%0A" class="amazon-affiliate-site-link">
                <span class="amazon-affiliate-site-name">Audible</span><br>
                <span class="amazon-affiliate-site-desc">Download<br>Audio Books</span>
            </a>
        </div>
    </td>
        </tr>
    </table>
    </div>
<script>
    if (typeof uet == 'function') {
      uet("be", "desktopFooter", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "desktopFooter", {wb: 1});
    }
</script>

    <script type="text/javascript">
        try {
            window.lumierePlayer = window.lumierePlayer || {};
            window.lumierePlayer.weblab = JSON.parse('{"IMDB_TV_REBRAND_212999":"T1","IMDB_VIDEO_PLAYER_162496":"C","IMDB_RELATED_VIDEOS_196868":"T1"}');
        } catch (error) {
            if (window.ueLogError) {
                window.ueLogError(error, {
                    logLevel: "WARN",
                    attribution: "videoplayer",
                    message: "Failed to parse weblabs for video player."
                });
            }
        }
    </script>
            </div>
        </div>

<script>
    if (typeof uet == 'function') {
      uet("bb", "LoadHeaderJS", {wb: 1});
    }
</script>



<script type="text/javascript" src="https://m.media-amazon.com/images/G/01/imdb/js/collections/common-3894086353._CB441580138_.js"></script>
<script type="text/javascript" src="https://m.media-amazon.com/images/G/01/imdb/js/collections/title-516316067._CB438917083_.js"></script>




<script>
    if (typeof uet == 'function') {
      uet("be", "LoadFooterJS", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "LoadFooterJS", {wb: 1});
    }
</script>

        <div id="servertime" time="515"/>



<script>
    if (typeof uet == 'function') {
      uet("be");
    }
</script>

    </body>
</html>


        '''
        # endregion
        expected_output = (1133953, 8.6, 24)

        actual_output = imdbratings._parse_imdb_result(input_model)

        self.assertEqual(expected_output, actual_output)

    def test_parse_imdb_page__error_return_Nones(self):
        input_model = ''
        expected_output = (None, None, None)

        actual_output = imdbratings._parse_imdb_result(input_model)

        self.assertEqual(expected_output, actual_output)

    def test_parse_imdb_page__changed_page_return_Nones(self):
        # region `input_model` changed IMDB page
        input_model = '''
<!DOCTYPE html>
<html
    <head>

        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <meta name="apple-itunes-app" content="app-id=342792525, app-argument=imdb:///title/tt0076759?src=mdot">

        <script type="text/javascript">var IMDbTimer={starttime: new Date().getTime(),pt:'java'};</script>
</head></body>

    </body>
</html>
        '''
        # endregion
        expected_output = (None, None, None)

        actual_output = imdbratings._parse_imdb_result(input_model)

        self.assertEqual(expected_output, actual_output)


    def test_assemble_imdbresult(self):
        input_model = 1, 2, 3
        expected_output = {'info': {'top250': 3}, 'ratings': {'imdb': {'rating': 2, 'votes': 1}}}

        actual_output = imdbratings._assemble_imdb_result(*input_model)

        self.assertDictEqual(expected_output, actual_output)


    def test_assemble_imdbresult__no_info_return_empty(self):
        input_model = None, None, None
        expected_output = {}

        actual_output = imdbratings._assemble_imdb_result(*input_model)

        self.assertDictEqual(expected_output, actual_output)

    def test_assemble_imdbresult__no_top250_return_rating(self):
        input_model = 1, 2, None
        expected_output = {'ratings': {'imdb': {'rating': 2, 'votes': 1}}}

        actual_output = imdbratings._assemble_imdb_result(*input_model)

        self.assertDictEqual(expected_output, actual_output)

    def test_assemble_imdbresult__votes_no_rating_return_no_rating(self):
        input_model = 1, None, 3
        expected_output = {'info': {'top250': 3}}

        actual_output = imdbratings._assemble_imdb_result(*input_model)

        self.assertDictEqual(expected_output, actual_output)

    def test_assemble_imdbresult__rating_no_votes_return_no_rating(self):
        input_model = None, 2, 3
        expected_output = {'info': {'top250': 3}}

        actual_output = imdbratings._assemble_imdb_result(*input_model)

        self.assertDictEqual(expected_output, actual_output)

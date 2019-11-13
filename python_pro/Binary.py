<!DOCTYPE html>
<!-- saved from url=(0044)https://www.geeksforgeeks.org/binary-search/ -->
<html lang="en-US" prefix="og: http://ogp.me/ns#" class=" js"><!--<![endif]--><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<meta name="viewport" content="width=device-width">
<meta name="description" content="A Computer Science portal for geeks. It contains well written, well thought and well explained computer science and programming articles, quizzes and practice/competitive programming/company interview Questions.">
<link rel="shortcut icon" href="https://www.geeksforgeeks.org/gfg.png" type="image/x-icon">

<meta name="theme-color" content="#0f9d58">

<meta property="og:image" content="https://www.geeksforgeeks.org/wp-content/uploads/gfg_200X200.png">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="200">
<meta property="og:image:height" content="200">
<script async="" src="./Binary_files/async-ads.js"></script><script type="text/javascript" async="" src="./Binary_files/f(9).txt"></script><script type="text/javascript" async="" src="./Binary_files/ga.js"></script><script src="./Binary_files/osd.js"></script><script src="./Binary_files/ca-pub-9465609616171866.js"></script><script type="text/javascript" async="" src="./Binary_files/f(9).txt"></script><script async="" type="text/javascript" src="./Binary_files/gpt.js"></script><script src="./Binary_files/require.min.js"></script>

<title>Binary Search - GeeksforGeeks</title>
<link rel="profile" href="http://gmpg.org/xfn/11">
<link rel="pingback" href="https://www.geeksforgeeks.org/binary-search/">
<!--[if lt IE 9]>
<script src="https://www.geeksforgeeks.org/wp-content/themes/iconic-one/js/html5.js" type="text/javascript"></script>
<![endif]-->

<script type="application/ld+json">
    {
        "@context" : "http://schema.org",
        "@type" : "Organization",
        "name" : "GeeksforGeeks",
        "url" : "https://www.geeksforgeeks.org/",
        "logo" : "https://www.geeksforgeeks.org/gfgLogo.png",
        "description" : "A computer science portal for geeks. It contains well written, well thought and well explained computer science and programming articles, quizzes and practice/competitive programming/company interview Questions.",
        "founder": [
            {
                "@type" : "Person",
                "name" : "Sandeep Jain",
                "url" : "https://in.linkedin.com/in/sandeep-jain-b3940815"
            }
        ],
        "sameAs" : [ "https://www.facebook.com/geeksforgeeks.org/",
            "https://twitter.com/geeksforgeeks",
            "https://www.linkedin.com/company/1299009",
            "https://www.youtube.com/geeksforgeeksvideos/"
        ]
    }
</script>
<script>

    var arrPostCat = new Array();
            arrPostCat.push('1750');
            arrPostCat.push('1751');
        var tIds = "1750,1751,2198,1679,1717,171,177,2073,2165";
    var domain = 1;
    var arrPost = new Array();
    var post_id = "142311";
    var post_type = "post";
    var post_slug = window.location.href;
    var ip = "52.15.127.153";
    var post_title = "Binary Search";
    var post_status = "publish";
    var post_date = "2014-01-28 13:22:36";
                            var isAdminLoggedIn = 0;
        </script>

<!-- This site is optimized with the Yoast SEO plugin v7.6 - https://yoast.com/wordpress/plugins/seo/ -->
<link rel="canonical" href="https://www.geeksforgeeks.org/binary-search/">
<meta property="og:locale" content="en_US">
<meta property="og:type" content="article">
<meta property="og:title" content="Binary Search - GeeksforGeeks">
<meta property="og:description" content="Given a sorted array arr[] of n elements, write a function to search a given element x in arr[]. A simple approach is to do… Read More »">
<meta property="og:url" content="https://www.geeksforgeeks.org/binary-search/">
<meta property="og:site_name" content="GeeksforGeeks">
<meta property="article:tag" content="Accenture">
<meta property="article:tag" content="Binary Search">
<meta property="article:tag" content="Infosys">
<meta property="article:tag" content="Oracle">
<meta property="article:tag" content="Qualcomm">
<meta property="article:tag" content="TCS">
<meta property="article:tag" content="Wipro">
<meta property="article:section" content="Divide and Conquer">
<meta property="article:published_time" content="2014-01-28T13:22:36+00:00">
<meta property="article:modified_time" content="2018-12-21T12:57:17+00:00">
<meta property="og:updated_time" content="2018-12-21T12:57:17+00:00">
<meta property="og:image" content="https://www.cdn.geeksforgeeks.org/wp-content/uploads/Binary-Search.png">
<meta property="og:image:secure_url" content="https://www.cdn.geeksforgeeks.org/wp-content/uploads/Binary-Search.png">
<meta property="og:image:width" content="1600">
<meta property="og:image:height" content="891">
<script type="application/ld+json">{"@context":"https:\/\/schema.org","@type":"Organization","url":"https:\/\/www.geeksforgeeks.org\/","sameAs":[],"@id":"https:\/\/www.geeksforgeeks.org\/#organization","name":"GeeksforGeeks","logo":"http:\/\/www.cdn.geeksforgeeks.org\/wp-content\/uploads\/gfg_200X200-1.png"}</script>
<!-- / Yoast SEO plugin. -->

<link rel="dns-prefetch" href="https://www.geeksforgeeks.org/">
<link rel="dns-prefetch" href="https://fonts.googleapis.com/">
<link rel="dns-prefetch" href="https://s.w.org/">
<link rel="alternate" type="application/rss+xml" title="GeeksforGeeks » Feed" href="https://www.geeksforgeeks.org/feed/">
<link rel="alternate" type="application/rss+xml" title="GeeksforGeeks » Comments Feed" href="https://www.geeksforgeeks.org/comments/feed/">
		<script type="text/javascript">
			window._wpemojiSettings = {"baseUrl":"https:\/\/s.w.org\/images\/core\/emoji\/11\/72x72\/","ext":".png","svgUrl":"https:\/\/s.w.org\/images\/core\/emoji\/11\/svg\/","svgExt":".svg","source":{"concatemoji":"https:\/\/www.geeksforgeeks.org\/wp-includes\/js\/wp-emoji-release.min.js?ver=4.9.8"}};
			!function(a,b,c){function d(a,b){var c=String.fromCharCode;l.clearRect(0,0,k.width,k.height),l.fillText(c.apply(this,a),0,0);var d=k.toDataURL();l.clearRect(0,0,k.width,k.height),l.fillText(c.apply(this,b),0,0);var e=k.toDataURL();return d===e}function e(a){var b;if(!l||!l.fillText)return!1;switch(l.textBaseline="top",l.font="600 32px Arial",a){case"flag":return!(b=d([55356,56826,55356,56819],[55356,56826,8203,55356,56819]))&&(b=d([55356,57332,56128,56423,56128,56418,56128,56421,56128,56430,56128,56423,56128,56447],[55356,57332,8203,56128,56423,8203,56128,56418,8203,56128,56421,8203,56128,56430,8203,56128,56423,8203,56128,56447]),!b);case"emoji":return b=d([55358,56760,9792,65039],[55358,56760,8203,9792,65039]),!b}return!1}function f(a){var c=b.createElement("script");c.src=a,c.defer=c.type="text/javascript",b.getElementsByTagName("head")[0].appendChild(c)}var g,h,i,j,k=b.createElement("canvas"),l=k.getContext&&k.getContext("2d");for(j=Array("flag","emoji"),c.supports={everything:!0,everythingExceptFlag:!0},i=0;i<j.length;i++)c.supports[j[i]]=e(j[i]),c.supports.everything=c.supports.everything&&c.supports[j[i]],"flag"!==j[i]&&(c.supports.everythingExceptFlag=c.supports.everythingExceptFlag&&c.supports[j[i]]);c.supports.everythingExceptFlag=c.supports.everythingExceptFlag&&!c.supports.flag,c.DOMReady=!1,c.readyCallback=function(){c.DOMReady=!0},c.supports.everything||(h=function(){c.readyCallback()},b.addEventListener?(b.addEventListener("DOMContentLoaded",h,!1),a.addEventListener("load",h,!1)):(a.attachEvent("onload",h),b.attachEvent("onreadystatechange",function(){"complete"===b.readyState&&c.readyCallback()})),g=c.source||{},g.concatemoji?f(g.concatemoji):g.wpemoji&&g.twemoji&&(f(g.twemoji),f(g.wpemoji)))}(window,document,window._wpemojiSettings);
		</script><script src="./Binary_files/wp-emoji-release.min.js" type="text/javascript" defer=""></script>
		<style type="text/css">
img.wp-smiley,
img.emoji {
	display: inline !important;
	border: none !important;
	box-shadow: none !important;
	height: 1em !important;
	width: 1em !important;
	margin: 0 .07em !important;
	vertical-align: -0.1em !important;
	background: none !important;
	padding: 0 !important;
}
</style>
<link rel="stylesheet" id="themonic-fonts-css" href="./Binary_files/css(3)" type="text/css" media="all">
<link rel="stylesheet" id="custom-style-css" href="./Binary_files/gfg.min.css" type="text/css" media="all">
<script type="text/javascript" src="./Binary_files/jquery.js"></script>
<script type="text/javascript" src="./Binary_files/jquery-migrate.min.js"></script>
<script type="text/javascript">
/* <![CDATA[ */
var gfgObject = {"authUrl":"https:\/\/auth.geeksforgeeks.org\/","contributeUrl":"https:\/\/contribute.geeksforgeeks.org\/","utilUrl":"https:\/\/util.geeksforgeeks.org\/"};
/* ]]> */
</script>
<script type="text/javascript" src="./Binary_files/gfg.min.js"></script>
<link rel="https://api.w.org/" href="https://www.geeksforgeeks.org/wp-json/">
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://www.cdn.geeksforgeeks.org/xmlrpc.php?rsd">
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://www.cdn.geeksforgeeks.org/wp-includes/wlwmanifest.xml"> 
<meta name="generator" content="WordPress 4.9.8">
<link rel="shortlink" href="https://www.geeksforgeeks.org/?p=142311">
<link rel="alternate" type="application/json+oembed" href="https://www.geeksforgeeks.org/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.geeksforgeeks.org%2Fbinary-search%2F">
<link rel="alternate" type="text/xml+oembed" href="https://www.geeksforgeeks.org/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.geeksforgeeks.org%2Fbinary-search%2F&amp;format=xml">
        <link rel="stylesheet" type="text/css" href="./Binary_files/cookieconsent.min.css">
        <script src="./Binary_files/cookieconsent.min.js"></script>
        <script>
        window.addEventListener("load", function(){
        window.cookieconsent.initialise({
        "palette": {
            "popup": {
              "background": "#3c404d",
              "text": "#d6d6d6"
            },
            "button": {
              "background": "#8bed4f"
            }
          },
          "theme": "classic",
            onStatusChange: function(status) {
            
            },
            law: {
              regionalLaw: false,
            },
            location: true,
            "content": {
            "message": "We use cookies to ensure you have the best browsing experience on our website. By using our site, you acknowledge that you have read and understood our <a href=\"https://www.geeksforgeeks.org/cookie-policy/\" class=\"cc-link\" target=\"_blank\">Cookie Policy</a> & ",
            "link": "Privacy Policy",
            "href": "/privacy-policy/"
            },
        cookie: {
        name : "geeksforgeeks_consent_status",
        }
        })});
    
        </script>
    <style>
#wpadminbar{
background: #ff0000 !important;
}
</style>
<style type="text/css" id="custom-background-css">
body.custom-background { background-color: #ffffff; }
</style>
<link rel="amphtml" href="https://www.geeksforgeeks.org/binary-search/amp/"><link rel="icon" href="https://www.cdn.geeksforgeeks.org/wp-content/uploads/gfg_200X200-100x100.png" sizes="32x32">
<link rel="icon" href="https://www.cdn.geeksforgeeks.org/wp-content/uploads/gfg_200X200.png" sizes="192x192">
<link rel="apple-touch-icon-precomposed" href="https://www.cdn.geeksforgeeks.org/wp-content/uploads/gfg_200X200.png">
<meta name="msapplication-TileImage" content="https://www.cdn.geeksforgeeks.org/wp-content/uploads/gfg_200X200.png">

<script type="text/javascript">
  var googletag = googletag || {};
  googletag.cmd = googletag.cmd || [];
  (function() {
    var gads = document.createElement('script');
    gads.async = true;
    gads.type = 'text/javascript';
    var useSSL = 'https:' == document.location.protocol;
    gads.src = (useSSL ? 'https:' : 'http:') +
      '//www.googletagservices.com/tag/js/gpt.js';
    var node = document.getElementsByTagName('script')[0];
    node.parentNode.insertBefore(gads, node);
  })();
</script>

<script type="text/javascript">
  googletag.cmd.push(function() {
    googletag.defineSlot('/27823234/SP', [300, 250], 'div-gpt-ad-1458112424022-0').addService(googletag.pubads());
    googletag.pubads().enableSingleRequest();
    googletag.enableServices();
  });
</script>
<!-- AutoAds -->
<script async="" src="./Binary_files/f(10).txt"></script>
<script>
(adsbygoogle = window.adsbygoogle || []).push({
google_ad_client: "ca-pub-9465609616171866",
enable_page_level_ads: true
});
</script>
<script type="text/javascript" async="" src="./Binary_files/bsa.js"></script><link rel="preload" href="./Binary_files/f(11).txt" as="script"><script type="text/javascript" src="./Binary_files/f(11).txt"></script><link rel="preload" href="./Binary_files/f(12).txt" as="script"><script type="text/javascript" src="./Binary_files/f(12).txt"></script><link rel="preload" href="https://pagead2.googlesyndication.com/pagead/js/r20190128/r20190131/show_ads_impl.js" as="script"><script src="./Binary_files/pubads_impl_299.js" async=""></script><script src="./Binary_files/cse_element__en.js" type="text/javascript"></script><link type="text/css" rel="stylesheet" href="./Binary_files/default+en.css"><link type="text/css" rel="stylesheet" href="./Binary_files/default.css"><style type="text/css">.gsc-control-cse{font-family:arial, sans-serif}.gsc-control-cse .gsc-table-result{font-family:arial, sans-serif}.gsc-control-cse{border-color:#FFFFFF;background-color:#FFFFFF}input.gsc-input,.gsc-input-box,.gsc-input-box-hover,.gsc-input-box-focus{border-color:#6AA84F}.gsc-search-button-v2,.gsc-search-button-v2:hover,.gsc-search-button-v2:focus{border-color:#000000;background-color:#6AA84F;background-image:none;filter:none}.gsc-search-button-v2 svg{fill:#FFFFFF}.gsc-tabHeader.gsc-tabhInactive{border-color:#E9E9E9;background-color:#E9E9E9}.gsc-tabHeader.gsc-tabhActive{border-color:#FF9900;border-bottom-color:#FFFFFF;background-color:#FFFFFF}.gsc-tabsArea{border-color:#FF9900}.gsc-webResult.gsc-result,.gsc-results .gsc-imageResult{border-color:#FFFFFF;background-color:#FFFFFF}.gsc-webResult.gsc-result:hover,.gsc-imageResult:hover{border-color:#FFFFFF;background-color:#FFFFFF}.gs-webResult.gs-result a.gs-title:link,.gs-webResult.gs-result a.gs-title:link b,.gs-imageResult a.gs-title:link,.gs-imageResult a.gs-title:link b{color:#006600}.gs-webResult.gs-result a.gs-title:visited,.gs-webResult.gs-result a.gs-title:visited b,.gs-imageResult a.gs-title:visited,.gs-imageResult a.gs-title:visited b{color:#EC4E20}.gs-webResult.gs-result a.gs-title:hover,.gs-webResult.gs-result a.gs-title:hover b,.gs-imageResult a.gs-title:hover,.gs-imageResult a.gs-title:hover b{color:#CA7700}.gs-webResult.gs-result a.gs-title:active,.gs-webResult.gs-result a.gs-title:active b,.gs-imageResult a.gs-title:active,.gs-imageResult a.gs-title:active b{color:#006600}.gsc-cursor-page{color:#006600}a.gsc-trailing-more-results:link{color:#006600}.gs-webResult .gs-snippet,.gs-imageResult .gs-snippet,.gs-fileFormatType{color:#000000}.gs-webResult div.gs-visibleUrl,.gs-imageResult div.gs-visibleUrl{color:#008000}.gs-webResult div.gs-visibleUrl-short{color:#008000}.gs-webResult div.gs-visibleUrl-short{display:none}.gs-webResult div.gs-visibleUrl-long{display:block}.gs-promotion div.gs-visibleUrl-short{display:none}.gs-promotion div.gs-visibleUrl-long{display:block}.gsc-cursor-box{border-color:#FFFFFF}.gsc-results .gsc-cursor-box .gsc-cursor-page{border-color:#E9E9E9;background-color:#FFFFFF;color:#006600;}.gsc-results .gsc-cursor-box .gsc-cursor-current-page{border-color:#FF9900;background-color:#FFFFFF;color:#EC4E20;}.gsc-webResult.gsc-result.gsc-promotion{border-color:#336699;background-color:#FFFFFF}.gsc-completion-title{color:#006600}.gsc-completion-snippet{color:#000000}.gs-promotion a.gs-title:link,.gs-promotion a.gs-title:link *,.gs-promotion .gs-snippet a:link{color:#006600}.gs-promotion a.gs-title:visited,.gs-promotion a.gs-title:visited *,.gs-promotion .gs-snippet a:visited{color:#EC4E20}.gs-promotion a.gs-title:hover,.gs-promotion a.gs-title:hover *,.gs-promotion .gs-snippet a:hover{color:#CA7700}.gs-promotion a.gs-title:active,.gs-promotion a.gs-title:active *,.gs-promotion .gs-snippet a:active{color:#006600}.gs-promotion .gs-snippet,.gs-promotion .gs-title .gs-promotion-title-right,.gs-promotion .gs-title .gs-promotion-title-right *{color:#000000}.gs-promotion .gs-visibleUrl,.gs-promotion .gs-visibleUrl-short{color:#008000}.gcsc-find-more-on-google{color:#006600}.gcsc-find-more-on-google-magnifier{fill:#006600}</style><script type="text/javascript" id="_bsap_js_785bf45b162de1c5511e8baa02854e5c" src="./Binary_files/s_785bf45b162de1c5511e8baa02854e5c.js" async="async"></script><style type="text/css">.gscb_a{display:inline-block;font:27px/13px arial,sans-serif}.gsst_a .gscb_a{color:#a1b9ed;cursor:pointer}.gsst_a:hover .gscb_a,.gsst_a:focus .gscb_a{color:#36c}.gsst_a{display:inline-block}.gsst_a{cursor:pointer;padding:0 4px}.gsst_a:hover{text-decoration:none!important}.gsst_b{font-size:16px;padding:0 2px;position:relative;user-select:none;-webkit-user-select:none;white-space:nowrap}.gsst_e{vertical-align:middle;opacity:0.55;}.gsst_a:hover .gsst_e,.gsst_a:focus .gsst_e{opacity:0.72;}.gsst_a:active .gsst_e{opacity:1;}.gsst_f{background:white;text-align:left}.gsst_g{background-color:white;border:1px solid #ccc;border-top-color:#d9d9d9;box-shadow:0 2px 4px rgba(0,0,0,0.2);-webkit-box-shadow:0 2px 4px rgba(0,0,0,0.2);margin:-1px -3px;padding:0 6px}.gsst_h{background-color:white;height:1px;margin-bottom:-1px;position:relative;top:-1px}.gsib_a{width:100%;padding:4px 6px 0}.gsib_a,.gsib_b{vertical-align:top}.gssb_c{border:0;position:absolute;z-index:989}.gssb_e{border:1px solid #ccc;border-top-color:#d9d9d9;box-shadow:0 2px 4px rgba(0,0,0,0.2);-webkit-box-shadow:0 2px 4px rgba(0,0,0,0.2);cursor:default}.gssb_f{visibility:hidden;white-space:nowrap}.gssb_k{border:0;display:block;position:absolute;top:0;z-index:988}.gsdd_a{border:none!important}.gsq_a{padding:0}.gssb_a{padding:0 7px}.gssb_a,.gssb_a td{white-space:nowrap;overflow:hidden;line-height:22px}#gssb_b{font-size:11px;color:#36c;text-decoration:none}#gssb_b:hover{font-size:11px;color:#36c;text-decoration:underline}.gssb_g{text-align:center;padding:8px 0 7px;position:relative}.gssb_h{font-size:15px;height:28px;margin:0.2em;-webkit-appearance:button}.gssb_i{background:#eee}.gss_ifl{visibility:hidden;padding-left:5px}.gssb_i .gss_ifl{visibility:visible}a.gssb_j{font-size:13px;color:#36c;text-decoration:none;line-height:100%}a.gssb_j:hover{text-decoration:underline}.gssb_l{height:1px;background-color:#e5e5e5}.gssb_m{color:#000;background:#fff}.gssb_a{padding:0 9px}.gsib_a{padding-right:8px;padding-left:8px}.gsst_a{padding-top:5.5px}.gssb_e{border:0}.gssb_l{margin:5px 0}input.gsc-input::-webkit-input-placeholder{font-size:14px}input.gsc-input:-moz-placeholder{font-size:14px}input.gsc-input::-moz-placeholder{font-size:14px}input.gsc-input:-ms-input-placeholder{font-size:14px}input.gsc-input:focus::-webkit-input-placeholder{color:transparent}input.gsc-input:focus:-moz-placeholder{color:transparent}input.gsc-input:focus::-moz-placeholder{color:transparent}input.gsc-input:focus:-ms-input-placeholder{color:transparent}.gssb_c .gsc-completion-container{position:static}.gssb_c{z-index:5000}.gsc-completion-container table{background:transparent;font-size:inherit;font-family:inherit}.gssb_c > tbody > tr,.gssb_c > tbody > tr > td,.gssb_d,.gssb_d > tbody > tr,.gssb_d > tbody > tr > td,.gssb_e,.gssb_e > tbody > tr,.gssb_e > tbody > tr > td{padding:0;margin:0;border:0}.gssb_a table,.gssb_a table tr,.gssb_a table tr td{padding:0;margin:0;border:0}</style><script src="./Binary_files/cse_element__en.js" type="text/javascript"></script><link type="text/css" rel="stylesheet" href="./Binary_files/default+en.css"><link type="text/css" rel="stylesheet" href="./Binary_files/default.css"><style type="text/css">.gsc-control-cse{font-family:arial, sans-serif}.gsc-control-cse .gsc-table-result{font-family:arial, sans-serif}.gsc-control-cse{border-color:#FFFFFF;background-color:#FFFFFF}input.gsc-input,.gsc-input-box,.gsc-input-box-hover,.gsc-input-box-focus{border-color:#6AA84F}.gsc-search-button-v2,.gsc-search-button-v2:hover,.gsc-search-button-v2:focus{border-color:#000000;background-color:#6AA84F;background-image:none;filter:none}.gsc-search-button-v2 svg{fill:#FFFFFF}.gsc-tabHeader.gsc-tabhInactive{border-color:#E9E9E9;background-color:#E9E9E9}.gsc-tabHeader.gsc-tabhActive{border-color:#FF9900;border-bottom-color:#FFFFFF;background-color:#FFFFFF}.gsc-tabsArea{border-color:#FF9900}.gsc-webResult.gsc-result,.gsc-results .gsc-imageResult{border-color:#FFFFFF;background-color:#FFFFFF}.gsc-webResult.gsc-result:hover,.gsc-imageResult:hover{border-color:#FFFFFF;background-color:#FFFFFF}.gs-webResult.gs-result a.gs-title:link,.gs-webResult.gs-result a.gs-title:link b,.gs-imageResult a.gs-title:link,.gs-imageResult a.gs-title:link b{color:#006600}.gs-webResult.gs-result a.gs-title:visited,.gs-webResult.gs-result a.gs-title:visited b,.gs-imageResult a.gs-title:visited,.gs-imageResult a.gs-title:visited b{color:#EC4E20}.gs-webResult.gs-result a.gs-title:hover,.gs-webResult.gs-result a.gs-title:hover b,.gs-imageResult a.gs-title:hover,.gs-imageResult a.gs-title:hover b{color:#CA7700}.gs-webResult.gs-result a.gs-title:active,.gs-webResult.gs-result a.gs-title:active b,.gs-imageResult a.gs-title:active,.gs-imageResult a.gs-title:active b{color:#006600}.gsc-cursor-page{color:#006600}a.gsc-trailing-more-results:link{color:#006600}.gs-webResult .gs-snippet,.gs-imageResult .gs-snippet,.gs-fileFormatType{color:#000000}.gs-webResult div.gs-visibleUrl,.gs-imageResult div.gs-visibleUrl{color:#008000}.gs-webResult div.gs-visibleUrl-short{color:#008000}.gs-webResult div.gs-visibleUrl-short{display:none}.gs-webResult div.gs-visibleUrl-long{display:block}.gs-promotion div.gs-visibleUrl-short{display:none}.gs-promotion div.gs-visibleUrl-long{display:block}.gsc-cursor-box{border-color:#FFFFFF}.gsc-results .gsc-cursor-box .gsc-cursor-page{border-color:#E9E9E9;background-color:#FFFFFF;color:#006600;}.gsc-results .gsc-cursor-box .gsc-cursor-current-page{border-color:#FF9900;background-color:#FFFFFF;color:#EC4E20;}.gsc-webResult.gsc-result.gsc-promotion{border-color:#336699;background-color:#FFFFFF}.gsc-completion-title{color:#006600}.gsc-completion-snippet{color:#000000}.gs-promotion a.gs-title:link,.gs-promotion a.gs-title:link *,.gs-promotion .gs-snippet a:link{color:#006600}.gs-promotion a.gs-title:visited,.gs-promotion a.gs-title:visited *,.gs-promotion .gs-snippet a:visited{color:#EC4E20}.gs-promotion a.gs-title:hover,.gs-promotion a.gs-title:hover *,.gs-promotion .gs-snippet a:hover{color:#CA7700}.gs-promotion a.gs-title:active,.gs-promotion a.gs-title:active *,.gs-promotion .gs-snippet a:active{color:#006600}.gs-promotion .gs-snippet,.gs-promotion .gs-title .gs-promotion-title-right,.gs-promotion .gs-title .gs-promotion-title-right *{color:#000000}.gs-promotion .gs-visibleUrl,.gs-promotion .gs-visibleUrl-short{color:#008000}.gcsc-find-more-on-google{color:#006600}.gcsc-find-more-on-google-magnifier{fill:#006600}</style><script type="text/javascript" src="./Binary_files/pro.js" id="_bsap_premium_pro"></script><script type="text/javascript" id="_bsaPRO_js" src="./Binary_files/saved_resource" async="async"></script><script id="_bsa_srv-CKYDL2JJ_0" type="text/javascript" src="./Binary_files/CKYDL2JJ.json"></script><style></style></head>

<body class="post-template-default single single-post postid-142311 single-format-standard custom-background custom-background-white custom-font-enabled"><div role="dialog" aria-live="polite" aria-label="cookieconsent" aria-describedby="cookieconsent:desc" class="cc-window cc-banner cc-type-info cc-theme-classic cc-bottom cc-color-override-382972913 " style=""><!--googleoff: all--><span id="cookieconsent:desc" class="cc-message">We use cookies to ensure you have the best browsing experience on our website. By using our site, you acknowledge that you have read and understood our <a href="https://www.geeksforgeeks.org/cookie-policy/" class="cc-link" target="_blank">Cookie Policy</a> &amp;  <a aria-label="learn more about cookies" role="button" tabindex="0" class="cc-link" href="https://www.geeksforgeeks.org/privacy-policy/" target="_blank">Privacy Policy</a></span><div class="cc-compliance"><a aria-label="dismiss cookie message" role="button" tabindex="0" class="cc-btn cc-dismiss">Got it!</a></div><!--googleon: all--></div>

<!-- BuySellAds Ad Code -->
<script type="text/javascript">
(function(){
  var bsa = document.createElement('script');
     bsa.type = 'text/javascript';
     bsa.async = true;
     bsa.src = '//s3.buysellads.com/ac/bsa.js';
  (document.getElementsByTagName('head')[0]||document.getElementsByTagName('body')[0]).appendChild(bsa);
})();
</script>
<!-- End BuySellAds Ad Code -->

<div id="page" style="position:relative;overflow: unset;z-index:2;" class="hfeed site">
	<header id="masthead" class="site-header" role="banner">
		<div style="margin-bottom: 5px;">	
		<div class="upper-header">
            <div id="container-g4g-header">
                <div id="MasterHead">
                    <div class="header-gfg-logo">
                                    <a href="https://www.geeksforgeeks.org/" title="GeeksforGeeks" rel="home"><img src="./Binary_files/geeksforgeeks-6.png" alt="GeeksforGeeks"></a>

                            </div>

     <span class="responsive-custom-search">
    <script>
      (function() {
        var cx = '009682134359037907028:tj6eafkv_be';
        var gcse = document.createElement('script');
        gcse.type = 'text/javascript';
        gcse.async = true;
        gcse.src = (document.location.protocol == 'https:' ? 'https:' : 'http:') +
            '//cse.google.com/cse.js?cx=' + cx;
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(gcse, s);
      })();
    </script>
    <div id="___gcse_0"><div class="gsc-control-cse gsc-control-cse-en"><div class="gsc-control-wrapper-cse" dir="ltr"><form class="gsc-search-box gsc-search-box-tools" accept-charset="utf-8"><table cellspacing="0" cellpadding="0" class="gsc-search-box"><tbody><tr><td class="gsc-input"><div class="gsc-input-box" id="gsc-iw-id1"><table cellspacing="0" cellpadding="0" id="gs_id50" class="gstl_50 gsc-input" style="width: 100%; padding: 0px;"><tbody><tr><td id="gs_tti50" class="gsib_a"><input autocomplete="off" type="text" size="10" class="gsc-input" name="search" title="search" id="gsc-i-id1" placeholder="Custom Search" dir="ltr" spellcheck="false" style="width: 100%; padding: 0px; border: none; margin: 0px; height: auto; background: url(&quot;https://www.google.com/cse/static/images/1x/googlelogo_lightgrey_46x16dp.png&quot;) left center no-repeat rgb(255, 255, 255); text-indent: 48px; outline: none;"></td><td class="gsib_b"><div class="gsst_b" id="gs_st50" dir="ltr"><a class="gsst_a" href="javascript:void(0)" style="display: none;"><span class="gscb_a" id="gs_cb50">×</span></a></div></td></tr></tbody></table></div></td><td class="gsc-search-button"><button class="gsc-search-button gsc-search-button-v2"><svg width="13" height="13" viewBox="0 0 13 13"><title>search</title><path d="m4.8495 7.8226c0.82666 0 1.5262-0.29146 2.0985-0.87438 0.57232-0.58292 0.86378-1.2877 0.87438-2.1144 0.010599-0.82666-0.28086-1.5262-0.87438-2.0985-0.59352-0.57232-1.293-0.86378-2.0985-0.87438-0.8055-0.010599-1.5103 0.28086-2.1144 0.87438-0.60414 0.59352-0.8956 1.293-0.87438 2.0985 0.021197 0.8055 0.31266 1.5103 0.87438 2.1144 0.56172 0.60414 1.2665 0.8956 2.1144 0.87438zm4.4695 0.2115 3.681 3.6819-1.259 1.284-3.6817-3.7 0.0019784-0.69479-0.090043-0.098846c-0.87973 0.76087-1.92 1.1413-3.1207 1.1413-1.3553 0-2.5025-0.46363-3.4417-1.3909s-1.4088-2.0686-1.4088-3.4239c0-1.3553 0.4696-2.4966 1.4088-3.4239 0.9392-0.92727 2.0864-1.3969 3.4417-1.4088 1.3553-0.011889 2.4906 0.45771 3.406 1.4088 0.9154 0.95107 1.379 2.0924 1.3909 3.4239 0 1.2126-0.38043 2.2588-1.1413 3.1385l0.098834 0.090049z"></path></svg></button></td><td class="gsc-clear-button"><div class="gsc-clear-button" title="clear results">&nbsp;</div></td></tr></tbody></table></form><div class="gsc-results-wrapper-overlay"><div class="gsc-results-close-btn" tabindex="0"></div><div class="gsc-tabsAreaInvisible"><div class="gsc-tabHeader gsc-inline-block gsc-tabhActive">Custom Search</div><span class="gs-spacer"> </span></div><div class="gsc-tabsAreaInvisible"></div><div class="gsc-above-wrapper-area-invisible"><table cellspacing="0" cellpadding="0" class="gsc-above-wrapper-area-container"><tbody><tr><td class="gsc-result-info-container"><div class="gsc-result-info-invisible"></div></td><td class="gsc-orderby-container"><div class="gsc-orderby-invisible"><div class="gsc-orderby-label gsc-inline-block">Sort by:</div><div class="gsc-option-menu-container gsc-inline-block"><div class="gsc-selected-option-container gsc-inline-block"><div class="gsc-selected-option">Relevance</div><div class="gsc-option-selector"></div></div><div class="gsc-option-menu-invisible"><div class="gsc-option-menu-item gsc-option-menu-item-highlighted"><div class="gsc-option">Relevance</div></div><div class="gsc-option-menu-item"><div class="gsc-option">Date</div></div></div></div></div></td></tr></tbody></table></div><div class="gsc-adBlockInvisible"></div><div class="gsc-wrapper"><div class="gsc-adBlockInvisible"></div><div class="gsc-resultsbox-invisible"><div class="gsc-resultsRoot gsc-tabData gsc-tabdActive"><table cellspacing="0" cellpadding="0" class="gsc-resultsHeader"><tbody><tr><td class="gsc-twiddleRegionCell"><div class="gsc-twiddle"><div class="gsc-title">Web</div></div><div class="gsc-stats"></div><div class="gsc-results-selector gsc-all-results-active"><div class="gsc-result-selector gsc-one-result" title="show one result">&nbsp;</div><div class="gsc-result-selector gsc-more-results" title="show more results">&nbsp;</div><div class="gsc-result-selector gsc-all-results" title="show all results">&nbsp;</div></div></td><td class="gsc-configLabelCell"></td></tr></tbody></table><div><div class="gsc-expansionArea"></div></div></div></div></div></div><div class="gsc-modal-background-image" tabindex="0"></div></div></div></div>
    </span>

                    <div class="buttonsProfileSide">
                        <div class="profile-buttons">
    <a class="login-modal-btn ButtonLogin" href="https://auth.geeksforgeeks.org/?to=https://www.geeksforgeeks.org/binary-search/">Login</a>
    </div><div class="masterhead-buttons">
                               
                                <a class="ButtonContribute" href="https://practice.geeksforgeeks.org/courses/" style="margin-bottom:5px;">Courses</a>
                                <a class="login-modal-btn ButtonContribute" href="https://contribute.geeksforgeeks.org/wp-admin/post-new.php">Write an Article</a>
                        </div>

                    </div>

                </div>
            </div>
            </div>


<div id="profile" style="float: right; margin-top: -1%;margin-right:1%;"></div>
</div>
</header></div>

		
		
		<nav id="site-navigation" class="themonic-nav" role="navigation" style="width: 100%; position: fixed; top: 0px; z-index: 99998;">
			<a class="assistive-text" href="https://www.geeksforgeeks.org/binary-search/#content" title="Skip to content">Skip to content</a>
			<div class="menu-iconic-container"><ul id="menu-top" class="nav-menu"><li id="menu-item-147519" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-147519"><a href="https://www.geeksforgeeks.org/" class="reduceMenuHeight"><img style="width: 30px;vertical-align: middle;" src="./Binary_files/gfg_transparent_white_small.png"></a></li>
<li id="menu-item-141975" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-141975"><a href="http://www.geeksforgeeks.org/fundamentals-of-algorithms/" class="reduceMenuHeight">Algo ▼</a>
<ul class="sub-menu">
	<li id="menu-item-135030" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135030"><a href="http://www.geeksforgeeks.org/fundamentals-of-algorithms/#AnalysisofAlgorithms" class="reduceMenuHeight">Analysis of Algorithms</a></li>
	<li id="menu-item-146823" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-146823"><a href="http://www.geeksforgeeks.org/fundamentals-of-algorithms/" class="reduceMenuHeight">Topicwise ►</a>
	<ul class="sub-menu">
		<li id="menu-item-147774" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-147774"><a href="http://www.geeksforgeeks.org/searching-algorithms/" class="reduceMenuHeight">Searching Algorithms</a></li>
		<li id="menu-item-147773" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-147773"><a href="http://www.geeksforgeeks.org/sorting-algorithms/" class="reduceMenuHeight">Sorting Algorithms</a></li>
		<li id="menu-item-135041" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135041"><a href="http://www.geeksforgeeks.org/graph-data-structure-and-algorithms/" class="reduceMenuHeight">Graph Algorithms</a></li>
		<li id="menu-item-135040" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135040"><a href="http://www.geeksforgeeks.org/bitwise-algorithms/" class="reduceMenuHeight">Bit Algorithms</a></li>
		<li id="menu-item-135034" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135034"><a href="https://www.geeksforgeeks.org/algorithms-gq/pattern-searching/" class="reduceMenuHeight">Pattern Searching</a></li>
		<li id="menu-item-135038" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135038"><a href="http://www.geeksforgeeks.org/geometric-algorithms/" class="reduceMenuHeight">Geometric Algorithms</a></li>
		<li id="menu-item-135039" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135039"><a href="http://www.geeksforgeeks.org/mathematical-algorithms/" class="reduceMenuHeight">Mathematical Algorithms</a></li>
		<li id="menu-item-135042" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135042"><a href="http://www.geeksforgeeks.org/randomized-algorithms/" class="reduceMenuHeight">Randomized Algorithms</a></li>
		<li id="menu-item-156520" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-156520"><a href="https://www.geeksforgeeks.org/game-theory/" class="reduceMenuHeight">Game Theory</a></li>
	</ul>
</li>
	<li id="menu-item-146824" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-146824"><a href="http://www.geeksforgeeks.org/fundamentals-of-algorithms/" class="reduceMenuHeight">Algorithm Paradigms ►</a>
	<ul class="sub-menu">
		<li id="menu-item-135032" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135032"><a href="http://www.geeksforgeeks.org/greedy-algorithms/" class="reduceMenuHeight">Greedy Algorithms</a></li>
		<li id="menu-item-135033" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135033"><a href="http://www.geeksforgeeks.org/dynamic-programming/" class="reduceMenuHeight">Dynamic Programming</a></li>
		<li id="menu-item-135037" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135037"><a href="http://www.geeksforgeeks.org/divide-and-conquer/" class="reduceMenuHeight">Divide and Conquer</a></li>
		<li id="menu-item-135036" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135036"><a href="http://www.geeksforgeeks.org/backtracking-algorithms/" class="reduceMenuHeight">Backtracking</a></li>
		<li id="menu-item-137933" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137933"><a href="https://www.geeksforgeeks.org/branch-and-bound-algorithm/" class="reduceMenuHeight">Branch &amp; Bound</a></li>
	</ul>
</li>
	<li id="menu-item-146911" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146911"><a href="http://www.geeksforgeeks.org/fundamentals-of-algorithms/" class="reduceMenuHeight">All Algorithms</a></li>
</ul>
</li>
<li id="menu-item-142016" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-142016"><a href="http://www.geeksforgeeks.org/data-structures/" class="reduceMenuHeight">DS  ▼</a>
<ul class="sub-menu">
	<li id="menu-item-135054" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135054"><a href="http://www.geeksforgeeks.org/array-data-structure/" class="reduceMenuHeight">Array</a></li>
	<li id="menu-item-135045" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135045"><a href="http://www.geeksforgeeks.org/data-structures/linked-list/" class="reduceMenuHeight">LinkedList</a></li>
	<li id="menu-item-135046" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135046"><a href="http://www.geeksforgeeks.org/stack-data-structure/" class="reduceMenuHeight">Stack</a></li>
	<li id="menu-item-135047" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135047"><a href="http://www.geeksforgeeks.org/queue-data-structure/" class="reduceMenuHeight">Queue</a></li>
	<li id="menu-item-146827" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-146827"><a href="http://www.geeksforgeeks.org/data-structures/" class="reduceMenuHeight">Tree based DS ►</a>
	<ul class="sub-menu">
		<li id="menu-item-135048" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135048"><a href="http://www.geeksforgeeks.org/binary-tree-data-structure/" class="reduceMenuHeight">Binary Tree</a></li>
		<li id="menu-item-135049" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135049"><a href="http://www.geeksforgeeks.org/binary-search-tree-data-structure/" class="reduceMenuHeight">Binary Search Tree</a></li>
		<li id="menu-item-135050" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135050"><a href="http://www.geeksforgeeks.org/heap-data-structure/" class="reduceMenuHeight">Heap</a></li>
	</ul>
</li>
	<li id="menu-item-135051" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135051"><a href="http://www.geeksforgeeks.org/hashing-data-structure/" class="reduceMenuHeight">Hashing</a></li>
	<li id="menu-item-135052" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135052"><a href="http://www.geeksforgeeks.org/graph-data-structure-and-algorithms/" class="reduceMenuHeight">Graph</a></li>
	<li id="menu-item-135053" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135053"><a href="http://www.geeksforgeeks.org/advanced-data-structures/" class="reduceMenuHeight">Advanced Data Structure</a></li>
	<li id="menu-item-135055" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135055"><a href="http://www.geeksforgeeks.org/matrix/" class="reduceMenuHeight">Matrix</a></li>
	<li id="menu-item-147716" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-147716"><a href="http://www.geeksforgeeks.org/string-data-structure/" class="reduceMenuHeight">Strings</a></li>
	<li id="menu-item-135056" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135056"><a href="http://www.geeksforgeeks.org/data-structures/" class="reduceMenuHeight">All Data Structures</a></li>
</ul>
</li>
<li id="menu-item-147478" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-147478"><a href="http://www.geeksforgeeks.org/category/program-output/" class="reduceMenuHeight">Languages ▼</a>
<ul class="sub-menu">
	<li id="menu-item-135006" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-135006"><a href="https://www.geeksforgeeks.org/c-programming-language/" class="reduceMenuHeight">C</a></li>
	<li id="menu-item-135007" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-135007"><a href="https://www.geeksforgeeks.org/c-plus-plus/" class="reduceMenuHeight">C++</a></li>
	<li id="menu-item-135012" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-135012"><a href="https://www.geeksforgeeks.org/java/" class="reduceMenuHeight">Java</a></li>
	<li id="menu-item-137004" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-137004"><a href="https://www.geeksforgeeks.org/python-programming-language/" class="reduceMenuHeight">Python</a></li>
	<li id="menu-item-255267" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-255267"><a href="https://www.geeksforgeeks.org/csharp-programming-language/" class="reduceMenuHeight">C#</a></li>
	<li id="menu-item-182096" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-182096"><a href="https://www.geeksforgeeks.org/php/" class="reduceMenuHeight">PHP</a></li>
	<li id="menu-item-188679" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-188679"><a href="https://www.geeksforgeeks.org/javascript-tutorial/" class="reduceMenuHeight">Javascript</a></li>
	<li id="menu-item-135016" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135016"><a href="http://www.geeksforgeeks.org/sql-tutorial/" class="reduceMenuHeight">SQL</a></li>
	<li id="menu-item-251185" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-251185"><a href="https://www.geeksforgeeks.org/html-tutorials/" class="reduceMenuHeight">HTML</a></li>
	<li id="menu-item-251186" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-251186"><a href="https://www.geeksforgeeks.org/css-tutorials/" class="reduceMenuHeight">CSS</a></li>
	<li id="menu-item-140854" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-140854"><a title="http://www.geeksforgeeks.org/category/program-output/" href="https://www.geeksforgeeks.org/category/program-output/" class="reduceMenuHeight">Program Output</a></li>
</ul>
</li>
<li id="menu-item-142017" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-142017"><a href="http://www.geeksforgeeks.org/about/interview-corner/" class="reduceMenuHeight">Interview  ▼</a>
<ul class="sub-menu">
	<li id="menu-item-141326" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-141326"><a href="https://www.geeksforgeeks.org/company-preparation/" class="reduceMenuHeight">Company Prep</a></li>
	<li id="menu-item-137171" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137171"><a href="http://www.geeksforgeeks.org/interview-preparation-for-software-developer/" class="reduceMenuHeight">Top Topics</a></li>
	<li id="menu-item-137172" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137172"><a href="https://practice.geeksforgeeks.org/company-tags" class="reduceMenuHeight">Practice Company Questions</a></li>
	<li id="menu-item-137173" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137173"><a href="http://www.geeksforgeeks.org/about/interview-corner/" class="reduceMenuHeight">Interview Experiences</a></li>
	<li id="menu-item-137174" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137174"><a href="https://www.geeksforgeeks.org/experienced-interview-experiences-company-wise/" class="reduceMenuHeight">Experienced Interviews</a></li>
	<li id="menu-item-137175" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137175"><a href="https://www.geeksforgeeks.org/internship-interview-experiences-company-wise/" class="reduceMenuHeight">Internship Interviews</a></li>
	<li id="menu-item-137176" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137176"><a href="http://www.geeksforgeeks.org/category/competitive-programming/" class="reduceMenuHeight">Competitive Programming</a></li>
	<li id="menu-item-147581" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-147581"><a href="http://www.geeksforgeeks.org/software-design-patterns/" class="reduceMenuHeight">Design Patterns</a></li>
	<li id="menu-item-137186" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137186"><a href="http://geeksquiz.com/quiz-corner/" class="reduceMenuHeight">Multiple Choice Quizzes</a></li>
</ul>
</li>
<li id="menu-item-137178" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-137178"><a href="http://www.geeksforgeeks.org/student-corner/" class="reduceMenuHeight">Students  ▼</a>
<ul class="sub-menu">
	<li id="menu-item-137183" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137183"><a href="http://www.geeksforgeeks.org/campus-ambassador-program-by-geeksforgeeks/" class="reduceMenuHeight">Campus Ambassador Program</a></li>
	<li id="menu-item-204869" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-204869"><a href="https://www.geeksforgeeks.org/computer-science-projects/" class="reduceMenuHeight">Project</a></li>
	<li id="menu-item-137179" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137179"><a href="http://www.geeksforgeeks.org/geek-of-the-month/" class="reduceMenuHeight">Geek of the Month</a></li>
	<li id="menu-item-137570" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137570"><a href="http://geeksquiz.com/placements/" class="reduceMenuHeight">Placement Course</a></li>
	<li id="menu-item-137180" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137180"><a href="http://www.geeksforgeeks.org/category/competitive-programming/" class="reduceMenuHeight">Competitive Programming</a></li>
	<li id="menu-item-137181" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137181"><a href="http://www.geeksforgeeks.org/testimonials/" class="reduceMenuHeight">Testimonials</a></li>
	<li id="menu-item-138863" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-138863"><a href="http://www.geeksforgeeks.org/category/geek-on-the-top/" class="reduceMenuHeight">Geek on the Top</a></li>
	<li id="menu-item-141974" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-141974"><a href="http://www.geeksforgeeks.org/careers/" class="reduceMenuHeight">Careers</a></li>
	<li id="menu-item-137378" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137378"><a href="http://www.geeksforgeeks.org/internship/" class="reduceMenuHeight">Internship</a></li>
	<li id="menu-item-147457" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-147457"><a href="http://www.geeksforgeeks.org/school-programming/" class="reduceMenuHeight">School Programming</a></li>
</ul>
</li>
<li id="menu-item-146712" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-146712"><a href="https://www.geeksforgeeks.org/gate-cs-notes-gq/" class="reduceMenuHeight">GATE ▼</a>
<ul class="sub-menu">
	<li id="menu-item-146714" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146714"><a href="http://www.geeksforgeeks.org/gate-cs-notes-gq/" class="reduceMenuHeight">GATE Notes</a></li>
	<li id="menu-item-146713" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146713"><a href="http://www.geeksforgeeks.org/gate-corner-2-gq/" class="reduceMenuHeight">GATE CS Corner</a></li>
	<li id="menu-item-146715" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146715"><a href="http://www.geeksforgeeks.org/lmns-gq/" class="reduceMenuHeight">Last Minute Notes</a></li>
	<li id="menu-item-146717" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146717"><a href="https://www.geeksforgeeks.org/gate-cs-2019-important-dates-and-links/" class="reduceMenuHeight">GATE 2019</a></li>
	<li id="menu-item-146716" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146716"><a href="http://www.geeksforgeeks.org/original-gate-previous-year-question-papers-cse-and-it-gq/" class="reduceMenuHeight">GATE Official Papers</a></li>
	<li id="menu-item-211326" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-211326"><a href="https://www.geeksforgeeks.org/isro-cs-preparation/" class="reduceMenuHeight">ISRO CS Exam</a></li>
	<li id="menu-item-211327" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-211327"><a href="https://www.geeksforgeeks.org/ugc-net-cs-preparation/" class="reduceMenuHeight">UGC NET Papers</a></li>
	<li id="menu-item-211328" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-211328"><a href="https://www.geeksforgeeks.org/ugc-net-cs-notes-according-to-syllabus-of-paper-ii/" class="reduceMenuHeight">UGC NET CS Paper II</a></li>
	<li id="menu-item-215230" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-215230"><a href="https://www.geeksforgeeks.org/ugc-net-cs-notes-according-to-syllabus-of-paper-iii-core-group/" class="reduceMenuHeight">UGC NET CS Paper III</a></li>
</ul>
</li>
<li id="menu-item-146718" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-146718"><a href="http://www.geeksforgeeks.org/articles-on-computer-science-subjects-gq/" class="reduceMenuHeight">CS Subjects ▼</a>
<ul class="sub-menu">
	<li id="menu-item-203861" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-203861"><a href="https://www.geeksforgeeks.org/gate-cs-notes-gq/" class="reduceMenuHeight">Core Subjects  ►</a>
	<ul class="sub-menu">
		<li id="menu-item-146727" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146727"><a href="http://www.geeksforgeeks.org/engineering-mathematics-tutorials/" class="reduceMenuHeight">Engg. Mathematics</a></li>
		<li id="menu-item-146729" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146729"><a href="http://www.geeksforgeeks.org/operating-systems/" class="reduceMenuHeight">Operating Systems</a></li>
		<li id="menu-item-146721" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146721"><a href="http://www.geeksforgeeks.org/computer-network-tutorials/" class="reduceMenuHeight">Computer Networks</a></li>
		<li id="menu-item-146724" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146724"><a href="http://www.geeksforgeeks.org/dbms/" class="reduceMenuHeight">DBMS</a></li>
		<li id="menu-item-146720" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146720"><a href="http://www.geeksforgeeks.org/compiler-design-tutorials/" class="reduceMenuHeight">Compiler Design</a></li>
		<li id="menu-item-146730" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146730"><a href="http://www.geeksforgeeks.org/theory-of-computation-automata-tutorials/" class="reduceMenuHeight">Theory of Computation</a></li>
		<li id="menu-item-146726" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146726"><a href="http://www.geeksforgeeks.org/digital-electronics-logic-design-tutorials/" class="reduceMenuHeight">Digital Electronics</a></li>
		<li id="menu-item-146722" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146722"><a href="http://www.geeksforgeeks.org/computer-organization-and-architecture-tutorials/" class="reduceMenuHeight">Computer Organization &amp; Architecture</a></li>
		<li id="menu-item-213498" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-213498"><a href="https://www.geeksforgeeks.org/software-engineering/" class="reduceMenuHeight">Software Engineering</a></li>
		<li id="menu-item-200760" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-200760"><a href="https://www.geeksforgeeks.org/microprocessor-tutorials/" class="reduceMenuHeight">Microprocessor</a></li>
	</ul>
</li>
	<li id="menu-item-147831" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-147831"><a href="http://www.geeksforgeeks.org/web-technology/" class="reduceMenuHeight">Web Technology</a></li>
	<li id="menu-item-147512" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-147512"><a href="http://www.geeksforgeeks.org/advanced-computer-subjects-tutorials/" class="reduceMenuHeight">Advanced Topics</a></li>
	<li id="menu-item-203862" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-203862"><a href="https://www.geeksforgeeks.org/machine-learning/" class="reduceMenuHeight">Machine Learning</a></li>
	<li id="menu-item-204870" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-204870"><a href="https://www.geeksforgeeks.org/computer-graphics-2/" class="reduceMenuHeight">Computer Graphics</a></li>
	<li id="menu-item-146725" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146725"><a href="http://www.geeksforgeeks.org/category/geeksquiz/articles-gq/difference-gq/" class="reduceMenuHeight">What’s Difference?</a></li>
</ul>
</li>
<li id="menu-item-140855" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-140855"><a href="http://quiz.geeksforgeeks.org/quiz-corner/" class="reduceMenuHeight">Quizzes ▼</a>
<ul class="sub-menu">
	<li id="menu-item-146748" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-146748"><a href="http://www.geeksforgeeks.org/quizzes-on-programming-languages-gq/" class="reduceMenuHeight">Languages ►</a>
	<ul class="sub-menu">
		<li id="menu-item-146743" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146743"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#C%20Programming%20Mock%20Tests" class="reduceMenuHeight">C</a></li>
		<li id="menu-item-146745" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146745"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#C++%20Programming%20Mock%20Tests" class="reduceMenuHeight">C++</a></li>
		<li id="menu-item-146746" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146746"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#Java%20Programming%20Mock%20Tests" class="reduceMenuHeight">Java</a></li>
		<li id="menu-item-146747" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146747"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#Python%20Programming%20Mock%20Tests" class="reduceMenuHeight">Python</a></li>
	</ul>
</li>
	<li id="menu-item-146825" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-146825"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#Data%20Structures%20Mock%20Tests" class="reduceMenuHeight">CS Subjectwise ►</a>
	<ul class="sub-menu">
		<li id="menu-item-146731" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146731"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#Data%20Structures%20Mock%20Tests" class="reduceMenuHeight">Data Structures</a></li>
		<li id="menu-item-146732" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146732"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#Algorithms%20Mock%20Tests" class="reduceMenuHeight">Algorithms</a></li>
		<li id="menu-item-146733" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146733"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#Operating%20Systems%20Mock%20Tests" class="reduceMenuHeight">Operating Systems</a></li>
		<li id="menu-item-146734" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146734"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#DBMS%20Mock%20Tests" class="reduceMenuHeight">DBMS</a></li>
		<li id="menu-item-146735" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146735"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#Compiler%20Design%20Mock%20Tests" class="reduceMenuHeight">Compiler Design</a></li>
		<li id="menu-item-146736" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146736"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#Computer%20Networks%20Mock%20Tests" class="reduceMenuHeight">Computer Networks</a></li>
		<li id="menu-item-146737" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146737"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#Theory%20of%20Computation%20Mock%20Tests" class="reduceMenuHeight">Theory of Computation</a></li>
		<li id="menu-item-146738" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146738"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#Computer%20Organization%20and%20Architecture" class="reduceMenuHeight">Computer Organization</a></li>
		<li id="menu-item-146739" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146739"><a href="http://www.geeksforgeeks.org/software-engineering-gq/" class="reduceMenuHeight">Software Engineering</a></li>
	</ul>
</li>
	<li id="menu-item-146740" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146740"><a href="http://www.geeksforgeeks.org/html-and-xml-gq/" class="reduceMenuHeight">HTML &amp; XML</a></li>
	<li id="menu-item-146741" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146741"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#Engineering%20Mathematics" class="reduceMenuHeight">Engg. Mathematics</a></li>
	<li id="menu-item-146742" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146742"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#Aptitude%20Mock%20Tests" class="reduceMenuHeight">Aptitude</a></li>
</ul>
</li>
<li id="menu-item-135367" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-135367"><a href="https://www.geeksforgeeks.org/category/guestblogs/" class="reduceMenuHeight">GBlog</a></li>
<li id="menu-item-141885" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-141885"><a href="http://www.geeksforgeeks.org/puzzles/" class="reduceMenuHeight">Puzzles</a></li>
<li id="menu-item-141816" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-141816"><a href="https://practice.geeksforgeeks.org/" class="reduceMenuHeight">Practice</a></li>
</ul><select class="selectnav" id="selectnav1"><option value="">Menu</option><option value="https://www.geeksforgeeks.org/"></option><option value="http://www.geeksforgeeks.org/fundamentals-of-algorithms/">Algo ▼</option><option value="http://www.geeksforgeeks.org/fundamentals-of-algorithms/#AnalysisofAlgorithms">- Analysis of Algorithms</option><option value="http://www.geeksforgeeks.org/fundamentals-of-algorithms/">- Topicwise ►</option><option value="http://www.geeksforgeeks.org/searching-algorithms/">-- Searching Algorithms</option><option value="http://www.geeksforgeeks.org/sorting-algorithms/">-- Sorting Algorithms</option><option value="http://www.geeksforgeeks.org/graph-data-structure-and-algorithms/">-- Graph Algorithms</option><option value="http://www.geeksforgeeks.org/bitwise-algorithms/">-- Bit Algorithms</option><option value="https://www.geeksforgeeks.org/algorithms-gq/pattern-searching/">-- Pattern Searching</option><option value="http://www.geeksforgeeks.org/geometric-algorithms/">-- Geometric Algorithms</option><option value="http://www.geeksforgeeks.org/mathematical-algorithms/">-- Mathematical Algorithms</option><option value="http://www.geeksforgeeks.org/randomized-algorithms/">-- Randomized Algorithms</option><option value="https://www.geeksforgeeks.org/game-theory/">-- Game Theory</option><option value="http://www.geeksforgeeks.org/fundamentals-of-algorithms/">- Algorithm Paradigms ►</option><option value="http://www.geeksforgeeks.org/greedy-algorithms/">-- Greedy Algorithms</option><option value="http://www.geeksforgeeks.org/dynamic-programming/">-- Dynamic Programming</option><option value="http://www.geeksforgeeks.org/divide-and-conquer/">-- Divide and Conquer</option><option value="http://www.geeksforgeeks.org/backtracking-algorithms/">-- Backtracking</option><option value="https://www.geeksforgeeks.org/branch-and-bound-algorithm/">-- Branch &amp; Bound</option><option value="http://www.geeksforgeeks.org/fundamentals-of-algorithms/">- All Algorithms</option><option value="http://www.geeksforgeeks.org/data-structures/">DS ▼</option><option value="http://www.geeksforgeeks.org/array-data-structure/">- Array</option><option value="http://www.geeksforgeeks.org/data-structures/linked-list/">- LinkedList</option><option value="http://www.geeksforgeeks.org/stack-data-structure/">- Stack</option><option value="http://www.geeksforgeeks.org/queue-data-structure/">- Queue</option><option value="http://www.geeksforgeeks.org/data-structures/">- Tree based DS ►</option><option value="http://www.geeksforgeeks.org/binary-tree-data-structure/">-- Binary Tree</option><option value="http://www.geeksforgeeks.org/binary-search-tree-data-structure/">-- Binary Search Tree</option><option value="http://www.geeksforgeeks.org/heap-data-structure/">-- Heap</option><option value="http://www.geeksforgeeks.org/hashing-data-structure/">- Hashing</option><option value="http://www.geeksforgeeks.org/graph-data-structure-and-algorithms/">- Graph</option><option value="http://www.geeksforgeeks.org/advanced-data-structures/">- Advanced Data Structure</option><option value="http://www.geeksforgeeks.org/matrix/">- Matrix</option><option value="http://www.geeksforgeeks.org/string-data-structure/">- Strings</option><option value="http://www.geeksforgeeks.org/data-structures/">- All Data Structures</option><option value="http://www.geeksforgeeks.org/category/program-output/">Languages ▼</option><option value="https://www.geeksforgeeks.org/c-programming-language/">- C</option><option value="https://www.geeksforgeeks.org/c-plus-plus/">- C++</option><option value="https://www.geeksforgeeks.org/java/">- Java</option><option value="https://www.geeksforgeeks.org/python-programming-language/">- Python</option><option value="https://www.geeksforgeeks.org/csharp-programming-language/">- C#</option><option value="https://www.geeksforgeeks.org/php/">- PHP</option><option value="https://www.geeksforgeeks.org/javascript-tutorial/">- Javascript</option><option value="http://www.geeksforgeeks.org/sql-tutorial/">- SQL</option><option value="https://www.geeksforgeeks.org/html-tutorials/">- HTML</option><option value="https://www.geeksforgeeks.org/css-tutorials/">- CSS</option><option value="https://www.geeksforgeeks.org/category/program-output/">- Program Output</option><option value="http://www.geeksforgeeks.org/about/interview-corner/">Interview ▼</option><option value="https://www.geeksforgeeks.org/company-preparation/">- Company Prep</option><option value="http://www.geeksforgeeks.org/interview-preparation-for-software-developer/">- Top Topics</option><option value="https://practice.geeksforgeeks.org/company-tags">- Practice Company Questions</option><option value="http://www.geeksforgeeks.org/about/interview-corner/">- Interview Experiences</option><option value="https://www.geeksforgeeks.org/experienced-interview-experiences-company-wise/">- Experienced Interviews</option><option value="https://www.geeksforgeeks.org/internship-interview-experiences-company-wise/">- Internship Interviews</option><option value="http://www.geeksforgeeks.org/category/competitive-programming/">- Competitive Programming</option><option value="http://www.geeksforgeeks.org/software-design-patterns/">- Design Patterns</option><option value="http://geeksquiz.com/quiz-corner/">- Multiple Choice Quizzes</option><option value="http://www.geeksforgeeks.org/student-corner/">Students ▼</option><option value="http://www.geeksforgeeks.org/campus-ambassador-program-by-geeksforgeeks/">- Campus Ambassador Program</option><option value="https://www.geeksforgeeks.org/computer-science-projects/">- Project</option><option value="http://www.geeksforgeeks.org/geek-of-the-month/">- Geek of the Month</option><option value="http://geeksquiz.com/placements/">- Placement Course</option><option value="http://www.geeksforgeeks.org/category/competitive-programming/">- Competitive Programming</option><option value="http://www.geeksforgeeks.org/testimonials/">- Testimonials</option><option value="http://www.geeksforgeeks.org/category/geek-on-the-top/">- Geek on the Top</option><option value="http://www.geeksforgeeks.org/careers/">- Careers</option><option value="http://www.geeksforgeeks.org/internship/">- Internship</option><option value="http://www.geeksforgeeks.org/school-programming/">- School Programming</option><option value="https://www.geeksforgeeks.org/gate-cs-notes-gq/">GATE ▼</option><option value="http://www.geeksforgeeks.org/gate-cs-notes-gq/">- GATE Notes</option><option value="http://www.geeksforgeeks.org/gate-corner-2-gq/">- GATE CS Corner</option><option value="http://www.geeksforgeeks.org/lmns-gq/">- Last Minute Notes</option><option value="https://www.geeksforgeeks.org/gate-cs-2019-important-dates-and-links/">- GATE 2019</option><option value="http://www.geeksforgeeks.org/original-gate-previous-year-question-papers-cse-and-it-gq/">- GATE Official Papers</option><option value="https://www.geeksforgeeks.org/isro-cs-preparation/">- ISRO CS Exam</option><option value="https://www.geeksforgeeks.org/ugc-net-cs-preparation/">- UGC NET Papers</option><option value="https://www.geeksforgeeks.org/ugc-net-cs-notes-according-to-syllabus-of-paper-ii/">- UGC NET CS Paper II</option><option value="https://www.geeksforgeeks.org/ugc-net-cs-notes-according-to-syllabus-of-paper-iii-core-group/">- UGC NET CS Paper III</option><option value="http://www.geeksforgeeks.org/articles-on-computer-science-subjects-gq/">CS Subjects ▼</option><option value="https://www.geeksforgeeks.org/gate-cs-notes-gq/">- Core Subjects  ►</option><option value="http://www.geeksforgeeks.org/engineering-mathematics-tutorials/">-- Engg. Mathematics</option><option value="http://www.geeksforgeeks.org/operating-systems/">-- Operating Systems</option><option value="http://www.geeksforgeeks.org/computer-network-tutorials/">-- Computer Networks</option><option value="http://www.geeksforgeeks.org/dbms/">-- DBMS</option><option value="http://www.geeksforgeeks.org/compiler-design-tutorials/">-- Compiler Design</option><option value="http://www.geeksforgeeks.org/theory-of-computation-automata-tutorials/">-- Theory of Computation</option><option value="http://www.geeksforgeeks.org/digital-electronics-logic-design-tutorials/">-- Digital Electronics</option><option value="http://www.geeksforgeeks.org/computer-organization-and-architecture-tutorials/">-- Computer Organization &amp; Architecture</option><option value="https://www.geeksforgeeks.org/software-engineering/">-- Software Engineering</option><option value="https://www.geeksforgeeks.org/microprocessor-tutorials/">-- Microprocessor</option><option value="http://www.geeksforgeeks.org/web-technology/">- Web Technology</option><option value="http://www.geeksforgeeks.org/advanced-computer-subjects-tutorials/">- Advanced Topics</option><option value="https://www.geeksforgeeks.org/machine-learning/">- Machine Learning</option><option value="https://www.geeksforgeeks.org/computer-graphics-2/">- Computer Graphics</option><option value="http://www.geeksforgeeks.org/category/geeksquiz/articles-gq/difference-gq/">- What’s Difference?</option><option value="http://quiz.geeksforgeeks.org/quiz-corner/">Quizzes ▼</option><option value="http://www.geeksforgeeks.org/quizzes-on-programming-languages-gq/">- Languages ►</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#C%20Programming%20Mock%20Tests">-- C</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#C++%20Programming%20Mock%20Tests">-- C++</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#Java%20Programming%20Mock%20Tests">-- Java</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#Python%20Programming%20Mock%20Tests">-- Python</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#Data%20Structures%20Mock%20Tests">- CS Subjectwise ►</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#Data%20Structures%20Mock%20Tests">-- Data Structures</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#Algorithms%20Mock%20Tests">-- Algorithms</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#Operating%20Systems%20Mock%20Tests">-- Operating Systems</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#DBMS%20Mock%20Tests">-- DBMS</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#Compiler%20Design%20Mock%20Tests">-- Compiler Design</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#Computer%20Networks%20Mock%20Tests">-- Computer Networks</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#Theory%20of%20Computation%20Mock%20Tests">-- Theory of Computation</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#Computer%20Organization%20and%20Architecture">-- Computer Organization</option><option value="http://www.geeksforgeeks.org/software-engineering-gq/">-- Software Engineering</option><option value="http://www.geeksforgeeks.org/html-and-xml-gq/">- HTML &amp; XML</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#Engineering%20Mathematics">- Engg. Mathematics</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#Aptitude%20Mock%20Tests">- Aptitude</option><option value="https://www.geeksforgeeks.org/category/guestblogs/">GBlog</option><option value="http://www.geeksforgeeks.org/puzzles/">Puzzles</option><option value="https://practice.geeksforgeeks.org/">Practice</option></select></div>		</nav><!-- #site-navigation -->
		<div class="clear"></div>
	<!-- #masthead -->
<button id="scrollTopBtn" title="Scroll to Top" type="button" class="btn btn-success" style="display: inline-block; opacity: 1;">▲</button>
	<div id="main" class="wrapper">

<!-- Following 2 files are included for Article Feedback Project 'GFGSW-556' -->
<link href="./Binary_files/icon" rel="stylesheet">
<script src="./Binary_files/materialize.min.js"></script>

<div class="leftSideBarParent">
    <div class="leftSideBar">
        <ul class="leftBarList"><li><a href="https://www.geeksforgeeks.org/quick-sort-vs-merge-sort/">Quick Sort vs Merge Sort</a></li><li><a href="https://www.geeksforgeeks.org/find-the-missing-number-in-a-sorted-array/">Find the Missing Number in a sorted array</a></li><li><a href="https://www.geeksforgeeks.org/modular-exponentiation-recursive/">Modular exponentiation (Recursive)</a></li><li><a href="https://www.geeksforgeeks.org/merge-sort-with-o1-extra-space-merge-and-on-lg-n-time/">Merge Sort with O(1) extra space merge and O(n lg n) time</a></li><li><a href="https://www.geeksforgeeks.org/largest-perfect-square-number-in-an-array/">Largest perfect square number in an Array</a></li><li><a href="https://www.geeksforgeeks.org/dynamic-programming-vs-divide-and-conquer/">Dynamic Programming vs Divide-and-Conquer</a></li><li><a href="https://www.geeksforgeeks.org/kth-smallest-sum-of-continuous-subarrays-of-positive-numbers/">Kth Smallest sum of continuous subarrays of positive numbers</a></li><li><a href="https://www.geeksforgeeks.org/binary-search-in-javascript/">Binary Search In JavaScript</a></li><li><a href="https://www.geeksforgeeks.org/find-nth-term-a-matrix-exponentiation-example/">Find Nth term (A matrix exponentiation example)</a></li><li><a href="https://www.geeksforgeeks.org/minimum-in-an-array-which-is-first-decreasing-then-increasing/">Minimum in an array which is first decreasing then increasing</a></li><li><a href="https://www.geeksforgeeks.org/queries-to-check-whether-a-given-digit-is-present-in-the-given-range/">Queries to check whether a given digit is present in the given Range</a></li><li><a href="https://www.geeksforgeeks.org/binary-search-bisect-in-python/">Binary Search (bisect) in Python</a></li><li><a href="https://www.geeksforgeeks.org/minimum-k-such-that-every-substring-of-length-atleast-k-contains-a-character-c/">Minimum K such that every substring of length atleast K contains a character c</a></li><li><a href="https://www.geeksforgeeks.org/search-in-a-sorted-2d-matrix-stored-in-row-major-order/">Search in a sorted 2D matrix (Stored in row major order)</a></li><li><a href="https://www.geeksforgeeks.org/java-8-arrays-parallelsort-method-with-examples/">Java 8 | Arrays parallelSort() method with Examples</a></li><li><a href="https://www.geeksforgeeks.org/range-and-update-sum-queries-with-factorial/">Range and Update Sum Queries with Factorial</a></li><li><a href="https://www.geeksforgeeks.org/cut-all-the-rods-with-some-length-such-that-the-sum-of-cut-off-length-is-maximized/">Cut all the rods with some length such that the sum of cut-off length is maximized</a></li><li><a href="https://www.geeksforgeeks.org/minimum-operations-of-the-given-type-required-to-make-a-complete-graph/">Minimum operations of the given type required to make a complete graph</a></li><li><a href="https://www.geeksforgeeks.org/minimum-number-n-such-that-total-set-bits-of-all-numbers-from-1-to-n-is-at-least-x/">Minimum number N such that total set bits of all numbers from 1 to N is at-least X</a></li><li><a href="https://www.geeksforgeeks.org/numbers-that-are-bitwise-and-of-at-least-one-non-empty-sub-array/">Numbers that are bitwise AND of at least one non-empty sub-array</a></li><li><a href="https://www.geeksforgeeks.org/find-element-position-in-given-monotonic-sequence/">Find element position in given monotonic sequence</a></li><li><a href="https://www.geeksforgeeks.org/first-strictly-greater-element-in-a-sorted-array-in-java/">First strictly greater element in a sorted array in Java</a></li><li><a href="https://www.geeksforgeeks.org/first-strictly-smaller-element-in-a-sorted-array-in-java/">First strictly smaller element in a sorted array in Java</a></li><li><a href="https://www.geeksforgeeks.org/number-of-ways-to-divide-a-given-number-as-a-set-of-integers-in-decreasing-order/">Number of ways to divide a given number as a set of integers in decreasing order</a></li><li><a href="https://www.geeksforgeeks.org/search-equal-bigger-or-smaller-in-a-sorted-array-in-java/">Search equal, bigger or smaller in a sorted array in Java</a></li></ul>
    <div class="promotional" style="margin-top:15px;max-width:300px;">
    <script async="" src="./Binary_files/f(10).txt"></script>
    <!-- GfG-LeftBar -->
    <ins class="adsbygoogle" style="display: block; height: 600px;" data-ad-client="ca-pub-9465609616171866" data-ad-slot="1800357638" data-ad-format="auto" data-full-width-responsive="true" data-adsbygoogle-status="done"><ins id="aswift_1_expand" style="display:inline-table;border:none;height:600px;margin:0;padding:0;position:relative;visibility:visible;width:243px;background-color:transparent;"><ins id="aswift_1_anchor" style="display:block;border:none;height:600px;margin:0;padding:0;position:relative;visibility:visible;width:243px;background-color:transparent;"><iframe width="243" height="600" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" onload="var i=this.id,s=window.google_iframe_oncopy,H=s&amp;&amp;s.handlers,h=H&amp;&amp;H[i],w=this.contentWindow,d;try{d=w.document}catch(e){}if(h&amp;&amp;d&amp;&amp;(!d.body||!d.body.firstChild)){if(h.call){setTimeout(h,0)}else if(h.match){try{h=s.upd(h,i)}catch(e){}w.location.replace(h)}}" id="aswift_1" name="aswift_1" style="left:0;position:absolute;top:0;border:0px;width:243px;height:600px;" src="./Binary_files/saved_resource(8).html"></iframe></ins></ins></ins>
    <script>
    (adsbygoogle = window.adsbygoogle || []).push({});
  </script>
    </div><div class="promotional" style="margin-top:15px;"><a target="_blank" href="https://practice.geeksforgeeks.org/courses/AKTU-First-Year?vb=125"><img style="width: 100%;" src="./Binary_files/CprogrammingBanner.png"></a></div>    </div>
</div> 
	<div id="primary" class="site-content">
		<div id="content" role="main">
                        							 	<article id="post-142311" class="post-142311 post type-post status-publish format-standard hentry category-divide-and-conquer category-searching tag-accenture tag-binary-search tag-infosys tag-oracle tag-qualcomm tag-tcs tag-wipro"><div id="userActionsIcon" class="tooltip clear" onclick="scrollToUserActionsDiv()"><i class="material-icons">perm_identity</i><span class="tooltiptext">User Actions</span></div>
				<header class="entry-header">
						<h1 class="entry-title">Binary Search</h1>
				
						</header><!-- .entry-header -->

				<div class="entry-content">
			<p>Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].<!--more--></p>
<p>A simple approach is to do <strong><a href="http://quiz.geeksforgeeks.org/linear-search/">linear search</a>.</strong>The time complexity of above algorithm is O(n). Another approach to perform the same task is using Binary Search.  </p>
<p><strong>Binary Search:</strong> Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.</p>
<p>Example :<br>
<img src="./Binary_files/Binary-Search.png" alt="" width="1600" height="891" class="alignnone size-full wp-image-256607" srcset="https://www.geeksforgeeks.org/wp-content/uploads/Binary-Search.png 1600w, https://www.geeksforgeeks.org/wp-content/uploads/Binary-Search-300x167.png 300w, https://www.geeksforgeeks.org/wp-content/uploads/Binary-Search-768x428.png 768w, https://www.geeksforgeeks.org/wp-content/uploads/Binary-Search-1024x570.png 1024w, https://www.geeksforgeeks.org/wp-content/uploads/Binary-Search-660x368.png 660w" sizes="(max-width: 1600px) 100vw, 1600px"></p>
<p>The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(Log n). </p><br>
        <script async="" src="./Binary_files/f(10).txt"></script>
          <!-- post_top_responsive -->
          <ins class="adsbygoogle" style="display: block; height: 75px;" data-ad-client="ca-pub-9465609616171866" data-ad-slot="4501693235" data-ad-format="auto" data-adsbygoogle-status="done"><ins id="aswift_2_expand" style="display: inline-table; border: none; height: 75px; margin: 0px; padding: 0px; position: relative; visibility: visible; width: 641px; background-color: transparent;"><ins id="aswift_2_anchor" style="display: block; border: none; height: 75px; margin: 0px; padding: 0px; position: relative; visibility: visible; width: 641px; background-color: transparent; overflow: hidden;"><iframe width="641" height="75" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" onload="var i=this.id,s=window.google_iframe_oncopy,H=s&amp;&amp;s.handlers,h=H&amp;&amp;H[i],w=this.contentWindow,d;try{d=w.document}catch(e){}if(h&amp;&amp;d&amp;&amp;(!d.body||!d.body.firstChild)){if(h.call){setTimeout(h,0)}else if(h.match){try{h=s.upd(h,i)}catch(e){}w.location.replace(h)}}" id="aswift_2" name="aswift_2" style="left: 0px; position: absolute; top: 0px; border: 0px; width: 641px; height: 75px;" src="./Binary_files/saved_resource(9).html"></iframe></ins></ins></ins>
          <script>
          (adsbygoogle = window.adsbygoogle || []).push({});
        </script>
        <br>
            
<div id="practiceLinkDiv">
<h2>
                                        <a href="https://practice.geeksforgeeks.org/problems/who-will-win/0">Recommended: Please solve it on “<b><i><u>PRACTICE</u></i></b> ” first, before moving on to the solution.</a><br>
                                    </h2>
<p></p></div>
<p>We basically ignore half of the elements just after one comparison.</p>
<ol>
<li>Compare x with the middle element. </li>
<li>If x matches with middle element, we return the mid index.  </li>
<li> Else If x is greater than the mid element, then x can only lie in right half subarray after the mid element.  So we recur for right half. </li>
<li> Else (x is smaller) recur for the left half.</li>
</ol>
<p align="center"><strong>Recursive </strong> implementation of Binary Search </p>
<div class="responsive-tabs-wrapper"><div class="responsive-tabs responsive-tabs--enabled"><ul class="responsive-tabs__list" role="tablist"><li class="responsive-tabs__list__item" id="tablist1-tab1" aria-controls="tablist1-panel1" role="tab" tabindex="0">C</li><li class="responsive-tabs__list__item" id="tablist1-tab2" aria-controls="tablist1-panel2" role="tab" tabindex="0">C++</li><li class="responsive-tabs__list__item" id="tablist1-tab3" aria-controls="tablist1-panel3" role="tab" tabindex="0">Java</li><li class="responsive-tabs__list__item responsive-tabs__list__item--active" id="tablist1-tab4" aria-controls="tablist1-panel4" role="tab" tabindex="0">Python</li><li class="responsive-tabs__list__item" id="tablist1-tab5" aria-controls="tablist1-panel5" role="tab" tabindex="0">C#</li><li class="responsive-tabs__list__item" id="tablist1-tab6" aria-controls="tablist1-panel6" role="tab" tabindex="0">PHP</li></ul>
<h2 class="tabtitle responsive-tabs__heading" tabindex="0">C</h2>
<div class="tabcontent responsive-tabs__panel" aria-hidden="true" role="tabpanel" aria-labelledby="tablist1-tab1" id="tablist1-panel1" style="display: none;">

<div class="code-block">
<div class="code-gutter">
<div class="editor-buttons-container">
<div class="editor-buttons">
<div class="editor-buttons-div" title="Run and Edit">
                                    <i id="copy-code-button" title="Copy Code" class="material-icons code-sidebar-button copy-code-button">filter_none</i><p></p>
<div id="run-and-edit-loader" class="ring-load"></div>
<p>                                    <i id="run-and-edit-button" title="Edit Code" lang="c" class="material-icons code-sidebar-button">edit</i><br>
                                    <i id="close-code-editor-button" title="Close Editor" class="material-icons code-sidebar-button close-code-editor-button">close</i></p>
<div id="run-code-loader" class="ring-load"></div>
<p>                                    <i id="run-code-button" lang="c" title="Run Code and See Output" class="material-icons code-sidebar-button">play_arrow</i></p>
<div id="generate-url-loader" class="ring-load"></div>
<p>                                    <i id="generate-url-and-run-button" title="Run Code and Generate IDE URL" lang="c" class="material-icons code-sidebar-button generate-url-and-run-button">link</i><br>
                                    <i title="Dark Mode" class="material-icons code-sidebar-button dark-editor-button">brightness_4</i><br>
                                    <i id="edit-on-ide-button" title="Edit on IDE" lang="c" class="material-icons code-sidebar-button edit-on-ide-button">code</i>
                                </p></div>
<p></p></div>
<p></p></div>
<p></p></div>
<div class="code-container">
<div id="highlighter_691206" class="syntaxhighlighter nogutter  ">
<table border="0" cellpadding="0" cellspacing="0">
<tbody>
<tr>
<td class="code">
<div class="container">
<div class="line number1 index0 alt2"><code class="comments">// C program to implement recursive Binary Search </code></div>
<div class="line number2 index1 alt1"><code class="preprocessor">#include &lt;stdio.h&gt; </code></div>
<div class="line number3 index2 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number4 index3 alt1"><code class="comments">// A recursive binary search function. It returns </code></div>
<div class="line number5 index4 alt2"><code class="comments">// location of x in given array arr[l..r] is present, </code></div>
<div class="line number6 index5 alt1"><code class="comments">// otherwise -1 </code></div>
<div class="line number7 index6 alt2"><code class="color1 bold">int</code> <code class="plain">binarySearch(</code><code class="color1 bold">int</code> <code class="plain">arr[], </code><code class="color1 bold">int</code> <code class="plain">l, </code><code class="color1 bold">int</code> <code class="plain">r, </code><code class="color1 bold">int</code> <code class="plain">x) </code></div>
<div class="line number8 index7 alt1"><code class="plain">{ </code></div>
<div class="line number9 index8 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">if</code> <code class="plain">(r &gt;= l) { </code></div>
<div class="line number10 index9 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="color1 bold">int</code> <code class="plain">mid = l + (r - l) / 2; </code></div>
<div class="line number11 index10 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number12 index11 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// If the element is present at the middle </code></div>
<div class="line number13 index12 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// itself </code></div>
<div class="line number14 index13 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">if</code> <code class="plain">(arr[mid] == x) </code></div>
<div class="line number15 index14 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">return</code> <code class="plain">mid; </code></div>
<div class="line number16 index15 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number17 index16 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// If element is smaller than mid, then </code></div>
<div class="line number18 index17 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// it can only be present in left subarray </code></div>
<div class="line number19 index18 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">if</code> <code class="plain">(arr[mid] &gt; x) </code></div>
<div class="line number20 index19 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">return</code> <code class="plain">binarySearch(arr, l, mid - 1, x); </code></div>
<div class="line number21 index20 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number22 index21 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// Else the element can only be present </code></div>
<div class="line number23 index22 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// in right subarray </code></div>
<div class="line number24 index23 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">return</code> <code class="plain">binarySearch(arr, mid + 1, r, x); </code></div>
<div class="line number25 index24 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">} </code></div>
<div class="line number26 index25 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number27 index26 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// We reach here when element is not </code></div>
<div class="line number28 index27 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// present in array </code></div>
<div class="line number29 index28 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">return</code> <code class="plain">-1; </code></div>
<div class="line number30 index29 alt1"><code class="plain">} </code></div>
<div class="line number31 index30 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number32 index31 alt1"><code class="color1 bold">int</code> <code class="plain">main(</code><code class="keyword bold">void</code><code class="plain">) </code></div>
<div class="line number33 index32 alt2"><code class="plain">{ </code></div>
<div class="line number34 index33 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="color1 bold">int</code> <code class="plain">arr[] = { 2, 3, 4, 10, 40 }; </code></div>
<div class="line number35 index34 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="color1 bold">int</code> <code class="plain">n = </code><code class="keyword bold">sizeof</code><code class="plain">(arr) / </code><code class="keyword bold">sizeof</code><code class="plain">(arr[0]); </code></div>
<div class="line number36 index35 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="color1 bold">int</code> <code class="plain">x = 10; </code></div>
<div class="line number37 index36 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="color1 bold">int</code> <code class="plain">result = binarySearch(arr, 0, n - 1, x); </code></div>
<div class="line number38 index37 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">(result == -1) ? </code><code class="functions bold">printf</code><code class="plain">(</code><code class="string">"Element is not present in array"</code><code class="plain">) </code></div>
<div class="line number39 index38 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">: </code><code class="functions bold">printf</code><code class="plain">(</code><code class="string">"Element is present at index %d"</code><code class="plain">, </code></div>
<div class="line number40 index39 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">result); </code></div>
<div class="line number41 index40 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">return</code> <code class="plain">0; </code></div>
<div class="line number42 index41 alt1"><code class="plain">} </code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div></div>
<div class="code-editor-container"></div>
<p></p></div>
<div class="code-output-container">
<div class="output-block">
                        <i id="output-icon" title="Output" class="material-icons code-sidebar-button output-icon">chevron_right</i><p></p>
<pre class="output-pre"></pre>
<p></p></div>
<div class="ide-link-div">
                        <i id="copy-url-button" title="Copy Generated Ide URL" class="material-icons code-sidebar-button copy-url-button">filter_none</i><p></p>
<pre id="ide-url"></pre>
<p></p></div>
<p></p></div>

</div><h2 class="tabtitle responsive-tabs__heading" tabindex="0">C++</h2>
<div class="tabcontent responsive-tabs__panel" aria-hidden="true" role="tabpanel" aria-labelledby="tablist1-tab2" id="tablist1-panel2" style="display: none;">

<div class="code-block">
<div class="code-gutter">
<div class="editor-buttons-container">
<div class="editor-buttons">
<div class="editor-buttons-div" title="Run and Edit">
                                    <i id="copy-code-button" title="Copy Code" class="material-icons code-sidebar-button copy-code-button">filter_none</i><p></p>
<div id="run-and-edit-loader" class="ring-load"></div>
<p>                                    <i id="run-and-edit-button" title="Edit Code" lang="cpp" class="material-icons code-sidebar-button">edit</i><br>
                                    <i id="close-code-editor-button" title="Close Editor" class="material-icons code-sidebar-button close-code-editor-button">close</i></p>
<div id="run-code-loader" class="ring-load"></div>
<p>                                    <i id="run-code-button" lang="cpp" title="Run Code and See Output" class="material-icons code-sidebar-button">play_arrow</i></p>
<div id="generate-url-loader" class="ring-load"></div>
<p>                                    <i id="generate-url-and-run-button" title="Run Code and Generate IDE URL" lang="cpp" class="material-icons code-sidebar-button generate-url-and-run-button">link</i><br>
                                    <i title="Dark Mode" class="material-icons code-sidebar-button dark-editor-button">brightness_4</i><br>
                                    <i id="edit-on-ide-button" title="Edit on IDE" lang="cpp" class="material-icons code-sidebar-button edit-on-ide-button">code</i>
                                </p></div>
<p></p></div>
<p></p></div>
<p></p></div>
<div class="code-container">
<div id="highlighter_263145" class="syntaxhighlighter nogutter  ">
<table border="0" cellpadding="0" cellspacing="0">
<tbody>
<tr>
<td class="code">
<div class="container">
<div class="line number1 index0 alt2"><code class="comments">// C++ program to implement recursive Binary Search </code></div>
<div class="line number2 index1 alt1"><code class="preprocessor">#include &lt;iostream&gt; </code></div>
<div class="line number3 index2 alt2"><code class="keyword bold">using</code> <code class="keyword bold">namespace</code> <code class="plain">std; </code></div>
<div class="line number4 index3 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number5 index4 alt2"><code class="comments">// A recursive binary search function. It returns </code></div>
<div class="line number6 index5 alt1"><code class="comments">// location of x in given array arr[l..r] is present, </code></div>
<div class="line number7 index6 alt2"><code class="comments">// otherwise -1 </code></div>
<div class="line number8 index7 alt1"><code class="color1 bold">int</code> <code class="plain">binarySearch(</code><code class="color1 bold">int</code> <code class="plain">arr[], </code><code class="color1 bold">int</code> <code class="plain">l, </code><code class="color1 bold">int</code> <code class="plain">r, </code><code class="color1 bold">int</code> <code class="plain">x) </code></div>
<div class="line number9 index8 alt2"><code class="plain">{ </code></div>
<div class="line number10 index9 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">if</code> <code class="plain">(r &gt;= l) { </code></div>
<div class="line number11 index10 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="color1 bold">int</code> <code class="plain">mid = l + (r - l) / 2; </code></div>
<div class="line number12 index11 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number13 index12 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// If the element is present at the middle </code></div>
<div class="line number14 index13 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// itself </code></div>
<div class="line number15 index14 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">if</code> <code class="plain">(arr[mid] == x) </code></div>
<div class="line number16 index15 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">return</code> <code class="plain">mid; </code></div>
<div class="line number17 index16 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number18 index17 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// If element is smaller than mid, then </code></div>
<div class="line number19 index18 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// it can only be present in left subarray </code></div>
<div class="line number20 index19 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">if</code> <code class="plain">(arr[mid] &gt; x) </code></div>
<div class="line number21 index20 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">return</code> <code class="plain">binarySearch(arr, l, mid - 1, x); </code></div>
<div class="line number22 index21 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number23 index22 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// Else the element can only be present </code></div>
<div class="line number24 index23 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// in right subarray </code></div>
<div class="line number25 index24 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">return</code> <code class="plain">binarySearch(arr, mid + 1, r, x); </code></div>
<div class="line number26 index25 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">} </code></div>
<div class="line number27 index26 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number28 index27 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// We reach here when element is not </code></div>
<div class="line number29 index28 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// present in array </code></div>
<div class="line number30 index29 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">return</code> <code class="plain">-1; </code></div>
<div class="line number31 index30 alt2"><code class="plain">} </code></div>
<div class="line number32 index31 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number33 index32 alt2"><code class="color1 bold">int</code> <code class="plain">main(</code><code class="keyword bold">void</code><code class="plain">) </code></div>
<div class="line number34 index33 alt1"><code class="plain">{ </code></div>
<div class="line number35 index34 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="color1 bold">int</code> <code class="plain">arr[] = { 2, 3, 4, 10, 40 }; </code></div>
<div class="line number36 index35 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="color1 bold">int</code> <code class="plain">x = 10; </code></div>
<div class="line number37 index36 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="color1 bold">int</code> <code class="plain">n = </code><code class="keyword bold">sizeof</code><code class="plain">(arr) / </code><code class="keyword bold">sizeof</code><code class="plain">(arr[0]); </code></div>
<div class="line number38 index37 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="color1 bold">int</code> <code class="plain">result = binarySearch(arr, 0, n - 1, x); </code></div>
<div class="line number39 index38 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">(result == -1) ? cout &lt;&lt; </code><code class="string">"Element is not present in array"</code></div>
<div class="line number40 index39 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">: cout &lt;&lt; </code><code class="string">"Element is present at index "</code> <code class="plain">&lt;&lt; result; </code></div>
<div class="line number41 index40 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">return</code> <code class="plain">0; </code></div>
<div class="line number42 index41 alt1"><code class="plain">} </code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div></div>
<div class="code-editor-container"></div>
<p></p></div>
<div class="code-output-container">
<div class="output-block">
                        <i id="output-icon" title="Output" class="material-icons code-sidebar-button output-icon">chevron_right</i><p></p>
<pre class="output-pre"></pre>
<p></p></div>
<div class="ide-link-div">
                        <i id="copy-url-button" title="Copy Generated Ide URL" class="material-icons code-sidebar-button copy-url-button">filter_none</i><p></p>
<pre id="ide-url"></pre>
<p></p></div>
<p></p></div>

</div><h2 class="tabtitle responsive-tabs__heading" tabindex="0">Java</h2>
<div class="tabcontent responsive-tabs__panel" aria-hidden="true" role="tabpanel" aria-labelledby="tablist1-tab3" id="tablist1-panel3" style="display: none;">

<div class="code-block">
<div class="code-gutter">
<div class="editor-buttons-container">
<div class="editor-buttons">
<div class="editor-buttons-div" title="Run and Edit">
                                    <i id="copy-code-button" title="Copy Code" class="material-icons code-sidebar-button copy-code-button">filter_none</i><p></p>
<div id="run-and-edit-loader" class="ring-load"></div>
<p>                                    <i id="run-and-edit-button" title="Edit Code" lang="java" class="material-icons code-sidebar-button">edit</i><br>
                                    <i id="close-code-editor-button" title="Close Editor" class="material-icons code-sidebar-button close-code-editor-button">close</i></p>
<div id="run-code-loader" class="ring-load"></div>
<p>                                    <i id="run-code-button" lang="java" title="Run Code and See Output" class="material-icons code-sidebar-button">play_arrow</i></p>
<div id="generate-url-loader" class="ring-load"></div>
<p>                                    <i id="generate-url-and-run-button" title="Run Code and Generate IDE URL" lang="java" class="material-icons code-sidebar-button generate-url-and-run-button">link</i><br>
                                    <i title="Dark Mode" class="material-icons code-sidebar-button dark-editor-button">brightness_4</i><br>
                                    <i id="edit-on-ide-button" title="Edit on IDE" lang="java" class="material-icons code-sidebar-button edit-on-ide-button">code</i>
                                </p></div>
<p></p></div>
<p></p></div>
<p></p></div>
<div class="code-container">
<div id="highlighter_561861" class="syntaxhighlighter nogutter  ">
<table border="0" cellpadding="0" cellspacing="0">
<tbody>
<tr>
<td class="code">
<div class="container">
<div class="line number1 index0 alt2"><code class="comments">// Java implementation of recursive Binary Search </code></div>
<div class="line number2 index1 alt1"><code class="keyword">class</code> <code class="plain">BinarySearch { </code></div>
<div class="line number3 index2 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// Returns index of x if it is present in arr[l.. </code></div>
<div class="line number4 index3 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// r], else return -1 </code></div>
<div class="line number5 index4 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">int</code> <code class="plain">binarySearch(</code><code class="keyword">int</code> <code class="plain">arr[], </code><code class="keyword">int</code> <code class="plain">l, </code><code class="keyword">int</code> <code class="plain">r, </code><code class="keyword">int</code> <code class="plain">x) </code></div>
<div class="line number6 index5 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">{ </code></div>
<div class="line number7 index6 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">if</code> <code class="plain">(r &gt;= l) { </code></div>
<div class="line number8 index7 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">int</code> <code class="plain">mid = l + (r - l) / </code><code class="value">2</code><code class="plain">; </code></div>
<div class="line number9 index8 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number10 index9 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// If the element is present at the </code></div>
<div class="line number11 index10 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// middle itself </code></div>
<div class="line number12 index11 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">if</code> <code class="plain">(arr[mid] == x) </code></div>
<div class="line number13 index12 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">return</code> <code class="plain">mid; </code></div>
<div class="line number14 index13 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number15 index14 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// If element is smaller than mid, then </code></div>
<div class="line number16 index15 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// it can only be present in left subarray </code></div>
<div class="line number17 index16 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">if</code> <code class="plain">(arr[mid] &gt; x) </code></div>
<div class="line number18 index17 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">return</code> <code class="plain">binarySearch(arr, l, mid - </code><code class="value">1</code><code class="plain">, x); </code></div>
<div class="line number19 index18 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number20 index19 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// Else the element can only be present </code></div>
<div class="line number21 index20 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// in right subarray </code></div>
<div class="line number22 index21 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">return</code> <code class="plain">binarySearch(arr, mid + </code><code class="value">1</code><code class="plain">, r, x); </code></div>
<div class="line number23 index22 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">} </code></div>
<div class="line number24 index23 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number25 index24 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// We reach here when element is not present </code></div>
<div class="line number26 index25 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// in array </code></div>
<div class="line number27 index26 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">return</code> <code class="plain">-</code><code class="value">1</code><code class="plain">; </code></div>
<div class="line number28 index27 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">} </code></div>
<div class="line number29 index28 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number30 index29 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// Driver method to test above </code></div>
<div class="line number31 index30 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">public</code> <code class="keyword">static</code> <code class="keyword">void</code> <code class="plain">main(String args[]) </code></div>
<div class="line number32 index31 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">{ </code></div>
<div class="line number33 index32 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">BinarySearch ob = </code><code class="keyword">new</code> <code class="plain">BinarySearch(); </code></div>
<div class="line number34 index33 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">int</code> <code class="plain">arr[] = { </code><code class="value">2</code><code class="plain">, </code><code class="value">3</code><code class="plain">, </code><code class="value">4</code><code class="plain">, </code><code class="value">10</code><code class="plain">, </code><code class="value">40</code> <code class="plain">}; </code></div>
<div class="line number35 index34 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">int</code> <code class="plain">n = arr.length; </code></div>
<div class="line number36 index35 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">int</code> <code class="plain">x = </code><code class="value">10</code><code class="plain">; </code></div>
<div class="line number37 index36 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">int</code> <code class="plain">result = ob.binarySearch(arr, </code><code class="value">0</code><code class="plain">, n - </code><code class="value">1</code><code class="plain">, x); </code></div>
<div class="line number38 index37 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">if</code> <code class="plain">(result == -</code><code class="value">1</code><code class="plain">) </code></div>
<div class="line number39 index38 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">System.out.println(</code><code class="string">"Element not present"</code><code class="plain">); </code></div>
<div class="line number40 index39 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">else</code></div>
<div class="line number41 index40 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">System.out.println(</code><code class="string">"Element found at index "</code> <code class="plain">+ result); </code></div>
<div class="line number42 index41 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">} </code></div>
<div class="line number43 index42 alt2"><code class="plain">} </code></div>
<div class="line number44 index43 alt1"><code class="comments">/* This code is contributed by Rajat Mishra */</code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div></div>
<div class="code-editor-container"></div>
<p></p></div>
<div class="code-output-container">
<div class="output-block">
                        <i id="output-icon" title="Output" class="material-icons code-sidebar-button output-icon">chevron_right</i><p></p>
<pre class="output-pre"></pre>
<p></p></div>
<div class="ide-link-div">
                        <i id="copy-url-button" title="Copy Generated Ide URL" class="material-icons code-sidebar-button copy-url-button">filter_none</i><p></p>
<pre id="ide-url"></pre>
<p></p></div>
<p></p></div>

</div><h2 class="tabtitle responsive-tabs__heading responsive-tabs__heading--active" tabindex="0">Python</h2>
<div class="tabcontent responsive-tabs__panel responsive-tabs__panel--active" aria-hidden="false" role="tabpanel" aria-labelledby="tablist1-tab4" id="tablist1-panel4" style="display: block;">

<div class="code-block">
<div class="code-gutter">
<div class="editor-buttons-container">
<div class="editor-buttons">
<div class="editor-buttons-div" title="Run and Edit">
                                    <i id="copy-code-button" title="Copy Code" class="material-icons code-sidebar-button copy-code-button">filter_none</i><p></p>
<div id="run-and-edit-loader" class="ring-load"></div>
<p>                                    <i id="run-and-edit-button" title="Edit Code" lang="python" class="material-icons code-sidebar-button">edit</i><br>
                                    <i id="close-code-editor-button" title="Close Editor" class="material-icons code-sidebar-button close-code-editor-button">close</i></p>
<div id="run-code-loader" class="ring-load"></div>
<p>                                    <i id="run-code-button" lang="python" title="Run Code and See Output" class="material-icons code-sidebar-button">play_arrow</i></p>
<div id="generate-url-loader" class="ring-load"></div>
<p>                                    <i id="generate-url-and-run-button" title="Run Code and Generate IDE URL" lang="python" class="material-icons code-sidebar-button generate-url-and-run-button">link</i><br>
                                    <i title="Dark Mode" class="material-icons code-sidebar-button dark-editor-button">brightness_4</i><br>
                                    <i id="edit-on-ide-button" title="Edit on IDE" lang="python" class="material-icons code-sidebar-button edit-on-ide-button">code</i>
                                </p></div>
<p></p></div>
<p></p></div>
<p></p></div>
<div class="code-container">
<div id="highlighter_762754" class="syntaxhighlighter nogutter  ">
<table border="0" cellpadding="0" cellspacing="0">
<tbody>
<tr>
<td class="code">
<div class="container">
<div class="line number1 index0 alt2"><code class="comments"># Python Program for recursive binary search. </code></div>
<div class="line number2 index1 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number3 index2 alt2 highlighted"><code class="comments"># Returns index of x in arr if present, else -1 </code></div>
<div class="line number4 index3 alt1"><code class="keyword">def</code> <code class="plain">binarySearch (arr, l, r, x): </code></div>
<div class="line number5 index4 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number6 index5 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments"># Check base case </code></div>
<div class="line number7 index6 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">if</code> <code class="plain">r &gt;</code><code class="keyword">=</code> <code class="plain">l: </code></div>
<div class="line number8 index7 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number9 index8 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">mid </code><code class="keyword">=</code> <code class="plain">l </code><code class="keyword">+</code> <code class="plain">(r </code><code class="keyword">-</code> <code class="plain">l)</code><code class="keyword">/</code><code class="value">2</code></div>
<div class="line number10 index9 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number11 index10 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments"># If element is present at the middle itself </code></div>
<div class="line number12 index11 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">if</code> <code class="plain">arr[mid] </code><code class="keyword">=</code><code class="keyword">=</code> <code class="plain">x: </code></div>
<div class="line number13 index12 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">return</code> <code class="plain">mid </code></div>
<div class="line number14 index13 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code>&nbsp;</div>
<div class="line number15 index14 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments"># If element is smaller than mid, then it&nbsp; </code></div>
<div class="line number16 index15 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments"># can only be present in left subarray </code></div>
<div class="line number17 index16 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">elif</code> <code class="plain">arr[mid] &gt; x: </code></div>
<div class="line number18 index17 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">return</code> <code class="plain">binarySearch(arr, l, mid</code><code class="keyword">-</code><code class="value">1</code><code class="plain">, x) </code></div>
<div class="line number19 index18 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number20 index19 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments"># Else the element can only be present&nbsp; </code></div>
<div class="line number21 index20 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments"># in right subarray </code></div>
<div class="line number22 index21 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">else</code><code class="plain">: </code></div>
<div class="line number23 index22 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">return</code> <code class="plain">binarySearch(arr, mid </code><code class="keyword">+</code> <code class="value">1</code><code class="plain">, r, x) </code></div>
<div class="line number24 index23 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number25 index24 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">else</code><code class="plain">: </code></div>
<div class="line number26 index25 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments"># Element is not present in the array </code></div>
<div class="line number27 index26 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">return</code> <code class="keyword">-</code><code class="value">1</code></div>
<div class="line number28 index27 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number29 index28 alt2"><code class="comments"># Test array </code></div>
<div class="line number30 index29 alt1"><code class="plain">arr </code><code class="keyword">=</code> <code class="plain">[ </code><code class="value">2</code><code class="plain">, </code><code class="value">3</code><code class="plain">, </code><code class="value">4</code><code class="plain">, </code><code class="value">10</code><code class="plain">, </code><code class="value">40</code> <code class="plain">] </code></div>
<div class="line number31 index30 alt2"><code class="plain">x </code><code class="keyword">=</code> <code class="value">10</code></div>
<div class="line number32 index31 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number33 index32 alt2"><code class="comments"># Function call </code></div>
<div class="line number34 index33 alt1"><code class="plain">result </code><code class="keyword">=</code> <code class="plain">binarySearch(arr, </code><code class="value">0</code><code class="plain">, </code><code class="functions">len</code><code class="plain">(arr)</code><code class="keyword">-</code><code class="value">1</code><code class="plain">, x) </code></div>
<div class="line number35 index34 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number36 index35 alt1"><code class="keyword">if</code> <code class="plain">result !</code><code class="keyword">=</code> <code class="keyword">-</code><code class="value">1</code><code class="plain">: </code></div>
<div class="line number37 index36 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="functions">print</code> <code class="string">"Element is present at index % d"</code> <code class="keyword">%</code> <code class="plain">result </code></div>
<div class="line number38 index37 alt1"><code class="keyword">else</code><code class="plain">: </code></div>
<div class="line number39 index38 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="functions">print</code> <code class="string">"Element is not present in array"</code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div></div>
<div class="code-editor-container"></div>
<p></p></div>
<div class="code-output-container">
<div class="output-block">
                        <i id="output-icon" title="Output" class="material-icons code-sidebar-button output-icon">chevron_right</i><p></p>
<pre class="output-pre"></pre>
<p></p></div>
<div class="ide-link-div">
                        <i id="copy-url-button" title="Copy Generated Ide URL" class="material-icons code-sidebar-button copy-url-button">filter_none</i><p></p>
<pre id="ide-url"></pre>
<p></p></div>
<p></p></div>

</div><h2 class="tabtitle responsive-tabs__heading" tabindex="0">C#</h2>
<div class="tabcontent responsive-tabs__panel" aria-hidden="true" role="tabpanel" aria-labelledby="tablist1-tab5" id="tablist1-panel5" style="display: none;">

<div class="code-block">
<div class="code-gutter">
<div class="editor-buttons-container">
<div class="editor-buttons">
<div class="editor-buttons-div" title="Run and Edit">
                                    <i id="copy-code-button" title="Copy Code" class="material-icons code-sidebar-button copy-code-button">filter_none</i><p></p>
<div id="run-and-edit-loader" class="ring-load"></div>
<p>                                    <i id="run-and-edit-button" title="Edit Code" lang="csharp" class="material-icons code-sidebar-button">edit</i><br>
                                    <i id="close-code-editor-button" title="Close Editor" class="material-icons code-sidebar-button close-code-editor-button">close</i></p>
<div id="run-code-loader" class="ring-load"></div>
<p>                                    <i id="run-code-button" lang="csharp" title="Run Code and See Output" class="material-icons code-sidebar-button">play_arrow</i></p>
<div id="generate-url-loader" class="ring-load"></div>
<p>                                    <i id="generate-url-and-run-button" title="Run Code and Generate IDE URL" lang="csharp" class="material-icons code-sidebar-button generate-url-and-run-button">link</i><br>
                                    <i title="Dark Mode" class="material-icons code-sidebar-button dark-editor-button">brightness_4</i><br>
                                    <i id="edit-on-ide-button" title="Edit on IDE" lang="csharp" class="material-icons code-sidebar-button edit-on-ide-button">code</i>
                                </p></div>
<p></p></div>
<p></p></div>
<p></p></div>
<div class="code-container">
<div id="highlighter_439931" class="syntaxhighlighter nogutter  ">
<table border="0" cellpadding="0" cellspacing="0">
<tbody>
<tr>
<td class="code">
<div class="container">
<div class="line number1 index0 alt2"><code class="comments">// C# implementation of recursive Binary Search </code></div>
<div class="line number2 index1 alt1"><code class="keyword">using</code> <code class="plain">System; </code></div>
<div class="line number3 index2 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number4 index3 alt1"><code class="keyword">class</code> <code class="plain">GFG { </code></div>
<div class="line number5 index4 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// Returns index of x if it is present in </code></div>
<div class="line number6 index5 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// arr[l..r], else return -1 </code></div>
<div class="line number7 index6 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">static</code> <code class="keyword">int</code> <code class="plain">binarySearch(</code><code class="keyword">int</code><code class="plain">[] arr, </code><code class="keyword">int</code> <code class="plain">l, </code></div>
<div class="line number8 index7 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">int</code> <code class="plain">r, </code><code class="keyword">int</code> <code class="plain">x) </code></div>
<div class="line number9 index8 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">{ </code></div>
<div class="line number10 index9 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">if</code> <code class="plain">(r &gt;= l) { </code></div>
<div class="line number11 index10 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">int</code> <code class="plain">mid = l + (r - l) / 2; </code></div>
<div class="line number12 index11 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number13 index12 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// If the element is present at the </code></div>
<div class="line number14 index13 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// middle itself </code></div>
<div class="line number15 index14 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">if</code> <code class="plain">(arr[mid] == x) </code></div>
<div class="line number16 index15 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">return</code> <code class="plain">mid; </code></div>
<div class="line number17 index16 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number18 index17 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// If element is smaller than mid, then </code></div>
<div class="line number19 index18 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// it can only be present in left subarray </code></div>
<div class="line number20 index19 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">if</code> <code class="plain">(arr[mid] &gt; x) </code></div>
<div class="line number21 index20 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">return</code> <code class="plain">binarySearch(arr, l, mid - 1, x); </code></div>
<div class="line number22 index21 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number23 index22 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// Else the element can only be present </code></div>
<div class="line number24 index23 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// in right subarray </code></div>
<div class="line number25 index24 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">return</code> <code class="plain">binarySearch(arr, mid + 1, r, x); </code></div>
<div class="line number26 index25 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">} </code></div>
<div class="line number27 index26 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number28 index27 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// We reach here when element is not present </code></div>
<div class="line number29 index28 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// in array </code></div>
<div class="line number30 index29 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">return</code> <code class="plain">-1; </code></div>
<div class="line number31 index30 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">} </code></div>
<div class="line number32 index31 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number33 index32 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// Driver method to test above </code></div>
<div class="line number34 index33 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">public</code> <code class="keyword">static</code> <code class="keyword">void</code> <code class="plain">Main() </code></div>
<div class="line number35 index34 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">{ </code></div>
<div class="line number36 index35 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number37 index36 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">int</code><code class="plain">[] arr = { 2, 3, 4, 10, 40 }; </code></div>
<div class="line number38 index37 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">int</code> <code class="plain">n = arr.Length; </code></div>
<div class="line number39 index38 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">int</code> <code class="plain">x = 10; </code></div>
<div class="line number40 index39 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number41 index40 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">int</code> <code class="plain">result = binarySearch(arr, 0, n - 1, x); </code></div>
<div class="line number42 index41 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number43 index42 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">if</code> <code class="plain">(result == -1) </code></div>
<div class="line number44 index43 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">Console.WriteLine(</code><code class="string">"Element not present"</code><code class="plain">); </code></div>
<div class="line number45 index44 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">else</code></div>
<div class="line number46 index45 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">Console.WriteLine(</code><code class="string">"Element found at index "</code></div>
<div class="line number47 index46 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">+ result); </code></div>
<div class="line number48 index47 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">} </code></div>
<div class="line number49 index48 alt2"><code class="plain">} </code></div>
<div class="line number50 index49 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number51 index50 alt2"><code class="comments">// This code is contributed by Sam007. </code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div></div>
<div class="code-editor-container"></div>
<p></p></div>
<div class="code-output-container">
<div class="output-block">
                        <i id="output-icon" title="Output" class="material-icons code-sidebar-button output-icon">chevron_right</i><p></p>
<pre class="output-pre"></pre>
<p></p></div>
<div class="ide-link-div">
                        <i id="copy-url-button" title="Copy Generated Ide URL" class="material-icons code-sidebar-button copy-url-button">filter_none</i><p></p>
<pre id="ide-url"></pre>
<p></p></div>
<p></p></div>

</div><h2 class="tabtitle responsive-tabs__heading" tabindex="0">PHP</h2>
<div class="tabcontent responsive-tabs__panel" aria-hidden="true" role="tabpanel" aria-labelledby="tablist1-tab6" id="tablist1-panel6" style="display: none;">

<div class="code-block">
<div class="code-gutter">
<div class="editor-buttons-container">
<div class="editor-buttons">
<div class="editor-buttons-div" title="Run and Edit">
                                    <i id="copy-code-button" title="Copy Code" class="material-icons code-sidebar-button copy-code-button">filter_none</i><p></p>
<div id="run-and-edit-loader" class="ring-load"></div>
<p>                                    <i id="run-and-edit-button" title="Edit Code" lang="php" class="material-icons code-sidebar-button">edit</i><br>
                                    <i id="close-code-editor-button" title="Close Editor" class="material-icons code-sidebar-button close-code-editor-button">close</i></p>
<div id="run-code-loader" class="ring-load"></div>
<p>                                    <i id="run-code-button" lang="php" title="Run Code and See Output" class="material-icons code-sidebar-button">play_arrow</i></p>
<div id="generate-url-loader" class="ring-load"></div>
<p>                                    <i id="generate-url-and-run-button" title="Run Code and Generate IDE URL" lang="php" class="material-icons code-sidebar-button generate-url-and-run-button">link</i><br>
                                    <i title="Dark Mode" class="material-icons code-sidebar-button dark-editor-button">brightness_4</i><br>
                                    <i id="edit-on-ide-button" title="Edit on IDE" lang="php" class="material-icons code-sidebar-button edit-on-ide-button">code</i>
                                </p></div>
<p></p></div>
<p></p></div>
<p></p></div>
<div class="code-container">
<div id="highlighter_51629" class="syntaxhighlighter nogutter  ">
<table border="0" cellpadding="0" cellspacing="0">
<tbody>
<tr>
<td class="code">
<div class="container">
<div class="line number1 index0 alt2"><code class="plain">&lt;?php </code></div>
<div class="line number2 index1 alt1"><code class="comments">// PHP program to implement </code></div>
<div class="line number3 index2 alt2"><code class="comments">// recursive Binary Search </code></div>
<div class="line number4 index3 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number5 index4 alt2"><code class="comments">// A recursive binary search </code></div>
<div class="line number6 index5 alt1"><code class="comments">// function. It returns location </code></div>
<div class="line number7 index6 alt2"><code class="comments">// of x in given array arr[l..r]&nbsp; </code></div>
<div class="line number8 index7 alt1"><code class="comments">// is present, otherwise -1 </code></div>
<div class="line number9 index8 alt2"><code class="keyword">function</code> <code class="plain">binarySearch(</code><code class="variable">$arr</code><code class="plain">, </code><code class="variable">$l</code><code class="plain">, </code><code class="variable">$r</code><code class="plain">, </code><code class="variable">$x</code><code class="plain">) </code></div>
<div class="line number10 index9 alt1"><code class="plain">{ </code></div>
<div class="line number11 index10 alt2"><code class="keyword">if</code> <code class="plain">(</code><code class="variable">$r</code> <code class="plain">&gt;= </code><code class="variable">$l</code><code class="plain">) </code></div>
<div class="line number12 index11 alt1"><code class="plain">{ </code></div>
<div class="line number13 index12 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="variable">$mid</code> <code class="plain">= </code><code class="variable">$l</code> <code class="plain">+ (</code><code class="variable">$r</code> <code class="plain">- </code><code class="variable">$l</code><code class="plain">) / 2; </code></div>
<div class="line number14 index13 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number15 index14 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// If the element is present&nbsp; </code></div>
<div class="line number16 index15 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// at the middle itself </code></div>
<div class="line number17 index16 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">if</code> <code class="plain">(</code><code class="variable">$arr</code><code class="plain">[</code><code class="variable">$mid</code><code class="plain">] == </code><code class="variable">$x</code><code class="plain">)&nbsp; </code></div>
<div class="line number18 index17 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">return</code> <code class="functions">floor</code><code class="plain">(</code><code class="variable">$mid</code><code class="plain">); </code></div>
<div class="line number19 index18 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number20 index19 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// If element is smaller than&nbsp; </code></div>
<div class="line number21 index20 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// mid, then it can only be&nbsp; </code></div>
<div class="line number22 index21 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// present in left subarray </code></div>
<div class="line number23 index22 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">if</code> <code class="plain">(</code><code class="variable">$arr</code><code class="plain">[</code><code class="variable">$mid</code><code class="plain">] &gt; </code><code class="variable">$x</code><code class="plain">)&nbsp; </code></div>
<div class="line number24 index23 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">return</code> <code class="plain">binarySearch(</code><code class="variable">$arr</code><code class="plain">, </code><code class="variable">$l</code><code class="plain">,&nbsp; </code></div>
<div class="line number25 index24 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="variable">$mid</code> <code class="plain">- 1, </code><code class="variable">$x</code><code class="plain">); </code></div>
<div class="line number26 index25 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number27 index26 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// Else the element can only&nbsp; </code></div>
<div class="line number28 index27 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// be present in right subarray </code></div>
<div class="line number29 index28 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">return</code> <code class="plain">binarySearch(</code><code class="variable">$arr</code><code class="plain">, </code><code class="variable">$mid</code> <code class="plain">+ 1,&nbsp; </code></div>
<div class="line number30 index29 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="variable">$r</code><code class="plain">, </code><code class="variable">$x</code><code class="plain">); </code></div>
<div class="line number31 index30 alt2"><code class="plain">} </code></div>
<div class="line number32 index31 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number33 index32 alt2"><code class="comments">// We reach here when element&nbsp; </code></div>
<div class="line number34 index33 alt1"><code class="comments">// is not present in array </code></div>
<div class="line number35 index34 alt2"><code class="keyword">return</code> <code class="plain">-1; </code></div>
<div class="line number36 index35 alt1"><code class="plain">} </code></div>
<div class="line number37 index36 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number38 index37 alt1"><code class="comments">// Driver Code </code></div>
<div class="line number39 index38 alt2"><code class="variable">$arr</code> <code class="plain">= </code><code class="keyword">array</code><code class="plain">(2, 3, 4, 10, 40); </code></div>
<div class="line number40 index39 alt1"><code class="variable">$n</code> <code class="plain">= </code><code class="functions">count</code><code class="plain">(</code><code class="variable">$arr</code><code class="plain">); </code></div>
<div class="line number41 index40 alt2"><code class="variable">$x</code> <code class="plain">= 10; </code></div>
<div class="line number42 index41 alt1"><code class="variable">$result</code> <code class="plain">= binarySearch(</code><code class="variable">$arr</code><code class="plain">, 0, </code><code class="variable">$n</code> <code class="plain">- 1, </code><code class="variable">$x</code><code class="plain">); </code></div>
<div class="line number43 index42 alt2"><code class="keyword">if</code><code class="plain">((</code><code class="variable">$result</code> <code class="plain">== -1)) </code></div>
<div class="line number44 index43 alt1"><code class="functions">echo</code> <code class="string">"Element is not present in array"</code><code class="plain">; </code></div>
<div class="line number45 index44 alt2"><code class="keyword">else</code></div>
<div class="line number46 index45 alt1"><code class="functions">echo</code> <code class="string">"Element is present at index "</code><code class="plain">, </code></div>
<div class="line number47 index46 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="variable">$result</code><code class="plain">; </code></div>
<div class="line number48 index47 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code>&nbsp;</div>
<div class="line number49 index48 alt2"><code class="comments">// This code is contributed by anuj_67. </code></div>
<div class="line number50 index49 alt1"><code class="plain">?&gt; </code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div></div>
<div class="code-editor-container"></div>
<p></p></div>
<div class="code-output-container">
<div class="output-block">
                        <i id="output-icon" title="Output" class="material-icons code-sidebar-button output-icon">chevron_right</i><p></p>
<pre class="output-pre"></pre>
<p></p></div>
<div class="ide-link-div">
                        <i id="copy-url-button" title="Copy Generated Ide URL" class="material-icons code-sidebar-button copy-url-button">filter_none</i><p></p>
<pre id="ide-url"></pre>
<p></p></div>
<p></p></div>
<p></p></div></div></div><br>
<strong>Output :</strong> <p></p>
<pre>Element is present at index 3</pre>
<p align="center"> <strong>Iterative </strong> implementation of Binary Search</p>
<div class="responsive-tabs-wrapper"><div class="responsive-tabs responsive-tabs--enabled"><ul class="responsive-tabs__list" role="tablist"><li class="responsive-tabs__list__item responsive-tabs__list__item--active" id="tablist2-tab1" aria-controls="tablist2-panel1" role="tab" tabindex="0">C</li><li class="responsive-tabs__list__item" id="tablist2-tab2" aria-controls="tablist2-panel2" role="tab" tabindex="0">C++</li><li class="responsive-tabs__list__item" id="tablist2-tab3" aria-controls="tablist2-panel3" role="tab" tabindex="0">Java</li><li class="responsive-tabs__list__item" id="tablist2-tab4" aria-controls="tablist2-panel4" role="tab" tabindex="0">Python</li><li class="responsive-tabs__list__item" id="tablist2-tab5" aria-controls="tablist2-panel5" role="tab" tabindex="0">C#</li><li class="responsive-tabs__list__item" id="tablist2-tab6" aria-controls="tablist2-panel6" role="tab" tabindex="0">PHP</li></ul>
<h2 class="tabtitle responsive-tabs__heading responsive-tabs__heading--active" tabindex="0">C</h2>
<div class="tabcontent responsive-tabs__panel responsive-tabs__panel--active" aria-hidden="false" role="tabpanel" aria-labelledby="tablist2-tab1" id="tablist2-panel1">

<div class="code-block">
<div class="code-gutter">
<div class="editor-buttons-container">
<div class="editor-buttons">
<div class="editor-buttons-div" title="Run and Edit">
                                    <i id="copy-code-button" title="Copy Code" class="material-icons code-sidebar-button copy-code-button">filter_none</i><p></p>
<div id="run-and-edit-loader" class="ring-load"></div>
<p>                                    <i id="run-and-edit-button" title="Edit Code" lang="c" class="material-icons code-sidebar-button">edit</i><br>
                                    <i id="close-code-editor-button" title="Close Editor" class="material-icons code-sidebar-button close-code-editor-button">close</i></p>
<div id="run-code-loader" class="ring-load"></div>
<p>                                    <i id="run-code-button" lang="c" title="Run Code and See Output" class="material-icons code-sidebar-button">play_arrow</i></p>
<div id="generate-url-loader" class="ring-load"></div>
<p>                                    <i id="generate-url-and-run-button" title="Run Code and Generate IDE URL" lang="c" class="material-icons code-sidebar-button generate-url-and-run-button">link</i><br>
                                    <i title="Dark Mode" class="material-icons code-sidebar-button dark-editor-button">brightness_4</i><br>
                                    <i id="edit-on-ide-button" title="Edit on IDE" lang="c" class="material-icons code-sidebar-button edit-on-ide-button">code</i>
                                </p></div>
<p></p></div>
<p></p></div>
<p></p></div>
<div class="code-container">
<div id="highlighter_988465" class="syntaxhighlighter nogutter  ">
<table border="0" cellpadding="0" cellspacing="0">
<tbody>
<tr>
<td class="code">
<div class="container">
<div class="line number1 index0 alt2"><code class="comments">// C program to implement iterative Binary Search </code></div>
<div class="line number2 index1 alt1"><code class="preprocessor">#include &lt;stdio.h&gt; </code></div>
<div class="line number3 index2 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number4 index3 alt1"><code class="comments">// A iterative binary search function. It returns </code></div>
<div class="line number5 index4 alt2"><code class="comments">// location of x in given array arr[l..r] if present, </code></div>
<div class="line number6 index5 alt1"><code class="comments">// otherwise -1 </code></div>
<div class="line number7 index6 alt2"><code class="color1 bold">int</code> <code class="plain">binarySearch(</code><code class="color1 bold">int</code> <code class="plain">arr[], </code><code class="color1 bold">int</code> <code class="plain">l, </code><code class="color1 bold">int</code> <code class="plain">r, </code><code class="color1 bold">int</code> <code class="plain">x) </code></div>
<div class="line number8 index7 alt1"><code class="plain">{ </code></div>
<div class="line number9 index8 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">while</code> <code class="plain">(l &lt;= r) { </code></div>
<div class="line number10 index9 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="color1 bold">int</code> <code class="plain">m = l + (r - l) / 2; </code></div>
<div class="line number11 index10 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number12 index11 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// Check if x is present at mid </code></div>
<div class="line number13 index12 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">if</code> <code class="plain">(arr[m] == x) </code></div>
<div class="line number14 index13 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">return</code> <code class="plain">m; </code></div>
<div class="line number15 index14 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number16 index15 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// If x greater, ignore left half </code></div>
<div class="line number17 index16 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">if</code> <code class="plain">(arr[m] &lt; x) </code></div>
<div class="line number18 index17 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">l = m + 1; </code></div>
<div class="line number19 index18 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number20 index19 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// If x is smaller, ignore right half </code></div>
<div class="line number21 index20 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">else</code></div>
<div class="line number22 index21 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">r = m - 1; </code></div>
<div class="line number23 index22 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">} </code></div>
<div class="line number24 index23 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number25 index24 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// if we reach here, then element was </code></div>
<div class="line number26 index25 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// not present </code></div>
<div class="line number27 index26 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">return</code> <code class="plain">-1; </code></div>
<div class="line number28 index27 alt1"><code class="plain">} </code></div>
<div class="line number29 index28 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number30 index29 alt1"><code class="color1 bold">int</code> <code class="plain">main(</code><code class="keyword bold">void</code><code class="plain">) </code></div>
<div class="line number31 index30 alt2"><code class="plain">{ </code></div>
<div class="line number32 index31 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="color1 bold">int</code> <code class="plain">arr[] = { 2, 3, 4, 10, 40 }; </code></div>
<div class="line number33 index32 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="color1 bold">int</code> <code class="plain">n = </code><code class="keyword bold">sizeof</code><code class="plain">(arr) / </code><code class="keyword bold">sizeof</code><code class="plain">(arr[0]); </code></div>
<div class="line number34 index33 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="color1 bold">int</code> <code class="plain">x = 10; </code></div>
<div class="line number35 index34 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="color1 bold">int</code> <code class="plain">result = binarySearch(arr, 0, n - 1, x); </code></div>
<div class="line number36 index35 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">(result == -1) ? </code><code class="functions bold">printf</code><code class="plain">(</code><code class="string">"Element is not present"</code></div>
<div class="line number37 index36 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="string">" in array"</code><code class="plain">) </code></div>
<div class="line number38 index37 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">: </code><code class="functions bold">printf</code><code class="plain">(</code><code class="string">"Element is present at "</code></div>
<div class="line number39 index38 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="string">"index %d"</code><code class="plain">, </code></div>
<div class="line number40 index39 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">result); </code></div>
<div class="line number41 index40 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">return</code> <code class="plain">0; </code></div>
<div class="line number42 index41 alt1"><code class="plain">} </code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div></div>
<div class="code-editor-container"></div>
<p></p></div>
<div class="code-output-container">
<div class="output-block">
                        <i id="output-icon" title="Output" class="material-icons code-sidebar-button output-icon">chevron_right</i><p></p>
<pre class="output-pre"></pre>
<p></p></div>
<div class="ide-link-div">
                        <i id="copy-url-button" title="Copy Generated Ide URL" class="material-icons code-sidebar-button copy-url-button">filter_none</i><p></p>
<pre id="ide-url"></pre>
<p></p></div>
<p></p></div>

</div><h2 class="tabtitle responsive-tabs__heading" tabindex="0">C++</h2>
<div class="tabcontent responsive-tabs__panel" aria-hidden="true" role="tabpanel" aria-labelledby="tablist2-tab2" id="tablist2-panel2" style="display: none;">

<div class="code-block">
<div class="code-gutter">
<div class="editor-buttons-container">
<div class="editor-buttons">
<div class="editor-buttons-div" title="Run and Edit">
                                    <i id="copy-code-button" title="Copy Code" class="material-icons code-sidebar-button copy-code-button">filter_none</i><p></p>
<div id="run-and-edit-loader" class="ring-load"></div>
<p>                                    <i id="run-and-edit-button" title="Edit Code" lang="cpp" class="material-icons code-sidebar-button">edit</i><br>
                                    <i id="close-code-editor-button" title="Close Editor" class="material-icons code-sidebar-button close-code-editor-button">close</i></p>
<div id="run-code-loader" class="ring-load"></div>
<p>                                    <i id="run-code-button" lang="cpp" title="Run Code and See Output" class="material-icons code-sidebar-button">play_arrow</i></p>
<div id="generate-url-loader" class="ring-load"></div>
<p>                                    <i id="generate-url-and-run-button" title="Run Code and Generate IDE URL" lang="cpp" class="material-icons code-sidebar-button generate-url-and-run-button">link</i><br>
                                    <i title="Dark Mode" class="material-icons code-sidebar-button dark-editor-button">brightness_4</i><br>
                                    <i id="edit-on-ide-button" title="Edit on IDE" lang="cpp" class="material-icons code-sidebar-button edit-on-ide-button">code</i>
                                </p></div>
<p></p></div>
<p></p></div>
<p></p></div>
<div class="code-container">
<div id="highlighter_604660" class="syntaxhighlighter nogutter  ">
<table border="0" cellpadding="0" cellspacing="0">
<tbody>
<tr>
<td class="code">
<div class="container">
<div class="line number1 index0 alt2"><code class="comments">// C++ program to implement recursive Binary Search </code></div>
<div class="line number2 index1 alt1"><code class="preprocessor">#include &lt;iostream&gt; </code></div>
<div class="line number3 index2 alt2"><code class="keyword bold">using</code> <code class="keyword bold">namespace</code> <code class="plain">std; </code></div>
<div class="line number4 index3 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number5 index4 alt2"><code class="comments">// A iterative binary search function. It returns </code></div>
<div class="line number6 index5 alt1"><code class="comments">// location of x in given array arr[l..r] if present, </code></div>
<div class="line number7 index6 alt2"><code class="comments">// otherwise -1 </code></div>
<div class="line number8 index7 alt1"><code class="color1 bold">int</code> <code class="plain">binarySearch(</code><code class="color1 bold">int</code> <code class="plain">arr[], </code><code class="color1 bold">int</code> <code class="plain">l, </code><code class="color1 bold">int</code> <code class="plain">r, </code><code class="color1 bold">int</code> <code class="plain">x) </code></div>
<div class="line number9 index8 alt2"><code class="plain">{ </code></div>
<div class="line number10 index9 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">while</code> <code class="plain">(l &lt;= r) { </code></div>
<div class="line number11 index10 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="color1 bold">int</code> <code class="plain">m = l + (r - l) / 2; </code></div>
<div class="line number12 index11 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number13 index12 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// Check if x is present at mid </code></div>
<div class="line number14 index13 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">if</code> <code class="plain">(arr[m] == x) </code></div>
<div class="line number15 index14 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">return</code> <code class="plain">m; </code></div>
<div class="line number16 index15 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number17 index16 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// If x greater, ignore left half </code></div>
<div class="line number18 index17 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">if</code> <code class="plain">(arr[m] &lt; x) </code></div>
<div class="line number19 index18 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">l = m + 1; </code></div>
<div class="line number20 index19 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number21 index20 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// If x is smaller, ignore right half </code></div>
<div class="line number22 index21 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">else</code></div>
<div class="line number23 index22 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">r = m - 1; </code></div>
<div class="line number24 index23 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">} </code></div>
<div class="line number25 index24 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number26 index25 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// if we reach here, then element was </code></div>
<div class="line number27 index26 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// not present </code></div>
<div class="line number28 index27 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">return</code> <code class="plain">-1; </code></div>
<div class="line number29 index28 alt2"><code class="plain">} </code></div>
<div class="line number30 index29 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number31 index30 alt2"><code class="color1 bold">int</code> <code class="plain">main(</code><code class="keyword bold">void</code><code class="plain">) </code></div>
<div class="line number32 index31 alt1"><code class="plain">{ </code></div>
<div class="line number33 index32 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="color1 bold">int</code> <code class="plain">arr[] = { 2, 3, 4, 10, 40 }; </code></div>
<div class="line number34 index33 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="color1 bold">int</code> <code class="plain">x = 10; </code></div>
<div class="line number35 index34 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="color1 bold">int</code> <code class="plain">n = </code><code class="keyword bold">sizeof</code><code class="plain">(arr) / </code><code class="keyword bold">sizeof</code><code class="plain">(arr[0]); </code></div>
<div class="line number36 index35 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="color1 bold">int</code> <code class="plain">result = binarySearch(arr, 0, n - 1, x); </code></div>
<div class="line number37 index36 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">(result == -1) ? cout &lt;&lt; </code><code class="string">"Element is not present in array"</code></div>
<div class="line number38 index37 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">: cout &lt;&lt; </code><code class="string">"Element is present at index "</code> <code class="plain">&lt;&lt; result; </code></div>
<div class="line number39 index38 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword bold">return</code> <code class="plain">0; </code></div>
<div class="line number40 index39 alt1"><code class="plain">} </code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div></div>
<div class="code-editor-container"></div>
<p></p></div>
<div class="code-output-container">
<div class="output-block">
                        <i id="output-icon" title="Output" class="material-icons code-sidebar-button output-icon">chevron_right</i><p></p>
<pre class="output-pre"></pre>
<p></p></div>
<div class="ide-link-div">
                        <i id="copy-url-button" title="Copy Generated Ide URL" class="material-icons code-sidebar-button copy-url-button">filter_none</i><p></p>
<pre id="ide-url"></pre>
<p></p></div>
<p></p></div>

</div><h2 class="tabtitle responsive-tabs__heading" tabindex="0">Java</h2>
<div class="tabcontent responsive-tabs__panel" aria-hidden="true" role="tabpanel" aria-labelledby="tablist2-tab3" id="tablist2-panel3" style="display: none;">

<div class="code-block">
<div class="code-gutter">
<div class="editor-buttons-container">
<div class="editor-buttons">
<div class="editor-buttons-div" title="Run and Edit">
                                    <i id="copy-code-button" title="Copy Code" class="material-icons code-sidebar-button copy-code-button">filter_none</i><p></p>
<div id="run-and-edit-loader" class="ring-load"></div>
<p>                                    <i id="run-and-edit-button" title="Edit Code" lang="java" class="material-icons code-sidebar-button">edit</i><br>
                                    <i id="close-code-editor-button" title="Close Editor" class="material-icons code-sidebar-button close-code-editor-button">close</i></p>
<div id="run-code-loader" class="ring-load"></div>
<p>                                    <i id="run-code-button" lang="java" title="Run Code and See Output" class="material-icons code-sidebar-button">play_arrow</i></p>
<div id="generate-url-loader" class="ring-load"></div>
<p>                                    <i id="generate-url-and-run-button" title="Run Code and Generate IDE URL" lang="java" class="material-icons code-sidebar-button generate-url-and-run-button">link</i><br>
                                    <i title="Dark Mode" class="material-icons code-sidebar-button dark-editor-button">brightness_4</i><br>
                                    <i id="edit-on-ide-button" title="Edit on IDE" lang="java" class="material-icons code-sidebar-button edit-on-ide-button">code</i>
                                </p></div>
<p></p></div>
<p></p></div>
<p></p></div>
<div class="code-container">
<div id="highlighter_653536" class="syntaxhighlighter nogutter  ">
<table border="0" cellpadding="0" cellspacing="0">
<tbody>
<tr>
<td class="code">
<div class="container">
<div class="line number1 index0 alt2"><code class="comments">// Java implementation of iterative Binary Search </code></div>
<div class="line number2 index1 alt1"><code class="keyword">class</code> <code class="plain">BinarySearch { </code></div>
<div class="line number3 index2 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// Returns index of x if it is present in arr[], </code></div>
<div class="line number4 index3 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// else return -1 </code></div>
<div class="line number5 index4 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">int</code> <code class="plain">binarySearch(</code><code class="keyword">int</code> <code class="plain">arr[], </code><code class="keyword">int</code> <code class="plain">x) </code></div>
<div class="line number6 index5 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">{ </code></div>
<div class="line number7 index6 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">int</code> <code class="plain">l = </code><code class="value">0</code><code class="plain">, r = arr.length - </code><code class="value">1</code><code class="plain">; </code></div>
<div class="line number8 index7 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">while</code> <code class="plain">(l &lt;= r) { </code></div>
<div class="line number9 index8 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">int</code> <code class="plain">m = l + (r - l) / </code><code class="value">2</code><code class="plain">; </code></div>
<div class="line number10 index9 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number11 index10 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// Check if x is present at mid </code></div>
<div class="line number12 index11 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">if</code> <code class="plain">(arr[m] == x) </code></div>
<div class="line number13 index12 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">return</code> <code class="plain">m; </code></div>
<div class="line number14 index13 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number15 index14 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// If x greater, ignore left half </code></div>
<div class="line number16 index15 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">if</code> <code class="plain">(arr[m] &lt; x) </code></div>
<div class="line number17 index16 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">l = m + </code><code class="value">1</code><code class="plain">; </code></div>
<div class="line number18 index17 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number19 index18 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// If x is smaller, ignore right half </code></div>
<div class="line number20 index19 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">else</code></div>
<div class="line number21 index20 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">r = m - </code><code class="value">1</code><code class="plain">; </code></div>
<div class="line number22 index21 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">} </code></div>
<div class="line number23 index22 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number24 index23 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// if we reach here, then element was </code></div>
<div class="line number25 index24 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// not present </code></div>
<div class="line number26 index25 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">return</code> <code class="plain">-</code><code class="value">1</code><code class="plain">; </code></div>
<div class="line number27 index26 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">} </code></div>
<div class="line number28 index27 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number29 index28 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// Driver method to test above </code></div>
<div class="line number30 index29 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">public</code> <code class="keyword">static</code> <code class="keyword">void</code> <code class="plain">main(String args[]) </code></div>
<div class="line number31 index30 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">{ </code></div>
<div class="line number32 index31 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">BinarySearch ob = </code><code class="keyword">new</code> <code class="plain">BinarySearch(); </code></div>
<div class="line number33 index32 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">int</code> <code class="plain">arr[] = { </code><code class="value">2</code><code class="plain">, </code><code class="value">3</code><code class="plain">, </code><code class="value">4</code><code class="plain">, </code><code class="value">10</code><code class="plain">, </code><code class="value">40</code> <code class="plain">}; </code></div>
<div class="line number34 index33 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">int</code> <code class="plain">n = arr.length; </code></div>
<div class="line number35 index34 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">int</code> <code class="plain">x = </code><code class="value">10</code><code class="plain">; </code></div>
<div class="line number36 index35 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">int</code> <code class="plain">result = ob.binarySearch(arr, x); </code></div>
<div class="line number37 index36 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">if</code> <code class="plain">(result == -</code><code class="value">1</code><code class="plain">) </code></div>
<div class="line number38 index37 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">System.out.println(</code><code class="string">"Element not present"</code><code class="plain">); </code></div>
<div class="line number39 index38 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">else</code></div>
<div class="line number40 index39 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">System.out.println(</code><code class="string">"Element found at "</code></div>
<div class="line number41 index40 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">+ </code><code class="string">"index "</code> <code class="plain">+ result); </code></div>
<div class="line number42 index41 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">} </code></div>
<div class="line number43 index42 alt2"><code class="plain">} </code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div></div>
<div class="code-editor-container"></div>
<p></p></div>
<div class="code-output-container">
<div class="output-block">
                        <i id="output-icon" title="Output" class="material-icons code-sidebar-button output-icon">chevron_right</i><p></p>
<pre class="output-pre"></pre>
<p></p></div>
<div class="ide-link-div">
                        <i id="copy-url-button" title="Copy Generated Ide URL" class="material-icons code-sidebar-button copy-url-button">filter_none</i><p></p>
<pre id="ide-url"></pre>
<p></p></div>
<p></p></div>

</div><h2 class="tabtitle responsive-tabs__heading" tabindex="0">Python</h2>
<div class="tabcontent responsive-tabs__panel" aria-hidden="true" role="tabpanel" aria-labelledby="tablist2-tab4" id="tablist2-panel4" style="display: none;">

<div class="code-block">
<div class="code-gutter">
<div class="editor-buttons-container">
<div class="editor-buttons">
<div class="editor-buttons-div" title="Run and Edit">
                                    <i id="copy-code-button" title="Copy Code" class="material-icons code-sidebar-button copy-code-button">filter_none</i><p></p>
<div id="run-and-edit-loader" class="ring-load"></div>
<p>                                    <i id="run-and-edit-button" title="Edit Code" lang="python" class="material-icons code-sidebar-button">edit</i><br>
                                    <i id="close-code-editor-button" title="Close Editor" class="material-icons code-sidebar-button close-code-editor-button">close</i></p>
<div id="run-code-loader" class="ring-load"></div>
<p>                                    <i id="run-code-button" lang="python" title="Run Code and See Output" class="material-icons code-sidebar-button">play_arrow</i></p>
<div id="generate-url-loader" class="ring-load"></div>
<p>                                    <i id="generate-url-and-run-button" title="Run Code and Generate IDE URL" lang="python" class="material-icons code-sidebar-button generate-url-and-run-button">link</i><br>
                                    <i title="Dark Mode" class="material-icons code-sidebar-button dark-editor-button">brightness_4</i><br>
                                    <i id="edit-on-ide-button" title="Edit on IDE" lang="python" class="material-icons code-sidebar-button edit-on-ide-button">code</i>
                                </p></div>
<p></p></div>
<p></p></div>
<p></p></div>
<div class="code-container">
<div id="highlighter_16791" class="syntaxhighlighter nogutter  ">
<table border="0" cellpadding="0" cellspacing="0">
<tbody>
<tr>
<td class="code">
<div class="container">
<div class="line number1 index0 alt2"><code class="comments"># Python code to implement iterative Binary&nbsp; </code></div>
<div class="line number2 index1 alt1"><code class="comments"># Search. </code></div>
<div class="line number3 index2 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number4 index3 alt1"><code class="comments"># It returns location of x in given array arr&nbsp; </code></div>
<div class="line number5 index4 alt2"><code class="comments"># if present, else returns -1 </code></div>
<div class="line number6 index5 alt1"><code class="keyword">def</code> <code class="plain">binarySearch(arr, l, r, x): </code></div>
<div class="line number7 index6 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number8 index7 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">while</code> <code class="plain">l &lt;</code><code class="keyword">=</code> <code class="plain">r: </code></div>
<div class="line number9 index8 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number10 index9 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">mid </code><code class="keyword">=</code> <code class="plain">l </code><code class="keyword">+</code> <code class="plain">(r </code><code class="keyword">-</code> <code class="plain">l)</code><code class="keyword">/</code><code class="value">2</code><code class="plain">; </code></div>
<div class="line number11 index10 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code>&nbsp;</div>
<div class="line number12 index11 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments"># Check if x is present at mid </code></div>
<div class="line number13 index12 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">if</code> <code class="plain">arr[mid] </code><code class="keyword">=</code><code class="keyword">=</code> <code class="plain">x: </code></div>
<div class="line number14 index13 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">return</code> <code class="plain">mid </code></div>
<div class="line number15 index14 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number16 index15 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments"># If x is greater, ignore left half </code></div>
<div class="line number17 index16 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">elif</code> <code class="plain">arr[mid] &lt; x: </code></div>
<div class="line number18 index17 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">l </code><code class="keyword">=</code> <code class="plain">mid </code><code class="keyword">+</code> <code class="value">1</code></div>
<div class="line number19 index18 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number20 index19 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments"># If x is smaller, ignore right half </code></div>
<div class="line number21 index20 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">else</code><code class="plain">: </code></div>
<div class="line number22 index21 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">r </code><code class="keyword">=</code> <code class="plain">mid </code><code class="keyword">-</code> <code class="value">1</code></div>
<div class="line number23 index22 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code>&nbsp;</div>
<div class="line number24 index23 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments"># If we reach here, then the element </code></div>
<div class="line number25 index24 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments"># was not present </code></div>
<div class="line number26 index25 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">return</code> <code class="keyword">-</code><code class="value">1</code></div>
<div class="line number27 index26 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number28 index27 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number29 index28 alt2"><code class="comments"># Test array </code></div>
<div class="line number30 index29 alt1"><code class="plain">arr </code><code class="keyword">=</code> <code class="plain">[ </code><code class="value">2</code><code class="plain">, </code><code class="value">3</code><code class="plain">, </code><code class="value">4</code><code class="plain">, </code><code class="value">10</code><code class="plain">, </code><code class="value">40</code> <code class="plain">] </code></div>
<div class="line number31 index30 alt2"><code class="plain">x </code><code class="keyword">=</code> <code class="value">10</code></div>
<div class="line number32 index31 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number33 index32 alt2"><code class="comments"># Function call </code></div>
<div class="line number34 index33 alt1"><code class="plain">result </code><code class="keyword">=</code> <code class="plain">binarySearch(arr, </code><code class="value">0</code><code class="plain">, </code><code class="functions">len</code><code class="plain">(arr)</code><code class="keyword">-</code><code class="value">1</code><code class="plain">, x) </code></div>
<div class="line number35 index34 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number36 index35 alt1"><code class="keyword">if</code> <code class="plain">result !</code><code class="keyword">=</code> <code class="keyword">-</code><code class="value">1</code><code class="plain">: </code></div>
<div class="line number37 index36 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">print</code> <code class="string">"Element is present at index % d"</code> <code class="keyword">%</code> <code class="plain">result </code></div>
<div class="line number38 index37 alt1"><code class="keyword">else</code><code class="plain">: </code></div>
<div class="line number39 index38 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="functions">print</code> <code class="string">"Element is not present in array"</code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div></div>
<div class="code-editor-container"></div>
<p></p></div>
<div class="code-output-container">
<div class="output-block">
                        <i id="output-icon" title="Output" class="material-icons code-sidebar-button output-icon">chevron_right</i><p></p>
<pre class="output-pre"></pre>
<p></p></div>
<div class="ide-link-div">
                        <i id="copy-url-button" title="Copy Generated Ide URL" class="material-icons code-sidebar-button copy-url-button">filter_none</i><p></p>
<pre id="ide-url"></pre>
<p></p></div>
<p></p></div>

</div><h2 class="tabtitle responsive-tabs__heading" tabindex="0">C#</h2>
<div class="tabcontent responsive-tabs__panel" aria-hidden="true" role="tabpanel" aria-labelledby="tablist2-tab5" id="tablist2-panel5" style="display: none;">

<div class="code-block">
<div class="code-gutter">
<div class="editor-buttons-container">
<div class="editor-buttons">
<div class="editor-buttons-div" title="Run and Edit">
                                    <i id="copy-code-button" title="Copy Code" class="material-icons code-sidebar-button copy-code-button">filter_none</i><p></p>
<div id="run-and-edit-loader" class="ring-load"></div>
<p>                                    <i id="run-and-edit-button" title="Edit Code" lang="csharp" class="material-icons code-sidebar-button">edit</i><br>
                                    <i id="close-code-editor-button" title="Close Editor" class="material-icons code-sidebar-button close-code-editor-button">close</i></p>
<div id="run-code-loader" class="ring-load"></div>
<p>                                    <i id="run-code-button" lang="csharp" title="Run Code and See Output" class="material-icons code-sidebar-button">play_arrow</i></p>
<div id="generate-url-loader" class="ring-load"></div>
<p>                                    <i id="generate-url-and-run-button" title="Run Code and Generate IDE URL" lang="csharp" class="material-icons code-sidebar-button generate-url-and-run-button">link</i><br>
                                    <i title="Dark Mode" class="material-icons code-sidebar-button dark-editor-button">brightness_4</i><br>
                                    <i id="edit-on-ide-button" title="Edit on IDE" lang="csharp" class="material-icons code-sidebar-button edit-on-ide-button">code</i>
                                </p></div>
<p></p></div>
<p></p></div>
<p></p></div>
<div class="code-container">
<div id="highlighter_690716" class="syntaxhighlighter nogutter  ">
<table border="0" cellpadding="0" cellspacing="0">
<tbody>
<tr>
<td class="code">
<div class="container">
<div class="line number1 index0 alt2"><code class="comments">// C# implementation of iterative Binary Search </code></div>
<div class="line number2 index1 alt1"><code class="keyword">using</code> <code class="plain">System; </code></div>
<div class="line number3 index2 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number4 index3 alt1"><code class="keyword">class</code> <code class="plain">GFG { </code></div>
<div class="line number5 index4 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// Returns index of x if it is present in arr[], </code></div>
<div class="line number6 index5 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// else return -1 </code></div>
<div class="line number7 index6 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">static</code> <code class="keyword">int</code> <code class="plain">binarySearch(</code><code class="keyword">int</code><code class="plain">[] arr, </code><code class="keyword">int</code> <code class="plain">x) </code></div>
<div class="line number8 index7 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">{ </code></div>
<div class="line number9 index8 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">int</code> <code class="plain">l = 0, r = arr.Length - 1; </code></div>
<div class="line number10 index9 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">while</code> <code class="plain">(l &lt;= r) { </code></div>
<div class="line number11 index10 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">int</code> <code class="plain">m = l + (r - l) / 2; </code></div>
<div class="line number12 index11 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number13 index12 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// Check if x is present at mid </code></div>
<div class="line number14 index13 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">if</code> <code class="plain">(arr[m] == x) </code></div>
<div class="line number15 index14 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">return</code> <code class="plain">m; </code></div>
<div class="line number16 index15 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number17 index16 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// If x greater, ignore left half </code></div>
<div class="line number18 index17 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">if</code> <code class="plain">(arr[m] &lt; x) </code></div>
<div class="line number19 index18 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">l = m + 1; </code></div>
<div class="line number20 index19 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number21 index20 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// If x is smaller, ignore right half </code></div>
<div class="line number22 index21 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">else</code></div>
<div class="line number23 index22 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">r = m - 1; </code></div>
<div class="line number24 index23 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">} </code></div>
<div class="line number25 index24 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number26 index25 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// if we reach here, then element was </code></div>
<div class="line number27 index26 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// not present </code></div>
<div class="line number28 index27 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">return</code> <code class="plain">-1; </code></div>
<div class="line number29 index28 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">} </code></div>
<div class="line number30 index29 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number31 index30 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// Driver method to test above </code></div>
<div class="line number32 index31 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">public</code> <code class="keyword">static</code> <code class="keyword">void</code> <code class="plain">Main() </code></div>
<div class="line number33 index32 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">{ </code></div>
<div class="line number34 index33 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">int</code><code class="plain">[] arr = { 2, 3, 4, 10, 40 }; </code></div>
<div class="line number35 index34 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">int</code> <code class="plain">n = arr.Length; </code></div>
<div class="line number36 index35 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">int</code> <code class="plain">x = 10; </code></div>
<div class="line number37 index36 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">int</code> <code class="plain">result = binarySearch(arr, x); </code></div>
<div class="line number38 index37 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">if</code> <code class="plain">(result == -1) </code></div>
<div class="line number39 index38 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">Console.WriteLine(</code><code class="string">"Element not present"</code><code class="plain">); </code></div>
<div class="line number40 index39 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">else</code></div>
<div class="line number41 index40 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">Console.WriteLine(</code><code class="string">"Element found at "</code></div>
<div class="line number42 index41 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">+ </code><code class="string">"index "</code> <code class="plain">+ result); </code></div>
<div class="line number43 index42 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">} </code></div>
<div class="line number44 index43 alt1"><code class="plain">} </code></div>
<div class="line number45 index44 alt2"><code class="comments">// This code is contributed by Sam007 </code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div></div>
<div class="code-editor-container"></div>
<p></p></div>
<div class="code-output-container">
<div class="output-block">
                        <i id="output-icon" title="Output" class="material-icons code-sidebar-button output-icon">chevron_right</i><p></p>
<pre class="output-pre"></pre>
<p></p></div>
<div class="ide-link-div">
                        <i id="copy-url-button" title="Copy Generated Ide URL" class="material-icons code-sidebar-button copy-url-button">filter_none</i><p></p>
<pre id="ide-url"></pre>
<p></p></div>
<p></p></div>

</div><h2 class="tabtitle responsive-tabs__heading" tabindex="0">PHP</h2>
<div class="tabcontent responsive-tabs__panel" aria-hidden="true" role="tabpanel" aria-labelledby="tablist2-tab6" id="tablist2-panel6" style="display: none;">

<div class="code-block">
<div class="code-gutter">
<div class="editor-buttons-container">
<div class="editor-buttons">
<div class="editor-buttons-div" title="Run and Edit">
                                    <i id="copy-code-button" title="Copy Code" class="material-icons code-sidebar-button copy-code-button">filter_none</i><p></p>
<div id="run-and-edit-loader" class="ring-load"></div>
<p>                                    <i id="run-and-edit-button" title="Edit Code" lang="php" class="material-icons code-sidebar-button">edit</i><br>
                                    <i id="close-code-editor-button" title="Close Editor" class="material-icons code-sidebar-button close-code-editor-button">close</i></p>
<div id="run-code-loader" class="ring-load"></div>
<p>                                    <i id="run-code-button" lang="php" title="Run Code and See Output" class="material-icons code-sidebar-button">play_arrow</i></p>
<div id="generate-url-loader" class="ring-load"></div>
<p>                                    <i id="generate-url-and-run-button" title="Run Code and Generate IDE URL" lang="php" class="material-icons code-sidebar-button generate-url-and-run-button">link</i><br>
                                    <i title="Dark Mode" class="material-icons code-sidebar-button dark-editor-button">brightness_4</i><br>
                                    <i id="edit-on-ide-button" title="Edit on IDE" lang="php" class="material-icons code-sidebar-button edit-on-ide-button">code</i>
                                </p></div>
<p></p></div>
<p></p></div>
<p></p></div>
<div class="code-container">
<div id="highlighter_805738" class="syntaxhighlighter nogutter  ">
<table border="0" cellpadding="0" cellspacing="0">
<tbody>
<tr>
<td class="code">
<div class="container">
<div class="line number1 index0 alt2"><code class="plain">&lt;?php </code></div>
<div class="line number2 index1 alt1"><code class="comments">// PHP program to implement </code></div>
<div class="line number3 index2 alt2"><code class="comments">// iterative Binary Search </code></div>
<div class="line number4 index3 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number5 index4 alt2"><code class="comments">// A iterative binary search&nbsp; </code></div>
<div class="line number6 index5 alt1"><code class="comments">// function. It returns location&nbsp; </code></div>
<div class="line number7 index6 alt2"><code class="comments">// of x in given array arr[l..r]&nbsp; </code></div>
<div class="line number8 index7 alt1"><code class="comments">// if present, otherwise -1 </code></div>
<div class="line number9 index8 alt2"><code class="keyword">function</code> <code class="plain">binarySearch(</code><code class="variable">$arr</code><code class="plain">, </code><code class="variable">$l</code><code class="plain">,&nbsp; </code></div>
<div class="line number10 index9 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="variable">$r</code><code class="plain">, </code><code class="variable">$x</code><code class="plain">) </code></div>
<div class="line number11 index10 alt2"><code class="plain">{ </code></div>
<div class="line number12 index11 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">while</code> <code class="plain">(</code><code class="variable">$l</code> <code class="plain">&lt;= </code><code class="variable">$r</code><code class="plain">) </code></div>
<div class="line number13 index12 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">{ </code></div>
<div class="line number14 index13 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="variable">$m</code> <code class="plain">= </code><code class="variable">$l</code> <code class="plain">+ (</code><code class="variable">$r</code> <code class="plain">- </code><code class="variable">$l</code><code class="plain">) / 2; </code></div>
<div class="line number15 index14 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number16 index15 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// Check if x is present at mid </code></div>
<div class="line number17 index16 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">if</code> <code class="plain">(</code><code class="variable">$arr</code><code class="plain">[</code><code class="variable">$m</code><code class="plain">] == </code><code class="variable">$x</code><code class="plain">) </code></div>
<div class="line number18 index17 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">return</code> <code class="functions">floor</code><code class="plain">(</code><code class="variable">$m</code><code class="plain">); </code></div>
<div class="line number19 index18 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number20 index19 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// If x greater, ignore </code></div>
<div class="line number21 index20 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// left half </code></div>
<div class="line number22 index21 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">if</code> <code class="plain">(</code><code class="variable">$arr</code><code class="plain">[</code><code class="variable">$m</code><code class="plain">] &lt; </code><code class="variable">$x</code><code class="plain">) </code></div>
<div class="line number23 index22 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="variable">$l</code> <code class="plain">= </code><code class="variable">$m</code> <code class="plain">+ 1; </code></div>
<div class="line number24 index23 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number25 index24 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// If x is smaller,&nbsp; </code></div>
<div class="line number26 index25 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// ignore right half </code></div>
<div class="line number27 index26 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">else</code></div>
<div class="line number28 index27 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="variable">$r</code> <code class="plain">= </code><code class="variable">$m</code> <code class="plain">- 1; </code></div>
<div class="line number29 index28 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="plain">} </code></div>
<div class="line number30 index29 alt1"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number31 index30 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// if we reach here, then&nbsp; </code></div>
<div class="line number32 index31 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="comments">// element was not present </code></div>
<div class="line number33 index32 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="keyword">return</code> <code class="plain">-1; </code></div>
<div class="line number34 index33 alt1"><code class="plain">} </code></div>
<div class="line number35 index34 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number36 index35 alt1"><code class="comments">// Driver Code </code></div>
<div class="line number37 index36 alt2"><code class="variable">$arr</code> <code class="plain">= </code><code class="keyword">array</code><code class="plain">(2, 3, 4, 10, 40); </code></div>
<div class="line number38 index37 alt1"><code class="variable">$n</code> <code class="plain">= </code><code class="functions">count</code><code class="plain">(</code><code class="variable">$arr</code><code class="plain">); </code></div>
<div class="line number39 index38 alt2"><code class="variable">$x</code> <code class="plain">= 10; </code></div>
<div class="line number40 index39 alt1"><code class="variable">$result</code> <code class="plain">= binarySearch(</code><code class="variable">$arr</code><code class="plain">, 0,&nbsp; </code></div>
<div class="line number41 index40 alt2"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="variable">$n</code> <code class="plain">- 1, </code><code class="variable">$x</code><code class="plain">); </code></div>
<div class="line number42 index41 alt1"><code class="keyword">if</code><code class="plain">((</code><code class="variable">$result</code> <code class="plain">== -1)) </code></div>
<div class="line number43 index42 alt2"><code class="functions">echo</code> <code class="string">"Element is not present in array"</code><code class="plain">; </code></div>
<div class="line number44 index43 alt1"><code class="keyword">else</code></div>
<div class="line number45 index44 alt2"><code class="functions">echo</code> <code class="string">"Element is present at index "</code><code class="plain">,&nbsp; </code></div>
<div class="line number46 index45 alt1"><code class="undefined spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="variable">$result</code><code class="plain">; </code></div>
<div class="line number47 index46 alt2"><code class="undefined spaces">&nbsp;</code>&nbsp;</div>
<div class="line number48 index47 alt1"><code class="comments">// This code is contributed by anuj_67. </code></div>
<div class="line number49 index48 alt2"><code class="plain">?&gt; </code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div></div>
<div class="code-editor-container"></div>
<p></p></div>
<div class="code-output-container">
<div class="output-block">
                        <i id="output-icon" title="Output" class="material-icons code-sidebar-button output-icon">chevron_right</i><p></p>
<pre class="output-pre"></pre>
<p></p></div>
<div class="ide-link-div">
                        <i id="copy-url-button" title="Copy Generated Ide URL" class="material-icons code-sidebar-button copy-url-button">filter_none</i><p></p>
<pre id="ide-url"></pre>
<p></p></div>
<p></p></div>
<p></p></div></div></div><br>
<strong>Output :</strong> <p></p>
<pre>Element is present at index 3</pre>
<p><strong>Time Complexity:</strong><br>
The time complexity of Binary Search can be written as  </p>
<pre>T(n) = T(n/2) + c </pre>
<p>The above recurrence can be solved either using Recurrence T ree method or Master method. It falls in case II of Master Method and solution of the recurrence is <img src="./Binary_files/quicklatex.com-14363a4f3a0fbdc0f692244e9705ad37_l3.svg" class="ql-img-inline-formula quicklatex-auto-format" alt="Theta(Logn)" title="Rendered by QuickLaTeX.com" height="27" width="148" style="vertical-align: -7px;">.</p>
<p><strong>Auxiliary Space:</strong> O(1) in case of iterative implementation. In case of recursive implementation, O(Logn) recursion call stack space.</p>
<p><strong>Algorithmic Paradigm:</strong> <a href="https://www.geeksforgeeks.org/decrease-and-conquer/"> Decrease and Conquer</a>.</p>
<p><iframe width="665" height="374" src="./Binary_files/T2sFYY-fT5o.html" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></p>
<div class="hideInCourse">
<strong>Interesting articles based on Binary Search.</strong><p></p>
<ul>
<li><a href="https://www.geeksforgeeks.org/the-ubiquitous-binary-search-set-1/" target="_blank">The Ubiquitous Binary Search</a></li>
<li><a href="https://www.geeksforgeeks.org/g-fact-84/" target="_blank">Interpolation search vs Binary search</a></li>
<li>
<a href="https://www.geeksforgeeks.org/find-minimum-element-in-a-sorted-and-rotated-array/" target="_blank">Find the minimum element in a sorted and rotated array</a></li>
<li>
<a href="https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/" target="_blank">Find a peak element</a></li>
<li>
<a href="https://www.geeksforgeeks.org/find-a-fixed-point-in-a-given-array/" target="_blank">Find a Fixed Point in a given array</a></li>
<li>
<a href="https://www.geeksforgeeks.org/count-number-of-occurrences-in-a-sorted-array/">Count the number of occurrences in a sorted array</a></li>
<li>
<a href="https://www.geeksforgeeks.org/median-of-two-sorted-arrays/" target="_blank">Median of two sorted arrays</a></li>
<li>
<a href="https://www.geeksforgeeks.org/search-floor-and-ceil-in-a-sorted-array/">Floor and Ceiling in a sorted array</a></li>
<li>
<a href="https://www.geeksforgeeks.org/find-the-maximum-element-in-an-array-which-is-first-increasing-and-then-decreasing/" target="_blank">Find the maximum element in an array which is first increasing and then decreasing</a></li>
</ul>
<p><strong><a href="https://practice.geeksforgeeks.org/tag-page.php?tag=binary+search&amp;isCmp=0">Coding Practice Questions on Binary Search</a></strong><br>
<a href="https://www.geeksforgeeks.org/tag/binary-search/">Recent Articles on Binary Search.</a></p>
<p>&nbsp;</p>
<p>
Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above.
</p>
</div>
<br><script async="" src="./Binary_files/f(10).txt"></script>
          <!-- post_bottom_responsive -->
          <ins class="adsbygoogle" style="display: block; height: 75px;" data-ad-client="ca-pub-9465609616171866" data-ad-slot="8385097921" data-ad-format="auto" data-adsbygoogle-status="done"><ins id="aswift_3_expand" style="display: inline-table; border: none; height: 75px; margin: 0px; padding: 0px; position: relative; visibility: visible; width: 641px; background-color: transparent;"><ins id="aswift_3_anchor" style="display: block; border: none; height: 75px; margin: 0px; padding: 0px; position: relative; visibility: visible; width: 641px; background-color: transparent; overflow: hidden;"><iframe width="641" height="75" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" onload="var i=this.id,s=window.google_iframe_oncopy,H=s&amp;&amp;s.handlers,h=H&amp;&amp;H[i],w=this.contentWindow,d;try{d=w.document}catch(e){}if(h&amp;&amp;d&amp;&amp;(!d.body||!d.body.firstChild)){if(h.call){setTimeout(h,0)}else if(h.match){try{h=s.upd(h,i)}catch(e){}w.location.replace(h)}}" id="aswift_3" name="aswift_3" style="left: 0px; position: absolute; top: 0px; border: 0px; width: 641px; height: 75px;" src="./Binary_files/saved_resource(10).html"></iframe></ins></ins></ins>
          <script>
          (adsbygoogle = window.adsbygoogle || []).push({});
        </script>
          <br>
            <div id="personalNoteDiv" class="clear hideIt">
    <div class="personalNoteHeader clear">
        <span class="noteHeaderText">My Personal Notes</span>
        <span class="hideNotesDivIcon"><i class="material-icons personalNotesIcon">arrow_drop_up</i></span>
    </div>
    <div class="collapsableDivPersonalNotes">
        <textarea maxlength="5000" id="enteredPersonalNote" class="personalNoteStyle" placeholder="Add your personal notes here! (max 5000 chars)"></textarea>
        <div class="saveNoteDiv">
            <span class="processSaveNote"></span>
            <button class="savePersonalNoteButton" onclick="saveUserPersonalNote()">Save</button>
        </div>
    </div>
</div><div class="recommendedPostsDiv"><h2 style="font-size:20px; color: #838383">Recommended Posts:</h2><ul><li><a href="https://www.geeksforgeeks.org/meta-binary-search-one-sided-binary-search/">Meta Binary Search | One-Sided Binary Search</a></li><li><a href="https://www.geeksforgeeks.org/binary-search-preferred-ternary-search/">Why is Binary Search preferred over Ternary Search?</a></li><li><a href="https://www.geeksforgeeks.org/linear-search-vs-binary-search/">Linear Search vs Binary Search</a></li><li><a href="https://www.geeksforgeeks.org/g-fact-84/">Interpolation search vs Binary search</a></li><li><a href="https://www.geeksforgeeks.org/binary-search-php/">Binary Search in PHP</a></li><li><a href="https://www.geeksforgeeks.org/the-ubiquitous-binary-search-set-1/">The Ubiquitous Binary Search | Set 1</a></li><li><a href="https://www.geeksforgeeks.org/binary-search-using-pthread/">Binary Search using pthread</a></li><li><a href="https://www.geeksforgeeks.org/binary-search-a-string/">Binary Search a String</a></li><li><a href="https://www.geeksforgeeks.org/binary-search-in-javascript/">Binary Search In JavaScript</a></li><li><a href="https://www.geeksforgeeks.org/variants-of-binary-search/">Variants of Binary Search</a></li><li><a href="https://www.geeksforgeeks.org/binary-search-in-java/">Binary Search in Java</a></li><li><a href="https://www.geeksforgeeks.org/floor-in-binary-search-tree-bst/">Floor in Binary Search Tree (BST)</a></li><li><a href="https://www.geeksforgeeks.org/problem-binary-search-implementations/">A Problem in Many Binary Search Implementations</a></li><li><a href="https://www.geeksforgeeks.org/randomized-binary-search-algorithm/">Randomized Binary Search Algorithm</a></li><li><a href="https://www.geeksforgeeks.org/binary-search-bisect-in-python/">Binary Search (bisect) in Python</a></li></ul></div><div id="improvedBy"><br><b>Improved By : </b> <a href="https://auth.geeksforgeeks.org/user/vt_m/">vt_m</a>, <a href="https://auth.geeksforgeeks.org/user/RishabhPrabhu/">RishabhPrabhu</a></div><br><script>jQuery('#showMoreImprove').click(function(){ jQuery(this).hide(); jQuery('#improvedByMore').css('display', 'inline'); });</script><script async="" src="./Binary_files/f(10).txt"></script>
      <!-- post_bottom_responsive -->
      <ins class="adsbygoogle" style="display: block; height: 75px;" data-ad-client="ca-pub-9465609616171866" data-ad-slot="8385097921" data-ad-format="auto" data-adsbygoogle-status="done"><ins id="aswift_4_expand" style="display: inline-table; border: none; height: 75px; margin: 0px; padding: 0px; position: relative; visibility: visible; width: 641px; background-color: transparent;"><ins id="aswift_4_anchor" style="display: block; border: none; height: 75px; margin: 0px; padding: 0px; position: relative; visibility: visible; width: 641px; background-color: transparent; overflow: hidden;"><iframe width="641" height="75" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" onload="var i=this.id,s=window.google_iframe_oncopy,H=s&amp;&amp;s.handlers,h=H&amp;&amp;H[i],w=this.contentWindow,d;try{d=w.document}catch(e){}if(h&amp;&amp;d&amp;&amp;(!d.body||!d.body.firstChild)){if(h.call){setTimeout(h,0)}else if(h.match){try{h=s.upd(h,i)}catch(e){}w.location.replace(h)}}" id="aswift_4" name="aswift_4" style="left: 0px; position: absolute; top: 0px; border: 0px; width: 641px; height: 75px;" src="./Binary_files/saved_resource(11).html"></iframe></ins></ins></ins>
      <script>
      (adsbygoogle = window.adsbygoogle || []).push({});
    </script>
      <br>
      <br>
      
					
		<footer class="entry-meta">
    <span><b>Article Tags : </b><div class="practiceButton"><a href="https://www.geeksforgeeks.org/category/algorithm/divide-and-conquer/" rel="category tag">Divide and Conquer</a></div><div class="practiceButton"><a href="https://www.geeksforgeeks.org/category/algorithm/searching/" rel="category tag">Searching</a></div></span><span><div class="practiceButton"><a href="https://www.geeksforgeeks.org/tag/accenture/" rel="tag">Accenture</a></div><div class="practiceButton"><a href="https://www.geeksforgeeks.org/tag/binary-search/" rel="tag">Binary Search</a></div><div class="practiceButton"><a href="https://www.geeksforgeeks.org/tag/infosys/" rel="tag">Infosys</a></div><div class="practiceButton"><a href="https://www.geeksforgeeks.org/tag/oracle/" rel="tag">Oracle</a></div><div class="practiceButton"><a href="https://www.geeksforgeeks.org/tag/qualcomm/" rel="tag">Qualcomm</a></div><div class="practiceButton"><a href="https://www.geeksforgeeks.org/tag/tcs/" rel="tag">TCS</a></div><div class="practiceButton"><a href="https://www.geeksforgeeks.org/tag/wipro/" rel="tag">Wipro</a></div></span>
           	<div class="no-p-tag" style="text-align:left;"><b style="color: #757575;">Practice Tags : </b> <div class="practiceButton"><a href="https://practice.geeksforgeeks.org/company/Infosys">Infosys</a></div><div class="practiceButton"><a href="https://practice.geeksforgeeks.org/company/Oracle">Oracle</a></div><div class="practiceButton"><a href="https://practice.geeksforgeeks.org/company/Qualcomm">Qualcomm</a></div><div class="practiceButton"><a href="https://practice.geeksforgeeks.org/company/TCS">TCS</a></div><div class="practiceButton"><a href="https://practice.geeksforgeeks.org/company/Wipro">Wipro</a></div><div class="practiceButton"><a href="https://practice.geeksforgeeks.org/company/Accenture">Accenture</a></div><div class="practiceButton"><a href="https://practice.geeksforgeeks.org/topics/Searching">Searching</a></div><div class="practiceButton"><a href="https://practice.geeksforgeeks.org/topics/Divide%20and%20Conquer">Divide and Conquer</a></div><div class="practiceButton"><a href="https://practice.geeksforgeeks.org/topics/Binary%20Search">Binary Search</a></div></div><br><div id="improveArticle" style="float: right;cursor: pointer;"></div>        <div class="plugins upvoteArticle">
         <div>
         <i class="material-icons upvoteIcon login-modal-btn" title="Upvote">thumb_up</i><br> 
                <span class="upvoteText">15</span></div>
                <div class="plugins" style="text-align:right;">
        <div pid="142311" ptitle="Binary Search" id="markPlugin">
            <div class="lists">
            <input id="todo" type="checkbox" class="mark">
            <label class="checkbox" for="todo">To-do</label>
            <input id="done" type="checkbox" class="mark">
            <label class="checkbox" for="done">Done</label>
            </div></div>
    <div class="difficultyRating" pid="142311" ptitle="Binary Search" id="ratePlugin">
            <div class="techno dropdown">
            <span id="rating_box" class="avg-rating level-1">1.6</span>
            <br>
            <br>
             
                 <span id="vote_count">Based on <b>190</b> vote(s)</span>
                    <div class="markRating dropdown-content">
            <input rating="1" type="button" class="box basic login-modal-btn" value="Basic">
            <input rating="2" type="button" class="box easy login-modal-btn" value="Easy">
            <input rating="3" type="button" class="box medium login-modal-btn" value="Medium">
            <input rating="4" type="button" class="box hard login-modal-btn" value="Hard">
            <input rating="5" type="button" class="box expert login-modal-btn" value="Expert">
        </div>
        <span class="process"></span>
        </div></div>
        </div>
        <div class="plugins userActionButtons">
        <div pid="142311" ptitle="Binary Search" id="feedbackButtonDiv" style="display:inline-block"><button class="feedbackButton login-modal-btn">Feedback</button><button class="feedbackButton login-modal-btn">Add Notes</button><button class="feedbackButton login-modal-btn">Improve Article</button></div>
        <div pid="142311" ptitle="Binary Search" id="addNoteButtonDiv" style="display:inline-block"></div>
        <div pid="142311" ptitle="Binary Search" id="improveArticleButtonDiv" style="display:inline-block"></div>
        </div>
<div class="common-bottom">Please write to us at contribute@geeksforgeeks.org to report any issue with the above content.</div>          	
					</div></footer><!-- .entry-meta -->
	</div></article><!-- #post -->




<!-- Added on 29 Oct 2015 for next and previous from same category -->

<nav class="nav-single">

 <div class="assistive-text">Post navigation</div>
    <span class="nav-previous"><div class="col-md-12 prev">Previous</div> <i class="material-icons">first_page</i> <a href="https://www.geeksforgeeks.org/quick-sort/" rel="prev"> QuickSort</a></span>
 
    <span class="nav-next"><div class="col-md-12 next">Next</div> <i class="material-icons">last_page</i> <a href="https://www.geeksforgeeks.org/strassens-matrix-multiplication/" rel="next">Divide and Conquer | Set 5 (Strassen’s Matrix Multiplication) </a> </span>

				</nav><!-- .nav-single -->
<!--
<script type="text/javascript">
	
				arrPost.push('');
	
		   <?php// } ?>

</script>
-->



<div id="author" name="Sandeep Jain"></div>
<br><br>

<style type="text/css">
 
#share-buttons img {
width: 35px;
padding: 5px;
border: 0;
box-shadow: 0;
display: inline;
}
#share-buttons a:hover {
	text-decoration: none;
}
</style>


<div id="share-buttons" style="display:none">
   
    <!-- Facebook -->
    <a href="http://www.facebook.com/sharer.php?u=https://www.geeksforgeeks.org/binary-search/" target="_blank" title="Share on Facebook">
        <img src="./Binary_files/facebook.png" alt="Facebook">
    </a>
    
    <!-- Google+ -->
    <a href="https://plus.google.com/share?url=https://www.geeksforgeeks.org/binary-search/" target="_blank" title="Share on Google">
        <img src="./Binary_files/google.png" alt="Google">
    </a>
    
    <!-- LinkedIn -->
    <a href="http://www.linkedin.com/shareArticle?mini=true&amp;url=https://www.geeksforgeeks.org/binary-search/" target="_blank" title="Share on LinkedIn">
        <img src="./Binary_files/linkedin.png" alt="LinkedIn">
    </a>
    
    <!-- Twitter -->
    <a href="https://twitter.com/share?url=https://www.geeksforgeeks.org/binary-search/&amp;text=Binary%20Search&amp;hashtags=GeeksforGeeks" target="_blank" title="Share on Twitter">
        <img src="./Binary_files/twitter.png" alt="Twitter">
    </a>

    <!-- Pinterest -->
    <a href="javascript:void((function()%7Bvar%20e=document.createElement(&#39;script&#39;);e.setAttribute(&#39;type&#39;,&#39;text/javascript&#39;);e.setAttribute(&#39;charset&#39;,&#39;UTF-8&#39;);e.setAttribute(&#39;src&#39;,&#39;http://assets.pinterest.com/js/pinmarklet.js?r=&#39;+Math.random()*99999999);document.body.appendChild(e)%7D)());" title="Share on Pinterest">
        <img src="./Binary_files/pinterest.png" alt="Pinterest">
    </a>
    
    <!-- Reddit -->
    <a href="http://reddit.com/submit?url=https://www.geeksforgeeks.org/binary-search/&amp;title=Binary%20Search" target="_blank" title="Share on Reddit">
        <img src="./Binary_files/reddit.png" alt="Reddit">
    </a>
    
    <!-- StumbleUpon-->
    <a href="http://www.stumbleupon.com/submit?url=https://www.geeksforgeeks.org/binary-search/&amp;title=Binary%20Search" target="_blank" title="Share on StumbleUpon">
        <img src="./Binary_files/stumbleupon.png" alt="StumbleUpon">
    </a>
    
    <!-- Tumblr-->
    <a href="http://www.tumblr.com/share/link?url=https://www.geeksforgeeks.org/binary-search/&amp;title=Binary%20Search" target="_blank" title="Share on Tumblr">
        <img src="./Binary_files/tumblr.png" alt="Tumblr">
    </a>
   
</div>

<br><br>
<div id="ide_link">
<p>Writing code in comment? Please use <a href="https://ide.geeksforgeeks.org/">ide.geeksforgeeks.org</a>, generate link and share the link here.</p>
</div>
<br>
<div style="display:flex">
<button id="comment" class="action-button" style="width:45%;cursor: pointer;margin-right:10%;box-shadow: 0 2px 5px 0 rgba(0,0,0,0.4), 0 6px 20px 0 rgba(0,0,0,0);border-color: #4cb96b;border-radius: 4px;">Load Comments</button>
<button id="share" class="action-button" onclick="document.getElementById(&#39;share-buttons&#39;).style.display=&#39;block&#39;;this.style.display=&#39;none&#39;;" style="width:45%;cursor: pointer;margin-right:10%;box-shadow: 0 2px 5px 0 rgba(0,0,0,0.4), 0 6px 20px 0 rgba(0,0,0,0);border-color: #4cb96b;border-radius: 4px;">Share this post!</button>

</div>

<div id="disqus_thread"></div>

					</div><!-- #content -->
	</div><!-- #primary -->


			<div id="secondary" class="widget-area" role="complementary">
			<aside id="text-11" class="widget widget_text">			<div class="textwidget"><p><script async="" src="./Binary_files/f(10).txt"></script><ins class="adsbygoogle" style="display:inline-block;width:300px;height:600px" data-ad-client="ca-pub-9465609616171866" data-ad-slot="4402736037" data-adsbygoogle-status="done"><ins id="aswift_5_expand" style="display:inline-table;border:none;height:600px;margin:0;padding:0;position:relative;visibility:visible;width:300px;background-color:transparent;"><ins id="aswift_5_anchor" style="display:block;border:none;height:600px;margin:0;padding:0;position:relative;visibility:visible;width:300px;background-color:transparent;"><iframe width="300" height="600" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" onload="var i=this.id,s=window.google_iframe_oncopy,H=s&amp;&amp;s.handlers,h=H&amp;&amp;H[i],w=this.contentWindow,d;try{d=w.document}catch(e){}if(h&amp;&amp;d&amp;&amp;(!d.body||!d.body.firstChild)){if(h.call){setTimeout(h,0)}else if(h.match){try{h=s.upd(h,i)}catch(e){}w.location.replace(h)}}" id="aswift_5" name="aswift_5" style="left:0;position:absolute;top:0;border:0px;width:300px;height:600px;" src="./Binary_files/saved_resource(12).html"></iframe></ins></ins></ins><br>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script></p>
</div>
		</aside>                    <div class="rightSideBarParent">
                    <div class="leftSideBar rightSideBar">
                    <div class="rightbar_lefthead"> </div>
                    <div class="rightbar_head">Most popular articles</div>
                    <div class="rightbar_righthead"> </div>
                    <ul class="leftBarList">
                        <li><a href="https://www.geeksforgeeks.org/amazon-interview-experience-sde-ll/" target="_blank">Amazon Interview Experience SDE ll</a></li><li><a href="https://www.geeksforgeeks.org/must-do-coding-questions-for-companies-like-amazon-microsoft-adobe/" target="_blank">Must Do Coding Questions for Companies like Amazon, Microsoft, Adobe, ...</a></li><li><a href="https://www.geeksforgeeks.org/must-coding-questions-company-wise/" target="_blank">Must Do Coding Questions Company-wise</a></li><li><a href="https://www.geeksforgeeks.org/practice-for-cracking-any-coding-interview/" target="_blank">Practice for cracking any coding interview</a></li><li><a href="https://www.geeksforgeeks.org/sorting-a-vector-in-c/" target="_blank">Sorting a vector in C++</a></li>                    </ul>  
                    </div>
                    </div><br>
                    <aside id="text-4" class="widget widget_text">			<div class="textwidget"><script async="" src="./Binary_files/f(10).txt"></script>
<!-- ResponsiveRightBarMay16 -->
<ins class="adsbygoogle" style="display: block; height: 281px;" data-ad-client="ca-pub-9465609616171866" data-ad-slot="7089558833" data-ad-format="auto" data-adsbygoogle-status="done"><ins id="aswift_6_expand" style="display: inline-table; border: none; height: 281px; margin: 0px; padding: 0px; position: relative; visibility: visible; width: 337px; background-color: transparent;"><ins id="aswift_6_anchor" style="display: block; border: none; height: 281px; margin: 0px; padding: 0px; position: relative; visibility: visible; width: 337px; background-color: transparent; overflow: hidden;"><iframe width="337" height="281" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" onload="var i=this.id,s=window.google_iframe_oncopy,H=s&amp;&amp;s.handlers,h=H&amp;&amp;H[i],w=this.contentWindow,d;try{d=w.document}catch(e){}if(h&amp;&amp;d&amp;&amp;(!d.body||!d.body.firstChild)){if(h.call){setTimeout(h,0)}else if(h.match){try{h=s.upd(h,i)}catch(e){}w.location.replace(h)}}" id="aswift_6" name="aswift_6" style="left: 0px; position: absolute; top: 0px; border: 0px; width: 337px; height: 281px;" src="./Binary_files/saved_resource(13).html"></iframe></ins></ins></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script></div>
		</aside>                 <div class="rightSideBarParent">
                    <div class="leftSideBar rightSideBar"> 
                    <div class="rightbar_lefthead"> </div>
                    <div class="rightbar_head">Most visited in Searching</div>
                    <div class="rightbar_righthead"> </div>
                    <ul class="leftBarList">
                    <li><a href="https://www.geeksforgeeks.org/oyo-rooms-interview-experience-on-campus/">OYO Rooms Interview Experience (On-Campus)</a></li><li><a href="https://www.geeksforgeeks.org/check-if-it-is-possible-to-reach-a-number-by-making-jumps-of-two-given-length/">Check if it is possible to reach a number by making jumps of two given length</a></li><li><a href="https://www.geeksforgeeks.org/next-smaller-element/">Next Smaller Element</a></li><li><a href="https://www.geeksforgeeks.org/longest-subarray-having-average-greater-than-or-equal-to-x/">Longest subarray having average greater than or equal to x</a></li><li><a href="https://www.geeksforgeeks.org/largest-subarray-having-sum-greater-than-k/">Largest subarray having sum greater than k</a></li>                    </ul>
                    </div>
                    </div><br> <aside id="text-7" class="widget widget_text">			<div class="textwidget"><script async="" src="./Binary_files/f(10).txt"></script>
<!-- GfGSideBottomResponsive -->
<ins class="adsbygoogle" style="display: block; height: 280px;" data-ad-client="ca-pub-9465609616171866" data-ad-slot="5749413230" data-ad-format="auto" data-adsbygoogle-status="done"><ins id="aswift_7_expand" style="display:inline-table;border:none;height:280px;margin:0;padding:0;position:relative;visibility:visible;width:337px;background-color:transparent;"><ins id="aswift_7_anchor" style="display:block;border:none;height:280px;margin:0;padding:0;position:relative;visibility:visible;width:337px;background-color:transparent;"><iframe width="337" height="280" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" onload="var i=this.id,s=window.google_iframe_oncopy,H=s&amp;&amp;s.handlers,h=H&amp;&amp;H[i],w=this.contentWindow,d;try{d=w.document}catch(e){}if(h&amp;&amp;d&amp;&amp;(!d.body||!d.body.firstChild)){if(h.call){setTimeout(h,0)}else if(h.match){try{h=s.upd(h,i)}catch(e){}w.location.replace(h)}}" id="aswift_7" name="aswift_7" style="left:0;position:absolute;top:0;border:0px;width:337px;height:280px;" src="./Binary_files/saved_resource(14).html"></iframe></ins></ins></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script></div>
		</aside><aside id="text-6" class="widget widget_text">			<div class="textwidget"><a target="_blank" href="https://practice.geeksforgeeks.org/courses/geeks-classes"><img src="./Binary_files/480x600VerticalBanner2Mar-min.png"></a></div>
		</aside>                        <div class="rightSideBarParent">
                        <div class="leftSideBar rightSideBar"> 
                        <div class="rightbar_lefthead"> </div>
                        <div class="rightbar_head">Most Trending Articles</div>
                        <div class="rightbar_righthead"> </div>
                        <ul class="leftBarList">
                        <li><a href="https://www.geeksforgeeks.org/sorting-in-java/" target="_blank">Sorting in Java</a></li><li><a href="https://www.geeksforgeeks.org/bitwise-operators-in-java/" target="_blank">Bitwise operators in Java</a></li><li><a href="https://www.geeksforgeeks.org/how-to-prepare-for-elitmus-hiring-potential-test-ph-test/" target="_blank">How to prepare for eLitmus Hiring Potential Test (pH Test)</a></li><li><a href="https://www.geeksforgeeks.org/int-1-sign-bit-31-data-bits-keyword-in-c/" target="_blank">int (1 sign bit + 31 data bits) keyword in C</a></li><li><a href="https://www.geeksforgeeks.org/program-error-signals/" target="_blank">Program error signals</a></li><li><a href="https://www.geeksforgeeks.org/longest-substring-with-count-of-1s-more-than-0s/" target="_blank">Longest substring with count of 1s more than 0s</a></li><li><a href="https://www.geeksforgeeks.org/html-introduction/" target="_blank">HTML | Introduction</a></li><li><a href="https://www.geeksforgeeks.org/make-all-numbers-of-an-array-equal/" target="_blank">Make all numbers of an array equal</a></li><li><a href="https://www.geeksforgeeks.org/why-array-index-starts-from-zero/" target="_blank">Why array index starts from zero ?</a></li><li><a href="https://www.geeksforgeeks.org/string-find-in-cpp/" target="_blank">string find in C++</a></li><li><a href="https://www.geeksforgeeks.org/taking-input-from-console-in-python/" target="_blank">Taking input from console in Python</a></li><li><a href="https://www.geeksforgeeks.org/python-list-sort/" target="_blank">Python list sort()</a></li><li><a href="https://www.geeksforgeeks.org/functions-in-python/" target="_blank">Functions in Python</a></li><li><a href="https://www.geeksforgeeks.org/codenation-interview-experience-on-campus-for-sde/" target="_blank">CodeNation Interview Experience | (On-Campus for SDE)</a></li><li><a href="https://www.geeksforgeeks.org/how-do-i-become-a-good-java-programmer/" target="_blank">How do I become a good Java programmer?</a></li>                        </ul>
                        </div>
                        </div><br> <aside id="text-9" class="widget widget_text">			<div class="textwidget"><!-- BuySellAds Zone Code -->
<div id="bsap_1304848" class="bsap bsap_1304848" data-serve="CVSIE53W">
<style type="text/css">
div.bsap_1304848{width:100%;display:block;}div.bsap_1304848 a{width:300px;}div.bsap_1304848 a img{padding:0;}div.bsap_1304848 a em{font-style:normal;}div.bsap_1304848 a{display:block;font-size:11px;color:#888;font-family:verdana,sans-serif;margin:0;text-align:center;text-decoration:none;overflow:hidden;float:left;}
div.bsap_1304848 img{border:0;clear:right;}
div.bsap_1304848 a.adhere{color:#666;font-weight:bold;font-size:12px;border:1px solid #ccc;background:#e7e7e7;text-align:center;}
div.bsap_1304848 a.adhere:hover{border:1px solid #999;background:#ddd;color:#333;}
div.bsap_1304848 iframe{display:block;font-size:11px;color:#888;font-family:verdana,sans-serif;margin:0;text-align:center;text-decoration:none;overflow:hidden;float:left;}div.bsap_1304848 a{line-height:100%;}div.bsap_1304848 a.adhere{width:300px;height:250px;line-height:2000%;}html>body div.bsap_1304848 a.adhere{width:298px;height:248px;}div.bsap_1304848 img.s{height:0;width:0;}div.bsap_1304848{line-height:9px;}div.bsap_1304848 .bsap_adhere a{height:19px !important;width:298px !important;font-size:10px;background:#f1f1f1;border:1px solid #e1e1e1;border-top:none;border-radius: 0 0 2px 2px;line-height:16px;}.bsap_backfillframe{border:0;}
</style>
<!-- no ad -->

<div class="bsap_adhere">

<a href="http://www.buysellads.com/buy/detail/269492/zone/1304848?utm_source=site_269492&amp;utm_medium=website&amp;utm_campaign=imagetext&amp;utm_content=zone_1304848" class="">Advertise Here</a>

</div>


<script type="text/javascript" id="auto_1" class="ignoreme"> if (typeof(BSACallback) !== 'undefined') BSACallback(); </script></div>
<!-- End BuySellAds Zone Code --></div>
		</aside>		</div><!-- #secondary -->
		</div><ins class="adsbygoogle adsbygoogle-noablate" data-adsbygoogle-status="done" style="display: none !important;"><ins id="aswift_0_expand" style="display:inline-table;border:none;height:0px;margin:0;padding:0;position:relative;visibility:visible;width:0px;background-color:transparent;"><ins id="aswift_0_anchor" style="display:block;border:none;height:0px;margin:0;padding:0;position:relative;visibility:visible;width:0px;background-color:transparent;"><iframe frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" onload="var i=this.id,s=window.google_iframe_oncopy,H=s&amp;&amp;s.handlers,h=H&amp;&amp;H[i],w=this.contentWindow,d;try{d=w.document}catch(e){}if(h&amp;&amp;d&amp;&amp;(!d.body||!d.body.firstChild)){if(h.call){setTimeout(h,0)}else if(h.match){try{h=s.upd(h,i)}catch(e){}w.location.replace(h)}}" id="aswift_0" name="aswift_0" style="left:0;position:absolute;top:0;border:0px;width:0px;height:0px;" src="./Binary_files/saved_resource(15).html"></iframe></ins></ins></ins><!-- #main .wrapper -->
  <footer>
    <div id="container-g4g-footer">

        <div id="footer">
            <div class="logo">
                <ul class="gfg-logo-ul">
                    <li>
                      <a href="https://www.geeksforgeeks.org/">
                        <img src="./Binary_files/GeeksforGeeksLogoFooterSmall.png" alt="GeeksforGeeks">
                      </a>
                    </li>
                </ul>
                <ul class="social-ul">
                    <li>710-B, Advant Navis Business Park,</li>
                    <li>Sector-142, Noida, Uttar Pradesh - 201305</li>
        <li>feedback@geeksforgeeks.org</li>
                </ul>
                
            </div>
            <div class="footer-column">
                <ul>
                    <li><b>COMPANY</b></li>
                    <li><a href="https://www.geeksforgeeks.org/about/">About Us</a></li>
                    <li><a href="https://www.geeksforgeeks.org/careers/">Careers</a></li>
                    <li><a href="https://www.geeksforgeeks.org/privacy-policy/">Privacy Policy</a></li>
                    <li><a href="https://www.geeksforgeeks.org/about/contact-us/">Contact Us</a></li>
                </ul>
            </div>


            <div class="footer-column">
                <ul>
                    <li><b>LEARN</b></li>
                    <li><a href="https://www.geeksforgeeks.org/fundamentals-of-algorithms/">Algorithms</a></li>
                    <li><a href="https://www.geeksforgeeks.org/data-structures/">Data Structures</a></li>
                    <li><a href="https://www.geeksforgeeks.org/category/program-output/">Languages</a></li>
                    <li><a href="https://www.geeksforgeeks.org/articles-on-computer-science-subjects-gq/">CS Subjects</a></li>
                    <li><a href="https://www.youtube.com/geeksforgeeksvideos/">Video Tutorials</a></li>
                </ul>
            </div>

            <div class="footer-column">
                <ul>
                    <li><b>PRACTICE</b></li>
                    <li><a href="https://practice.geeksforgeeks.org/company-tags/">Company-wise</a></li>
                    <li><a href="https://practice.geeksforgeeks.org/topic-tags/">Topic-wise</a></li>
                    <li><a href="https://practice.geeksforgeeks.org/contests/">Contests</a></li>
                    <li><a href="https://practice.geeksforgeeks.org/subjective-page.php">Subjective Questions</a></li>
                </ul>
            </div>

            <div class="footer-column">
                <ul>
                    <li><b>CONTRIBUTE</b>
                    </li><li><a href="https://www.geeksforgeeks.org/contribute/">Write an Article</a></li>
                    <li><a href="https://www.geeksforgeeks.org/write-interview-experience/">Write Interview Experience</a></li>
                    <li><a href="https://www.geeksforgeeks.org/internship/">Internships</a></li>
                    <li><a href="https://www.geeksforgeeks.org/how-to-contribute-videos-to-geeksforgeeks/">Videos</a></li>
                </ul>
            </div>

        </div>

        <div class="footer-bottom-div footer-bottom-social">
    <ul class="social-ul" style="padding-left: 0px;">
                    <li>
                        <a class="social-link" href="https://www.facebook.com/GeeksforGeeks-316764689022/timeline/"><div class="social-img-div"></div></a>
                        <a class="social-link" href="https://in.linkedin.com/company/geeksforgeeks"><div class="social-img-div"></div></a>
                        <a class="social-link" href="https://play.google.com/store/apps/details?id=free.programming.programming&amp;hl=en"><div class="social-img-div"></div></a>
                        <a class="social-link" href="https://twitter.com/geeksforgeeks"><div class="social-img-div"></div></a>
                        <a class="social-link" href="https://www.youtube.com/geeksforgeeksvideos"><div class="social-img-div"></div></a>
                    </li>
                </ul>
  </div>
  <div class="footer-bottom-div">
            @geeksforgeeks, <a style="color:#fff !important" href="https://creativecommons.org/licenses/by-sa/4.0/">Some rights reserved</a>
        </div>

    </div>
</footer>
<!-- #page -->

<iframe id="google_osd_static_frame_3256759856947" name="google_osd_static_frame" style="display: none; width: 0px; height: 0px;" src="./Binary_files/saved_resource(16).html"></iframe><script type="text/javascript" src="./Binary_files/wp-embed.min.js"></script>

<script>jQuery(document).ready(function($) { RESPONSIVEUI.responsiveTabs(); })</script>

<style>
.eventLink{
border: 1px solid #868686;
background-color: #e0e0e0;
padding: 10px;
box-shadow: none;
display: block;
text-align: center;
color: #555 !important;
font-size: 14px;
font-weight: bold;
}
</style>

<script type="text/javascript">
// below changes to be added in gfg.js in future.
// load comment button click when page scroll to it and positioned ad in mobile view.
flag=0;jQuery(window).scroll(function(){if(jQuery('#comment').length !=0 ){var hT=jQuery('#comment').offset().top,hH=jQuery('#comment').outerHeight(),wH=jQuery(window).height(),wS=jQuery(this).scrollTop();if(wS>(hT+hH-wH-70)&&!flag){jQuery('#comment').click();flag=1}}});
/*var temp_width=jQuery(window).width();if(temp_width<468){if(jQuery('article').length>1){jQuery(jQuery('.responsiveAd')).insertAfter('article:eq(2)');jQuery('.rectangleAd').hide()}
else if(jQuery('#practiceLinkDiv').length>0){jQuery(jQuery('.responsiveAd')).insertAfter('#practiceLinkDiv');jQuery('.rectangleAd').css('width','')}else{jQuery('.responsiveAd').hide();jQuery('.rectangleAd').css('width','')}}
*/

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-12148232-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
</script>
<script type="text/javascript" src="./Binary_files/monetization.js"></script>
<script>
(function(){
    if(typeof _bsa !== 'undefined' && _bsa) {
        _bsa.init('fancybar', 'C6ADVKE', 'placement:geeksforgeeks');
    }
})();
</script>



<!-- Dynamic page generated in 2.263 seconds. -->
<!-- Cached page generated by WP-Super-Cache on 2019-02-01 12:31:11 -->

<!-- Compression = gzip --><table cellspacing="0" cellpadding="0" class="gstl_50 gssb_c" style="width: 379px; display: none; top: 32px; position: absolute; left: 330px;"><tbody><tr><td class="gssb_f"></td><td class="gssb_e" style="width: 100%;"></td></tr></tbody></table><script type="text/javascript" src="./Binary_files/saved_resource(1)"></script><script type="text/javascript" src="./Binary_files/geoip2.js"></script></body><iframe id="google_shimpl" style="display: none;" src="./Binary_files/saved_resource(17).html"></iframe><iframe id="google_esf" name="google_esf" src="./Binary_files/zrt_lookup.html" data-ad-client="ca-pub-9465609616171866" style="display: none;"></iframe></html>
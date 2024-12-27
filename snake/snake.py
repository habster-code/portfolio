




<!DOCTYPE html>
<html class="gl-light ui-neutral with-top-bar with-header " lang="en">
<head prefix="og: http://ogp.me/ns#">
<meta charset="utf-8">
<meta content="IE=edge" http-equiv="X-UA-Compatible">
<meta content="width=device-width, initial-scale=1" name="viewport">
<title>2_semester/snake_gamev1/v1/snake.py · main · Liza Poznyak / homework · GitLab</title>
<script type="text/javascript" src="https://ff.kis.v2.scr.kaspersky-labs.com/FD126C42-EBFA-4E12-B309-BB3FDD723AC1/main.js?attr=rJGjKP-JJz4IPy3iuLXPBNViTcLOmEI1qrfhU2Pr6A49NH6P80fa4QoztjLXR5P3mPvJG6QTUU-_RAH3xroNtW8nnculE1ua4JD1jxA4oG36NQ49BFF2kO8MPI_4FvWdPLclWZZ6Uxmo_CzvO0PubA" nonce="b30abc3e1c035ab9399297ac2c7d1370" charset="UTF-8"></script><script nonce="vIvYYGVV4eRBqz+pee7pUw==">
//<![CDATA[
window.gon={};gon.math_rendering_limits_enabled=true;gon.features={"inlineBlame":false,"blobOverflowMenu":false};gon.licensed_features={"remoteDevelopment":true};
//]]>
</script>


<script nonce="vIvYYGVV4eRBqz+pee7pUw==">
//<![CDATA[
var gl = window.gl || {};
gl.startup_calls = null;
gl.startup_graphql_calls = [{"query":"query getBlobInfo(\n  $projectPath: ID!\n  $filePath: [String!]!\n  $ref: String!\n  $refType: RefType\n  $shouldFetchRawText: Boolean!\n) {\n  project(fullPath: $projectPath) {\n    __typename\n    id\n    repository {\n      __typename\n      empty\n      blobs(paths: $filePath, ref: $ref, refType: $refType) {\n        __typename\n        nodes {\n          __typename\n          id\n          webPath\n          name\n          size\n          rawSize\n          rawTextBlob @include(if: $shouldFetchRawText)\n          fileType\n          language\n          path\n          blamePath\n          editBlobPath\n          gitpodBlobUrl\n          ideEditPath\n          forkAndEditPath\n          ideForkAndEditPath\n          codeNavigationPath\n          projectBlobPathRoot\n          forkAndViewPath\n          environmentFormattedExternalUrl\n          environmentExternalUrlForRouteMap\n          canModifyBlob\n          canModifyBlobWithWebIde\n          canCurrentUserPushToBranch\n          archived\n          storedExternally\n          externalStorage\n          externalStorageUrl\n          rawPath\n          replacePath\n          pipelineEditorPath\n          simpleViewer {\n            fileType\n            tooLarge\n            type\n            renderError\n          }\n          richViewer {\n            fileType\n            tooLarge\n            type\n            renderError\n          }\n        }\n      }\n    }\n  }\n}\n","variables":{"projectPath":"hico_art/homework","ref":"main","refType":null,"filePath":"2_semester/snake_gamev1/v1/snake.py","shouldFetchRawText":true}}];

if (gl.startup_calls && window.fetch) {
  Object.keys(gl.startup_calls).forEach(apiCall => {
   gl.startup_calls[apiCall] = {
      fetchCall: fetch(apiCall, {
        // Emulate XHR for Rails AJAX request checks
        headers: {
          'X-Requested-With': 'XMLHttpRequest'
        },
        // fetch won’t send cookies in older browsers, unless you set the credentials init option.
        // We set to `same-origin` which is default value in modern browsers.
        // See https://github.com/whatwg/fetch/pull/585 for more information.
        credentials: 'same-origin'
      })
    };
  });
}
if (gl.startup_graphql_calls && window.fetch) {
  const headers = {"X-CSRF-Token":"rlCYk0HEoz-pcjunFec-2YMTqDMbNkBs4CNDRWFMAjfdBUEifKbiqN-6gug7PuvgEs9BsnTFfUPAThHNjUtsxw","x-gitlab-feature-category":"source_code_management"};
  const url = `https://gitlab.com/api/graphql`

  const opts = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...headers,
    }
  };

  gl.startup_graphql_calls = gl.startup_graphql_calls.map(call => ({
    ...call,
    fetchCall: fetch(url, {
      ...opts,
      credentials: 'same-origin',
      body: JSON.stringify(call)
    })
  }))
}


//]]>
</script>

<link rel="prefetch" href="/assets/webpack/monaco.6231c21c.chunk.js">

<link rel="stylesheet" href="/assets/application-6848772727e17bfcf14bb4ea721e2e5f47b62d867ebe0e08c1a80c8b0f7650a0.css" />
<link rel="stylesheet" href="/assets/page_bundles/tree-1a6911fec8a6a30a6077bf8f2c0ec4cc0413a62add4fb6906a7fac3ee4a6655f.css" /><link rel="stylesheet" href="/assets/page_bundles/projects-b2f9523c89dc95755fdb6942f493913f221e18ac53599acd035ef8fc5645e675.css" /><link rel="stylesheet" href="/assets/page_bundles/commit_description-1e2cba4dda3c7b30dd84924809020c569f1308dea51520fe1dd5d4ce31403195.css" /><link rel="stylesheet" href="/assets/page_bundles/work_items-22a76cdd1fe2ae5431b7ff603f86212acaf81b49c4a932f19e3b3222dc1881ee.css" /><link rel="stylesheet" href="/assets/page_bundles/notes_shared-7e727ab1e91b421915feadeb04a1b9d57213cb1b2f8f56f4d894b34d6b42e9b3.css" />
<link rel="stylesheet" href="/assets/application_utilities-73b9a1c83703ccfccd0e1e418c7d8dc606fcac533fa38b9fa86792f098db0f9a.css" />
<link rel="stylesheet" href="/assets/tailwind-fc9d69b846f077677d1d5c7557e56a498f7336e11c1ed2c8aab18d2f43e97c8d.css" />


<link rel="stylesheet" href="/assets/fonts-fae5d3f79948bd85f18b6513a025f863b19636e85b09a1492907eb4b1bb0557b.css" />
<link rel="stylesheet" href="/assets/highlight/themes/white-e31d355458ead69f8798dbb62f54c60c4ccc7db35289cbbd2353ddfdf5109aac.css" />

<script src="/assets/webpack/runtime.09e43ef2.bundle.js" defer="defer" nonce="vIvYYGVV4eRBqz+pee7pUw=="></script>
<script src="/assets/webpack/main.7e06be95.chunk.js" defer="defer" nonce="vIvYYGVV4eRBqz+pee7pUw=="></script>
<script src="/assets/webpack/tracker.e29f8a9a.chunk.js" defer="defer" nonce="vIvYYGVV4eRBqz+pee7pUw=="></script>
<script src="/assets/webpack/analytics.c2952ea0.chunk.js" defer="defer" nonce="vIvYYGVV4eRBqz+pee7pUw=="></script>
<script nonce="vIvYYGVV4eRBqz+pee7pUw==">
//<![CDATA[
window.snowplowOptions = {"namespace":"gl","hostname":"snowplowprd.trx.gitlab.net","cookieDomain":".gitlab.com","appId":"gitlab","formTracking":true,"linkClickTracking":true}

gl = window.gl || {};
gl.snowplowStandardContext = {"schema":"iglu:com.gitlab/gitlab_standard/jsonschema/1-1-1","data":{"environment":"production","source":"gitlab-rails","correlation_id":"01JG470QT7BE58MV0RFR82CMKZ","plan":"free","extra":{},"user_id":null,"global_user_id":null,"is_gitlab_team_member":null,"namespace_id":59927826,"project_id":44663777,"feature_enabled_by_namespace_ids":null,"realm":"saas","instance_id":"ea8bf810-1d6f-4a6a-b4fd-93e8cbd8b57f","host_name":"gitlab-webservice-web-5b6bc49d99-spsqb","instance_version":"17.8.0","context_generated_at":"2024-12-27T14:06:09.963Z"}}
gl.snowplowPseudonymizedPageUrl = "https://gitlab.com/namespace59927826/project44663777/-/blob/:repository_path";
gl.maskedDefaultReferrerUrl = "https://gitlab.com/namespace/project/-/tree/id";
gl.ga4MeasurementId = 'G-ENFH3X7M5Y';


//]]>
</script>
<link rel="preload" href="/assets/application_utilities-73b9a1c83703ccfccd0e1e418c7d8dc606fcac533fa38b9fa86792f098db0f9a.css" as="style" type="text/css" nonce="siQMsOnLa8Eopo834wRnCg==">
<link rel="preload" href="/assets/application-6848772727e17bfcf14bb4ea721e2e5f47b62d867ebe0e08c1a80c8b0f7650a0.css" as="style" type="text/css" nonce="siQMsOnLa8Eopo834wRnCg==">
<link rel="preload" href="/assets/highlight/themes/white-e31d355458ead69f8798dbb62f54c60c4ccc7db35289cbbd2353ddfdf5109aac.css" as="style" type="text/css" nonce="siQMsOnLa8Eopo834wRnCg==">
<link crossorigin="" href="https://snowplowprd.trx.gitlab.net" rel="preconnect">
<link as="font" crossorigin="" href="/assets/gitlab-sans/GitLabSans-1e0a5107ea3bbd4be93e8ad2c503467e43166cd37e4293570b490e0812ede98b.woff2" rel="preload">
<link as="font" crossorigin="" href="/assets/gitlab-sans/GitLabSans-Italic-38eaf1a569a54ab28c58b92a4a8de3afb96b6ebc250cf372003a7b38151848cc.woff2" rel="preload">
<link as="font" crossorigin="" href="/assets/gitlab-mono/GitLabMono-08d2c5e8ff8fd3d2d6ec55bc7713380f8981c35f9d2df14e12b835464d6e8f23.woff2" rel="preload">
<link as="font" crossorigin="" href="/assets/gitlab-mono/GitLabMono-Italic-38e58d8df29485a20c550da1d0111e2c2169f6dcbcf894f2cd3afbdd97bcc588.woff2" rel="preload">
<link rel="preload" href="/assets/fonts-fae5d3f79948bd85f18b6513a025f863b19636e85b09a1492907eb4b1bb0557b.css" as="style" type="text/css" nonce="siQMsOnLa8Eopo834wRnCg==">



<script src="/assets/webpack/sentry.d58f1caa.chunk.js" defer="defer" nonce="vIvYYGVV4eRBqz+pee7pUw=="></script>

<script src="/assets/webpack/9.49e5c3e3.chunk.js" defer="defer" nonce="vIvYYGVV4eRBqz+pee7pUw=="></script>
<script src="/assets/webpack/11.7809366b.chunk.js" defer="defer" nonce="vIvYYGVV4eRBqz+pee7pUw=="></script>
<script src="/assets/webpack/13.692c1530.chunk.js" defer="defer" nonce="vIvYYGVV4eRBqz+pee7pUw=="></script>
<script src="/assets/webpack/commons-pages.groups.analytics.dashboards-pages.groups.harbor.repositories-pages.groups.iteration_ca-b07ae190.ba6536d6.chunk.js" defer="defer" nonce="vIvYYGVV4eRBqz+pee7pUw=="></script>
<script src="/assets/webpack/commons-pages.groups.new-pages.import.gitlab_projects.new-pages.import.manifest.new-pages.projects.n-44c6c18e.140f13e0.chunk.js" defer="defer" nonce="vIvYYGVV4eRBqz+pee7pUw=="></script>
<script src="/assets/webpack/commons-pages.search.show-super_sidebar.f3ea103b.chunk.js" defer="defer" nonce="vIvYYGVV4eRBqz+pee7pUw=="></script>
<script src="/assets/webpack/super_sidebar.ac5c2549.chunk.js" defer="defer" nonce="vIvYYGVV4eRBqz+pee7pUw=="></script>
<script src="/assets/webpack/commons-pages.projects-pages.projects.activity-pages.projects.alert_management.details-pages.project-bce54798.ba9ff334.chunk.js" defer="defer" nonce="vIvYYGVV4eRBqz+pee7pUw=="></script>
<script src="/assets/webpack/commons-pages.groups.packages-pages.groups.registry.repositories-pages.groups.security.policies.edit-429ebfda.3ef44b0f.chunk.js" defer="defer" nonce="vIvYYGVV4eRBqz+pee7pUw=="></script>
<script src="/assets/webpack/103.6f90a8f4.chunk.js" defer="defer" nonce="vIvYYGVV4eRBqz+pee7pUw=="></script>
<script src="/assets/webpack/127.0afe360f.chunk.js" defer="defer" nonce="vIvYYGVV4eRBqz+pee7pUw=="></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.snippets.show-pages.projects.tre-c684fcf6.1a49c045.chunk.js" defer="defer" nonce="vIvYYGVV4eRBqz+pee7pUw=="></script>
<script src="/assets/webpack/141.2b0e483e.chunk.js" defer="defer" nonce="vIvYYGVV4eRBqz+pee7pUw=="></script>
<script src="/assets/webpack/commons-pages.projects.blob.edit-pages.projects.blob.new-pages.projects.blob.show-pages.projects.sho-ec79e51c.bb2c02d0.chunk.js" defer="defer" nonce="vIvYYGVV4eRBqz+pee7pUw=="></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.branches.index-pages.projects.show-pages.projects.ta-c9380b86.f804dfa3.chunk.js" defer="defer" nonce="vIvYYGVV4eRBqz+pee7pUw=="></script>
<script src="/assets/webpack/commons-pages.groups.show-pages.projects.blob.show-pages.projects.show-pages.projects.tree.show.a78f7ef7.chunk.js" defer="defer" nonce="vIvYYGVV4eRBqz+pee7pUw=="></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.tree.show.1a3b2914.chunk.js" defer="defer" nonce="vIvYYGVV4eRBqz+pee7pUw=="></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.tree.show-treeList.edbd1c7d.chunk.js" defer="defer" nonce="vIvYYGVV4eRBqz+pee7pUw=="></script>
<script src="/assets/webpack/pages.projects.blob.show.5762cbff.chunk.js" defer="defer" nonce="vIvYYGVV4eRBqz+pee7pUw=="></script>

<meta content="object" property="og:type">
<meta content="GitLab" property="og:site_name">
<meta content="2_semester/snake_gamev1/v1/snake.py · main · Liza Poznyak / homework · GitLab" property="og:title">
<meta content="GitLab.com" property="og:description">
<meta content="https://gitlab.com/assets/twitter_card-570ddb06edf56a2312253c5872489847a0f385112ddbcd71ccfa1570febab5d2.jpg" property="og:image">
<meta content="64" property="og:image:width">
<meta content="64" property="og:image:height">
<meta content="https://gitlab.com/hico_art/homework/-/blob/main/2_semester/snake_gamev1/v1/snake.py" property="og:url">
<meta content="summary" property="twitter:card">
<meta content="2_semester/snake_gamev1/v1/snake.py · main · Liza Poznyak / homework · GitLab" property="twitter:title">
<meta content="GitLab.com" property="twitter:description">
<meta content="https://gitlab.com/assets/twitter_card-570ddb06edf56a2312253c5872489847a0f385112ddbcd71ccfa1570febab5d2.jpg" property="twitter:image">

<meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="yKNX0AYle-Pr41Yv_tycxVhCsZ8LAmOtKu5DD2jPTHy79o5hO0c6dJ0r72DQBUn8yZ5YHmTxXoIKgxGHhMgijA" />
<meta name="csp-nonce" content="vIvYYGVV4eRBqz+pee7pUw==" />
<meta name="action-cable-url" content="/-/cable" />
<link href="/-/manifest.json" rel="manifest">
<link rel="icon" type="image/png" href="/assets/favicon-72a2cad5025aa931d6ea56c3201d1f18e68a8cd39788c7c80d5b2b82aa5143ef.png" id="favicon" data-original-href="/assets/favicon-72a2cad5025aa931d6ea56c3201d1f18e68a8cd39788c7c80d5b2b82aa5143ef.png" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/apple-touch-icon-b049d4bc0dd9626f31db825d61880737befc7835982586d015bded10b4435460.png" />
<link href="/search/opensearch.xml" rel="search" title="Search GitLab" type="application/opensearchdescription+xml">




<meta content="GitLab.com" name="description">
<meta content="#ececef" name="theme-color">
</head>

<body class="tab-width-8 gl-browser-firefox gl-platform-windows" data-namespace-id="59927826" data-page="projects:blob:show" data-page-type-id="main/2_semester/snake_gamev1/v1/snake.py" data-project="homework" data-project-full-path="hico_art/homework" data-project-id="44663777">

<script nonce="vIvYYGVV4eRBqz+pee7pUw==">
//<![CDATA[
gl = window.gl || {};
gl.client = {"isFirefox":true,"isWindows":true};


//]]>
</script>


<header class="header-logged-out" data-testid="navbar">
<a class="gl-sr-only gl-accessibility" href="#content-body">Skip to content</a>
<div class="container-fluid">
<nav aria-label="Explore GitLab" class="header-logged-out-nav gl-flex gl-gap-3 gl-justify-between">
<div class="gl-flex gl-items-center gl-gap-1">
<span class="gl-sr-only">GitLab</span>
<a title="Homepage" id="logo" class="header-logged-out-logo has-tooltip" aria-label="Homepage" data-track-label="main_navigation" data-track-action="click_gitlab_logo_link" data-track-property="navigation_top" href="/"><svg aria-hidden="true" role="img" class="tanuki-logo" width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path class="tanuki-shape tanuki" d="m24.507 9.5-.034-.09L21.082.562a.896.896 0 0 0-1.694.091l-2.29 7.01H7.825L5.535.653a.898.898 0 0 0-1.694-.09L.451 9.411.416 9.5a6.297 6.297 0 0 0 2.09 7.278l.012.01.03.022 5.16 3.867 2.56 1.935 1.554 1.176a1.051 1.051 0 0 0 1.268 0l1.555-1.176 2.56-1.935 5.197-3.89.014-.01A6.297 6.297 0 0 0 24.507 9.5Z"
        fill="#E24329"/>
  <path class="tanuki-shape right-cheek" d="m24.507 9.5-.034-.09a11.44 11.44 0 0 0-4.56 2.051l-7.447 5.632 4.742 3.584 5.197-3.89.014-.01A6.297 6.297 0 0 0 24.507 9.5Z"
        fill="#FC6D26"/>
  <path class="tanuki-shape chin" d="m7.707 20.677 2.56 1.935 1.555 1.176a1.051 1.051 0 0 0 1.268 0l1.555-1.176 2.56-1.935-4.743-3.584-4.755 3.584Z"
        fill="#FCA326"/>
  <path class="tanuki-shape left-cheek" d="M5.01 11.461a11.43 11.43 0 0 0-4.56-2.05L.416 9.5a6.297 6.297 0 0 0 2.09 7.278l.012.01.03.022 5.16 3.867 4.745-3.584-7.444-5.632Z"
        fill="#FC6D26"/>
</svg>

</a></div>
<ul class="gl-list-none gl-p-0 gl-m-0 gl-flex gl-gap-3 gl-items-center gl-grow">
<li class="header-logged-out-nav-item header-logged-out-dropdown md:gl-hidden">
<button class="header-logged-out-toggle" data-toggle="dropdown" type="button">
<span class="gl-sr-only">
Menu
</span>
<svg class="s16" data-testid="hamburger-icon"><use href="/assets/icons-8791a66659d025e0a4c801978c79a1fbd82db1d27d85f044a35728ea7cf0ae80.svg#hamburger"></use></svg>
</button>
<div class="dropdown-menu">
<ul>
<li>
<a href="https://about.gitlab.com/why-gitlab">Why GitLab
</a></li>
<li>
<a href="https://about.gitlab.com/pricing">Pricing
</a></li>
<li>
<a href="https://about.gitlab.com/sales">Contact Sales
</a></li>
<li>
<a href="/explore">Explore</a>
</li>
</ul>
</div>
</li>
<li class="header-logged-out-nav-item gl-hidden md:gl-inline-block">
<a href="https://about.gitlab.com/why-gitlab">Why GitLab
</a></li>
<li class="header-logged-out-nav-item gl-hidden md:gl-inline-block">
<a href="https://about.gitlab.com/pricing">Pricing
</a></li>
<li class="header-logged-out-nav-item gl-hidden gl-inline-block">
<a href="https://about.gitlab.com/sales">Contact Sales
</a></li>
<li class="header-logged-out-nav-item gl-hidden md:gl-inline-block">
<a class="" href="/explore">Explore</a>
</li>
</ul>
<ul class="gl-list-none gl-p-0 gl-m-0 gl-flex gl-gap-3 gl-items-center gl-justify-end">
<li class="header-logged-out-nav-item">
<a href="/users/sign_in?redirect_to_referer=yes">Sign in</a>
</li>
<li class="header-logged-out-nav-item">
<a class="gl-button btn btn-md btn-confirm !gl-inline-flex" href="/users/sign_up"><span class="gl-button-text">
Get free trial

</span>

</a></li>
</ul>
</nav>
</div>
</header>

<div class="layout-page page-with-super-sidebar">
<aside class="js-super-sidebar super-sidebar super-sidebar-loading" data-command-palette="{&quot;project_files_url&quot;:&quot;/hico_art/homework/-/files/main?format=json&quot;,&quot;project_blob_url&quot;:&quot;/hico_art/homework/-/blob/main&quot;}" data-force-desktop-expanded-sidebar="" data-is-saas="true" data-root-path="/" data-sidebar="{&quot;whats_new_most_recent_release_items_count&quot;:6,&quot;whats_new_version_digest&quot;:&quot;c955dbe1b30a1468b032fe6896086eda50f884ff9559d966e5ef75c34eee3ff0&quot;,&quot;is_logged_in&quot;:false,&quot;context_switcher_links&quot;:[{&quot;title&quot;:&quot;Explore&quot;,&quot;link&quot;:&quot;/explore&quot;,&quot;icon&quot;:&quot;compass&quot;}],&quot;current_menu_items&quot;:[{&quot;id&quot;:&quot;project_overview&quot;,&quot;title&quot;:&quot;homework&quot;,&quot;entity_id&quot;:44663777,&quot;link&quot;:&quot;/hico_art/homework&quot;,&quot;link_classes&quot;:&quot;shortcuts-project&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;manage_menu&quot;,&quot;title&quot;:&quot;Manage&quot;,&quot;icon&quot;:&quot;users&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/hico_art/homework/activity&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;activity&quot;,&quot;title&quot;:&quot;Activity&quot;,&quot;link&quot;:&quot;/hico_art/homework/activity&quot;,&quot;link_classes&quot;:&quot;shortcuts-project-activity&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;members&quot;,&quot;title&quot;:&quot;Members&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/project_members&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;labels&quot;,&quot;title&quot;:&quot;Labels&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/labels&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;plan_menu&quot;,&quot;title&quot;:&quot;Plan&quot;,&quot;icon&quot;:&quot;planning&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/issues&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;project_issue_list&quot;,&quot;title&quot;:&quot;Issues&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/issues&quot;,&quot;pill_count_field&quot;:&quot;openIssuesCount&quot;,&quot;link_classes&quot;:&quot;shortcuts-issues has-sub-items&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;boards&quot;,&quot;title&quot;:&quot;Issue boards&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/boards&quot;,&quot;link_classes&quot;:&quot;shortcuts-issue-boards&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;milestones&quot;,&quot;title&quot;:&quot;Milestones&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/milestones&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;project_wiki&quot;,&quot;title&quot;:&quot;Wiki&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/wikis/home&quot;,&quot;link_classes&quot;:&quot;shortcuts-wiki&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;code_menu&quot;,&quot;title&quot;:&quot;Code&quot;,&quot;icon&quot;:&quot;code&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/merge_requests&quot;,&quot;is_active&quot;:true,&quot;items&quot;:[{&quot;id&quot;:&quot;project_merge_request_list&quot;,&quot;title&quot;:&quot;Merge requests&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/merge_requests&quot;,&quot;pill_count_field&quot;:&quot;openMergeRequestsCount&quot;,&quot;link_classes&quot;:&quot;shortcuts-merge_requests&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;files&quot;,&quot;title&quot;:&quot;Repository&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/tree/main&quot;,&quot;link_classes&quot;:&quot;shortcuts-tree&quot;,&quot;is_active&quot;:true},{&quot;id&quot;:&quot;branches&quot;,&quot;title&quot;:&quot;Branches&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/branches&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;commits&quot;,&quot;title&quot;:&quot;Commits&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/commits/main?ref_type=heads&quot;,&quot;link_classes&quot;:&quot;shortcuts-commits&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;tags&quot;,&quot;title&quot;:&quot;Tags&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/tags&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;graphs&quot;,&quot;title&quot;:&quot;Repository graph&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/network/main?ref_type=heads&quot;,&quot;link_classes&quot;:&quot;shortcuts-network&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;compare&quot;,&quot;title&quot;:&quot;Compare revisions&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/compare?from=main\u0026to=main&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;project_snippets&quot;,&quot;title&quot;:&quot;Snippets&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/snippets&quot;,&quot;link_classes&quot;:&quot;shortcuts-snippets&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;build_menu&quot;,&quot;title&quot;:&quot;Build&quot;,&quot;icon&quot;:&quot;rocket&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/pipelines&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;pipelines&quot;,&quot;title&quot;:&quot;Pipelines&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/pipelines&quot;,&quot;link_classes&quot;:&quot;shortcuts-pipelines&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;jobs&quot;,&quot;title&quot;:&quot;Jobs&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/jobs&quot;,&quot;link_classes&quot;:&quot;shortcuts-builds&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;pipeline_schedules&quot;,&quot;title&quot;:&quot;Pipeline schedules&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/pipeline_schedules&quot;,&quot;link_classes&quot;:&quot;shortcuts-builds&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;artifacts&quot;,&quot;title&quot;:&quot;Artifacts&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/artifacts&quot;,&quot;link_classes&quot;:&quot;shortcuts-builds&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;deploy_menu&quot;,&quot;title&quot;:&quot;Deploy&quot;,&quot;icon&quot;:&quot;deployments&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/releases&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;releases&quot;,&quot;title&quot;:&quot;Releases&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/releases&quot;,&quot;link_classes&quot;:&quot;shortcuts-deployments-releases&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;packages_registry&quot;,&quot;title&quot;:&quot;Package Registry&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/packages&quot;,&quot;link_classes&quot;:&quot;shortcuts-container-registry&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;container_registry&quot;,&quot;title&quot;:&quot;Container Registry&quot;,&quot;link&quot;:&quot;/hico_art/homework/container_registry&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;model_registry&quot;,&quot;title&quot;:&quot;Model registry&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/ml/models&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;operations_menu&quot;,&quot;title&quot;:&quot;Operate&quot;,&quot;icon&quot;:&quot;cloud-pod&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/environments&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;environments&quot;,&quot;title&quot;:&quot;Environments&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/environments&quot;,&quot;link_classes&quot;:&quot;shortcuts-environments&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;infrastructure_registry&quot;,&quot;title&quot;:&quot;Terraform modules&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/terraform_module_registry&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;monitor_menu&quot;,&quot;title&quot;:&quot;Monitor&quot;,&quot;icon&quot;:&quot;monitor&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/incidents&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;incidents&quot;,&quot;title&quot;:&quot;Incidents&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/incidents&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;service_desk&quot;,&quot;title&quot;:&quot;Service Desk&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/issues/service_desk&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;analyze_menu&quot;,&quot;title&quot;:&quot;Analyze&quot;,&quot;icon&quot;:&quot;chart&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/value_stream_analytics&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;cycle_analytics&quot;,&quot;title&quot;:&quot;Value stream analytics&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/value_stream_analytics&quot;,&quot;link_classes&quot;:&quot;shortcuts-project-cycle-analytics&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;contributors&quot;,&quot;title&quot;:&quot;Contributor analytics&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/graphs/main?ref_type=heads&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;ci_cd_analytics&quot;,&quot;title&quot;:&quot;CI/CD analytics&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/pipelines/charts&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;repository_analytics&quot;,&quot;title&quot;:&quot;Repository analytics&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/graphs/main/charts&quot;,&quot;link_classes&quot;:&quot;shortcuts-repository-charts&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;model_experiments&quot;,&quot;title&quot;:&quot;Model experiments&quot;,&quot;link&quot;:&quot;/hico_art/homework/-/ml/experiments&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false}],&quot;current_context_header&quot;:&quot;Project&quot;,&quot;support_path&quot;:&quot;https://about.gitlab.com/get-help/&quot;,&quot;docs_path&quot;:&quot;/help/docs&quot;,&quot;display_whats_new&quot;:true,&quot;show_version_check&quot;:null,&quot;search&quot;:{&quot;search_path&quot;:&quot;/search&quot;,&quot;issues_path&quot;:&quot;/dashboard/issues&quot;,&quot;mr_path&quot;:&quot;/dashboard/merge_requests&quot;,&quot;autocomplete_path&quot;:&quot;/search/autocomplete&quot;,&quot;settings_path&quot;:&quot;/search/settings&quot;,&quot;search_context&quot;:{&quot;project&quot;:{&quot;id&quot;:44663777,&quot;name&quot;:&quot;homework&quot;},&quot;project_metadata&quot;:{&quot;mr_path&quot;:&quot;/hico_art/homework/-/merge_requests&quot;,&quot;issues_path&quot;:&quot;/hico_art/homework/-/issues&quot;},&quot;code_search&quot;:true,&quot;ref&quot;:&quot;main&quot;,&quot;scope&quot;:null,&quot;for_snippets&quot;:null}},&quot;panel_type&quot;:&quot;project&quot;,&quot;shortcut_links&quot;:[{&quot;title&quot;:&quot;Snippets&quot;,&quot;href&quot;:&quot;/explore/snippets&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-snippets&quot;},{&quot;title&quot;:&quot;Groups&quot;,&quot;href&quot;:&quot;/explore/groups&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-groups&quot;},{&quot;title&quot;:&quot;Projects&quot;,&quot;href&quot;:&quot;/explore/projects/starred&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-projects&quot;}],&quot;terms&quot;:&quot;/-/users/terms&quot;}"></aside>

<div class="content-wrapper">
<div class="broadcast-wrapper">




</div>
<div class="alert-wrapper alert-wrapper-top-space gl-flex gl-flex-col gl-gap-3 container-fluid container-limited">



























</div>
<div class="top-bar-fixed container-fluid" data-testid="top-bar">
<div class="top-bar-container gl-flex gl-items-center gl-gap-2">
<div class="gl-grow gl-basis-0 gl-flex gl-items-center gl-justify-start">
<button class="gl-button btn btn-icon btn-md btn-default btn-default-tertiary js-super-sidebar-toggle-expand super-sidebar-toggle -gl-ml-3" aria-controls="super-sidebar" aria-expanded="false" aria-label="Primary navigation sidebar" type="button"><svg class="s16 gl-icon gl-button-icon " data-testid="sidebar-icon"><use href="/assets/icons-8791a66659d025e0a4c801978c79a1fbd82db1d27d85f044a35728ea7cf0ae80.svg#sidebar"></use></svg>

</button>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Liza Poznyak","item":"https://gitlab.com/hico_art"},{"@type":"ListItem","position":2,"name":"homework","item":"https://gitlab.com/hico_art/homework"},{"@type":"ListItem","position":3,"name":"Repository","item":"https://gitlab.com/hico_art/homework/-/blob/main/2_semester/snake_gamev1/v1/snake.py"}]}


</script>
<div data-testid="breadcrumb-links" id="js-vue-page-breadcrumbs-wrapper">
<div data-breadcrumbs-json="[{&quot;text&quot;:&quot;Liza Poznyak&quot;,&quot;href&quot;:&quot;/hico_art&quot;,&quot;avatarPath&quot;:null},{&quot;text&quot;:&quot;homework&quot;,&quot;href&quot;:&quot;/hico_art/homework&quot;,&quot;avatarPath&quot;:null},{&quot;text&quot;:&quot;Repository&quot;,&quot;href&quot;:&quot;/hico_art/homework/-/blob/main/2_semester/snake_gamev1/v1/snake.py&quot;,&quot;avatarPath&quot;:null}]" id="js-vue-page-breadcrumbs"></div>
<div id="js-injected-page-breadcrumbs"></div>
</div>


</div>
<div class="gl-flex-none gl-flex gl-items-center gl-justify-center">
<div id="js-advanced-search-modal"></div>

</div>
<div class="gl-grow gl-basis-0 gl-flex gl-items-center gl-justify-end">
<div id="js-work-item-feedback"></div>


</div>
</div>
</div>

<div class="container-fluid container-limited project-highlight-puc">
<main class="content" id="content-body" itemscope itemtype="http://schema.org/SoftwareSourceCode">
<div class="flash-container flash-container-page sticky" data-testid="flash-container">
<div id="js-global-alerts"></div>
</div>






<div class="js-signature-container" data-signatures-path="/hico_art/homework/-/commits/ad44b4d7f1c12510cf46e864d08c4328030e4742/signatures?limit=1"></div>

<div class="tree-holder gl-pt-4" id="tree-holder">
<div class="nav-block">
<div class="tree-ref-container">
<div class="tree-ref-holder gl-max-w-26">
<div data-project-id="44663777" data-project-root-path="/hico_art/homework" data-ref="main" data-ref-type="" id="js-tree-ref-switcher"></div>
</div>
<ul class="breadcrumb repo-breadcrumb">
<li class="breadcrumb-item">
<a href="/hico_art/homework/-/tree/main">homework
</a></li>
<li class="breadcrumb-item">
<a href="/hico_art/homework/-/tree/main/2_semester">2_semester</a>
</li>
<li class="breadcrumb-item">
<a href="/hico_art/homework/-/tree/main/2_semester/snake_gamev1">snake_gamev1</a>
</li>
<li class="breadcrumb-item">
<a href="/hico_art/homework/-/tree/main/2_semester/snake_gamev1/v1">v1</a>
</li>
<li class="breadcrumb-item">
<a href="/hico_art/homework/-/blob/main/2_semester/snake_gamev1/v1/snake.py"><strong>snake.py</strong>
</a></li>
</ul>
</div>
<div class="tree-controls gl-flex gl-flex-wrap sm:gl-flex-nowrap gl-items-baseline gl-gap-3">
<button class="gl-button btn btn-md btn-default has-tooltip shortcuts-find-file" title="Go to file, press &lt;kbd class=&#39;flat ml-1&#39; aria-hidden=true&gt;/~&lt;/kbd&gt; or &lt;kbd class=&#39;flat ml-1&#39; aria-hidden=true&gt;t&lt;/kbd&gt;" aria-keyshortcuts="/+~ t" data-html="true" data-event-tracking="click_find_file_button_on_repository_pages" type="button"><span class="gl-button-text">
Find file

</span>

</button>
<a data-event-tracking="click_blame_control_on_blob_page" class="gl-button btn btn-md btn-default js-blob-blame-link" href="/hico_art/homework/-/blame/main/2_semester/snake_gamev1/v1/snake.py"><span class="gl-button-text">
Blame
</span>

</a>
<a aria-keyshortcuts="y" class="gl-button btn btn-md btn-default has-tooltip js-data-file-blob-permalink-url" data-html="true" title="Go to permalink &lt;kbd class=&#39;flat ml-1&#39; aria-hidden=true&gt;y&lt;/kbd&gt;" href="/hico_art/homework/-/blob/9df6afd81f6f69eaab359b0c5ed8aa5eb12c04ae/2_semester/snake_gamev1/v1/snake.py"><span class="gl-button-text">
Permalink
</span>

</a>
</div>
</div>

<div class="info-well">
<div class="well-segment">
<ul class="blob-commit-info">
<li class="commit flex-row js-toggle-container" id="commit-ad44b4d7">
<div class="gl-self-start gl-block">
<a href="/hico_art"><img alt="Liza Poznyak&#39;s avatar" src="https://secure.gravatar.com/avatar/d0eb9c8b567ea75eea8c3ee0400d2d99901427b077d5277d348f74c69412b06d?s=128&amp;d=identicon" class="avatar s32 gl-inline-block" title="Liza Poznyak"></a>
</div>
<div class="commit-detail flex-list gl-flex gl-justify-between gl-items-start gl-grow gl-min-w-0 gl-mb-3">
<div class="commit-content gl-self-center" data-testid="commit-content">
<div class="gl-flex sm:gl-hidden gl-gap-3 gl-items-center">
<div class="committer gl-text-sm">
<time class="js-timeago" title="May 22, 2023 1:33am" datetime="2023-05-22T01:33:48Z" data-toggle="tooltip" data-placement="bottom" data-container="body">May 22, 2023</time>
</div>
<a class="gl-button btn btn-md btn-link commit-row-message js-onboarding-commit-item" href="/hico_art/homework/-/commit/ad44b4d7f1c12510cf46e864d08c4328030e4742"><svg class="s16 gl-icon gl-button-icon " data-testid="commit-icon"><use href="/assets/icons-8791a66659d025e0a4c801978c79a1fbd82db1d27d85f044a35728ea7cf0ae80.svg#commit"></use></svg>
<span class="gl-button-text">
ad44b4d7

</span>

</a></div>
<div class="gl-hidden sm:gl-block">
<a class="commit-row-message item-title js-onboarding-commit-item " href="/hico_art/homework/-/commit/ad44b4d7f1c12510cf46e864d08c4328030e4742">Обновила файлы, теперь всё работает как надо :)</a>
<span class="commit-row-message d-inline d-sm-none">
&middot;
ad44b4d7
</span>
<div class="committer gl-text-sm">
<a class="commit-author-link js-user-link" data-user-id="12964067" href="/hico_art">Liza Poznyak</a> authored <time class="js-timeago" title="May 22, 2023 1:33am" datetime="2023-05-22T01:33:48Z" data-toggle="tooltip" data-placement="bottom" data-container="body">May 22, 2023</time>
</div>


</div>
</div>
<div class="commit-actions gl-flex gl-items-center gl-gap-3">
<div class="gl-hidden sm:gl-flex gl-items-center gl-gap-3">

<div class="js-commit-pipeline-status" data-endpoint="/hico_art/homework/-/commit/ad44b4d7f1c12510cf46e864d08c4328030e4742/pipelines?ref=main"></div>
<div class="commit-sha-group btn-group gl-hidden sm:gl-flex">
<div class="label label-monospace monospace">
ad44b4d7
</div>
<button class="gl-button btn btn-icon btn-md btn-default " title="Copy commit SHA" aria-label="Copy commit SHA" aria-live="polite" data-toggle="tooltip" data-placement="bottom" data-container="body" data-html="true" data-category="primary" data-size="medium" data-clipboard-text="ad44b4d7f1c12510cf46e864d08c4328030e4742" type="button"><svg class="s16 gl-icon gl-button-icon " data-testid="copy-to-clipboard-icon"><use href="/assets/icons-8791a66659d025e0a4c801978c79a1fbd82db1d27d85f044a35728ea7cf0ae80.svg#copy-to-clipboard"></use></svg>

</button>

</div>
</div>
<div class="gl-block sm:gl-hidden">
<button class="gl-button btn btn-icon btn-md btn-default button-ellipsis-horizontal text-expander js-toggle-button" data-toggle="tooltip" data-container="body" data-collapse-title="Toggle commit description" data-expand-title="Toggle commit description" title="Toggle commit description" aria-label="Toggle commit description" type="button"><svg class="s16 gl-icon gl-button-icon " data-testid="ellipsis_h-icon"><use href="/assets/icons-8791a66659d025e0a4c801978c79a1fbd82db1d27d85f044a35728ea7cf0ae80.svg#ellipsis_h"></use></svg>

</button>
</div>
<div data-event-tracking="click_history_control_on_blob_page" data-history-link="/hico_art/homework/-/commits/main/2_semester/snake_gamev1/v1/snake.py" id="js-commit-history-link"></div>
</div>
</div>
<div class="gl-block sm:gl-hidden">
<div class="gl-hidden js-toggle-content gl-mt-6">
<a class="commit-row-message item-title js-onboarding-commit-item " href="/hico_art/homework/-/commit/ad44b4d7f1c12510cf46e864d08c4328030e4742">Обновила файлы, теперь всё работает как надо :)</a>
<div class="committer gl-text-sm">
<a class="commit-author-link js-user-link" data-user-id="12964067" href="/hico_art">Liza Poznyak</a> authored <time class="js-timeago" title="May 22, 2023 1:33am" datetime="2023-05-22T01:33:48Z" data-toggle="tooltip" data-placement="bottom" data-container="body">May 22, 2023</time>
</div>

</div>
</div>
</li>

</ul>
</div>
<div class="gl-hidden sm:gl-block">

</div>
</div>
<div class="blob-content-holder js-per-page" data-blame-per-page="1000" id="blob-content-holder">
<div data-blob-path="2_semester/snake_gamev1/v1/snake.py" data-can-download-code="true" data-explain-code-available="false" data-new-workspace-path="/-/remote_development/workspaces/new" data-original-branch="main" data-project-path="hico_art/homework" data-ref-type="" data-resource-id="gid://gitlab/Project/44663777" data-user-id="" id="js-view-blob-app">
<div class="gl-spinner-container" role="status"><span aria-hidden class="gl-spinner gl-spinner-md gl-spinner-dark !gl-align-text-bottom"></span><span class="gl-sr-only !gl-absolute">Loading</span>
</div>
</div>
</div>

</div>
<script nonce="vIvYYGVV4eRBqz+pee7pUw==">
//<![CDATA[
  window.gl = window.gl || {};
  window.gl.webIDEPath = '/-/ide/project/hico_art/homework/edit/main/-/2_semester/snake_gamev1/v1/snake.py'


//]]>
</script>
<div data-ambiguous="false" data-ref="main" id="js-ambiguous-ref-modal"></div>

</main>
</div>


</div>
</div>


<script nonce="vIvYYGVV4eRBqz+pee7pUw==">
//<![CDATA[
if ('loading' in HTMLImageElement.prototype) {
  document.querySelectorAll('img.lazy').forEach(img => {
    img.loading = 'lazy';
    let imgUrl = img.dataset.src;
    // Only adding width + height for avatars for now
    if (imgUrl.indexOf('/avatar/') > -1 && imgUrl.indexOf('?') === -1) {
      const targetWidth = img.getAttribute('width') || img.width;
      imgUrl += `?width=${targetWidth}`;
    }
    img.src = imgUrl;
    img.removeAttribute('data-src');
    img.classList.remove('lazy');
    img.classList.add('js-lazy-loaded');
    img.dataset.testid = 'js-lazy-loaded-content';
  });
}

//]]>
</script>
<script nonce="vIvYYGVV4eRBqz+pee7pUw==">
//<![CDATA[
gl = window.gl || {};
gl.experiments = {};


//]]>
</script>

</body>
</html>


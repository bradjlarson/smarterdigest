  


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>code-snippets/python/crm.py at master · samdeane/code-snippets · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="http://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="OkckEAlRdfB0bL/DyadjffjfnFOdyvNPF9xf172vgMg=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/assets/github-4af97e95c6d3eb9a566ad339560cd70651729a71.css" media="screen" rel="stylesheet" type="text/css" />
    <link href="https://a248.e.akamai.net/assets.github.com/assets/github2-20b8ad2ab65181cb9473a741cb5501ee2231c3bf.css" media="screen" rel="stylesheet" type="text/css" />
    


      <script src="https://a248.e.akamai.net/assets.github.com/assets/frameworks-ad1b87fda705d87118448f87fb6a20bdb15bd841.js" type="text/javascript"></script>
      <script src="https://a248.e.akamai.net/assets.github.com/assets/github-b27053786ad844f1131cdcf2ce344545cfc35c61.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="c38adbe003ebcf811acfac11dfe77893">

        <link data-pjax-transient rel='permalink' href='/samdeane/code-snippets/blob/3e4e8a0d3c9e16f258a9adb0fdb8393b68eace18/python/crm.py'>
    <meta property="og:title" content="code-snippets"/>
    <meta property="og:type" content="githubog:gitrepository"/>
    <meta property="og:url" content="https://github.com/samdeane/code-snippets"/>
    <meta property="og:image" content="https://secure.gravatar.com/avatar/eb593ea546c75985f2697d8a0a8bc4b9?s=420&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png"/>
    <meta property="og:site_name" content="GitHub"/>
    <meta property="og:description" content="Various odds &amp; ends of useful code. Contribute to code-snippets development by creating an account on GitHub."/>
    <meta property="twitter:card" content="summary"/>
    <meta property="twitter:site" content="@GitHub">
    <meta property="twitter:title" content="samdeane/code-snippets"/>

    <meta name="description" content="Various odds &amp; ends of useful code. Contribute to code-snippets development by creating an account on GitHub." />

  <link href="https://github.com/samdeane/code-snippets/commits/master.atom" rel="alternate" title="Recent Commits to code-snippets:master" type="application/atom+xml" />

  </head>


  <body class="logged_out page-blob  vis-public env-production  ">
    <div id="wrapper">

      

      

      

      


        <div class="header header-logged-out">
          <div class="container clearfix">

            <a class="header-logo-wordmark" href="https://github.com/">
              <img alt="GitHub" class="github-logo-4x" height="30" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7@4x.png?1338945075" />
              <img alt="GitHub" class="github-logo-4x-hover" height="30" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7@4x-hover.png?1338945075" />
            </a>

              
<ul class="top-nav">
    <li class="explore"><a href="https://github.com/explore">Explore GitHub</a></li>
  <li class="search"><a href="https://github.com/search">Search</a></li>
  <li class="features"><a href="https://github.com/features">Features</a></li>
    <li class="blog"><a href="https://github.com/blog">Blog</a></li>
</ul>


            <div class="header-actions">
                <a class="button primary" href="https://github.com/signup">Sign up for free</a>
              <a class="button" href="https://github.com/login?return_to=%2Fsamdeane%2Fcode-snippets%2Fblob%2Fmaster%2Fpython%2Fcrm.py">Sign in</a>
            </div>

          </div>
        </div>


      

      


            <div class="site hfeed" itemscope itemtype="http://schema.org/WebPage">
      <div class="hentry">
        
        <div class="pagehead repohead instapaper_ignore readability-menu ">
          <div class="container">
            <div class="title-actions-bar">
              


<ul class="pagehead-actions">



    <li>
      <a href="/login?return_to=%2Fsamdeane%2Fcode-snippets"
        class="minibutton js-toggler-target star-button entice tooltipped upwards"
        title="You must be signed in to use this feature" rel="nofollow">
        <span class="mini-icon mini-icon-star"></span>Star
      </a>
      <a class="social-count js-social-count" href="/samdeane/code-snippets/stargazers">
        4
      </a>
    </li>
    <li>
      <a href="/login?return_to=%2Fsamdeane%2Fcode-snippets"
        class="minibutton js-toggler-target fork-button entice tooltipped upwards"
        title="You must be signed in to fork a repository" rel="nofollow">
        <span class="mini-icon mini-icon-fork"></span>Fork
      </a>
      <a href="/samdeane/code-snippets/network" class="social-count">
        0
      </a>
    </li>
</ul>

              <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
                <span class="repo-label"><span>public</span></span>
                <span class="mega-icon mega-icon-public-repo"></span>
                <span class="author vcard">
                  <a href="/samdeane" class="url fn" itemprop="url" rel="author">
                  <span itemprop="title">samdeane</span>
                  </a></span> /
                <strong><a href="/samdeane/code-snippets" class="js-current-repository">code-snippets</a></strong>
              </h1>
            </div>

            
  <ul class="tabs">
    <li><a href="/samdeane/code-snippets" class="selected" highlight="repo_source repo_downloads repo_commits repo_tags repo_branches">Code</a></li>
    <li><a href="/samdeane/code-snippets/network" highlight="repo_network">Network</a></li>
    <li><a href="/samdeane/code-snippets/pulls" highlight="repo_pulls">Pull Requests <span class='counter'>0</span></a></li>

      <li><a href="/samdeane/code-snippets/issues" highlight="repo_issues">Issues <span class='counter'>0</span></a></li>



    <li><a href="/samdeane/code-snippets/graphs" highlight="repo_graphs repo_contributors">Graphs</a></li>


  </ul>
  
<div class="tabnav">

  <span class="tabnav-right">
    <ul class="tabnav-tabs">
          <li><a href="/samdeane/code-snippets/tags" class="tabnav-tab" highlight="repo_tags">Tags <span class="counter blank">0</span></a></li>
    </ul>
    
  </span>

  <div class="tabnav-widget scope">


    <div class="select-menu js-menu-container js-select-menu js-branch-menu">
      <a class="minibutton select-menu-button js-menu-target" data-hotkey="w" data-ref="master">
        <span class="mini-icon mini-icon-branch"></span>
        <i>branch:</i>
        <span class="js-select-button">master</span>
      </a>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container js-select-menu-pane">

        <div class="select-menu-modal js-select-menu-pane">
          <div class="select-menu-header">
            <span class="select-menu-title">Switch branches/tags</span>
            <span class="mini-icon mini-icon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-filters">
            <div class="select-menu-text-filter">
              <input type="text" id="commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
            </div>
            <div class="select-menu-tabs">
              <ul>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
                </li>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
                </li>
              </ul>
            </div><!-- /.select-menu-tabs -->
          </div><!-- /.select-menu-filters -->

          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="branches" data-filterable-for="commitish-filter-field" data-filterable-type="substring">


              <div class="select-menu-item js-navigation-item js-navigation-target selected">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/samdeane/code-snippets/blob/master/python/crm.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" rel="nofollow" title="master">master</a>
              </div> <!-- /.select-menu-item -->

              <div class="select-menu-no-results js-not-filterable">Nothing to show</div>
          </div> <!-- /.select-menu-list -->


          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="tags" data-filterable-for="commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-no-results js-not-filterable">Nothing to show</div>

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

  </div> <!-- /.scope -->

  <ul class="tabnav-tabs">
    <li><a href="/samdeane/code-snippets" class="selected tabnav-tab" highlight="repo_source">Files</a></li>
    <li><a href="/samdeane/code-snippets/commits/master" class="tabnav-tab" highlight="repo_commits">Commits</a></li>
    <li><a href="/samdeane/code-snippets/branches" class="tabnav-tab" highlight="repo_branches" rel="nofollow">Branches <span class="counter ">1</span></a></li>
  </ul>

</div>

  
  
  


            
          </div>
        </div><!-- /.repohead -->

        <div id="js-repo-pjax-container" class="container context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:d021a2c1f7f51fa9e2fef89893d35fd3 -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:d021a2c1f7f51fa9e2fef89893d35fd3 -->


<div id="slider">
    <div class="frame-meta">

      <p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

        <div class="breadcrumb">
          <span class='bold'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/samdeane/code-snippets" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">code-snippets</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/samdeane/code-snippets/tree/master/python" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">python</span></a></span><span class="separator"> / </span><strong class="final-path">crm.py</strong> <span class="js-zeroclipboard zeroclipboard-button" data-clipboard-text="python/crm.py" data-copied-hint="copied!" title="copy to clipboard"><span class="mini-icon mini-icon-clipboard"></span></span>
        </div>

      <a href="/samdeane/code-snippets/find/master" class="js-slide-to" data-hotkey="t" style="display:none">Show File Finder</a>


        
  <div class="commit file-history-tease">
    <img class="main-avatar" height="24" src="https://secure.gravatar.com/avatar/46c29b422f13f2918cb377c9071b603d?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
    <span class="author"><span rel="author">Sam Deane</span></span>
    <time class="js-relative-date" datetime="2010-02-19T00:13:01-08:00" title="2010-02-19 00:13:01">February 19, 2010</time>
    <div class="commit-title">
        <a href="/samdeane/code-snippets/commit/2e3411b93ea1ee7464c22fc76a22d753ea2b121c" class="message">added python crm wrapper</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>0</strong> contributors</a></p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2>Users on GitHub who have contributed to this file</h2>
      <ul class="facebox-user-list">
      </ul>
    </div>
  </div>


    </div><!-- ./.frame-meta -->

    <div class="frames">
      <div class="frame" data-permalink-url="/samdeane/code-snippets/blob/3e4e8a0d3c9e16f258a9adb0fdb8393b68eace18/python/crm.py" data-title="code-snippets/python/crm.py at master · samdeane/code-snippets · GitHub" data-type="blob">

        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><b class="mini-icon mini-icon-text-file"></b></span>
                <span class="mode" title="File Mode">executable file</span>
                  <span>143 lines (102 sloc)</span>
                <span>4.812 kb</span>
              </div>
              <div class="actions">
                <div class="button-group">
                      <a class="minibutton js-entice" href=""
                         data-entice="You must be signed in and on a branch to make or propose changes">Edit</a>
                  <a href="/samdeane/code-snippets/raw/master/python/crm.py" class="button minibutton " id="raw-url">Raw</a>
                    <a href="/samdeane/code-snippets/blame/master/python/crm.py" class="button minibutton ">Blame</a>
                  <a href="/samdeane/code-snippets/commits/master/python/crm.py" class="button minibutton " rel="nofollow">History</a>
                </div><!-- /.button-group -->
              </div><!-- /.actions -->

            </div>
                <div class="data type-python js-blob-data">
      <table cellpadding="0" cellspacing="0" class="lines">
        <tr>
          <td>
            <pre class="line_numbers"><span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
</pre>
          </td>
          <td width="100%">
                  <div class="highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/python</span></div><div class='line' id='LC2'><br/></div><div class='line' id='LC3'><span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC4'><span class="sd">$Id: crm.py 158 2005-06-07 17:45:47Z sam $</span></div><div class='line' id='LC5'><br/></div><div class='line' id='LC6'><span class="sd">Python wrapper classes for the CRM114 Discriminator (http://crm114.sourceforge.net/).</span></div><div class='line' id='LC7'><br/></div><div class='line' id='LC8'><span class="sd">Requires the crm command to be installed and in your command path.</span></div><div class='line' id='LC9'><br/></div><div class='line' id='LC10'><span class="sd">The latest version of this file can be obtained from the Elegant Chaos subversion server (user=guest, pass=guest) at:</span></div><div class='line' id='LC11'><span class="sd">	$URL: http://source.elegantchaos.com/projects/com/elegantchaos/libraries/python/crm.py $</span></div><div class='line' id='LC12'><br/></div><div class='line' id='LC13'><span class="sd">This module provides a very simplified interface to crm114. It does not attempt to expose all of crm114&#39;s power, instead it</span></div><div class='line' id='LC14'><span class="sd">tries to hide almost all of the gory details.</span></div><div class='line' id='LC15'><br/></div><div class='line' id='LC16'><span class="sd">To use the module, create an instance of the Classifier class, giving it a path (where to store the data files), and a list</span></div><div class='line' id='LC17'><span class="sd">of category strings (these are the &quot;labels&quot; to classify the text with).</span></div><div class='line' id='LC18'><br/></div><div class='line' id='LC19'><span class="sd">e.g:</span></div><div class='line' id='LC20'><span class="sd">	c = Classifier(&quot;/path/to/my/data&quot;, [&quot;good&quot;, &quot;bad&quot;])</span></div><div class='line' id='LC21'><br/></div><div class='line' id='LC22'><span class="sd">To teach the classifier object about some text, call the learn method passing in a category (on of the ones that you provided originally),</span></div><div class='line' id='LC23'><span class="sd">and the text.</span></div><div class='line' id='LC24'><br/></div><div class='line' id='LC25'><span class="sd">e.g:</span></div><div class='line' id='LC26'><span class="sd">	c.learn(&quot;good&quot;, &quot;some good text&quot;)</span></div><div class='line' id='LC27'><span class="sd">	c.learn(&quot;bad&quot;, &quot;some bad text&quot;)</span></div><div class='line' id='LC28'><span class="sd">	</span></div><div class='line' id='LC29'><span class="sd">To find out what the classifier things about some text, call the classify method passing in the text. The result of this</span></div><div class='line' id='LC30'><span class="sd">method is a pair - the first item being the category best matching the text, and the second item being the probability of the match.</span></div><div class='line' id='LC31'><br/></div><div class='line' id='LC32'><span class="sd">e.g:</span></div><div class='line' id='LC33'><span class="sd">	(classification, probability) = c.classify(&quot;some text&quot;)</span></div><div class='line' id='LC34'><br/></div><div class='line' id='LC35'><span class="sd">TODO: use proper path separator variable in the regular expression instead of assuming that it&#39;s a slash</span></div><div class='line' id='LC36'><span class="sd">	</span></div><div class='line' id='LC37'><span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC38'><br/></div><div class='line' id='LC39'><span class="n">__version__</span> <span class="o">=</span> <span class="s">&quot;1.0.0a1&quot;</span></div><div class='line' id='LC40'><br/></div><div class='line' id='LC41'><span class="n">__license__</span> <span class="o">=</span> <span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC42'><span class="s">Copyright (C) 2005 Sam Deane.</span></div><div class='line' id='LC43'><br/></div><div class='line' id='LC44'><span class="s">This program is free software; you can redistribute it and/or</span></div><div class='line' id='LC45'><span class="s">modify it under the terms of the GNU General Public License</span></div><div class='line' id='LC46'><span class="s">as published by the Free Software Foundation; either version 2</span></div><div class='line' id='LC47'><span class="s">of the License, or (at your option) any later version.</span></div><div class='line' id='LC48'><br/></div><div class='line' id='LC49'><span class="s">This program is distributed in the hope that it will be useful,</span></div><div class='line' id='LC50'><span class="s">but WITHOUT ANY WARRANTY; without even the implied warranty of</span></div><div class='line' id='LC51'><span class="s">MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the</span></div><div class='line' id='LC52'><span class="s">GNU General Public License for more details.</span></div><div class='line' id='LC53'><br/></div><div class='line' id='LC54'><span class="s">You should have received a copy of the GNU General Public License</span></div><div class='line' id='LC55'><span class="s">along with this program; if not, write to the Free Software</span></div><div class='line' id='LC56'><span class="s">Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA</span></div><div class='line' id='LC57'><span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC58'><br/></div><div class='line' id='LC59'><span class="kn">import</span> <span class="nn">os</span><span class="p">;</span></div><div class='line' id='LC60'><span class="kn">import</span> <span class="nn">string</span><span class="p">;</span></div><div class='line' id='LC61'><br/></div><div class='line' id='LC62'><span class="c">#constants</span></div><div class='line' id='LC63'><br/></div><div class='line' id='LC64'><span class="n">kCrmPath</span> <span class="o">=</span> <span class="s">&quot;crm&quot;</span></div><div class='line' id='LC65'><br/></div><div class='line' id='LC66'><span class="n">kClassificationType</span> <span class="o">=</span> <span class="s">&quot;&lt;osb unique microgroom&gt;&quot;</span></div><div class='line' id='LC67'><span class="n">kClassificationExtension</span> <span class="o">=</span> <span class="s">&quot;.css&quot;</span></div><div class='line' id='LC68'><br/></div><div class='line' id='LC69'><span class="n">kLearnCommand</span> <span class="o">=</span> <span class="s">&quot; &#39;-{ learn </span><span class="si">%s</span><span class="s"> ( </span><span class="si">%s</span><span class="s"> ) }&#39;&quot;</span></div><div class='line' id='LC70'><span class="n">kClassifyCommand</span> <span class="o">=</span> <span class="s">&quot; &#39;-{ isolate (:stats:); classify </span><span class="si">%s</span><span class="s"> ( </span><span class="si">%s</span><span class="s"> ) (:stats:); match [:stats:] (:: :best: :prob:) /Best match to file .. \(</span><span class="si">%s</span><span class="s">\/([[:graph:]]+)</span><span class="se">\\</span><span class="si">%s</span><span class="s">\) prob: ([0-9.]+)/; output /:*:best:</span><span class="se">\\</span><span class="s">t:*:prob:/ }&#39;&quot;</span></div><div class='line' id='LC71'><br/></div><div class='line' id='LC72'><br/></div><div class='line' id='LC73'><span class="c"># wrapper for crm114</span></div><div class='line' id='LC74'><span class="k">class</span> <span class="nc">Classifier</span><span class="p">:</span></div><div class='line' id='LC75'><br/></div><div class='line' id='LC76'>	<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">categories</span> <span class="o">=</span> <span class="p">[]</span> <span class="p">):</span></div><div class='line' id='LC77'>		<span class="bp">self</span><span class="o">.</span><span class="n">categories</span> <span class="o">=</span> <span class="n">categories</span></div><div class='line' id='LC78'>		<span class="bp">self</span><span class="o">.</span><span class="n">path</span> <span class="o">=</span> <span class="n">path</span></div><div class='line' id='LC79'>		<span class="bp">self</span><span class="o">.</span><span class="n">makeFiles</span><span class="p">()</span></div><div class='line' id='LC80'><br/></div><div class='line' id='LC81'>	<span class="c"># learn the classifier what category some new text is in </span></div><div class='line' id='LC82'>	<span class="k">def</span> <span class="nf">learn</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">category</span><span class="p">,</span> <span class="n">text</span> <span class="p">):</span></div><div class='line' id='LC83'>		<span class="n">command</span> <span class="o">=</span> <span class="n">kCrmPath</span> <span class="o">+</span> <span class="p">(</span> <span class="n">kLearnCommand</span> <span class="o">%</span> <span class="p">(</span> <span class="n">kClassificationType</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span> <span class="bp">self</span><span class="o">.</span><span class="n">path</span><span class="p">,</span> <span class="n">category</span> <span class="o">+</span> <span class="n">kClassificationExtension</span> <span class="p">)</span> <span class="p">)</span> <span class="p">)</span></div><div class='line' id='LC84'><br/></div><div class='line' id='LC85'>		<span class="n">pipe</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">popen</span><span class="p">(</span> <span class="n">command</span><span class="p">,</span> <span class="s">&#39;w&#39;</span> <span class="p">)</span></div><div class='line' id='LC86'>		<span class="n">pipe</span><span class="o">.</span><span class="n">write</span><span class="p">(</span> <span class="n">text</span> <span class="p">)</span></div><div class='line' id='LC87'>		<span class="n">pipe</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC88'><br/></div><div class='line' id='LC89'>	<span class="c"># ask the classifier what category best matches some text	</span></div><div class='line' id='LC90'>	<span class="k">def</span> <span class="nf">classify</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">text</span> <span class="p">):</span></div><div class='line' id='LC91'>		<span class="n">path</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">path</span><span class="p">,</span> <span class="s">&quot;/&quot;</span><span class="p">,</span> <span class="s">&quot;</span><span class="se">\\</span><span class="s">/&quot;</span><span class="p">)</span> <span class="c"># need to escape path separator for the regexp matching</span></div><div class='line' id='LC92'>		<span class="n">command</span> <span class="o">=</span> <span class="n">kCrmPath</span> <span class="o">+</span> <span class="p">(</span> <span class="n">kClassifyCommand</span> <span class="o">%</span> <span class="p">(</span><span class="n">kClassificationType</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">getFileListString</span><span class="p">(),</span> <span class="n">path</span><span class="p">,</span> <span class="n">kClassificationExtension</span><span class="p">)</span> <span class="p">)</span></div><div class='line' id='LC93'>		<span class="p">(</span><span class="n">fin</span><span class="p">,</span> <span class="n">fout</span><span class="p">)</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">popen2</span><span class="p">(</span> <span class="n">command</span> <span class="p">)</span></div><div class='line' id='LC94'>		<span class="n">fin</span><span class="o">.</span><span class="n">write</span><span class="p">(</span> <span class="n">text</span> <span class="p">)</span></div><div class='line' id='LC95'>		<span class="n">fin</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC96'>		<span class="nb">list</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">fout</span><span class="o">.</span><span class="n">readline</span><span class="p">())</span></div><div class='line' id='LC97'>		<span class="n">fout</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC98'>		<span class="k">if</span> <span class="nb">list</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC99'>			<span class="k">return</span> <span class="p">(</span><span class="s">&quot;&quot;</span><span class="p">,</span> <span class="mf">0.0</span><span class="p">)</span></div><div class='line' id='LC100'>		<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC101'>			<span class="n">category</span> <span class="o">=</span> <span class="nb">list</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC102'>			<span class="n">probability</span> <span class="o">=</span> <span class="nb">float</span><span class="p">(</span><span class="nb">list</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span></div><div class='line' id='LC103'>			<span class="k">return</span> <span class="p">(</span><span class="n">category</span><span class="p">,</span> <span class="n">probability</span><span class="p">)</span></div><div class='line' id='LC104'><br/></div><div class='line' id='LC105'>	<span class="c"># ensure that data files exist, by calling learn with an empty string</span></div><div class='line' id='LC106'>	<span class="k">def</span> <span class="nf">makeFiles</span><span class="p">(</span> <span class="bp">self</span> <span class="p">):</span></div><div class='line' id='LC107'>		<span class="c"># make directory if necessary</span></div><div class='line' id='LC108'>		<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span> <span class="bp">self</span><span class="o">.</span><span class="n">path</span> <span class="p">):</span></div><div class='line' id='LC109'>				<span class="n">os</span><span class="o">.</span><span class="n">mkdir</span><span class="p">(</span> <span class="bp">self</span><span class="o">.</span><span class="n">path</span> <span class="p">)</span></div><div class='line' id='LC110'><br/></div><div class='line' id='LC111'>		<span class="c"># make category files</span></div><div class='line' id='LC112'>		<span class="k">for</span> <span class="n">category</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">categories</span><span class="p">:</span></div><div class='line' id='LC113'>			<span class="bp">self</span><span class="o">.</span><span class="n">learn</span><span class="p">(</span> <span class="n">category</span><span class="p">,</span> <span class="s">&quot;&quot;</span> <span class="p">)</span></div><div class='line' id='LC114'><br/></div><div class='line' id='LC115'><br/></div><div class='line' id='LC116'>	<span class="c"># return a list of classification files</span></div><div class='line' id='LC117'>	<span class="k">def</span> <span class="nf">getFileList</span><span class="p">(</span> <span class="bp">self</span> <span class="p">):</span></div><div class='line' id='LC118'><br/></div><div class='line' id='LC119'>		<span class="c"># internal method to build a file path given a category</span></div><div class='line' id='LC120'>		<span class="k">def</span> <span class="nf">getFilePath</span><span class="p">(</span> <span class="nb">file</span> <span class="p">):</span></div><div class='line' id='LC121'>			<span class="k">return</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span> <span class="bp">self</span><span class="o">.</span><span class="n">path</span><span class="p">,</span> <span class="nb">file</span> <span class="o">+</span> <span class="n">kClassificationExtension</span> <span class="p">)</span></div><div class='line' id='LC122'><br/></div><div class='line' id='LC123'>		<span class="c"># return list of all category paths</span></div><div class='line' id='LC124'>		<span class="k">return</span> <span class="nb">map</span><span class="p">(</span> <span class="n">getFilePath</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">categories</span> <span class="p">)</span></div><div class='line' id='LC125'><br/></div><div class='line' id='LC126'><br/></div><div class='line' id='LC127'>	<span class="c"># return a list of classification files as a string</span></div><div class='line' id='LC128'>	<span class="k">def</span> <span class="nf">getFileListString</span><span class="p">(</span> <span class="bp">self</span> <span class="p">):</span></div><div class='line' id='LC129'>		<span class="k">return</span> <span class="n">string</span><span class="o">.</span><span class="n">join</span><span class="p">(</span> <span class="bp">self</span><span class="o">.</span><span class="n">getFileList</span><span class="p">(),</span> <span class="s">&quot; &quot;</span> <span class="p">)</span></div><div class='line' id='LC130'><br/></div><div class='line' id='LC131'>	<span class="c"># perform some self tests	</span></div><div class='line' id='LC132'>	<span class="k">def</span> <span class="nf">test</span><span class="p">(</span> <span class="bp">self</span> <span class="p">):</span></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;		<span class="k">print</span> <span class="bp">self</span><span class="o">.</span><span class="n">getFileList</span><span class="p">()</span></div><div class='line' id='LC134'>&nbsp;&nbsp;&nbsp;&nbsp;		<span class="bp">self</span><span class="o">.</span><span class="n">learn</span><span class="p">(</span> <span class="s">&quot;good&quot;</span><span class="p">,</span> <span class="s">&quot;this is a test&quot;</span> <span class="p">)</span></div><div class='line' id='LC135'>&nbsp;&nbsp;&nbsp;&nbsp;		<span class="bp">self</span><span class="o">.</span><span class="n">learn</span><span class="p">(</span> <span class="s">&quot;bad&quot;</span><span class="p">,</span> <span class="s">&quot;this is very bad&quot;</span> <span class="p">)</span></div><div class='line' id='LC136'>&nbsp;&nbsp;&nbsp;&nbsp;		<span class="k">print</span> <span class="s">&quot;class was: </span><span class="si">%s</span><span class="s">, prob was:</span><span class="si">%f</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span> <span class="bp">self</span><span class="o">.</span><span class="n">classify</span><span class="p">(</span> <span class="s">&quot;this is a test&quot;</span> <span class="p">)</span> <span class="p">)</span></div><div class='line' id='LC137'><br/></div><div class='line' id='LC138'><br/></div><div class='line' id='LC139'><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&quot;__main__&quot;</span><span class="p">:</span></div><div class='line' id='LC140'>	<span class="c"># perform a simple test</span></div><div class='line' id='LC141'>	<span class="n">c</span> <span class="o">=</span> <span class="n">Classifier</span><span class="p">(</span> <span class="s">&quot;test/data&quot;</span><span class="p">,</span> <span class="p">[</span> <span class="s">&quot;good&quot;</span><span class="p">,</span> <span class="s">&quot;bad&quot;</span> <span class="p">]</span> <span class="p">)</span></div><div class='line' id='LC142'>&nbsp;	<span class="n">c</span><span class="o">.</span><span class="n">test</span><span class="p">()</span></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>

        <a href="#jump-to-line" rel="facebox" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
        <div id="jump-to-line" style="display:none">
          <h2>Jump to Line</h2>
          <form accept-charset="UTF-8" class="js-jump-to-line-form">
            <input class="textfield js-jump-to-line-field" type="text">
            <div class="full-button">
              <button type="submit" class="button">Go</button>
            </div>
          </form>
        </div>

      </div>
    </div>
</div>

<div id="js-frame-loading-template" class="frame frame-loading large-loading-area" style="display:none;">
  <img class="js-frame-loading-spinner" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-128.gif?1347543527" height="64" width="64">
</div>


        </div>
      </div>
      <div class="context-overlay"></div>
    </div>

      <div id="footer-push"></div><!-- hack for sticky footer -->
    </div><!-- end of wrapper - hack for sticky footer -->

      <!-- footer -->
      <div id="footer">
  <div class="container clearfix">

      <dl class="footer_nav">
        <dt>GitHub</dt>
        <dd><a href="https://github.com/about">About us</a></dd>
        <dd><a href="https://github.com/blog">Blog</a></dd>
        <dd><a href="https://github.com/contact">Contact &amp; support</a></dd>
        <dd><a href="http://enterprise.github.com/">GitHub Enterprise</a></dd>
        <dd><a href="http://status.github.com/">Site status</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Applications</dt>
        <dd><a href="http://mac.github.com/">GitHub for Mac</a></dd>
        <dd><a href="http://windows.github.com/">GitHub for Windows</a></dd>
        <dd><a href="http://eclipse.github.com/">GitHub for Eclipse</a></dd>
        <dd><a href="http://mobile.github.com/">GitHub mobile apps</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Services</dt>
        <dd><a href="http://get.gaug.es/">Gauges: Web analytics</a></dd>
        <dd><a href="http://speakerdeck.com">Speaker Deck: Presentations</a></dd>
        <dd><a href="https://gist.github.com">Gist: Code snippets</a></dd>
        <dd><a href="http://jobs.github.com/">Job board</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Documentation</dt>
        <dd><a href="http://help.github.com/">GitHub Help</a></dd>
        <dd><a href="http://developer.github.com/">Developer API</a></dd>
        <dd><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></dd>
        <dd><a href="http://pages.github.com/">GitHub Pages</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>More</dt>
        <dd><a href="http://training.github.com/">Training</a></dd>
        <dd><a href="https://github.com/edu">Students &amp; teachers</a></dd>
        <dd><a href="http://shop.github.com">The Shop</a></dd>
        <dd><a href="/plans">Plans &amp; pricing</a></dd>
        <dd><a href="http://octodex.github.com/">The Octodex</a></dd>
      </dl>

      <hr class="footer-divider">


    <p class="right">&copy; 2013 <span title="0.04761s from fe2.rs.github.com">GitHub</span>, Inc. All rights reserved.</p>
    <a class="left" href="https://github.com/">
      <span class="mega-icon mega-icon-invertocat"></span>
    </a>
    <ul id="legal">
        <li><a href="https://github.com/site/terms">Terms of Service</a></li>
        <li><a href="https://github.com/site/privacy">Privacy</a></li>
        <li><a href="https://github.com/security">Security</a></li>
    </ul>

  </div><!-- /.container -->

</div><!-- /.#footer -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/samdeane/code-snippets/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-icon mega-icon-normalscreen"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="mini-icon mini-icon-brightness"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="mini-icon mini-icon-exclamation"></span>
      Something went wrong with that request. Please try again.
      <a href="#" class="mini-icon mini-icon-remove-close ajax-error-dismiss"></a>
    </div>

    
    
    <span id='server_response_time' data-time='0.04806' data-host='fe2'></span>
    
  </body>
</html>


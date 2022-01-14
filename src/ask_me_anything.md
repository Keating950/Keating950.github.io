---
title: "Ask me anything"
bar_title: "Article: Ask me anything"
image_html: |+
    <div class="multi_img_container">
        <!-- Item 1 -->
        <a href=#img1> 
            <img src="media/thumbnails/posts_per_year_tb.gif"  class="thumbnail"> 
        </a>
        <a href="#_" class="lightbox" id="img1"> 
            <iframe src="iframe_figures/posts_per_year.html"  class="lightbox_iframe" 
                    id="posts_per_year"></iframe> 
        </a>
        <!-- Item 2 --> 
        <a href=#img2> 
            <img src="media/thumbnails/upvotes_by_time_tb.gif"	class="thumbnail"> 
        </a>
        <a href="#_" class="lightbox" id="img2"> 
            <iframe
                src="iframe_figures/upvotes_by_time.html"
                class="lightbox_iframe"
                id="upvotes_by_time">
            </iframe> 
        </a>
    </div>
    <p class="caption">Click images to view interactively.</p>
---
	
<p class="main_text"> 
"<a href="http://www.mcgilltribune.com/ask-me-anything/" target="_blank">Ask me
Anything: Mining through the 10 year history of /r/McGill"</a> is a
feature-length data journalism project that I produced with my colleague Kyle
Dewsnap in the winter of 2019—2020. We scraped every post in the subreddit's
history (totalling over 30,000) from Reddit's API and enriched them with data
from <a href="https://pushshift.io/" target="_blank">pushshift.io</a>. I then
applied various natural language processing techniques in Python, such as
k-means clustering and sentiment analysis; the notebook below shows some
examples of my work. 
</p>
<iframe  
     height="700px" 
     width=100%
     src="https://view.datalore.io/notebook/9aNxaBkR9tWJkybtWeAw6p"
     style="margin-top: 36px;  background-color: rgb(238, 238, 238);"
     allowTransparency="false"> 
</iframe>

// auto scroll effects 
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click",function(e){
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior : "smooth"
        });
    });
});




// search input clear
if(document.getElementById("search_xmark")!=null){
    const search_xmark = document.getElementById("search_xmark")
    const search_video_link = document.getElementById("link")
    search_xmark.addEventListener("click",()=>{search_video_link.value="";})
}
searchInput = document.getElementById("link")
search_btn = document.querySelector(".search_btn");
    search_btn.onclick = function(){
        if(searchInput.value.length>0){
        this.style = " display: grid; place-content: center;"
        this.innerHTML = "<div class='loader'></div>";
        // setTimeout(()=>{
        //     this.style = " display: block;"
        //     this.innerHTML = "<i class='fa-solid fa-download'></i>download ";
        // },10000);
    }
}

// form-post submition
id_download_video = 0;
Downloader_section = document.getElementById('Downloader_section');
containt_text=`<div class="article-contener" id=${id_download_video} style="padding-top:10px;">
<ul class="groups">
    <li>
        <div class="downloader_card">
            <div class="image-session">
                <span class="thumbain_image" id="downloader_card_img"></span>
            </div>
            <div class="meta-sission">
                <div class="head" id="downloader_card_catodry">
                    <a href="#" class="catogry" id="downloader_catogry"></a>
                    <span class="flexone"></span>
                </div>
                <div class="body">
                    <h3 class="title" id="downloader_card_title"></h3>
                   
                </div>
                <div class="footer">
                    <a href="#" class="button" id="downloader_card_button" download>download</a>
                </div>
            </div>
        </div>
    </li>
    
</ul>
</div>`


$(document).on('submit', '#post-form', function (e) {
    e.preventDefault();
    
    Downloader_section.innerHTML=containt_text;

    $.ajax({
        type: 'POST',
        url: '/download',
        data: {
            link: $('#link').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            data = $.parseJSON(data);
            thumb_img = document.getElementById("downloader_card_img")
            catogry = document.getElementById("downloader_card_catodry")
            title = document.getElementById("downloader_card_title")
            download_btn = document.getElementById("downloader_card_button")
            
            // settting Styles

            thumb_img.style= 'animation-play-state: paused;';
            catogry.style= 'animation-play-state: paused; background:white;';
            title.style= 'animation-play-state: paused; background:white;height:auto;';
            download_btn.style= 'animation-play-state: paused;background:#063a78';

            // style of download main button of search bar
            search_btn.style = " display: block;";
            search_btn.innerHTML = " download ";

            // setting data 
            if(data['error']==""){
                if(data['Pinstory']==0){
                    download_btn.href=`static/video/${data['filename']}`
                    thumb_img.style.backgroundImage = `url(${data['thumbnail']})`;
                    document.getElementById('downloader_catogry').innerText=data['alloader'];
                    title.innerText = data['title'];
                }else{
                    
                    

                    for (let i = 1; i < data['video_url'].length; i++) {
                        thumb=data['thumbnail'][0];
                        title.innerText = data['title'];
                        document.getElementById('downloader_catogry').innerText=`Story 1`;
                        thumb_img.style.backgroundImage = `url(${thumb})`;
                        thumb=data['thumbnail'][i];                        
                        
                        Downloader_section.innerHTML+=`<div class="article-contener" id=${i} style="padding-top:10px;">
                        
                        <ul class="groups">
                            <li>
                                <div class="downloader_card">
                                    <div class="image-session">
                                        <span class="thumbain_image" id="downloader_card_img" style =" background-image:url(${thumb});animation-play-state: paused;"></span>
                                    </div>
                                    <div class="meta-sission">
                                        <div class="head" id="downloader_card_catodry" style="animation-play-state: paused; background:white;">
                                            <a href="#" class="catogry" id="downloader_catogry">Story ${i+1}</a>
                                            <span class="flexone"></span>
                                        </div>
                                        <div class="body">
                                            <h3 class="title" id="downloader_card_title" style="animation-play-state: paused; background:white;height:auto;">${data['title']}
                                            Pins
                                            </h3>
                                           
                                        </div>
                                        <div class="footer">
                                            <a href="#" class="button" id="downloader_card_button" download style="animation-play-state: paused;background:#063a78">download</a>
                                        </div>
                                    </div>
                                </div>
                            </li>
                            
                        </ul>
                        </div>`;
                    }
                   
        

                  
                }
                
            }else{
                title.innerText = data['error'];
                title.style.color="red";
                
            }


        }
    })
})



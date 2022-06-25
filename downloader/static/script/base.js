// search input clear
if(document.getElementById("search_xmark")!=null){
    const search_xmark = document.getElementById("search_xmark")
    const search_video_link = document.getElementById("search_video_link")
    search_xmark.addEventListener("click",()=>{search_video_link.value="";})
}
searchInput = document.getElementById("search_video_link")
search_btn = document.querySelector(".search_btn");
    search_btn.onclick = function(){
        if(searchInput.value.length>0){
        this.style = " display: grid; place-content: center;"
        this.innerHTML = "<div class='loader'></div>";
        setTimeout(()=>{
            this.style = " display: block;"
            this.innerHTML = "<i class='fa-solid fa-download'></i>download ";
        },10000);
    }
}
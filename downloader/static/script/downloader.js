// download page buttons options
const Preview_video_btn = document.getElementById("Preview_video_btn")
const Video_thumbnail_btn = document.getElementById("Video_thumbnail_btn")
const Download_thumbnail_btn = document.getElementById("Download_thumbnail_btn")
const Download_video_btn = document.getElementById("Download_video_btn")
const Download_btn = document.getElementById("download_btn")

// query seletions and dynamic variables
video_area = document.getElementById("Preview_video_and_thumbnails")
thumbnail = document.getElementById("thumbnail_img")
_video_url = document.getElementById("Preview_video_main_url")

var switch_flag = 0;
const video = document.createElement('video');
video.autoplay = true;
video.controls = true;
video.muted = true;
video.height = 300; // 👈️ in px
// video.width = 320; // 👈️ in px
video.loop = true;
video.src = _video_url.href
video.poster = thumbnail.src
video.id="preview_video_id"


Preview_video_btn.addEventListener("click",play_preview_video);
Video_thumbnail_btn.addEventListener("click",open_video_thumbnail);
Download_thumbnail_btn.addEventListener("click",download_thumbnail);
Download_video_btn.addEventListener("click",download_video);
Download_btn.addEventListener("click",download_video);

function play_preview_video(){
    if(switch_flag==0){
        thumbnail.remove();
        video_area.appendChild(video)
        switch_flag = 1;
    }
    else{
        video.remove()
        video_area.appendChild(thumbnail)
        switch_flag = 0;
    }
};

function open_video_thumbnail(){console.log("video thumbnail")};
function download_thumbnail(){console.log("download thumbnail")};
function download_video(){console.log("download video")};
async function videoLoop()
{
    var rand_sec;
    while (true)
    {
        rand_sec = getRandomInt(2,3)*1000;
        await wait(rand_sec);
        var id = "";
        id = appendVideo();
        removeVideo(id);
    }
}

function appendVideo()
{
    // file name and video id 
    var file_num = getRandomInt(1,6).toString();
    var fileName = 'src/'+file_num+".mp4";
    var vedioId = "video" + file_num;
    var marginTopSize ="";
    var marginLeftSize ="";
    var videoWidthSize = "";
    var videoHeightSize = "";

    // locate the element to append children
    var container = document.getElementById("container");

    // showbox to control shpae and sizes
    var showbox = document.createElement("div");
    showbox.setAttribute("id",file_num);

    var text = clipPathGen();
    if ("" != text)   // controls of the rectangle shape
    {
        marginTopSize = (getRandomInt(0, 3)*200).toString() + "px";
        marginLeftSize = (getRandomInt(0, 4)*400).toString() + "px";

        // random width size
        videoWidthSize = (getRandomInt(4, 13)*200).toString() + "px";
        videoHeightSize = (getRandomInt(4, 11)*200).toString() + "px";

        showbox.style.width = videoWidthSize;
        showbox.style.height = videoHeightSize;
        showbox.style.marginTop = marginTopSize;
        showbox.style.marginLeft = marginLeftSize;
        showbox.style.position = "absolute";
        showbox.style.clipPath = text;
    }
    else // controls of the polygon shape
    {
        marginTopSize = (getRandomInt(0, 3)*100).toString() + "px";
        marginLeftSize = (getRandomInt(0, 4)*400).toString() + "px";

        // random width size
        videoWidthSize = (getRandomInt(4, 16)*200).toString() + "px";
        videoHeightSize = (getRandomInt(4, 16)*200).toString() + "px";

        showbox.style.width = videoWidthSize;
        showbox.style.height = videoHeightSize;
        showbox.style.marginTop = marginTopSize;
        showbox.style.marginLeft = marginLeftSize;
        showbox.style.position = "absolute";
        showbox.style.clipPath = text;
    }
    
    // video box to define the video sources
    var video = document.createElement("video");
    video.setAttribute("id", vedioId);
    video.setAttribute("src",fileName);
    video.setAttribute("width", "100%");   // fit showbox width
    video.setAttribute("height", "100%");  //fit showbox height
    video.autoplay = true;
    video.muted = true;
    video.loop = true;

    // append children
    container.appendChild(showbox);
    showbox.appendChild(video);

    return file_num;
}

function clipPathGen()
{
    // polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%)
    // inset(100px 50px 100px 50px round 20px)

    // var onepx = getRandomInt(100, 201).toString() + "px";
    // var twopx = getRandomInt(100, 201).toString() + "px";
    // var threepx = getRandomInt(100, 201).toString() + "px";
    // var fourpx = getRandomInt(100, 201).toString() + "px";
    // var fivepx = getRandomInt(100, 201).toString() + "px";

    // var p1_x = getRandomInt(80, 101).toString() + "%";
    // var p1_y = getRandomInt(0, 51).toString() + "%";

    // var p2_x = getRandomInt(80, 101).toString() + "%";
    // var p2_y = getRandomInt(0, 51).toString() + "%";

    // var p3_x = getRandomInt(80, 101).toString() + "%";
    // var p3_y = getRandomInt(0, 51).toString() + "%";

    // var p4_x = getRandomInt(80, 101).toString() + "%";
    // var p4_y = getRandomInt(0, 51).toString() + "%";

    // var circle = getRandomInt(0, 51).toString() + "%";

    // var text1 = "polygon(" + p1_x + " " + p1_y + ", " + p2_x + " " + p2_y + ", " + p3_x + " " + p3_y + ", " + p4_x + " " + p4_y + ")" 
    // var text2 = "ellipse(" + onepx + " " + twopx + " at " + p2_x + " " + p2_y +")";
    // var text3 = "circle(" + circle +")"
    // var text4 = "inset(" + onepx + " " + twopx + " " + threepx + " " + fourpx + " round " + fivepx + ")";
    var text5 = "";
    // var text6 = "polygon(36% 0, 100% 0, 85% 100%, 37% 100%)"

    var arr = [text5,
                "polygon(36% 0, 100% 0, 85% 100%, 37% 100%)",
                "polygon(16% 46%, 100% 0, 85% 100%, 55% 100%)",
                "polygon(41% 3%, 94% 39%, 100% 90%, 23% 90%)",
                "polygon(0 0, 46% 5%, 100% 90%, 45% 100%)",
                "polygon(6% 55%, 99% 15%, 88% 80%, 0 96%)",
                "polygon(0 48%, 90% 33%, 100% 76%, 24% 84%)",
                "polygon(44% 0, 70% 0, 49% 100%, 21% 100%)"
                ];

    rand_num = getRandomInt(0,8)


    // "polygon(40% 0, 61% 0, 58% 100%, 39% 100%)",
    // "polygon(0 32%, 100% 31%, 100% 54%, 0 54%)",
    // "polygon(0 53%, 100% 0, 100% 41%, 0 100%)"

    return arr[rand_num];
}

function removeVideo(id)
{   
    // random time within 3000~10000 ms
    var msec = 0;
    msec = getRandomInt(5,10)*1000;
    var container = document.getElementById("container");
    
    if (container.hasChildNodes())
    {
        window.setTimeout('container.removeChild(container.firstElementChild)', msec);
    }
}

function wait(ms)
{
    return new Promise(resolve => {
            setTimeout(()=>{resolve('')},ms);
        })
}

function getRandomInt(min, max)
{
    //The maximum is exclusive and the minimum is inclusive
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min) + min);
     
  }
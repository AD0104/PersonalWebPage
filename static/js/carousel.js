let carousel = document.querySelector(".carousel");
let carousel_items = document.getElementsByClassName("hero__carousel-card__card");
let carousel_current_item = 1;
let last_translated = 0;
let max_translated = 0;
function goToNext(){
    if(carousel_current_item < carousel_items.length){
        last_translated = last_translated -100;
        if(max_translated > last_translated){
            max_translated=last_translated
        }
        carousel.style.transform = "translateX("+last_translated+"%)";
        carousel_current_item++;
    }else{
        last_translated = 0;
        carousel.style.transform = "translateX(0%)";
        carousel_current_item=1;
    }
}
function goToPrevious(){
    if(carousel_current_item > 1){
        last_translated = last_translated+100
        carousel.style.transform = "translateX("+last_translated+"%)";
        carousel_current_item--;
    }else{
        last_translated = max_translated = -100*(carousel_items.length-1)
        carousel.style.transform = "translateX("+max_translated+"%)";
        carousel_current_item=carousel_items.length;
    }
}
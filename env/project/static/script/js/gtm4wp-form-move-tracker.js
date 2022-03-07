document.addEventListener("focusin", function(event) {
    const elem = event.target.closest("input,select,textarea,button,meter,progress");
    if (elem) {
        window[gtm4wp_datalayer_name].push({
            'event': 'gtm4wp.formElementEnter',

            'inputID': elem.getAttribute("id") || "(no input ID)",
            'inputName': elem.getAttribute("name") || "(no input name)",
            'inputClass': elem.getAttribute("class") || "(no input class)",

            'formID': elem.form.getAttribute("id") || "(no form ID)",
            'formName': elem.form.getAttribute("name") || "(no form name)",
            'formClass': elem.form.getAttribute("class") || "(no form class)"
        });
    }
}, false);


$(function() {
    $(document).one('click', '.like-review', function(e) {
        $(this).html('<i class="fa fa-heart" aria-hidden="true"></i> You liked this');
        $(this).children('.fa-heart').addClass('animate-like');
    });
});

angular.module("app", [])

// like button directive
.directive("likeButton", function() {
    return {
        restrict: "E",
        scope: {
            liked: "=ngModel" // enable ng-model
        },
        // would be in likeButton.html
        template: "<div class='like-button' ng-click='liked = true'> \
         <div class='like-button-like'> \
           <i class='ion-heart'></i> \
           like \
         </div> \
         <div class='like-button-liked' ng-class='{ show: liked }'> \
           <i class='ion-checkmark'></i> \
           liked \
         </div> \
    	 </div>"
    };
});

$(function() {
    $(".heart").on("click", function() {
        $(this).toggleClass("is-active");
    });
});


document.addEventListener("focusout", function(event) {
    const elem = event.target.closest("input,select,textarea,button,meter,progress");
    if (elem) {
        window[gtm4wp_datalayer_name].push({
            'event': 'gtm4wp.formElementLeave',

            'inputID': elem.getAttribute("id") || "(no input ID)",
            'inputName': elem.getAttribute("name") || "(no input name)",
            'inputClass': elem.getAttribute("class") || "(no input class)",

            'formID': elem.form.getAttribute("id") || "(no form ID)",
            'formName': elem.form.getAttribute("name") || "(no form name)",
            'formClass': elem.form.getAttribute("class") || "(no form class)"
        });
    };
}, false);
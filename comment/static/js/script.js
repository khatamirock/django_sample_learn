
document.addEventListener('DOMContentLoaded', function () {

    var navls = document.querySelectorAll('.navbar ul li');
    console.log(navls);

    navls.forEach(function (navl) {
        navl.addEventListener('click', function () {

            var position = navl.getAttribute('data-pos');
            window.location.href = '/api/' + position;
        })
    })


    var postDivs = document.querySelectorAll('.postview');


    postDivs.forEach(function (postDiv) {
        postDiv.addEventListener('click', function () {
            var postId = postDiv.getAttribute('data-postid');
            console.log(postId);
            window.location.href = '/api/postd/' + postId;
        });

    });
});
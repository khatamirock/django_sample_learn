
document.addEventListener('DOMContentLoaded', function () {
    // post.hmtl >> add comment buttn








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



    var addCommentBtn = document.querySelector('.commentsection button');
    addCommentBtn.addEventListener('click', function () {
        const commentTextarea = document.querySelector('.commentsection textarea');
        // add comment
        var postid = addCommentBtn.getAttribute('data-postid');
        // alert(commentTextarea.value);
        fetch('/add_comment/', {
            method: 'POST',
            body: JSON.stringify({
                id: postid,
                comment: commentContent
            })
        })
            .then(response => response.json())
            .then(data => console.log(data))

    });












});
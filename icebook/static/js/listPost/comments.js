export const viewComments = (e, posts) => {
    const commentsSection = document.querySelector(".comments-section");
    const postID = e.target.getAttribute("data-id");
    const postComments = posts.find(element => element.id == postID).comments;

    for (const [username, userData] of Object.entries(postComments)){
        const commentsHTML = allCommentsHTML(username, userData)
        commentsSection.insertAdjacentHTML('beforeend', commentsHTML);
    }

    const commentsDiv = document.querySelector(".post-comments")
    commentsDiv.classList.add("comments-slide")

    const commentForm = document.querySelector(".add-comment-form")

    commentForm.addEventListener("submit", e => {
        e.preventDefault();
        const commentInputField = document.querySelector(".comment-input");
        const commentValue = commentInputField.value;
        commentInputField.value = "";

        // TODO: append new comment to post obj.

        postComment(commentValue, postID, commentsSection);
    })

    const exitBtn = document.querySelector(".exit-btn")
    exitBtn.addEventListener("click", e => {
        commentsSection.innerHTML = ""
        commentsDiv.classList.remove("comments-slide")
    })
}

const allCommentsHTML = (username, userData) => {
    let allCommentsMarkup = "";

    for (const [comment, commentedTime] of Object.entries(userData.comments)) {

        
        allCommentsMarkup += commentMarkup(username, userData.profile_pic, comment, commentedTime);

    }
    return allCommentsMarkup
}

const postComment = async (comment, postID, commentsSection, posts) => {
    const csrfToken = document.cookie.split(";").map(el => el.split("=")).find(element => {
        if (element[0] === "csrftoken"){
            return element
        }
    })[1];
    const response = await fetch("/api/add-comment", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({newComment: comment, postID: postID})
    })
    const result = await response.json()

    commentsSection.insertAdjacentHTML("afterbegin", commentMarkup(
        result.user.username,
        result.user.profile_picture,
        result.comment_object.comment,
        result.comment_object.commented_time
    ))
}

const commentMarkup = (username, profile_pic, comment, commentedTime) => {
    const commentedTimeString = new Date(commentedTime).toDateString().replace(" ", ", ")
    return `
    <div class="comment-container">
        <div class="user-profile-pic">
            <img src="${profile_pic}" alt="User-img" height=40" width="40">
        </div>
        <div class="comment">
            <h3 class="author-name">${username}</h3>
            <p>${comment}</p>
            <small>${commentedTimeString}</small>
        </div>
    </div>
    `;
}

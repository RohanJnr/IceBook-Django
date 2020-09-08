import { commentMarkup } from "../markups.js";
import { fetchComments, postComment } from "../apiCalls.js";

export const viewComments = (e) => {
    // Retrieve post ID from comment button.
    const postID = e.target.getAttribute("data-id");

    // fetch Comments for specific post.
    fetchComments(postID).then((comments) => {
        // gather markup/HTML for each comment.
        
        const finalMarkup = comments.reduce((markup, comment) => {
            markup += commentMarkup(comment);
            return markup;
        }, " ");

    });
    // form to add new comment.
    /*
    const commentForm = document.querySelector(".add-comment-form");

    commentForm.addEventListener("submit", (form) => {
        form.preventDefault();
        const commentInputField = document.querySelector(".comment-input");
        const commentValue = commentInputField.value;
        commentInputField.value = "";

        // add comment via POST request to server.
        postComment(commentValue, postID).then((result) => {
            // the result is a comment.
            // TODO: handle errors

            const markup = commentMarkup(result);
            commentsSection.insertAdjacentHTML("afterbegin", markup);

            // update comment number on Span
            const commentsNumSpan = document.querySelector(
                `.comments-no.post-${postID}`
            );
            commentsNumSpan.innerText = +commentsNumSpan.innerText + 1;
        });
    });
    */
};

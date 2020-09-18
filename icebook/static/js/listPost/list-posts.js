import { toggleSpinner, toggleLike } from "../utils.js";
import { viewComments } from "./comments.js";
import { generatePostHTML } from "../markups.js";
import { getPosts } from "../apiCalls.js";

toggleSpinner();
getPosts().then((posts) => {
    toggleSpinner();
    const postsDiv = document.querySelector(".posts");
    posts.forEach((post) => {
        const postHTML = generatePostHTML(post);
        postsDiv.insertAdjacentHTML("beforeend", postHTML);
    });
    const likeBtnIcon = document.querySelectorAll(".social-btn.like-btn i");
    const commentBtnIcon = document.querySelectorAll(
        ".social-btn.comment-btn i"
    );
    likeBtnIcon.forEach((btn) => btn.addEventListener("click", toggleLike));

    // view comments on post.
    commentBtnIcon.forEach(btn => btn.addEventListener("click", e => viewComments(e)))
});

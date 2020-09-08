import { iconClassNames } from "../variables.js";
import { toggleSpinner } from "../utils.js";
import { viewComments } from "./comments.js";
import { generatePostHTML } from "../markups.js";
import { getPosts } from "../apiCalls.js";

toggleSpinner();
getPosts().then((posts) => {
    toggleSpinner();
    posts.forEach((post) => {
        const postHTML = generatePostHTML(post);
        const postsDiv = document.querySelector(".posts");
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

const toggleLike = async (e) => {
    const postID = e.target.getAttribute("data-id");
    try {
        const response = await fetch(`/api/toggle-like/${postID}`);
        const result = await response.json();
        e.target.classList.toggle(iconClassNames.likedToggle);
        const likesNumSpan = document.querySelector(`.likes-no.post-${postID}`);

        if (result.has_liked) {
            likesNumSpan.innerText = +likesNumSpan.innerText + 1;
        } else {
            likesNumSpan.innerText = +likesNumSpan.innerText - 1;
        }
    } catch (error) {
        alert(error);
    }
};

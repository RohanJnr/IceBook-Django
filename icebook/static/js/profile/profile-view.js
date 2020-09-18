import { toggleLike } from "../utils.js";
import { getUserPosts } from "../apiCalls.js";
import { generatePostHTML } from "../markups.js";

/* Disable archive feature temporarily until database redesign.
const allPosts = {
    archived: [],
    unarchived: [],
};

const showArchivedPosts = (e) => {
    // show only archived posts.
    e.target.classList.add("active");
    postsBtn.classList.remove("active");
};

const showPosts = (e) => {
    // show only unarchived posts.
    e.target.classList.add("active");
    archivedBtn.classList.remove("active");
};

const postsBtn = document.getElementById("posts-btn");

const archivedBtn = document.getElementById("archived-btn");

postsBtn.addEventListener("click", showPosts);
if (archivedBtn !== null) {
    archivedBtn.addEventListener("click", showArchivedPosts);
}
*/
const username = window.location.pathname.split("/")[2];
getUserPosts(username).then((posts) => {
    const userPosts = document.getElementById("profile-posts-div");
    posts.forEach((post) => {
        const postHTML = generatePostHTML(post);
        userPosts.insertAdjacentHTML("beforeend", postHTML);
    });
    const likeBtnIcon = document.querySelectorAll(".social-btn.like-btn i");
    const commentBtnIcon = document.querySelectorAll(
        ".social-btn.comment-btn i"
    );

    likeBtnIcon.forEach((btn) => btn.addEventListener("click", toggleLike));
});

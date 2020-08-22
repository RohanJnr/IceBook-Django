import { iconClassNames } from "../variables.js";
import { toggleSpinner } from "../utils.js";
import { viewComments } from "./comments.js"

const getPosts  = async () => {
    try{
        let res = await fetch("/api/posts");
        let posts = await res.json();
        return posts;
    } catch(error){
        alert(error);
    }
}
toggleSpinner()
getPosts().then(posts => {
    toggleSpinner()
    posts.forEach(post => {
        const postHTML = generatePostHTML(post);
        const postsDiv = document.querySelector(".posts");
        postsDiv.insertAdjacentHTML('beforeend', postHTML);
    })
    const likeBtns = document.querySelectorAll(".social-btn.like-btn i");
    const commentBtns = document.querySelectorAll(".social-btn.comment-btn i");
    likeBtns.forEach(btn => btn.addEventListener("click", toggleLike))
    commentBtns.forEach(btn => btn.addEventListener("click", e => viewComments(e, posts)))
})

const generatePostHTML = post => {
    const postedOn = new Date(post.created).toDateString().replace(" ", ", ");
    var md = window.markdownit();
    const html = `
    <article class="post-container">
        <section class="user-details">
            <div class="user-profile-pic">
                <img src="${post.user.profile_picture_url}" alt="User-img" height=50" width="50">
            </div>
            <div class="user-data">
                <h4 class="author-name">${post.user.username}</h4>
                <small>Posted On: ${postedOn}</small>
            </div>
        </section>
        <section class="post-data">
            <div class="markdown">
                <h2 class="post-title"><a href="#">${post.title}</a></h2>
                ${md.render(post.description)}
            </div>
        </section>
        <section class="social-btns">

            <span class="likes-no">${post.num_likes}</span><button type="button" class="social-btn like-btn"><i class="far fa-thumbs-up ${post.has_liked ? 'liked' : 'not-liked'}" data-id="${post.id}"></i></button>

            <span class="comments-no">${post.num_comments}</span><button type="button" class="social-btn comment-btn"><i class="far fa-comment" data-id="${post.id}"></i></button>

        </section>
    </article>
    `;
    return html;
}

const toggleLike = async (e) => {
    const postID = e.target.getAttribute("data-id");
    try{
        const response = await fetch(`/api/toggle-like/${postID}`);
        const result = await response.json();
        e.target.classList.toggle(iconClassNames.likedToggle);
        const likesNumSpan = document.querySelector(".likes-no");
    
        if (result.has_liked){
            likesNumSpan.innerText = +likesNumSpan.innerText + 1;
        }else{
            likesNumSpan.innerText = +likesNumSpan.innerText - 1;
        }
    }catch(error){
        alert(error)
    }
}

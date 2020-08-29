export const generatePostHTML = post => {
    const postedOn = new Date(post.created).toDateString().replace(" ", ", ");
    const md = window.markdownit();
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

            <span class="likes-no post-${post.id}">${post.num_likes}</span><button type="button" class="social-btn like-btn"><i class="far fa-thumbs-up ${post.has_liked ? 'liked' : 'not-liked'}" data-id="${post.id}"></i></button>

            <span class="comments-no post-${post.id}">${post.num_comments}</span><button type="button" class="social-btn comment-btn"><i class="far fa-comment" data-id="${post.id}"></i></button>

        </section>
    </article>
    `;
    return html;
}

export const commentMarkup = (comment) => {
    console.log("hello")
    const commentedTimeString = new Date(comment.commented_time).toDateString().replace(" ", ", ")
    return `
    <div class="comment-container">
        <div class="user-profile-pic">
            <img src="${comment.user.profile_picture_url}" alt="User-img" height=40" width="40">
        </div>
        <div class="comment">
            <h3 class="author-name">${comment.user.username}</h3>
            <p>${comment.comment}</p>
            <small>${commentedTimeString}</small>
        </div>
    </div>
    `;
}
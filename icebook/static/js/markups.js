export const generatePostHTML = (post) => {
    const postedOn = new Date(post.created).toDateString().replace(" ", ", ");
    const html = `
    <article class="post-container">
        <section class="user-details">
            <div class="user-profile">
                <div class="left">
                    <img src="${post.user.profile_picture_url}" alt="User-img"
                    height=40" width="40">
                    <h4 class="author-name"><a href="/profile/${
                        post.user.username
                    }">${post.user.username}</a></h4>
                </div>
                <div class="right ${post.has_control ? 'yes-control' : 'no-control'}">
                    <button class="control-btn edit-btn">Edit</button>
                    <button class="control-btn delete-btn">Delete</button>
                </div>
            </div>
        </section>
        <section class="post-data">
            <div class="post-image">
                <img src="${post.image}" alt="Post-img" />
            </div>
            <small class="posted-on">${postedOn}</small>
            <p class="post-description">${post.description}</p>
        </section>
        <section class="social-btns">

            <span class="likes-no post-${post.id}">${
        post.num_likes
    }</span><button type="button" class="social-btn like-btn"><i class="far fa-thumbs-up ${
        post.has_liked ? "liked" : ""
    }" data-id="${post.id}"></i></button>

            <span class="comments-no post-${post.id}">${
        post.num_comments
    }</span><button type="button" class="social-btn comment-btn"><i class="far fa-comment" data-id="${
        post.id
    }"></i></button>

        </section>
    
    </article>
    `;
    return html;
};

export const commentMarkup = (comment) => {
    // TODO: need to be overhauled
    const commentedTimeString = new Date(comment.commented_time)
        .toDateString()
        .replace(" ", ", ");
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
};

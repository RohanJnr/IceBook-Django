export const iconClassNames = {
    likedToggle: "liked",
};

export const routes = {
    getPosts: "some route",
    getComments: postID => {
        return `/api/comment?post_id=${postID}`
    },
    getPostDetail: "some route",
    postComment: "/api/comment",
    addPost: "/api/posts/",  // send a POST request to add a `post` (blog post) to the database.
}
const getPosts  = async () => {
    let res = await fetch("http://localhost:8000/api/posts/1")
    let data = await res.json()
    return data
}

getPosts()
    .then(data => console.log(data))
    .catch(reason => console.log(reason.message))

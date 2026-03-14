import { useState, useEffect } from "react";
import axios from "axios";
import PostForm from "./components/PostForm";
import PostItem from "./components/PostItem";

function App() {
  const [posts, setPosts] = useState([]);

  const fetchPosts = async () => {
    const res = await axios.get("http://127.0.0.1:8000/api/posts/");
    setPosts(res.data);
  };

  useEffect(() => {
    fetchPosts();
  }, []);

  const handleDelete = async (id) => {
    await axios.delete(`http://127.0.0.1:8000/api/posts/delete/${id}/`);
    fetchPosts();
  };

  return (
    <div style={{ maxWidth: "900px", margin: "0 auto", padding: "20px" }}>
      <h1>My Full-Stack Blog</h1>
      <PostForm onPostCreated={fetchPosts} />
      <hr />
      {posts.map((post) => (
        <PostItem key={post.id} post={post} onDelete={handleDelete} />
      ))}
    </div>
  );
}

export default App;

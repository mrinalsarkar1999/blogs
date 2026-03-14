import { useState, useEffect } from "react";
import axios from "axios";

const PostForm = ({ onPostCreated }) => {
  const [formData, setFormData] = useState({
    title: "",
    slug: "",
    content: "",
    tags: "",
    author: 1,
  });
  const [image, setImage] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Use FormData for file uploads
    const data = new FormData();
    data.append("title", formData.title);
    data.append("slug", formData.slug);
    data.append("content", formData.content);
    data.append("author", formData.author);
    if (image) data.append("cover_image", image);
    // Tags usually need to be handled as a comma-separated string or array
    data.append("tags", formData.tags);

    try {
      await axios.post("http://127.0.0.1:8000/api/posts/create/", data, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      onPostCreated();
      setFormData({ title: "", slug: "", content: "", tags: "", author: 1 });
      setImage(null);
    } catch (err) {
      console.error("Upload failed", err);
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      style={{
        border: "1px solid #ddd",
        padding: "20px",
        marginBottom: "20px",
      }}
    >
      <input
        type="text"
        placeholder="Title"
        value={formData.title}
        onChange={(e) => setFormData({ ...formData, title: e.target.value })}
      />
      <input
        type="text"
        placeholder="Slug"
        value={formData.slug}
        onChange={(e) => setFormData({ ...formData, slug: e.target.value })}
      />
      <textarea
        placeholder="Content"
        value={formData.content}
        onChange={(e) => setFormData({ ...formData, content: e.target.value })}
      />
      <input
        type="text"
        placeholder="Tags (comma separated)"
        value={formData.tags}
        onChange={(e) => setFormData({ ...formData, tags: e.target.value })}
      />
      <input type="file" onChange={(e) => setImage(e.target.files[0])} />
      <button type="submit">Save Post</button>
    </form>
  );
};

export default PostForm;

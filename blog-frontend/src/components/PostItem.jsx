// src/components/PostItem.jsx
const PostItem = ({ post, onDelete }) => {
  // Construct the full image URL
  const imageUrl = post.cover_image
    ? `http://127.0.0.1:8000${post.cover_image}`
    : "https://via.placeholder.com/600x400?text=No+Image";

  return (
    <div style={styles.card}>
      {/* Header: Author Info */}
      <div style={styles.header}>
        <div style={styles.avatar}>{post.author[0].toUpperCase()}</div>
        <span style={styles.username}>{post.author}</span>
        <button onClick={() => onDelete(post.id)} style={styles.deleteBtn}>
          ×
        </button>
      </div>

      {/* Image Section */}
      <div style={styles.imageContainer}>
        <img src={imageUrl} alt={post.title} style={styles.image} />
      </div>

      {/* Content Section (Caption Style) */}
      <div style={styles.contentSection}>
        <p>
          <strong>{post.author}</strong> {post.content}
        </p>

        {/* Tags Section */}
        <div style={styles.tagContainer}>
          {post.tags &&
            post.tags.map((tag, index) => (
              <span key={index} style={styles.tag}>
                #{tag.name || tag}
              </span>
            ))}
        </div>

        <div style={styles.date}>
          {new Date(post.created_at).toLocaleDateString()}
        </div>
      </div>
    </div>
  );
};

const styles = {
  card: {
    maxWidth: "600px",
    margin: "20px auto",
    backgroundColor: "#fff",
    border: "1px solid #dbdbdb",
    borderRadius: "3px",
    fontFamily:
      '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif',
  },
  header: {
    display: "flex",
    alignItems: "center",
    padding: "14px",
    position: "relative",
  },
  avatar: {
    width: "32px",
    height: "32px",
    borderRadius: "50%",
    backgroundColor: "#efefef",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    marginRight: "10px",
    fontWeight: "bold",
    fontSize: "14px",
  },
  username: {
    fontWeight: "600",
    fontSize: "14px",
  },
  deleteBtn: {
    position: "absolute",
    right: "15px",
    background: "none",
    border: "none",
    fontSize: "20px",
    cursor: "pointer",
    color: "#8e8e8e",
  },
  imageContainer: {
    width: "100%",
    backgroundColor: "#fafafa",
  },
  image: {
    width: "100%",
    display: "block",
  },
  contentSection: {
    padding: "12px 16px",
    fontSize: "14px",
    lineHeight: "18px",
  },
  tagContainer: {
    marginTop: "8px",
  },
  tag: {
    color: "#00376b",
    marginRight: "5px",
    cursor: "pointer",
  },
  date: {
    color: "#8e8e8e",
    fontSize: "10px",
    marginTop: "10px",
    textTransform: "uppercase",
  },
};

export default PostItem;

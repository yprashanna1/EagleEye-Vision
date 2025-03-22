// src/components/VideoUpload.js
import React, { useState } from 'react';
import api from '../services/api';

const VideoUpload = () => {
  // State for storing the selected file
  const [file, setFile] = useState(null);
  // State for storing the video URL if user chooses to input a link
  const [videoLink, setVideoLink] = useState("");
  // State for storing the detection result from the backend
  const [result, setResult] = useState(null);
  // State for handling loading and error messages
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // Handle file selection
  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setError("");
  };

  // Handle video link change
  const handleLinkChange = (e) => {
    setVideoLink(e.target.value);
    setError("");
  };

  // Function to upload file to the backend
  const handleFileUpload = async (e) => {
    e.preventDefault();
    if (!file) {
      setError("Please select a video file to upload.");
      return;
    }
    setLoading(true);
    setResult(null);
    try {
      const formData = new FormData();
      formData.append("file", file);
      // POST the file to the /api/video/detect endpoint
      const response = await api.post("/api/video/detect", formData);
      setResult(response.data);
    } catch (err) {
      setError("Error uploading file. Please try again.");
      console.error("File upload error:", err);
    } finally {
      setLoading(false);
    }
  };

  // (Optional) Function to handle video link submission
  const handleLinkSubmit = async (e) => {
    e.preventDefault();
    if (!videoLink) {
      setError("Please enter a valid video URL.");
      return;
    }
    setLoading(true);
    setResult(null);
    try {
      // For demonstration, we'll simulate sending the link
      // In a real app, you'll need a backend endpoint that accepts a video URL.
      const response = await api.post("/api/video/detect", { videoLink });
      setResult(response.data);
    } catch (err) {
      setError("Error processing video link. Please try again.");
      console.error("Video link error:", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ border: "1px solid #ccc", padding: "20px", borderRadius: "8px", margin: "20px 0" }}>
      <h2>Upload a Video</h2>
      <form onSubmit={handleFileUpload}>
        <div>
          <input type="file" accept="video/*" onChange={handleFileChange} />
        </div>
        <button type="submit" disabled={loading}>
          {loading ? "Uploading..." : "Upload Video"}
        </button>
      </form>
      <h3>Or Enter a Video Link</h3>
      <form onSubmit={handleLinkSubmit}>
        <div>
          <input
            type="text"
            placeholder="Enter video URL"
            value={videoLink}
            onChange={handleLinkChange}
            style={{ width: "80%", padding: "8px" }}
          />
        </div>
        <button type="submit" disabled={loading}>
          {loading ? "Processing..." : "Submit Video Link"}
        </button>
      </form>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {result && (
        <div>
          <h3>Detection Results:</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default VideoUpload;

// src/components/VideoFeed.js
import React, { useEffect, useState } from 'react';
import api from '../services/api';

const VideoFeed = () => {
  const [testMessage, setTestMessage] = useState("");

  useEffect(() => {
    // Call the test endpoint from the backend
    api.get("/api/video/test")
      .then(response => {
        setTestMessage(response.data.message);
      })
      .catch(error => {
        console.error("Error fetching test data:", error);
      });
  }, []);

  return (
    <div>
      <h2>Live Video Feed</h2>
      <p>{testMessage ? testMessage : "Loading video feed..."}</p>
    </div>
  );
};

export default VideoFeed;

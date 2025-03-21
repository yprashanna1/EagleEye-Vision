// src/components/Dashboard.js
import React from 'react';
import VideoFeed from './VideoFeed';  // Import the VideoFeed component

const Dashboard = () => {
  return (
    <div>
      <h1>EagleEye Vision Dashboard</h1>
      {/* Render the VideoFeed component */}
      <VideoFeed />
      {/* You can add more components here later (like alerts, controls, etc.) */}
    </div>
  );
};

export default Dashboard;

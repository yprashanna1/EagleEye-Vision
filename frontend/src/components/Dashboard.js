// src/components/Dashboard.js
import React from 'react';
import VideoFeed from './VideoFeed';
import AlertVerification from './AlertVerification';
import VideoUpload from './VideoUpload'; // Import the new component

const Dashboard = () => {
  return (
    <div style={{ padding: "20px" }}>
      <h1>EagleEye Vision Dashboard</h1>
      {/* Video Upload Interface */}
      <VideoUpload />
      {/* Other components for displaying video feed and alerts */}
      <VideoFeed />
      <AlertVerification />
    </div>
  );
};

export default Dashboard;

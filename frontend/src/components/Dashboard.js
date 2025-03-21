// src/components/Dashboard.js
import React from 'react';
import VideoFeed from './VideoFeed';
import AlertVerification from './AlertVerification';

const Dashboard = () => {
  return (
    <div>
      <h1>EagleEye Vision Dashboard</h1>
      <VideoFeed />
      <AlertVerification />
    </div>
  );
};

export default Dashboard;

// src/components/AlertVerification.js
import React, { useEffect, useState } from 'react';
import api from '../services/api';

const AlertVerification = () => {
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    // Fetch alerts that need human verification from the backend
    api.get("/api/alert/verify")
      .then(response => {
        setAlerts(response.data.alerts);
      })
      .catch(error => {
        console.error("Error fetching verification alerts:", error);
      });
  }, []);

  return (
    <div>
      <h2>Alerts Needing Verification</h2>
      {alerts.length === 0 ? (
        <p>No alerts require verification at this time.</p>
      ) : (
        <ul>
          {alerts.map(alert => (
            <li key={alert.id}>
              {alert.message} - <strong>{alert.needs_verification ? "Needs Verification" : "Verified"}</strong>
              {/* Buttons for human action can be added here */}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default AlertVerification;

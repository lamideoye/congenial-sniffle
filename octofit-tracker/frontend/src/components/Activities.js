import React, { useEffect, useState } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch('https://urban-space-spork-6rw45ppg7w7cr47g-8000.app.github.dev/api/activities/')
      .then(response => response.json())
      .then(data => setActivities(data))
      .catch(error => console.error('Error fetching activities:', error));
  }, []);

  return (
    <div>
      <h1>Activities</h1>
      <ul>
        {activities.map(activity => (
          <li key={activity._id}>{activity.type} - {activity.duration} minutes</li>
        ))}
      </ul>
    </div>
  );
}

export default Activities;

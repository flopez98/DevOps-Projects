import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [count, setCount] = useState(null);

  const fetchData = () => {
    console.log('Fetching data...');
    fetch('http://172.28.0.10:5000/get_counter')
      .then(response => response.json())
      .then(data => {
        console.log('Received data:', data);
        setCount(data.count);
      })
      .catch(error => {
        console.error("There was an error fetching data", error);
      });
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div>
      <h1 className="App-header">Counter: {count !== null ? count : 'Loading...'}</h1>
      <button className="App-button" onClick={fetchData}>Reload Count</button>
    </div>
  );
}

export default App;

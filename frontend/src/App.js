import React, {useState, useEffect} from 'react';
import Map from './Components/Map';
import Controls from './Components/Controls';
import Display from './Components/Display';
import './App.css';

function App() {
  const [map, setMap] = useState([]); /*map represented by array*/
  const [points, setPoints] = useState([]) /* start and end points */
  const [running, setRunning] = useState(false) /*if the pathfinder algo is running*/
  const [ready, setReady] = useState(false) /* True if the points have been chosen and wall construction is finished*/


  /* Function to fetch the map array from backend  */
  const getMap = async () => {
    try{
        const response = await fetch('http://127.0.0.1:5000/fetch_map');
        const data = await response.json();

        console.log(data);
        setMap(data);
    }
    catch(error){
        console.error('Failed to get map: ', error);
    }
  }

  /*function to update map array*/
  const updateMap = async (i, j, value) => {
    /*update map based on tile clicks and other events*/
    try{
      const response = await fetch('http://127.0.0.1:5000/update_map',
      {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({i,j,value})
      });
      
      const data = await response.json();

      console.log(data);
      setMap(data);
    }
    catch(error){
        console.error('Failed to get map: ', error);
    }
  }

  const clearMap = async () =>{
    try{
      const response = await fetch('http://127.0.0.1:5000/clear_map',
        {
          method: 'POST',
          headers: {'Content-Type':'application/json'},
      });
      
      const data = await response.json();
      setPoints([]);
      setMap(data);
    }
    catch(error){
      console.error('Failed to clear map: ', error);
    }
  }

  /*Function runs with selected algorithm once the Controls component's start button is clicked */
  const start = (algo) => {
    console.log("Running Algorithm");
  }

  /*function to handle cell clicks */
  const cellClick = (i,j) => {
    console.log(i + " " + j);
    if(points.length === 0){
      updateMap(i, j, 2)
      let p = [i,j]
      setPoints(p)
    }
    if(points.length === 2){
      updateMap(i, j, 3)
      let p = [points[0], points[1], i, j]
      setPoints(p)
    }
    if(points.length === 4 && !ready ){
      updateMap(i, j, 1)
    }
  }

  return (
    <div className="App">
      <Controls fetchMap={getMap} clearMap={clearMap}/>
      <Map main_map = {map} cellClick={cellClick}/>
    </div>
  );
}

export default App;
